/**
 * Storage Manager for Aviation Examination & Training Platform
 * Handles LocalStorage persistence with error handling and fallback.
 */
const Storage = (() => {
  const PREFIX = 'aetp_v1_';

  const isAvailable = () => {
    try {
      const test = '__storage_test__';
      localStorage.setItem(test, test);
      localStorage.removeItem(test);
      return true;
    } catch (e) {
      console.warn('LocalStorage is not available:', e);
      return false;
    }
  };

  const get = (key, defaultValue = null) => {
    if (!isAvailable()) return defaultValue;
    try {
      const val = localStorage.getItem(PREFIX + key);
      return val ? JSON.parse(val) : defaultValue;
    } catch (e) {
      console.error(`Error reading key ${key} from storage:`, e);
      return defaultValue;
    }
  };

  const set = (key, value) => {
    if (!isAvailable()) return false;
    try {
      localStorage.setItem(PREFIX + key, JSON.stringify(value));
      return true;
    } catch (e) {
      console.error(`Error saving key ${key} to storage:`, e);
      return false;
    }
  };

  const remove = (key) => {
    if (!isAvailable()) return;
    try {
      localStorage.removeItem(PREFIX + key);
    } catch (e) {
      console.error(`Error removing key ${key} from storage:`, e);
    }
  };

  // Aircraft-specific draft answers
  const getDraftAnswers = (aircraft) => {
    return get(`answers_${aircraft}`, {});
  };

  const saveDraftAnswers = (aircraft, answers) => {
    return set(`answers_${aircraft}`, answers);
  };

  const clearDraftAnswers = (aircraft) => {
    remove(`answers_${aircraft}`);
  };

  // Aircraft-specific flags
  const getDraftFlags = (aircraft) => {
    return get(`flags_${aircraft}`, []);
  };

  const saveDraftFlags = (aircraft, flags) => {
    return set(`flags_${aircraft}`, flags);
  };

  // Exam History
  const getHistory = () => {
    return get('history', []);
  };

  const saveExamResult = (record) => {
    const list = getHistory();
    list.unshift({
      id: 'EXAM-' + Date.now(),
      timestamp: new Date().toISOString(),
      ...record
    });
    // keep maximum 50 records
    return set('history', list.slice(0, 50));
  };

  const clearHistory = () => {
    remove('history');
  };

  // Settings
  const getSettings = () => {
    return get('settings', {
      theme: 'dark',
      passingScore: 75,
      soundEffects: true
    });
  };

  const updateSettings = (updates) => {
    const current = getSettings();
    const updated = { ...current, ...updates };
    set('settings', updated);
    return updated;
  };

  return {
    isAvailable,
    get,
    set,
    remove,
    getDraftAnswers,
    saveDraftAnswers,
    clearDraftAnswers,
    getDraftFlags,
    saveDraftFlags,
    getHistory,
    saveExamResult,
    clearHistory,
    getSettings,
    updateSettings
  };
})();

if (typeof module !== 'undefined' && module.exports) {
  module.exports = Storage;
}
if (typeof globalThis !== 'undefined') {
  globalThis.Storage = Storage;
}
