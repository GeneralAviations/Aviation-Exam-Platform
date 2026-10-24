/**
 * Master Application Coordinator for Aviation Examination & Training Platform
 */
const App = (() => {
  let catalog = [];
  let currentAircraftData = null;
  let activeExamResult = null;
  let bankQuestions = [];

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

      return `
        <div class="aircraft-card" data-aircraft="${item.aircraft}">
          <div class="card-badge-row">
            <span class="badge badge-accent">${item.aircraft}</span>
            <span class="badge badge-subtle">${item.sourceDocument}</span>
          </div>
          <h3 class="card-title">${item.title}</h3>
          <p class="card-desc">${item.description}</p>
          
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
            <button class="btn btn-secondary" onclick="App.openPaperMode('${item.aircraft}')">
              Lembar Cetak
            </button>
          </div>
        </div>
      `;
    }).join('');
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
    const inputEl = document.getElementById('exam-answer-input');
    const unitEl = document.getElementById('exam-q-unit');
    const flagBtn = document.getElementById('exam-flag-btn');
    const practiceBox = document.getElementById('exam-practice-box');

    if (catEl) catEl.textContent = q.category;
    if (secEl) secEl.textContent = q.section;
    if (textEl) textEl.textContent = q.question;
    if (unitEl) {
      if (q.unit) {
        unitEl.textContent = `Satuan: [ ${q.unit} ]`;
        unitEl.removeAttribute('hidden');
      } else {
        unitEl.setAttribute('hidden', '');
      }
    }

    if (inputEl) {
      inputEl.value = state.currentAnswer || '';
      inputEl.dataset.questionId = q.id;
      inputEl.focus();
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
          feedbackEl.textContent = `${state.instantCheck.feedback} (Kunci: ${q.answer})`;
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
      const isAns = (state.answers[q.id] || '').trim().length > 0;
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
      items = items.filter(i => i.evaluation.status === 'incorrect' || i.evaluation.status === 'review');
    } else if (filter === 'correct') {
      items = items.filter(i => i.evaluation.status === 'correct');
    } else if (filter === 'empty') {
      items = items.filter(i => i.evaluation.status === 'empty');
    }

    container.innerHTML = items.map((item, idx) => {
      const q = item.question;
      const ev = item.evaluation;
      const statusClass = ev.status === 'correct' ? 'badge-correct' : ev.status === 'empty' ? 'badge-empty' : 'badge-wrong';
      const statusText = ev.status === 'correct' ? 'BENAR' : ev.status === 'empty' ? 'KOSONG' : 'SALAH';

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

          <p class="review-q-text">${q.question}</p>

          <div class="review-comparison-grid">
            <div class="answer-box user-box ${ev.status}">
              <span class="box-label">Jawaban Anda:</span>
              <span class="box-value">${item.userAnswer || '<em class="text-muted">(Tidak dijawab)</em>'}</span>
            </div>
            <div class="answer-box target-box">
              <span class="box-label">Kunci Dokumen Resmi:</span>
              <span class="box-value">${q.answer}</span>
            </div>
          </div>

          ${q.acceptedAnswers && q.acceptedAnswers.length > 1 ? `
            <div class="accepted-variants-note">
              <small>Variasi diterima: ${q.acceptedAnswers.join(' | ')}</small>
            </div>
          ` : ''}

          <div class="review-citation-footer">
            <span>📄 Dokumen: ${q.sourceDocument} ${q.sourcePage ? `(Hal. ${q.sourcePage})` : ''}</span>
            <span>Nilai: ${ev.score} / ${q.points || 1} poin</span>
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
  // PAPER / MANUAL EXAM MODE
  // ==========================================
  function openPaperMode(aircraftId) {
    QuestionLoader.loadAircraftData(aircraftId).then(data => {
      openPaperView(data, data.questions);
    });
  }

  function openPaperView(data, questions) {
    const container = document.getElementById('paper-sheet-content');
    const titleEl = document.getElementById('paper-aircraft-title');
    const docEl = document.getElementById('paper-source-doc');

    if (titleEl) titleEl.textContent = data.title;
    if (docEl) docEl.textContent = data.sourceDocument;

    // Group questions by Section
    const sections = [...new Set(questions.map(q => q.section))];

    container.innerHTML = sections.map(sec => {
      const secQuestions = questions.filter(q => q.section === sec);
      return `
        <div class="paper-section-block">
          <h2 class="paper-section-title">${sec}</h2>
          <div class="paper-questions-list">
            ${secQuestions.map((q, idx) => `
              <div class="paper-question-item">
                <div class="paper-q-text">
                  <span class="paper-q-num">${idx + 1}.</span>
                  <span class="paper-q-body">${q.question}</span>
                  <span class="paper-dots">..........................................................................................</span>
                  <span class="paper-unit">${q.unit ? `[ ${q.unit} ]` : ''}</span>
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    }).join('');

    Navigation.navigateTo('paper');
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
          ExamEngine.nextQuestion();
        } else if (e.key === 'ArrowLeft' && e.altKey) {
          ExamEngine.prevQuestion();
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
    onAnswerKeyDown,
    promptSubmitExam,
    filterReview,
    retakeWrongOnly,
    exportResultCSV,
    openPaperMode,
    renderBankFiltered,
    exportBankJSON,
    clearAllHistory
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
