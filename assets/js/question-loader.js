/**
 * Question Loader for Aviation Examination & Training Platform
 * Fetches aircraft catalogs and question banks via relative paths.
 */
const QuestionLoader = (() => {
  const cache = {};
  let aircraftCatalog = null;

  /**
   * Fetches the master aircraft catalog
   */
  async function loadCatalog() {
    if (aircraftCatalog) return aircraftCatalog;
    try {
      const res = await fetch('./data/aircraft-index.json');
      if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
      aircraftCatalog = await res.json();
      return aircraftCatalog;
    } catch (e) {
      console.error('Failed to load aircraft catalog:', e);
      throw e;
    }
  }

  /**
   * Loads the full question bank for an aircraft
   */
  async function loadAircraftData(aircraftId) {
    if (cache[aircraftId]) return cache[aircraftId];

    // Find file from catalog or resolve standard filename
    let filename = '';
    const norm = aircraftId.toLowerCase();
    if (norm.includes('mi-17') || norm.includes('mi17')) {
      filename = 'data/mi-17v5.json';
    } else if (norm.includes('412')) {
      filename = 'data/bell-412-ep.json';
    } else if (norm.includes('fennec')) {
      filename = 'data/fennec-as550.json';
    } else if (norm.includes('sikorsky') || norm.includes('s300')) {
      filename = 'data/sikorsky-s300c.json';
    } else if (norm.includes('casa') || norm.includes('212') || norm.includes('aviocar')) {
      filename = 'data/casa-212-200.json';
    } else if (norm.includes('ah-64') || norm.includes('ah64') || norm.includes('apache')) {
      filename = 'data/ah-64e.json';
    } else if (norm.includes('bo-105') || norm.includes('bo105')) {
      filename = 'data/bo-105.json';
    } else {
      const catalog = await loadCatalog();
      const entry = catalog.find(c => c.aircraft === aircraftId);
      if (entry) filename = entry.file;
    }

    if (!filename) throw new Error(`Unknown aircraft ID: ${aircraftId}`);

    try {
      const res = await fetch('./' + filename);
      if (!res.ok) throw new Error(`HTTP error! status: ${res.status} when loading ${filename}`);
      const data = await res.json();
      cache[aircraftId] = data;
      return data;
    } catch (e) {
      console.error(`Error loading aircraft data for ${aircraftId}:`, e);
      throw e;
    }
  }

  /**
   * Shuffles an array immutably using Fisher-Yates
   */
  function shuffle(array) {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  /**
   * Filters and prepares questions based on exam configuration
   */
  function prepareQuestions(aircraftData, options = {}) {
    let list = [...(aircraftData.questions || [])];

    // Filter by selected categories if provided
    if (options.categories && options.categories.length > 0 && !options.categories.includes('ALL')) {
      list = list.filter(q => options.categories.includes(q.category));
    }

    // Filter by section if provided
    if (options.section && options.section !== 'ALL') {
      list = list.filter(q => q.section === options.section);
    }

    // Filter specific IDs (e.g., for retaking wrong questions)
    if (options.specificIds && options.specificIds.length > 0) {
      list = list.filter(q => options.specificIds.includes(q.id));
    }

    // Shuffle if enabled
    if (options.shuffle) {
      list = shuffle(list);
    }

    // Limit count if specified and valid
    if (options.limit && options.limit > 0 && options.limit < list.length) {
      list = list.slice(0, options.limit);
    }

    return list;
  }

  return {
    loadCatalog,
    loadAircraftData,
    prepareQuestions,
    shuffle
  };
})();

if (typeof module !== 'undefined' && module.exports) {
  module.exports = QuestionLoader;
}
if (typeof globalThis !== 'undefined') {
  globalThis.QuestionLoader = QuestionLoader;
}
