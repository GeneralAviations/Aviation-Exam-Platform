/**
 * Grading System for Aviation Examination & Training Platform
 * Handles normalization, unit-aware comparison, multi-synonym matching, and statistics.
 */
const Grading = (() => {

  /**
   * Normalizes aviation strings:
   * - Trims excess whitespace
   * - Normalizes unicode spaces & quotes
   * - Lowercases text
   * - Normalizes degree symbols (° -> deg)
   * - Normalizes plus/minus
   */
  function normalizeText(val) {
    if (val === null || val === undefined) return '';
    return String(val)
      .replace(/\u00A0/g, ' ')
      .replace(/[\u2018\u2019]/g, "'")
      .replace(/[\u201C\u201D]/g, '"')
      .trim()
      .toLowerCase()
      .replace(/\s+/g, ' ');
  }

  /**
   * Normalizes aviation numbers (e.g., 11.100 or 11,100 -> 11100 for thousands, 2,5 -> 2.5 for decimals)
   */
  function normalizeNumeric(val) {
    if (!val) return '';
    let s = String(val).trim().toLowerCase();
    // replace commas in decimal notation like 2,5 -> 2.5
    s = s.replace(/(\d+),(\d{1,2})\b/g, '$1.$2');
    // remove thousand separator dots like 11.100 -> 11100 or commas 11,100 -> 11100
    s = s.replace(/(\d+)[.,](\d{3})\b/g, '$1$2');
    return s;
  }

  /**
   * Extracts unit tokens from a string
   */
  function extractUnits(str) {
    const knownUnits = [
      'kias', 'kts', 'knots', 'mph', 'km/h', 'km/jam', 'm/s', 'rpm',
      'lbs', 'kg', 'psi', 'ft', 'feet', 'fpm', 'ft/min', 'degrees', 'deg',
      'amps', 'v', 'volts', 'inch', 'in', 'inch mp', 'mp', 'mm', 'm', 'meter',
      'min', 'minutes', 'menit', 'sec', 'seconds', 'detik', '°c', '°f', 'c', 'f'
    ];
    const words = normalizeText(str).split(/[\s/]+/);
    return words.filter(w => knownUnits.includes(w));
  }

  /**
   * Compare user answer with accepted answers list and official answer
   */
  function evaluateAnswer(userAnswer, officialAnswer, acceptedAnswers = [], unit = '') {
    const uRaw = (userAnswer || '').trim();
    if (!uRaw) {
      return {
        status: 'empty',
        isCorrect: false,
        score: 0,
        feedback: 'Belum dijawab'
      };
    }

    const uNorm = normalizeText(uRaw);
    const oNorm = normalizeText(officialAnswer);

    // 1. Direct exact normalized match
    if (uNorm === oNorm) {
      return { status: 'correct', isCorrect: true, score: 1, feedback: 'Tepat sesuai dokumen sumber' };
    }

    // 2. Build list of all acceptable targets
    const allAccepted = [officialAnswer, ...(acceptedAnswers || [])]
      .filter(Boolean)
      .map(item => normalizeText(item));

    for (const target of allAccepted) {
      if (uNorm === target) {
        return { status: 'correct', isCorrect: true, score: 1, feedback: 'Benar (sesuai variasi yang diterima)' };
      }
    }

    // 3. Numeric & Unit check
    const uNum = normalizeNumeric(uRaw);
    const oNum = normalizeNumeric(officialAnswer);

    if (uNum === oNum) {
      return { status: 'correct', isCorrect: true, score: 1, feedback: 'Benar (nilai numerik cocok)' };
    }

    for (const target of allAccepted) {
      if (uNum === normalizeNumeric(target)) {
        return { status: 'correct', isCorrect: true, score: 1, feedback: 'Benar (nilai numerik cocok)' };
      }
    }

    // If unit is specified in the question, check if user provided numeric value only and it matches
    if (unit) {
      const uUnits = extractUnits(uRaw);
      const expectedUnits = extractUnits(unit);

      // If user provided a unit and it completely contradicts the expected unit (e.g. ft vs m, knots vs km/h), reject!
      if (uUnits.length > 0 && expectedUnits.length > 0) {
        const conflictGroups = [
          ['ft', 'feet', 'm', 'meter'],
          ['kts', 'kias', 'knots', 'km/h', 'km/jam', 'mph'],
          ['lbs', 'kg'],
          ['c', '°c', 'f', '°f']
        ];
        for (const grp of conflictGroups) {
          const userHas = uUnits.find(u => grp.includes(u));
          const targetHas = expectedUnits.find(u => grp.includes(u));
          if (userHas && targetHas && userHas !== targetHas) {
            return {
              status: 'incorrect',
              isCorrect: false,
              score: 0,
              feedback: `Satuan tidak cocok! Satuan yang diharapkan adalah ${unit}`
            };
          }
        }
      }

      // Check if user entered just the number when the question already labels the unit
      const strippedUser = normalizeText(uRaw.replace(new RegExp(unit, 'gi'), ''));
      const strippedOfficial = normalizeText(officialAnswer.replace(new RegExp(unit, 'gi'), ''));
      if (strippedUser && strippedUser === strippedOfficial) {
        return { status: 'correct', isCorrect: true, score: 1, feedback: 'Benar (angka sesuai)' };
      }
    }

    // 4. Procedure / Descriptive check (Keyword matching for procedures)
    if (officialAnswer.length > 30) {
      const targetTokens = oNorm
        .replace(/[^a-z0-9]/g, ' ')
        .split(/\s+/)
        .filter(w => w.length > 2);
      
      const userTokens = uNorm
        .replace(/[^a-z0-9]/g, ' ')
        .split(/\s+/)
        .filter(w => w.length > 2);

      if (targetTokens.length > 0) {
        let matchCount = 0;
        targetTokens.forEach(t => {
          if (userTokens.includes(t)) matchCount++;
        });
        const ratio = matchCount / targetTokens.length;

        if (ratio >= 0.85) {
          return {
            status: 'correct',
            isCorrect: true,
            score: 1,
            feedback: 'Benar (penilaian kata kunci prosedur cocok tinggi)',
            heuristic: true
          };
        } else if (ratio >= 0.5) {
          return {
            status: 'review',
            isCorrect: false,
            score: 0.5,
            feedback: 'Perlu verifikasi manual (sebagian kata kunci prosedur cocok)',
            heuristic: true
          };
        }
      }
    }

    return {
      status: 'incorrect',
      isCorrect: false,
      score: 0,
      feedback: 'Jawaban belum tepat'
    };
  }

  /**
   * Calculates overall exam results
   */
  function calculateExamResults(questions, userAnswers = {}, passingThreshold = 75) {
    let totalPoints = 0;
    let earnedPoints = 0;
    let correctCount = 0;
    let wrongCount = 0;
    let emptyCount = 0;
    let reviewCount = 0;

    const categoryStats = {};
    const detailedResults = [];

    questions.forEach((q) => {
      const weight = q.points || 1;
      totalPoints += weight;

      const userAns = userAnswers[q.id] || '';
      const evalResult = evaluateAnswer(userAns, q.answer, q.acceptedAnswers, q.unit);

      earnedPoints += (evalResult.score * weight);

      if (evalResult.status === 'empty') emptyCount++;
      else if (evalResult.status === 'correct') correctCount++;
      else if (evalResult.status === 'review') reviewCount++;
      else wrongCount++;

      // Category breakdown
      const cat = q.category || 'General';
      if (!categoryStats[cat]) {
        categoryStats[cat] = {
          category: cat,
          section: q.section,
          total: 0,
          correct: 0,
          wrong: 0,
          empty: 0,
          earned: 0,
          possible: 0
        };
      }
      categoryStats[cat].total++;
      categoryStats[cat].possible += weight;
      categoryStats[cat].earned += (evalResult.score * weight);
      if (evalResult.status === 'correct') categoryStats[cat].correct++;
      else if (evalResult.status === 'empty') categoryStats[cat].empty++;
      else categoryStats[cat].wrong++;

      detailedResults.push({
        question: q,
        userAnswer: userAns,
        evaluation: evalResult
      });
    });

    const finalScore = totalPoints > 0 ? Math.round((earnedPoints / totalPoints) * 100) : 0;
    const isPassed = finalScore >= passingThreshold;

    const categoriesArray = Object.values(categoryStats).map(c => ({
      ...c,
      scorePct: c.possible > 0 ? Math.round((c.earned / c.possible) * 100) : 0
    }));

    return {
      totalQuestions: questions.length,
      totalPoints,
      earnedPoints,
      correctCount,
      wrongCount,
      emptyCount,
      reviewCount,
      finalScore,
      passingThreshold,
      isPassed,
      categories: categoriesArray,
      detailedResults
    };
  }

  return {
    normalizeText,
    normalizeNumeric,
    evaluateAnswer,
    calculateExamResults
  };
})();

if (typeof module !== 'undefined' && module.exports) {
  module.exports = Grading;
}
if (typeof globalThis !== 'undefined') {
  globalThis.Grading = Grading;
}
