/**
 * Exam Engine for Aviation Examination & Training Platform
 * Manages active session, navigation, timers, instant auto-save, and submissions.
 */
const ExamEngine = (() => {
  let session = null;
  let timerInterval = null;
  let onUpdateCallback = null;
  let onFinishCallback = null;

  /**
   * Starts a new exam or training session
   */
  function startSession(config, onUpdate, onFinish) {
    clearInterval(timerInterval);
    onUpdateCallback = onUpdate;
    onFinishCallback = onFinish;

    const savedAnswers = (typeof Storage !== 'undefined' ? Storage.getDraftAnswers(config.aircraft) : {}) || {};
    const savedFlags = (typeof Storage !== 'undefined' ? Storage.getDraftFlags(config.aircraft) : []) || [];

    // Combine any existing answers if resuming or start clean
    const answers = config.resume ? { ...savedAnswers } : {};
    const flags = config.resume ? [...savedFlags] : [];

    session = {
      aircraft: config.aircraft,
      aircraftData: config.aircraftData,
      mode: config.mode || 'exam', // 'practice', 'exam', 'manual'
      questions: config.questions || [],
      currentIndex: 0,
      answers: answers,
      flags: flags,
      revealedAnswers: {}, // used in practice mode
      instantFeedback: {}, // used in practice mode
      startTime: Date.now(),
      endTime: null,
      timerDuration: (config.timerMinutes || 0) * 60, // seconds
      timeRemaining: (config.timerMinutes || 0) * 60,
      timerActive: Boolean(config.timerMinutes && config.timerMinutes > 0),
      isCompleted: false
    };

    // If starting fresh (not resume), save initial state
    if (!config.resume && typeof Storage !== 'undefined') {
      Storage.saveDraftAnswers(session.aircraft, session.answers);
      Storage.saveDraftFlags(session.aircraft, session.flags);
    }

    if (session.timerActive) {
      startTimer();
    }

    if (onUpdateCallback) onUpdateCallback(getState());
    return session;
  }

  function startTimer() {
    clearInterval(timerInterval);
    timerInterval = setInterval(() => {
      if (!session || session.isCompleted) {
        clearInterval(timerInterval);
        return;
      }

      session.timeRemaining--;

      if (session.timeRemaining === 300) {
        if (typeof window !== 'undefined' && window.App && window.App.showToast) {
          window.App.showToast('Peringatan: Waktu pengerjaan tersisa 5 menit!', 'warning');
        }
      }

      if (session.timeRemaining <= 0) {
        clearInterval(timerInterval);
        session.timeRemaining = 0;
        if (typeof window !== 'undefined' && window.App && window.App.showToast) {
          window.App.showToast('Waktu ujian telah habis! Ujian dikumpulkan secara otomatis.', 'error');
        }
        submitExam(true);
      } else {
        if (onUpdateCallback) onUpdateCallback(getState());
      }
    }, 1000);
  }

  function formatTime(seconds) {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  }

  function getState() {
    if (!session) return null;
    const currentQ = session.questions[session.currentIndex] || null;
    const answeredCount = Object.keys(session.answers).filter(id => {
      const ans = session.answers[id];
      if (typeof ans === 'object' && ans !== null) {
        return Object.values(ans).some(v => (v || '').trim().length > 0);
      }
      return (ans || '').trim().length > 0;
    }).length;

    return {
      aircraft: session.aircraft,
      mode: session.mode,
      totalQuestions: session.questions.length,
      currentIndex: session.currentIndex,
      currentQuestion: currentQ,
      currentAnswer: currentQ ? (session.answers[currentQ.id] !== undefined ? session.answers[currentQ.id] : '') : '',
      isFlagged: currentQ ? session.flags.includes(currentQ.id) : false,
      answers: session.answers,
      flags: session.flags,
      answeredCount,
      unansweredCount: session.questions.length - answeredCount,
      timeRemaining: session.timeRemaining,
      timeFormatted: formatTime(session.timeRemaining),
      timerActive: session.timerActive,
      revealed: currentQ ? Boolean(session.revealedAnswers[currentQ.id]) : false,
      instantCheck: currentQ ? session.instantFeedback[currentQ.id] : null,
      isCompleted: session.isCompleted,
      questions: session.questions
    };
  }

  function setAnswer(questionId, value, subId = null) {
    if (!session || session.isCompleted) return;

    if (subId) {
      if (typeof session.answers[questionId] !== 'object' || session.answers[questionId] === null) {
        session.answers[questionId] = {};
      }
      session.answers[questionId][subId] = value;
    } else {
      session.answers[questionId] = value;
    }

    // Persist draft immediately
    if (typeof Storage !== 'undefined') {
      Storage.saveDraftAnswers(session.aircraft, session.answers);
    }

    // If in practice mode and feedback was showing, re-evaluate or clear
    if (session.mode === 'practice' && session.instantFeedback[questionId]) {
      const q = session.questions.find(item => item.id === questionId);
      if (q && typeof Grading !== 'undefined') {
        session.instantFeedback[questionId] = Grading.evaluateAnswer(
          session.answers[questionId],
          q.answer,
          q.acceptedAnswers,
          q.unit,
          q.subQuestions
        );
      }
    }

    if (onUpdateCallback) onUpdateCallback(getState());
  }

  function toggleFlag(questionId) {
    if (!session) return;
    const idx = session.flags.indexOf(questionId);
    if (idx >= 0) {
      session.flags.splice(idx, 1);
    } else {
      session.flags.push(questionId);
    }
    if (typeof Storage !== 'undefined') {
      Storage.saveDraftFlags(session.aircraft, session.flags);
    }
    if (onUpdateCallback) onUpdateCallback(getState());
  }

  function nextQuestion() {
    if (!session) return;
    if (session.currentIndex < session.questions.length - 1) {
      session.currentIndex++;
      if (onUpdateCallback) onUpdateCallback(getState());
    }
  }

  function prevQuestion() {
    if (!session) return;
    if (session.currentIndex > 0) {
      session.currentIndex--;
      if (onUpdateCallback) onUpdateCallback(getState());
    }
  }

  function jumpTo(index) {
    if (!session) return;
    if (index >= 0 && index < session.questions.length) {
      session.currentIndex = index;
      if (onUpdateCallback) onUpdateCallback(getState());
    }
  }

  // Practice mode: Reveal reference answer
  function revealAnswer(questionId) {
    if (!session || session.mode === 'exam') return;
    session.revealedAnswers[questionId] = true;
    const q = session.questions.find(item => item.id === questionId);
    if (q) {
      if (q.subQuestions && Array.isArray(q.subQuestions) && q.subQuestions.length > 0) {
        const obj = {};
        q.subQuestions.forEach(sub => {
          obj[sub.id] = sub.answer;
        });
        session.answers[questionId] = obj;
      } else {
        session.answers[questionId] = q.answer;
      }
      if (typeof Storage !== 'undefined') {
        Storage.saveDraftAnswers(session.aircraft, session.answers);
      }
      session.instantFeedback[questionId] = {
        status: 'correct',
        isCorrect: true,
        feedback: 'Kunci jawaban ditampilkan (Mode Latihan)'
      };
    }
    if (onUpdateCallback) onUpdateCallback(getState());
  }

  // Practice mode: Check single answer
  function checkSingleAnswer(questionId) {
    if (!session || session.mode === 'exam') return;
    const q = session.questions.find(item => item.id === questionId);
    if (!q) return;
    const userVal = session.answers[questionId] !== undefined ? session.answers[questionId] : '';
    if (typeof Grading !== 'undefined') {
      const res = Grading.evaluateAnswer(userVal, q.answer, q.acceptedAnswers, q.unit, q.subQuestions);
      session.instantFeedback[questionId] = res;
    }
    if (onUpdateCallback) onUpdateCallback(getState());
  }

  function submitExam(isAuto = false) {
    if (!session || session.isCompleted) return;
    clearInterval(timerInterval);
    session.isCompleted = true;
    session.endTime = Date.now();

    const elapsedSeconds = Math.round((session.endTime - session.startTime) / 1000);
    const settings = typeof Storage !== 'undefined' ? Storage.getSettings() : { passingScore: 75 };
    const results = typeof Grading !== 'undefined' 
      ? Grading.calculateExamResults(session.questions, session.answers, settings.passingScore)
      : { finalScore: 0, categories: [] };

    const submissionRecord = {
      aircraft: session.aircraft,
      mode: session.mode,
      finalScore: results.finalScore,
      totalQuestions: results.totalQuestions,
      correctCount: results.correctCount,
      wrongCount: results.wrongCount,
      emptyCount: results.emptyCount,
      reviewCount: results.reviewCount,
      isPassed: results.isPassed,
      durationSeconds: elapsedSeconds,
      categories: results.categories
    };

    // Save to persistent exam history
    if (typeof Storage !== 'undefined') {
      Storage.saveExamResult(submissionRecord);
      // Clear draft answers now that exam is finalized
      Storage.clearDraftAnswers(session.aircraft);
    }

    const fullResultPayload = {
      ...results,
      elapsedSeconds,
      elapsedFormatted: formatTime(elapsedSeconds),
      submissionRecord,
      aircraftData: session.aircraftData,
      isAuto
    };

    if (onFinishCallback) {
      onFinishCallback(fullResultPayload);
    }

    return fullResultPayload;
  }

  function endSession() {
    clearInterval(timerInterval);
    session = null;
  }

  return {
    startSession,
    getState,
    setAnswer,
    toggleFlag,
    nextQuestion,
    prevQuestion,
    jumpTo,
    revealAnswer,
    checkSingleAnswer,
    submitExam,
    endSession
  };
})();

if (typeof module !== 'undefined' && module.exports) {
  module.exports = ExamEngine;
}
if (typeof globalThis !== 'undefined') {
  globalThis.ExamEngine = ExamEngine;
}
