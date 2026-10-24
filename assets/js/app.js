/**
 * Master Application Coordinator for Aviation Examination & Training Platform
 */
const App = (() => {
  let catalog = [];
  let currentAircraftData = null;
  let activeExamResult = null;
  let bankQuestions = [];
  let currentPaperData = null;
  let currentPaperQuestions = [];
  let boldFaceSubMode = 'practice';
  let boldFaceKeysRevealed = false;

  const FLEET_METADATA = {
    'AH-64E APACHE': {
      category: 'COMBAT',
      heli: true,
      roleBadge: '⚔️ ATTACK HELICOPTER',
      tagline: 'Helikopter Tempur Utama Tandem / Sistem Sensor Malam & Rudal',
      icon: '⚔️'
    },
    'ANKA MALE UAV': {
      category: 'UAV',
      heli: false,
      roleBadge: '🛸 MALE UNMANNED AERIAL VEHICLE',
      tagline: 'Drone Pengintai Taktis Jarak Jauh / Satcom & Dual FLIR Payload',
      icon: '🛸'
    },
    'BELL 412 EP': {
      category: 'HELI',
      heli: true,
      roleBadge: '🚁 TACTICAL UTILITY HELICOPTER',
      tagline: 'Twin-Turbine Multi-Mission / Angkut Personel & Medevac',
      icon: '🚁'
    },
    'BO-105': {
      category: 'HELI',
      heli: true,
      roleBadge: '🚁 LIGHT SCOUT & LIAISON',
      tagline: 'Dual-Turbine Rigid Rotor / Agilitas Tinggi & Observasi Udara',
      icon: '🚁'
    },
    'CASA 212-200': {
      category: 'PLANE',
      heli: false,
      roleBadge: '✈️ TWIN TURBOPROP TRANSPORT',
      tagline: 'Pesawat Angkut Taktis Sayap Tetap / STOL Operasi Perintis',
      icon: '✈️'
    },
    'FENNEC AS550': {
      category: 'HELI',
      heli: true,
      roleBadge: '🚁 LIGHT ARMED SCOUT',
      tagline: 'Helikopter Serbu Ringan & Pengawal / FADEC Turbomeca Arriel',
      icon: '🚁'
    },
    'MI-17V5': {
      category: 'HELI',
      heli: true,
      roleBadge: '🚁 HEAVY MEDIUM TRANSPORT',
      tagline: 'Helikopter Angkut Berat & Pasukan / Kapasitas Kargo 4.000 kg',
      icon: '🚁'
    },
    'SIKORSKY S300C': {
      category: 'HELI',
      heli: true,
      roleBadge: '🚁 PRIMARY FLIGHT TRAINER',
      tagline: 'Helikopter Latih Dasar Penerbang / Piston Lycoming HIO-360',
      icon: '🚁'
    }
  };

  let currentFleetFilter = 'ALL';
  let fleetSearchQuery = '';

  function filterFleetCategory(category, buttonEl) {
    currentFleetFilter = category;
    document.querySelectorAll('.fleet-filter-pill').forEach(btn => btn.classList.remove('active'));
    if (buttonEl) buttonEl.classList.add('active');
    applyFleetFilters();
  }

  function onFleetSearch(event) {
    fleetSearchQuery = (event.target.value || '').trim().toLowerCase();
    const clearBtn = document.getElementById('fleet-search-clear');
    if (clearBtn) {
      clearBtn.style.display = fleetSearchQuery ? 'block' : 'none';
    }
    applyFleetFilters();
  }

  function clearFleetSearch() {
    fleetSearchQuery = '';
    const input = document.getElementById('fleet-search-input');
    if (input) input.value = '';
    const clearBtn = document.getElementById('fleet-search-clear');
    if (clearBtn) clearBtn.style.display = 'none';
    applyFleetFilters();
  }

  function applyFleetFilters() {
    const cards = document.querySelectorAll('.aircraft-card');
    let visibleCount = 0;

    cards.forEach(card => {
      const aircraft = card.getAttribute('data-aircraft');
      const meta = FLEET_METADATA[aircraft] || { category: 'HELI', heli: true };

      let matchCat = false;
      if (currentFleetFilter === 'ALL') {
        matchCat = true;
      } else if (currentFleetFilter === 'HELI') {
        matchCat = meta.heli === true;
      } else if (currentFleetFilter === 'PLANE') {
        matchCat = meta.category === 'PLANE';
      } else if (currentFleetFilter === 'UAV') {
        matchCat = meta.category === 'UAV';
      } else if (currentFleetFilter === 'COMBAT') {
        matchCat = meta.category === 'COMBAT';
      }

      let matchSearch = true;
      if (fleetSearchQuery) {
        const textContent = (card.textContent || '').toLowerCase();
        matchSearch = textContent.includes(fleetSearchQuery);
      }

      if (matchCat && matchSearch) {
        card.style.display = '';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    const emptyBox = document.getElementById('aircraft-empty-search');
    if (emptyBox) {
      emptyBox.style.display = (visibleCount === 0) ? 'block' : 'none';
    }
  }

  async function init() {
    initTheme();
    setupGlobalEvents();
    Navigation.init();

    try {
      catalog = await QuestionLoader.loadCatalog();
      renderHome();
      updateDashboardStats();
    } catch (e) {
      console.error('Initialization error:', e);
      showToast('Gagal memuat katalog materi. Silakan refresh halaman.', 'error');
    }
  }

  // ==========================================
  // THEME MANAGEMENT
  // ==========================================
  function initTheme() {
    const settings = Storage.getSettings();
    document.documentElement.dataset.theme = settings.theme || 'dark';
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) {
      updateThemeButtonIcon(themeBtn, settings.theme);
      themeBtn.addEventListener('click', toggleTheme);
    }
  }

  function toggleTheme() {
    const current = document.documentElement.dataset.theme === 'light' ? 'light' : 'dark';
    const newTheme = current === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = newTheme;
    Storage.updateSettings({ theme: newTheme });
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) updateThemeButtonIcon(themeBtn, newTheme);
  }

  function updateThemeButtonIcon(btn, theme) {
    btn.innerHTML = theme === 'dark' 
      ? '<span class="icon">☀️</span> <span class="btn-text">Light</span>' 
      : '<span class="icon">🌙</span> <span class="btn-text">Dark</span>';
  }

  // ==========================================
  // TOAST NOTIFICATIONS
  // ==========================================
  function showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    const icon = type === 'success' ? '✓' : type === 'error' ? '✕' : type === 'warning' ? '⚠️' : 'ℹ️';
    toast.innerHTML = `<span class="toast-icon">${icon}</span><span class="toast-msg">${message}</span>`;
    container.appendChild(toast);

    setTimeout(() => {
      toast.classList.add('fade-out');
      setTimeout(() => toast.remove(), 300);
    }, 3500);
  }

  // ==========================================
  // VIEW CHANGE HANDLER
  // ==========================================
  async function onViewChanged(viewName, params) {
    if (viewName === 'home') {
      renderHome();
      updateDashboardStats();
    } else if (viewName === 'setup') {
      const aircraft = params.get('aircraft') || 'BELL 412 EP';
      await loadAndRenderSetup(aircraft);
    } else if (viewName === 'bank') {
      await loadAndRenderQuestionBank();
    } else if (viewName === 'history') {
      renderHistory();
    } else if (viewName === 'exam') {
      if (!ExamEngine.getState()) {
        Navigation.navigateTo('home');
      }
    }
  }

  // ==========================================
  // HOME VIEW
  // ==========================================
  function renderHome() {
    const container = document.getElementById('aircraft-card-grid');
    if (!container || !catalog.length) return;

    container.innerHTML = catalog.map(item => {
      const draftAnswers = Storage.getDraftAnswers(item.aircraft);
      const draftCount = Object.keys(draftAnswers || {}).filter(k => (draftAnswers[k] || '').trim()).length;
      const meta = FLEET_METADATA[item.aircraft] || {
        category: 'HELI',
        roleBadge: '🚁 AVIATION FLEET',
        tagline: item.description || '',
        icon: '✈️'
      };

      return `
        <div class="aircraft-card" data-aircraft="${item.aircraft}">
          <div class="card-role-badge">${meta.roleBadge}</div>
          <div class="card-badge-row">
            <span class="badge badge-accent">${item.aircraft}</span>
            <span class="badge badge-subtle">${item.sourceDocument}</span>
          </div>
          <h3 class="card-title">${item.title}</h3>
          <p class="card-desc">${meta.tagline || item.description}</p>
          
          <div class="card-stats-grid">
            <div class="card-stat-item">
              <span class="stat-number">${item.totalQuestions}</span>
              <span class="stat-label">Total Soal</span>
            </div>
            <div class="card-stat-item">
              <span class="stat-number">${item.categoriesCount}</span>
              <span class="stat-label">Kategori</span>
            </div>
            <div class="card-stat-item">
              <span class="stat-number">100%</span>
              <span class="stat-label">Diverifikasi</span>
            </div>
          </div>

          <div class="card-actions">
            ${draftCount > 0 ? `
              <button class="btn btn-warning btn-sm" onclick="App.resumeExam('${item.aircraft}')">
                Lanjutkan (${draftCount} dijawab)
              </button>
            ` : ''}
            <button class="btn btn-primary" onclick="App.openSetup('${item.aircraft}')">
              Mulai Ujian
            </button>
            <button class="btn btn-secondary" onclick="App.openBoldFaceDirect('${item.aircraft}')">
              Lembar Bold Face ⭐
            </button>
            <button class="btn btn-secondary btn-sm" onclick="App.openPaperMode('${item.aircraft}')">
              Cetak PDF
            </button>
          </div>
        </div>
      `;
    }).join('');

    applyFleetFilters();
  }

  function updateDashboardStats() {
    const history = Storage.getHistory();
    const totalAvail = catalog.reduce((acc, c) => acc + c.totalQuestions, 0);

    const totalExamsEl = document.getElementById('dash-total-exams');
    const avgScoreEl = document.getElementById('dash-avg-score');
    const totalQuestionsEl = document.getElementById('dash-total-questions');
    const passRateEl = document.getElementById('dash-pass-rate');

    if (totalQuestionsEl) totalQuestionsEl.textContent = String(totalAvail);

    if (history.length > 0) {
      if (totalExamsEl) totalExamsEl.textContent = String(history.length);
      const avg = Math.round(history.reduce((a, b) => a + (b.finalScore || 0), 0) / history.length);
      if (avgScoreEl) avgScoreEl.textContent = `${avg}%`;
      const passedCount = history.filter(h => h.isPassed).length;
      const passRate = Math.round((passedCount / history.length) * 100);
      if (passRateEl) passRateEl.textContent = `${passRate}%`;
    } else {
      if (totalExamsEl) totalExamsEl.textContent = '0';
      if (avgScoreEl) avgScoreEl.textContent = '0%';
      if (passRateEl) passRateEl.textContent = '0%';
    }
  }

  // ==========================================
  // SETUP VIEW
  // ==========================================
  async function loadAndRenderSetup(aircraftId) {
    try {
      currentAircraftData = await QuestionLoader.loadAircraftData(aircraftId);
      const titleEl = document.getElementById('setup-aircraft-title');
      const descEl = document.getElementById('setup-aircraft-desc');
      const docEl = document.getElementById('setup-aircraft-doc');

      if (titleEl) titleEl.textContent = currentAircraftData.title;
      if (descEl) descEl.textContent = currentAircraftData.description;
      if (docEl) docEl.textContent = currentAircraftData.sourceDocument;

      // Group categories
      const categories = [...new Set(currentAircraftData.questions.map(q => q.category))].sort();
      const catContainer = document.getElementById('setup-categories-list');

      if (catContainer) {
        catContainer.innerHTML = `
          <label class="category-chip select-all">
            <input type="checkbox" id="setup-check-all-cats" checked onchange="App.toggleAllCategories(this.checked)" />
            <span>Pilih Semua Kategori (${categories.length})</span>
          </label>
          ${categories.map(cat => {
            const count = currentAircraftData.questions.filter(q => q.category === cat).length;
            return `
              <label class="category-chip">
                <input type="checkbox" name="setup-cat" value="${cat}" checked onchange="App.updateSelectedCatCount()" />
                <span>${cat} <small>(${count})</small></span>
              </label>
            `;
          }).join('')}
        `;
      }

      updateSelectedCatCount();
    } catch (e) {
      console.error('Setup load error:', e);
      showToast('Gagal memuat materi pesawat: ' + aircraftId, 'error');
    }
  }

  function toggleAllCategories(checked) {
    document.querySelectorAll('input[name="setup-cat"]').forEach(cb => {
      cb.checked = checked;
    });
    updateSelectedCatCount();
  }

  function updateSelectedCatCount() {
    const checked = Array.from(document.querySelectorAll('input[name="setup-cat"]:checked')).map(cb => cb.value);
    const countBadge = document.getElementById('setup-selected-count');
    if (!currentAircraftData) return;

    const matchingQuestions = currentAircraftData.questions.filter(q => checked.includes(q.category));
    if (countBadge) {
      countBadge.textContent = `${matchingQuestions.length} Soal Terpilih`;
    }
  }

  async function startExamFromSetup() {
    if (!currentAircraftData) {
      const { params } = Navigation.parseHash();
      const aircraft = params.get('aircraft') || 'BELL 412 EP';
      try {
        await loadAndRenderSetup(aircraft);
      } catch (e) {
        showToast('Gagal memuat materi pesawat. Silakan kembali ke Beranda.', 'error');
        return;
      }
    }

    if (!currentAircraftData) {
      showToast('Pilih jenis pesawat terlebih dahulu dari Beranda.', 'warning');
      return;
    }

    const selectedCats = Array.from(document.querySelectorAll('input[name="setup-cat"]:checked')).map(cb => cb.value);
    if (selectedCats.length === 0) {
      showToast('Pilih minimal 1 kategori materi!', 'warning');
      return;
    }

    const mode = document.querySelector('input[name="exam-mode"]:checked')?.value || 'exam';
    const timerVal = parseInt(document.getElementById('setup-timer-select')?.value || '0', 10);
    const shuffle = document.getElementById('setup-shuffle-toggle')?.checked || false;
    const limitVal = parseInt(document.getElementById('setup-limit-select')?.value || '0', 10);

    const questions = QuestionLoader.prepareQuestions(currentAircraftData, {
      categories: selectedCats,
      shuffle,
      limit: limitVal
    });

    if (questions.length === 0) {
      showToast('Tidak ada soal yang cocok dengan pilihan Anda.', 'warning');
      return;
    }

    if (mode === 'boldface') {
      openBoldFaceSheet(currentAircraftData, questions, 'practice');
      return;
    }

    if (mode === 'manual') {
      openPaperView(currentAircraftData, questions);
      return;
    }

    ExamEngine.startSession({
      aircraft: currentAircraftData.aircraft,
      aircraftData: currentAircraftData,
      mode,
      timerMinutes: timerVal,
      questions,
      resume: false
    }, renderExamState, onExamFinished);

    Navigation.navigateTo('exam');
  }

  async function resumeExam(aircraftId) {
    try {
      const data = await QuestionLoader.loadAircraftData(aircraftId);
      ExamEngine.startSession({
        aircraft: data.aircraft,
        aircraftData: data,
        mode: 'exam',
        timerMinutes: 0,
        questions: data.questions,
        resume: true
      }, renderExamState, onExamFinished);

      Navigation.navigateTo('exam');
      showToast(`Melanjutkan sesi ${aircraftId}`, 'info');
    } catch (e) {
      showToast('Gagal melanjutkan latihan.', 'error');
    }
  }

  // ==========================================
  // EXAM ENGINE VIEW
  // ==========================================
  function renderExamState(state) {
    if (!state) return;

    // Progress Bar HUD
    const progressBar = document.getElementById('exam-progress-bar-fill');
    if (progressBar && state.totalQuestions > 0) {
      const pct = Math.round(((state.currentIndex + 1) / state.totalQuestions) * 100);
      progressBar.style.width = `${pct}%`;
    }

    // Header info
    const titleEl = document.getElementById('exam-aircraft-badge');
    const counterEl = document.getElementById('exam-counter');
    const timerBadge = document.getElementById('exam-timer-badge');
    const modeBadge = document.getElementById('exam-mode-badge');

    if (titleEl) titleEl.textContent = state.aircraft;
    if (counterEl) counterEl.textContent = `Soal ${state.currentIndex + 1} / ${state.totalQuestions}`;
    if (modeBadge) modeBadge.textContent = state.mode === 'practice' ? 'Mode Latihan' : 'Mode Ujian';

    if (timerBadge) {
      if (state.timerActive) {
        timerBadge.removeAttribute('hidden');
        timerBadge.textContent = `⏱️ ${state.timeFormatted}`;
        timerBadge.classList.toggle('timer-urgent', state.timeRemaining < 300);
      } else {
        timerBadge.setAttribute('hidden', '');
      }
    }

    // Question content
    const q = state.currentQuestion;
    if (!q) return;

    const catEl = document.getElementById('exam-q-category');
    const secEl = document.getElementById('exam-q-section');
    const textEl = document.getElementById('exam-q-text');
    const singleInputGroup = document.getElementById('single-input-group');
    const inputEl = document.getElementById('exam-answer-input');
    const multiGrid = document.getElementById('multi-input-grid');
    const unitEl = document.getElementById('exam-q-unit');
    const flagBtn = document.getElementById('exam-flag-btn');
    const practiceBox = document.getElementById('exam-practice-box');

    if (catEl) catEl.textContent = q.category;
    if (secEl) secEl.textContent = q.section;
    if (textEl) textEl.textContent = (q.question || '').replace(/^\d+[\.\)]\s*/, '');

    const hasSub = q.subQuestions && Array.isArray(q.subQuestions) && q.subQuestions.length > 0;

    if (hasSub) {
      if (singleInputGroup) singleInputGroup.style.display = 'none';
      if (unitEl) unitEl.setAttribute('hidden', '');

      if (multiGrid) {
        multiGrid.style.display = 'grid';
        const userObj = (typeof state.currentAnswer === 'object' && state.currentAnswer !== null) ? state.currentAnswer : {};
        const subChecks = state.instantCheck?.subResults || {};

        multiGrid.innerHTML = q.subQuestions.map((subQ, sIdx) => {
          const val = userObj[subQ.id] || '';
          const subRes = Array.isArray(subChecks) ? subChecks.find(s => s.id === subQ.id) : subChecks?.[subQ.id];
          let statusCls = '';
          let subFeedbackHtml = '';

          if (state.mode === 'practice' && subRes) {
            statusCls = subRes.isCorrect ? 'is-valid' : subRes.isEmpty ? 'is-empty' : 'is-invalid';
            subFeedbackHtml = `
              <div class="sub-param-feedback ${subRes.status}">
                <span>${subRes.isCorrect ? '✓ Benar' : subRes.isEmpty ? '⚠️ Belum diisi' : '✕ Kunci: ' + subQ.answer}</span>
              </div>
            `;
          }

          return `
            <div class="sub-param-card ${statusCls}">
              <div class="sub-param-header">
                <span class="sub-param-label">
                  <span class="sub-idx">${sIdx + 1}</span>
                  <strong>${subQ.label || 'Parameter'}</strong>
                </span>
                ${subQ.unit ? `<span class="sub-unit-tag">${subQ.unit}</span>` : ''}
              </div>
              <div class="sub-input-wrapper">
                <input 
                  type="text" 
                  class="text-answer-input sub-param-input ${statusCls}" 
                  id="sub-input-${subQ.id}" 
                  data-question-id="${q.id}" 
                  data-sub-id="${subQ.id}" 
                  value="${val}" 
                  placeholder="Ketik nilai ${subQ.label}..." 
                  autocomplete="off" 
                  autocapitalize="off" 
                  spellcheck="false" 
                  oninput="App.onSubAnswerInput(event)" 
                  onkeydown="App.onAnswerKeyDown(event)" 
                />
              </div>
              ${subFeedbackHtml}
            </div>
          `;
        }).join('');

        // Autofocus first input if none currently focused
        const firstInput = multiGrid.querySelector('.sub-param-input');
        if (firstInput && (!document.activeElement || document.activeElement.tagName !== 'INPUT')) {
          firstInput.focus();
        }
      }
    } else {
      if (multiGrid) multiGrid.style.display = 'none';
      if (singleInputGroup) singleInputGroup.style.display = 'flex';

      if (unitEl) {
        if (q.unit) {
          unitEl.textContent = `Satuan: [ ${q.unit} ]`;
          unitEl.removeAttribute('hidden');
        } else {
          unitEl.setAttribute('hidden', '');
        }
      }

      if (inputEl) {
        inputEl.value = (typeof state.currentAnswer === 'string' ? state.currentAnswer : '') || '';
        inputEl.dataset.questionId = q.id;
        if (!document.activeElement || document.activeElement.tagName !== 'INPUT') {
          inputEl.focus();
        }
      }
    }

    if (flagBtn) {
      flagBtn.classList.toggle('flagged', state.isFlagged);
      flagBtn.innerHTML = state.isFlagged ? '🚩 Ragu-ragu' : '🏳️ Tandai Ragu';
    }

    // Practice controls & feedback
    if (practiceBox) {
      if (state.mode === 'practice') {
        practiceBox.removeAttribute('hidden');
        const feedbackEl = document.getElementById('practice-feedback-text');
        if (state.instantCheck) {
          feedbackEl.className = `practice-feedback ${state.instantCheck.status}`;
          if (hasSub) {
            feedbackEl.innerHTML = `<strong>${state.instantCheck.feedback}</strong>`;
          } else {
            feedbackEl.textContent = `${state.instantCheck.feedback} (Kunci: ${q.answer})`;
          }
        } else {
          feedbackEl.className = 'practice-feedback';
          feedbackEl.textContent = '';
        }
      } else {
        practiceBox.setAttribute('hidden', '');
      }
    }

    // Prev / Next button states
    const prevBtn = document.getElementById('exam-prev-btn');
    const nextBtn = document.getElementById('exam-next-btn');
    if (prevBtn) prevBtn.disabled = state.currentIndex === 0;
    if (nextBtn) {
      if (state.currentIndex === state.totalQuestions - 1) {
        nextBtn.textContent = 'Selesai & Kumpulkan';
        nextBtn.classList.add('btn-success');
      } else {
        nextBtn.textContent = 'Selanjutnya →';
        nextBtn.classList.remove('btn-success');
      }
    }

    // Render Question Navigator Grid
    renderQuestionGrid(state);
  }

  function renderQuestionGrid(state) {
    const grid = document.getElementById('exam-navigator-grid');
    if (!grid) return;

    grid.innerHTML = state.questions ? state.questions.map((q, idx) => {
      const rawAns = state.answers[q.id];
      let isAns = false;
      if (typeof rawAns === 'object' && rawAns !== null) {
        isAns = Object.values(rawAns).some(v => typeof v === 'string' && v.trim().length > 0);
      } else if (typeof rawAns === 'string') {
        isAns = rawAns.trim().length > 0;
      }

      const isFlag = state.flags.includes(q.id);
      const isCurr = state.currentIndex === idx;

      let cls = 'nav-num-btn';
      if (isCurr) cls += ' active';
      if (isFlag) cls += ' flagged';
      else if (isAns) cls += ' answered';

      return `<button class="${cls}" onclick="ExamEngine.jumpTo(${idx})" title="${q.category}: ${q.question}">${idx + 1}</button>`;
    }).join('') : '';
  }

  function onAnswerInput(e) {
    const input = e.target;
    const qId = input.dataset.questionId;
    if (qId) {
      ExamEngine.setAnswer(qId, input.value);
    }
  }

  function onSubAnswerInput(e) {
    const input = e.target;
    const qId = input.dataset.questionId;
    const subId = input.dataset.subId;
    if (qId && subId) {
      ExamEngine.setAnswer(qId, input.value, subId);
    }
  }

  function checkCurrentQuestion() {
    const state = ExamEngine.getState();
    if (!state || !state.currentQuestion) return;
    ExamEngine.checkSingleAnswer(state.currentQuestion.id);
  }

  function revealCurrentQuestion() {
    const state = ExamEngine.getState();
    if (!state || !state.currentQuestion) return;
    ExamEngine.revealAnswer(state.currentQuestion.id);
  }

  function toggleCurrentFlag() {
    const state = ExamEngine.getState();
    if (!state || !state.currentQuestion) return;
    ExamEngine.toggleFlag(state.currentQuestion.id);
  }

  function onAnswerKeyDown(e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      const state = ExamEngine.getState();
      if (state.currentIndex === state.totalQuestions - 1) {
        promptSubmitExam();
      } else {
        ExamEngine.nextQuestion();
      }
    }
  }

  function promptSubmitExam() {
    const state = ExamEngine.getState();
    if (!state) return;

    const unanswered = state.unansweredCount;
    let msg = `Anda telah menjawab ${state.answeredCount} dari ${state.totalQuestions} soal.`;
    if (unanswered > 0) {
      msg += `\nMasih ada ${unanswered} soal yang belum dijawab.`;
    }
    msg += '\n\nApakah Anda yakin ingin mengumpulkan ujian sekarang?';

    if (window.confirm(msg)) {
      ExamEngine.submitExam(false);
    }
  }

  // ==========================================
  // RESULTS VIEW
  // ==========================================
  function onExamFinished(results) {
    activeExamResult = results;
    Navigation.navigateTo('result');
    renderResultView(results);
  }

  function renderResultView(results) {
    const scoreValEl = document.getElementById('res-score-value');
    const badgeEl = document.getElementById('res-status-badge');
    const airEl = document.getElementById('res-aircraft-name');
    const timeEl = document.getElementById('res-time-taken');
    const correctEl = document.getElementById('res-correct-count');
    const wrongEl = document.getElementById('res-wrong-count');
    const emptyEl = document.getElementById('res-empty-count');

    if (scoreValEl) scoreValEl.textContent = `${results.finalScore}%`;
    if (airEl) airEl.textContent = results.aircraft || results.submissionRecord?.aircraft || '';
    if (timeEl) timeEl.textContent = results.elapsedFormatted || '00:00';
    if (correctEl) correctEl.textContent = String(results.correctCount);
    if (wrongEl) wrongEl.textContent = String(results.wrongCount + (results.reviewCount || 0));
    if (emptyEl) emptyEl.textContent = String(results.emptyCount);

    if (badgeEl) {
      if (results.isPassed) {
        badgeEl.textContent = 'LULUS (MEMENUHI SYARAT)';
        badgeEl.className = 'status-badge status-pass';
      } else {
        badgeEl.textContent = `TIDAK LULUS (STANDAR ${results.passingThreshold}%)`;
        badgeEl.className = 'status-badge status-fail';
      }
    }

    // Category progress meters
    const catContainer = document.getElementById('res-category-breakdown');
    if (catContainer && results.categories) {
      catContainer.innerHTML = results.categories.map(c => `
        <div class="category-result-row">
          <div class="cat-label-row">
            <span class="cat-title">${c.category}</span>
            <span class="cat-score">${c.earned}/${c.possible} Poin (${c.scorePct}%)</span>
          </div>
          <div class="progress-bar-track">
            <div class="progress-bar-fill ${c.scorePct >= 75 ? 'fill-green' : c.scorePct >= 50 ? 'fill-yellow' : 'fill-red'}" style="width: ${c.scorePct}%"></div>
          </div>
        </div>
      `).join('');
    }

    // Detailed question list
    renderDetailedReview('all');
  }

  function renderDetailedReview(filter = 'all') {
    if (!activeExamResult) return;
    const container = document.getElementById('res-question-review-list');
    if (!container) return;

    let items = activeExamResult.detailedResults || [];
    if (filter === 'wrong') {
      items = items.filter(i => i.evaluation.status === 'incorrect' || i.evaluation.status === 'review' || i.evaluation.status === 'partial');
    } else if (filter === 'correct') {
      items = items.filter(i => i.evaluation.status === 'correct');
    } else if (filter === 'empty') {
      items = items.filter(i => i.evaluation.status === 'empty');
    }

    container.innerHTML = items.map((item, idx) => {
      const q = item.question;
      const ev = item.evaluation;
      let statusClass = 'badge-wrong';
      let statusText = 'SALAH';

      if (ev.status === 'correct') {
        statusClass = 'badge-correct';
        statusText = 'BENAR';
      } else if (ev.status === 'partial') {
        statusClass = 'badge-partial';
        statusText = `SEBAGIAN (${Math.round(ev.score * 100)}%)`;
      } else if (ev.status === 'empty') {
        statusClass = 'badge-empty';
        statusText = 'KOSONG';
      }

      const hasSub = q.subQuestions && Array.isArray(q.subQuestions) && q.subQuestions.length > 0 && ev.subResults;

      let comparisonHtml = '';
      if (hasSub) {
        comparisonHtml = `
          <div class="review-sub-breakdown">
            <div class="review-sub-grid">
              ${q.subQuestions.map(sq => {
                const sr = (Array.isArray(ev.subResults) ? ev.subResults.find(s => s.id === sq.id) : ev.subResults?.[sq.id]) || {};
                const subBadge = sr.isCorrect ? '<span class="badge badge-correct">✓ Tepat</span>' : sr.isEmpty ? '<span class="badge badge-empty">Kosong</span>' : '<span class="badge badge-wrong">✕ Salah</span>';
                return `
                  <div class="review-sub-card ${sr.status || 'empty'}">
                    <div class="review-sub-header">
                      <strong>${sq.label}</strong>
                      ${subBadge}
                    </div>
                    <div class="review-sub-row">
                      <span class="sub-key-lbl">Jawaban Anda:</span>
                      <span class="sub-val ${sr.isCorrect ? 'text-success' : 'text-danger'}">${sr.userAnswer || '<em class="text-muted">(Kosong)</em>'}</span>
                    </div>
                    <div class="review-sub-row">
                      <span class="sub-key-lbl">Kunci Resmi:</span>
                      <span class="sub-val text-accent"><strong>${sq.answer} ${sq.unit || ''}</strong></span>
                    </div>
                  </div>
                `;
              }).join('')}
            </div>
          </div>
        `;
      } else {
        const displayUserAns = typeof item.userAnswer === 'string' ? item.userAnswer : (item.userAnswer ? JSON.stringify(item.userAnswer) : '');
        comparisonHtml = `
          <div class="review-comparison-grid">
            <div class="answer-box user-box ${ev.status}">
              <span class="box-label">Jawaban Anda:</span>
              <span class="box-value">${displayUserAns || '<em class="text-muted">(Tidak dijawab)</em>'}</span>
            </div>
            <div class="answer-box target-box">
              <span class="box-label">Kunci Dokumen Resmi:</span>
              <span class="box-value">${q.answer}</span>
            </div>
          </div>
        `;
      }

      return `
        <div class="review-item-card ${ev.status}">
          <div class="review-item-header">
            <div class="q-meta">
              <span class="q-num">#${idx + 1}</span>
              <span class="badge badge-subtle">${q.category}</span>
              ${q.unit ? `<span class="badge badge-accent">${q.unit}</span>` : ''}
            </div>
            <span class="badge ${statusClass}">${statusText}</span>
          </div>

          <p class="review-q-text">${(q.question || '').replace(/^\d+[\.\)]\s*/, '')}</p>

          ${comparisonHtml}

          ${q.acceptedAnswers && q.acceptedAnswers.length > 1 ? `
            <div class="accepted-variants-note">
              <small>Variasi diterima: ${q.acceptedAnswers.join(' | ')}</small>
            </div>
          ` : ''}

          <div class="review-citation-footer">
            <span>📄 Dokumen: ${q.sourceDocument} ${q.sourcePage ? `(Hal. ${q.sourcePage})` : ''}</span>
            <span>Nilai: ${Math.round(ev.score * (q.points || 1) * 10) / 10} / ${q.points || 1} poin</span>
          </div>
        </div>
      `;
    }).join('');
  }

  function filterReview(filterType, btn) {
    document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    renderDetailedReview(filterType);
  }

  function retakeWrongOnly() {
    if (!activeExamResult) return;
    const wrongIds = (activeExamResult.detailedResults || [])
      .filter(i => !i.evaluation.isCorrect)
      .map(i => i.question.id);

    if (wrongIds.length === 0) {
      showToast('Selamat! Tidak ada soal yang salah.', 'success');
      return;
    }

    const wrongQuestions = (activeExamResult.detailedResults || [])
      .filter(i => wrongIds.includes(i.question.id))
      .map(i => i.question);

    ExamEngine.startSession({
      aircraft: activeExamResult.aircraft,
      aircraftData: activeExamResult.aircraftData,
      mode: 'practice',
      timerMinutes: 0,
      questions: wrongQuestions,
      resume: false
    }, renderExamState, onExamFinished);

    Navigation.navigateTo('exam');
    showToast(`Memulai latihan ulang ${wrongQuestions.length} soal yang perlu diperbaiki`, 'info');
  }

  function exportResultCSV() {
    if (!activeExamResult) return;
    const rows = [
      ['Nomor', 'Kategori', 'Pertanyaan', 'Jawaban Pengguna', 'Kunci Resmi', 'Status', 'Skor', 'Dokumen Sumber']
    ];

    (activeExamResult.detailedResults || []).forEach((item, idx) => {
      const q = item.question;
      const ev = item.evaluation;
      rows.push([
        idx + 1,
        `"${q.category.replace(/"/g, '""')}"`,
        `"${q.question.replace(/"/g, '""')}"`,
        `"${(item.userAnswer || '').replace(/"/g, '""')}"`,
        `"${q.answer.replace(/"/g, '""')}"`,
        ev.status.toUpperCase(),
        ev.score,
        `"${q.sourceDocument}"`
      ]);
    });

    const csvContent = 'data:text/csv;charset=utf-8,' + rows.map(e => e.join(',')).join('\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', `Hasil_Ujian_${activeExamResult.aircraft}_${Date.now()}.csv`);
    document.body.appendChild(link);
    link.click();
    link.remove();
  }

  // ==========================================
  // BOLD FACE & PAPER SHEET MODE (STYLE ANKA)
  // ==========================================
  async function openBoldFaceDirect(aircraftId) {
    try {
      const data = await QuestionLoader.loadAircraftData(aircraftId);
      currentAircraftData = data;
      openBoldFaceSheet(data, data.questions, 'practice');
    } catch (e) {
      console.error(e);
      showToast('Gagal memuat lembar Bold Face untuk: ' + aircraftId, 'error');
    }
  }

  function openPaperMode(aircraftId) {
    QuestionLoader.loadAircraftData(aircraftId).then(data => {
      openPaperView(data, data.questions);
    });
  }

  function openPaperView(data, questions) {
    openBoldFaceSheet(data, questions, 'manual');
  }

  function openBoldFaceSheet(data, questions, subMode = 'practice') {
    currentPaperData = data;
    currentPaperQuestions = questions && questions.length ? questions : (data.questions || []);
    boldFaceSubMode = subMode;
    boldFaceKeysRevealed = false;

    // Sidebar Info
    const aTitle = document.getElementById('bf-aircraft-title');
    const aSub = document.getElementById('bf-doc-sub');
    if (aTitle) aTitle.textContent = data.aircraft;
    if (aSub) aSub.textContent = data.sourceDocument || data.title;

    // Header Paper Info
    const pTitle = document.getElementById('paper-aircraft-title');
    const pDoc = document.getElementById('paper-source-doc');
    if (pTitle) pTitle.textContent = data.title;
    if (pDoc) pDoc.textContent = data.sourceDocument;

    // Candidate default Date
    const dateInput = document.getElementById('paper-cand-date');
    if (dateInput && !dateInput.value) {
      const now = new Date();
      dateInput.value = `${String(now.getDate()).padStart(2, '0')}/${String(now.getMonth() + 1).padStart(2, '0')}/${now.getFullYear()}`;
    }

    const candScore = document.getElementById('paper-cand-score');
    if (candScore) candScore.textContent = '-';

    setBoldFaceSubMode(subMode, false);

    // Render Navigation tabs in sidebar
    const sections = [...new Set(currentPaperQuestions.map(q => q.section || 'UMUM'))];
    const tabsContainer = document.getElementById('bf-tabs-list');
    if (tabsContainer) {
      tabsContainer.innerHTML = `
        <button type="button" class="bf-tab-btn active" data-tab-sec="ALL" onclick="App.filterBoldFaceSection('ALL')">
          <span>Semua Bagian</span>
          <span class="bf-tab-badge">${currentPaperQuestions.length}</span>
        </button>
        ${sections.map(sec => {
          const count = currentPaperQuestions.filter(q => (q.section || 'UMUM') === sec).length;
          return `
            <button type="button" class="bf-tab-btn" data-tab-sec="${sec}" onclick="App.filterBoldFaceSection('${sec}')">
              <span>${sec}</span>
              <span class="bf-tab-badge">${count}</span>
            </button>
          `;
        }).join('')}
      `;
    }

    // Render questions onto document sheet
    renderBoldFaceQuestions(currentPaperQuestions, subMode === 'manual');

    // Restore draft answers from Storage
    const drafts = Storage.getDraftAnswers(data.aircraft) || {};
    currentPaperQuestions.forEach(q => {
      if (q.subQuestions && q.subQuestions.length > 0) {
        q.subQuestions.forEach(sq => {
          const subInp = document.getElementById(`paper-input-${q.id}-${sq.id}`);
          if (subInp && drafts[q.id] && typeof drafts[q.id] === 'object' && drafts[q.id][sq.id]) {
            subInp.value = drafts[q.id][sq.id];
          }
        });
      } else {
        const input = document.getElementById(`paper-input-${q.id}`);
        if (input && drafts[q.id]) {
          input.value = typeof drafts[q.id] === 'string' ? drafts[q.id] : '';
        }
      }
    });

    resetBoldFaceStatsUI();
    Navigation.navigateTo('paper');
  }

  function renderBoldFaceQuestions(questionsList, isPrintOnly) {
    const container = document.getElementById('paper-sheet-content');
    if (!container) return;

    const sections = [...new Set(questionsList.map(q => q.section || 'UMUM'))];

    container.innerHTML = sections.map(sec => {
      const secQuestions = questionsList.filter(q => (q.section || 'UMUM') === sec);
      return `
        <div class="paper-section-block" id="paper-sec-${sec.replace(/\s+/g, '-')}">
          <h2 class="paper-section-title">${sec}</h2>
          <div class="paper-questions-list">
            ${secQuestions.map((q, idx) => {
              const prevQ = idx > 0 ? secQuestions[idx - 1] : null;
              const isNewCat = !prevQ || (prevQ.category !== q.category);
              const catHeaderHtml = (isNewCat && q.category) ? `
                <div class="paper-category-header">
                  <h3 class="paper-cat-title">${q.category}</h3>
                </div>
              ` : '';

              const hasSub = q.subQuestions && q.subQuestions.length > 0;
              const cleanQText = (q.question || '').replace(/^\d+[\.\)]\s*/, '');
              if (hasSub) {
                return `
                  ${catHeaderHtml}
                  <div class="paper-question-item paper-multi-item" id="paper-item-${q.id}" data-qid="${q.id}" data-section="${sec}">
                    <div class="paper-q-text">
                      <span class="paper-q-num">${idx + 1}.</span>
                      <span class="paper-q-body">${cleanQText}</span>
                    </div>
                    <div class="paper-sub-list">
                      ${q.subQuestions.map((sq, sIdx) => {
                        const subLetter = String.fromCharCode(97 + sIdx);
                        return `
                        <div class="paper-sub-row">
                          <span class="paper-sub-label">${subLetter}. ${sq.label}:</span>
                          <span class="paper-dots ${isPrintOnly ? '' : 'print-only'}">....................................................</span>
                          ${!isPrintOnly ? `
                            <div class="paper-input-wrapper no-print">
                              <input 
                                type="text" 
                                class="paper-answer-input paper-sub-input" 
                                id="paper-input-${q.id}-${sq.id}" 
                                data-qid="${q.id}" 
                                data-subid="${sq.id}" 
                                placeholder="Ketik..." 
                                autocomplete="off" 
                                spellcheck="false" 
                                oninput="App.onBoldFaceSubInput('${q.id}', '${sq.id}')"
                                onkeydown="App.onBoldFaceKeyDown(event, '${q.id}')"
                              />
                            </div>
                          ` : ''}
                          <span class="paper-unit">${sq.unit ? `[ ${sq.unit} ]` : ''}</span>
                        </div>
                      `;
                      }).join('')}
                    </div>
                    ${!isPrintOnly ? `
                      <div class="paper-feedback-box no-print" id="paper-feedback-${q.id}" style="display: none;">
                        <span class="paper-feedback-text"></span>
                      </div>
                    ` : ''}
                  </div>
                `;
              }
              return `
                ${catHeaderHtml}
                <div class="paper-question-item" id="paper-item-${q.id}" data-qid="${q.id}" data-section="${sec}">
                  <div class="paper-q-text">
                    <span class="paper-q-num">${idx + 1}.</span>
                    <span class="paper-q-body">${cleanQText}</span>
                    <span class="paper-dots ${isPrintOnly ? '' : 'print-only'}">..........................................................................................</span>
                    ${!isPrintOnly ? `
                      <div class="paper-input-wrapper no-print">
                        <input 
                          type="text" 
                          class="paper-answer-input" 
                          id="paper-input-${q.id}" 
                          data-qid="${q.id}" 
                          placeholder="Ketik jawaban..." 
                          autocomplete="off" 
                          spellcheck="false"
                          oninput="App.onBoldFaceInput('${q.id}')"
                          onkeydown="App.onBoldFaceKeyDown(event, '${q.id}')"
                        />
                      </div>
                    ` : ''}
                    <span class="paper-unit">${q.unit ? `[ ${q.unit} ]` : ''}</span>
                  </div>
                  ${!isPrintOnly ? `
                    <div class="paper-feedback-box no-print" id="paper-feedback-${q.id}" style="display: none;">
                      <span class="paper-feedback-text"></span>
                    </div>
                  ` : ''}
                </div>
              `;
            }).join('')}
          </div>
        </div>
      `;
    }).join('');
  }

  function setBoldFaceSubMode(mode, showNotification = true) {
    boldFaceSubMode = mode;
    const btnPractice = document.getElementById('bf-mode-btn-practice');
    const btnExam = document.getElementById('bf-mode-btn-exam');
    const toggleKeysBtn = document.getElementById('bf-toggle-keys-btn');

    if (btnPractice) btnPractice.classList.toggle('active', mode === 'practice');
    if (btnExam) btnExam.classList.toggle('active', mode === 'exam');

    if (toggleKeysBtn) {
      toggleKeysBtn.style.display = mode === 'exam' ? 'none' : 'block';
    }

    if (showNotification) {
      showToast(mode === 'exam' ? 'Mode Ujian aktif: Kunci jawaban disembunyikan sampai dikoreksi.' : 'Mode Latihan aktif: Anda dapat mengecek dan melihat kunci jawaban.', 'info');
    }
  }

  function checkBoldFaceAnswers() {
    if (!currentPaperQuestions || currentPaperQuestions.length === 0) return;

    let correctCount = 0;
    let wrongCount = 0;
    let emptyCount = 0;
    let totalPoints = 0;
    let earnedPoints = 0;

    currentPaperQuestions.forEach(q => {
      const fbBox = document.getElementById(`paper-feedback-${q.id}`);
      const weight = q.points || 1;
      totalPoints += weight;

      const hasSub = q.subQuestions && q.subQuestions.length > 0;
      let evalRes;

      if (hasSub) {
        const userObj = {};
        q.subQuestions.forEach(sq => {
          const subInp = document.getElementById(`paper-input-${q.id}-${sq.id}`);
          userObj[sq.id] = subInp ? subInp.value.trim() : '';
        });
        evalRes = Grading.evaluateAnswer(userObj, q.answer, q.acceptedAnswers, q.unit, q.subQuestions);

        q.subQuestions.forEach(sq => {
          const subInp = document.getElementById(`paper-input-${q.id}-${sq.id}`);
          const subEval = Array.isArray(evalRes.subResults) ? evalRes.subResults.find(s => s.id === sq.id) : evalRes.subResults?.[sq.id];
          if (subInp && subEval) {
            subInp.classList.remove('correct', 'incorrect', 'auto-filled');
            if (subEval.isCorrect) {
              subInp.classList.add('correct');
            } else {
              subInp.classList.add('incorrect');
            }
          }
        });
      } else {
        const input = document.getElementById(`paper-input-${q.id}`);
        const userVal = input ? input.value.trim() : '';
        evalRes = Grading.evaluateAnswer(userVal, q.answer, q.acceptedAnswers, q.unit);

        if (input) {
          input.classList.remove('correct', 'incorrect', 'auto-filled');
          if (evalRes.status === 'correct') {
            input.classList.add('correct');
          } else {
            input.classList.add('incorrect');
          }
        }
      }

      earnedPoints += (evalRes.score * weight);

      if (fbBox) {
        if (evalRes.status === 'correct') {
          fbBox.className = 'paper-feedback-box correct-box no-print';
          fbBox.innerHTML = `✓ <strong>Tepat!</strong> Kunci: ${q.answer}`;
          fbBox.style.display = 'flex';
          correctCount++;
        } else if (evalRes.status === 'partial') {
          fbBox.className = 'paper-feedback-box partial-box no-print';
          fbBox.innerHTML = `⚠️ <strong>Sebagian Benar (${Math.round(evalRes.score * 100)}%).</strong> Kunci: ${q.answer}`;
          fbBox.style.display = 'flex';
          correctCount += evalRes.score;
        } else if (evalRes.status === 'empty') {
          fbBox.className = 'paper-feedback-box no-print';
          fbBox.innerHTML = `⚠️ <em>Belum diisi.</em> Kunci: <strong>${q.answer}</strong>`;
          fbBox.style.display = 'flex';
          emptyCount++;
        } else {
          fbBox.className = 'paper-feedback-box no-print';
          fbBox.innerHTML = `✕ <strong>Kurang tepat.</strong> Kunci: <strong>${q.answer}</strong>`;
          fbBox.style.display = 'flex';
          wrongCount++;
        }
      }
    });

    const finalScore = totalPoints > 0 ? Math.round((earnedPoints / totalPoints) * 100) : 0;
    const settings = Storage.getSettings();
    const isPassed = finalScore >= (settings.passingScore || 75);

    const elBenar = document.getElementById('bf-stat-benar');
    const elSalah = document.getElementById('bf-stat-salah');
    const elKosong = document.getElementById('bf-stat-kosong');
    const elNilai = document.getElementById('bf-stat-nilai');
    const elBadge = document.getElementById('bf-stat-badge');
    const candScore = document.getElementById('paper-cand-score');

    if (elBenar) elBenar.textContent = String(Math.round(correctCount));
    if (elSalah) elSalah.textContent = String(wrongCount);
    if (elKosong) elKosong.textContent = String(emptyCount);
    if (elNilai) elNilai.textContent = `${finalScore}%`;
    if (candScore) candScore.textContent = `${finalScore}% (${isPassed ? 'LULUS' : 'TIDAK LULUS'})`;

    if (elBadge) {
      elBadge.textContent = isPassed ? `LULUS (STANDAR ${settings.passingScore || 75}%)` : `TIDAK LULUS (STANDAR ${settings.passingScore || 75}%)`;
      elBadge.className = `bf-stat-badge ${isPassed ? 'status-pass' : 'status-fail'}`;
    }

    if (boldFaceSubMode === 'exam' && currentPaperData) {
      Storage.saveExamResult({
        aircraft: currentPaperData.aircraft,
        mode: 'boldface-sheet',
        finalScore,
        totalQuestions: currentPaperQuestions.length,
        correctCount: Math.round(correctCount),
        wrongCount,
        emptyCount,
        reviewCount: 0,
        isPassed,
        durationSeconds: 0,
        categories: []
      });
      Storage.clearDraftAnswers(currentPaperData.aircraft);
    }

    showToast(`Koreksi selesai! Skor: ${finalScore}% (${Math.round(correctCount)} Benar, ${wrongCount} Salah, ${emptyCount} Kosong)`, isPassed ? 'success' : 'warning');
  }

  function toggleBoldFaceKeys() {
    if (!currentPaperQuestions) return;
    boldFaceKeysRevealed = !boldFaceKeysRevealed;
    const toggleBtn = document.getElementById('bf-toggle-keys-btn');

    currentPaperQuestions.forEach(q => {
      const fbBox = document.getElementById(`paper-feedback-${q.id}`);

      if (q.subQuestions && q.subQuestions.length > 0) {
        q.subQuestions.forEach(sq => {
          const subInp = document.getElementById(`paper-input-${q.id}-${sq.id}`);
          if (!subInp) return;
          if (boldFaceKeysRevealed) {
            subInp.dataset.origVal = subInp.value;
            subInp.value = sq.answer;
            subInp.classList.add('auto-filled');
          } else {
            subInp.value = subInp.dataset.origVal || '';
            subInp.classList.remove('auto-filled', 'correct', 'incorrect');
          }
        });
        if (fbBox) {
          if (boldFaceKeysRevealed) {
            fbBox.className = 'paper-feedback-box correct-box no-print';
            fbBox.innerHTML = `💡 Kunci: <strong>${q.answer}</strong>`;
            fbBox.style.display = 'flex';
          } else {
            fbBox.style.display = 'none';
          }
        }
      } else {
        const input = document.getElementById(`paper-input-${q.id}`);
        if (!input) return;

        if (boldFaceKeysRevealed) {
          input.dataset.origVal = input.value;
          input.value = q.answer;
          input.classList.add('auto-filled');
          if (fbBox) {
            fbBox.className = 'paper-feedback-box correct-box no-print';
            fbBox.innerHTML = `💡 Kunci: <strong>${q.answer}</strong>`;
            fbBox.style.display = 'flex';
          }
        } else {
          input.value = input.dataset.origVal || '';
          input.classList.remove('auto-filled', 'correct', 'incorrect');
          if (fbBox) fbBox.style.display = 'none';
        }
      }
    });

    if (toggleBtn) {
      toggleBtn.innerHTML = boldFaceKeysRevealed ? '🙈 Sembunyikan Kunci' : '💡 Tampilkan Jawaban';
    }

    showToast(boldFaceKeysRevealed ? 'Kunci jawaban diisikan ke lembar.' : 'Kunci jawaban disembunyikan.', 'info');
  }

  function resetBoldFaceSheet() {
    if (!currentPaperQuestions || !currentPaperData) return;
    if (!window.confirm('Kosongkan seluruh isian jawaban pada lembar dokumen ini?')) return;

    currentPaperQuestions.forEach(q => {
      const fbBox = document.getElementById(`paper-feedback-${q.id}`);
      if (q.subQuestions && q.subQuestions.length > 0) {
        q.subQuestions.forEach(sq => {
          const subInp = document.getElementById(`paper-input-${q.id}-${sq.id}`);
          if (subInp) {
            subInp.value = '';
            subInp.classList.remove('correct', 'incorrect', 'auto-filled');
          }
        });
      } else {
        const input = document.getElementById(`paper-input-${q.id}`);
        if (input) {
          input.value = '';
          input.classList.remove('correct', 'incorrect', 'auto-filled');
        }
      }
      if (fbBox) {
        fbBox.style.display = 'none';
      }
    });

    Storage.clearDraftAnswers(currentPaperData.aircraft);
    resetBoldFaceStatsUI();
    boldFaceKeysRevealed = false;
    const toggleBtn = document.getElementById('bf-toggle-keys-btn');
    if (toggleBtn) toggleBtn.innerHTML = '💡 Tampilkan Jawaban';

    showToast('Seluruh isian lembar telah dikosongkan.', 'info');
  }

  function resetBoldFaceStatsUI() {
    const elBenar = document.getElementById('bf-stat-benar');
    const elSalah = document.getElementById('bf-stat-salah');
    const elKosong = document.getElementById('bf-stat-kosong');
    const elNilai = document.getElementById('bf-stat-nilai');
    const elBadge = document.getElementById('bf-stat-badge');
    const candScore = document.getElementById('paper-cand-score');

    if (elBenar) elBenar.textContent = '0';
    if (elSalah) elSalah.textContent = '0';
    if (elKosong) elKosong.textContent = '0';
    if (elNilai) elNilai.textContent = '0%';
    if (candScore) candScore.textContent = '-';
    if (elBadge) {
      elBadge.textContent = 'BELUM DIKOREKSI';
      elBadge.className = 'bf-stat-badge';
    }
  }

  function filterBoldFaceSection(sec) {
    document.querySelectorAll('.bf-tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tabSec === sec);
    });

    const blocks = document.querySelectorAll('.paper-section-block');
    if (sec === 'ALL') {
      blocks.forEach(b => b.style.display = 'block');
    } else {
      blocks.forEach(b => {
        const titleEl = b.querySelector('.paper-section-title');
        const match = titleEl && titleEl.textContent.trim() === sec;
        b.style.display = match ? 'block' : 'none';
      });
    }
  }

  function onBoldFaceInput(qid) {
    if (!currentPaperData) return;
    const drafts = Storage.getDraftAnswers(currentPaperData.aircraft) || {};
    const input = document.getElementById(`paper-input-${qid}`);
    if (input) {
      input.classList.remove('correct', 'incorrect', 'auto-filled');
      drafts[qid] = input.value;
      Storage.saveDraftAnswers(currentPaperData.aircraft, drafts);
    }
    const fbBox = document.getElementById(`paper-feedback-${qid}`);
    if (fbBox && boldFaceSubMode !== 'practice') {
      fbBox.style.display = 'none';
    }
  }

  function onBoldFaceSubInput(qid, subid) {
    if (!currentPaperData) return;
    const drafts = Storage.getDraftAnswers(currentPaperData.aircraft) || {};
    const input = document.getElementById(`paper-input-${qid}-${subid}`);
    if (input) {
      input.classList.remove('correct', 'incorrect', 'auto-filled');
      if (typeof drafts[qid] !== 'object' || drafts[qid] === null) {
        drafts[qid] = {};
      }
      drafts[qid][subid] = input.value;
      Storage.saveDraftAnswers(currentPaperData.aircraft, drafts);
    }
    const fbBox = document.getElementById(`paper-feedback-${qid}`);
    if (fbBox && boldFaceSubMode !== 'practice') {
      fbBox.style.display = 'none';
    }
  }

  function onBoldFaceKeyDown(e, qid) {
    if (e.key === 'Enter') {
      e.preventDefault();
      const inputs = Array.from(document.querySelectorAll('.paper-answer-input'));
      const currIdx = inputs.indexOf(e.target);
      if (currIdx >= 0 && currIdx < inputs.length - 1) {
        inputs[currIdx + 1].focus();
      }
    }
  }

  // ==========================================
  // QUESTION BANK VIEW
  // ==========================================
  async function loadAndRenderQuestionBank() {
    const listContainer = document.getElementById('bank-questions-table-body');
    const totalCountEl = document.getElementById('bank-total-count');

    // Aggregate questions from all catalog items
    bankQuestions = [];
    for (const c of catalog) {
      try {
        const d = await QuestionLoader.loadAircraftData(c.aircraft);
        bankQuestions.push(...(d.questions || []));
      } catch (e) {
        console.warn('Bank load error for', c.aircraft);
      }
    }

    if (totalCountEl) totalCountEl.textContent = String(bankQuestions.length);
    renderBankFiltered();
  }

  function renderBankFiltered() {
    const tbody = document.getElementById('bank-questions-table-body');
    const searchVal = (document.getElementById('bank-search-input')?.value || '').toLowerCase().trim();
    const aircraftVal = document.getElementById('bank-aircraft-filter')?.value || 'ALL';

    if (!tbody) return;

    let filtered = bankQuestions;
    if (aircraftVal !== 'ALL') {
      filtered = filtered.filter(q => q.aircraft === aircraftVal);
    }
    if (searchVal) {
      filtered = filtered.filter(q => 
        q.question.toLowerCase().includes(searchVal) || 
        q.answer.toLowerCase().includes(searchVal) ||
        q.category.toLowerCase().includes(searchVal)
      );
    }

    tbody.innerHTML = filtered.slice(0, 150).map((q, idx) => `
      <tr>
        <td><strong>${idx + 1}</strong></td>
        <td><span class="badge badge-accent">${q.aircraft}</span></td>
        <td><span class="badge badge-subtle">${q.category}</span></td>
        <td class="td-question">${q.question}</td>
        <td class="td-answer"><strong>${q.answer}</strong></td>
        <td>${q.unit || '-'}</td>
        <td><small class="text-muted">${q.sourceDocument}</small></td>
      </tr>
    `).join('');
  }

  function exportBankJSON() {
    const blob = new Blob([JSON.stringify(bankQuestions, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `Aviation_Question_Bank_Export_${Date.now()}.json`;
    link.click();
    URL.revokeObjectURL(url);
    showToast('Bank soal berhasil diekspor ke JSON.', 'success');
  }

  // ==========================================
  // HISTORY VIEW
  // ==========================================
  function renderHistory() {
    const history = Storage.getHistory();
    const container = document.getElementById('history-records-container');
    if (!container) return;

    if (history.length === 0) {
      container.innerHTML = `
        <div class="empty-state">
          <div class="empty-icon">📂</div>
          <h3>Belum Ada Riwayat Ujian</h3>
          <p>Selesaikan latihan atau ujian untuk mencatat hasil dan perkembangan Anda di sini.</p>
          <button class="btn btn-primary" onclick="Navigation.navigateTo('home')">Mulai Sekarang</button>
        </div>
      `;
      return;
    }

    container.innerHTML = `
      <div class="history-actions-bar">
        <span>Menampilkan ${history.length} sesi ujian tersimpan</span>
        <button class="btn btn-danger btn-sm" onclick="App.clearAllHistory()">Hapus Semua Riwayat</button>
      </div>
      <div class="history-grid">
        ${history.map(item => `
          <div class="history-card ${item.isPassed ? 'card-pass' : 'card-fail'}">
            <div class="history-header">
              <span class="badge badge-accent">${item.aircraft}</span>
              <span class="history-date">${new Date(item.timestamp).toLocaleString('id-ID')}</span>
            </div>
            <div class="history-score-display">
              <span class="score-large">${item.finalScore}%</span>
              <span class="history-status">${item.isPassed ? 'LULUS' : 'TIDAK LULUS'}</span>
            </div>
            <div class="history-metrics">
              <span>✓ Benar: ${item.correctCount}</span>
              <span>✕ Salah: ${item.wrongCount}</span>
              <span>⏱️ Durasi: ${Math.round(item.durationSeconds / 60)} mnt</span>
            </div>
          </div>
        `).join('')}
      </div>
    `;
  }

  function clearAllHistory() {
    if (window.confirm('Apakah Anda yakin ingin menghapus seluruh riwayat ujian dari LocalStorage? Tindakan ini tidak dapat dibatalkan.')) {
      Storage.clearHistory();
      renderHistory();
      updateDashboardStats();
      showToast('Riwayat ujian berhasil dibersihkan.', 'success');
    }
  }

  // ==========================================
  // GLOBAL LISTENERS & NAVIGATION HOOKS
  // ==========================================
  function setupGlobalEvents() {
    // Navigation bar clicks
    document.querySelectorAll('[data-nav-view]').forEach(btn => {
      btn.addEventListener('click', () => {
        Navigation.navigateTo(btn.dataset.navView);
      });
    });

    // Keyboard navigation during exam
    window.addEventListener('keydown', (e) => {
      const active = Navigation.getCurrentView();
      if (active === 'exam') {
        if (e.key === 'ArrowRight' && e.altKey) {
          e.preventDefault();
          ExamEngine.nextQuestion();
        } else if (e.key === 'ArrowLeft' && e.altKey) {
          e.preventDefault();
          ExamEngine.prevQuestion();
        } else if ((e.key === 'f' || e.key === 'F') && e.altKey) {
          e.preventDefault();
          toggleCurrentFlag();
        }
      }
    });
  }

  function openSetup(aircraftId) {
    Navigation.navigateTo('setup', { aircraft: aircraftId });
  }

  return {
    init,
    showToast,
    onViewChanged,
    openSetup,
    resumeExam,
    toggleAllCategories,
    updateSelectedCatCount,
    startExamFromSetup,
    onAnswerInput,
    onSubAnswerInput,
    onAnswerKeyDown,
    checkCurrentQuestion,
    revealCurrentQuestion,
    toggleCurrentFlag,
    promptSubmitExam,
    filterReview,
    retakeWrongOnly,
    exportResultCSV,
    openPaperMode,
    openBoldFaceDirect,
    openBoldFaceSheet,
    setBoldFaceSubMode,
    checkBoldFaceAnswers,
    toggleBoldFaceKeys,
    resetBoldFaceSheet,
    filterBoldFaceSection,
    onBoldFaceInput,
    onBoldFaceSubInput,
    onBoldFaceKeyDown,
    renderBankFiltered,
    exportBankJSON,
    clearAllHistory,
    filterFleetCategory,
    onFleetSearch,
    clearFleetSearch
  };
})();

if (typeof module !== 'undefined' && module.exports) {
  module.exports = App;
}
if (typeof globalThis !== 'undefined') {
  globalThis.App = App;
}
if (typeof window !== 'undefined') {
  window.App = App;
}

// Start application when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  App.init();
});
