/**
 * Automated Verification & Test Suite for Aviation Examination & Training Platform
 */
const fs = require('fs');
const path = require('path');
const http = require('http');

const ROOT_DIR = path.resolve(__dirname, '..');

console.log('====================================================');
console.log('🧪 RUNNING AVIATION EXAM PLATFORM AUTOMATED TEST SUITE');
console.log('====================================================');

let totalTests = 0;
let passedTests = 0;
let failedTests = 0;

function assert(condition, message) {
  totalTests++;
  if (condition) {
    passedTests++;
    console.log(`  ✓ PASS: ${message}`);
  } else {
    failedTests++;
    console.error(`  ✕ FAIL: ${message}`);
  }
}

// ----------------------------------------------------
// TEST 1: File Existence & Project Structure
// ----------------------------------------------------
console.log('\n--- Test 1: File Existence & Project Structure ---');
const requiredFiles = [
  'index.html',
  '.nojekyll',
  '.github/workflows/deploy.yml',
  'assets/css/style.css',
  'assets/js/storage.js',
  'assets/js/grading.js',
  'assets/js/question-loader.js',
  'assets/js/exam-engine.js',
  'assets/js/navigation.js',
  'assets/js/anka-renderer.js',
  'assets/js/app.js',
  'data/aircraft-index.json',
  'data/mi-17v5.json',
  'data/bell-412-ep.json',
  'data/fennec-as550.json',
  'data/sikorsky-s300c.json',
  'data/anka-male-uav.json'
];

requiredFiles.forEach(file => {
  const fullPath = path.join(ROOT_DIR, file);
  assert(fs.existsSync(fullPath), `File exists: ${file}`);
});

// ----------------------------------------------------
// TEST 2: Data Banks Schema & Integrity Check
// ----------------------------------------------------
console.log('\n--- Test 2: Data Banks Schema & Integrity ---');
const dataFiles = [
  'data/mi-17v5.json',
  'data/bell-412-ep.json',
  'data/fennec-as550.json',
  'data/sikorsky-s300c.json',
  'data/casa-212-200.json',
  'data/ah-64e.json',
  'data/bo-105.json',
  'data/anka-male-uav.json'
];

const allIds = new Set();
let totalExtractedQuestions = 0;

dataFiles.forEach(df => {
  const content = JSON.parse(fs.readFileSync(path.join(ROOT_DIR, df), 'utf8'));
  assert(Boolean(content.aircraft), `${df} has aircraft identifier (${content.aircraft})`);
  assert(Boolean(content.sourceDocument), `${df} has source document citation (${content.sourceDocument})`);
  assert(Array.isArray(content.questions) && content.questions.length > 0, `${df} contains questions (${content.questions.length})`);
  totalExtractedQuestions += content.questions.length;

  content.questions.forEach((q, idx) => {
    if (allIds.has(q.id)) {
      assert(false, `Duplicate question ID detected: ${q.id}`);
    } else {
      allIds.add(q.id);
    }

    if (!q.question || !q.answer) {
      assert(false, `Question at index ${idx} in ${df} is missing question or answer`);
    }
  });
});

assert(totalExtractedQuestions >= 270, `Total verified questions extracted: ${totalExtractedQuestions} (>= 270 questions)`);

// ----------------------------------------------------
// TEST 3: Grading Engine Unit Tests
// ----------------------------------------------------
console.log('\n--- Test 3: Grading Engine Tests ---');
const Grading = require(path.join(ROOT_DIR, 'assets/js/grading.js'));

assert(typeof Grading.evaluateAnswer === 'function', 'Grading.evaluateAnswer exists');

// Exact matching
const resExact = Grading.evaluateAnswer('82 KIAS', '82 KIAS', ['82', '82 KIAS'], 'KIAS');
assert(resExact.isCorrect && resExact.status === 'correct', 'Exact match evaluates as correct');

// Numeric tolerance matching
const resNumeric = Grading.evaluateAnswer('82', '82 KIAS', ['82', '82 KIAS'], 'KIAS');
assert(resNumeric.isCorrect, 'Numeric variation matches accepted answer');

// Casing & whitespace normalization
const resTrim = Grading.evaluateAnswer('  land as soon as practicable  ', 'LAND AS SOON AS PRACTICABLE');
assert(resTrim.isCorrect, 'Trims and normalizes casing correctly');

// Unit mismatch rejection
const resUnitFail = Grading.evaluateAnswer('1000 m', '1000 ft', [], 'ft');
assert(!resUnitFail.isCorrect, 'Rejects conflicting units (1000 m vs 1000 ft)');

const resSpeedFail = Grading.evaluateAnswer('100 knots', '100 km/h', [], 'km/h');
assert(!resSpeedFail.isCorrect, 'Rejects conflicting speed units (100 knots vs 100 km/h)');

// Empty response check
const resEmpty = Grading.evaluateAnswer('', '100 knots');
assert(resEmpty.status === 'empty' && !resEmpty.isCorrect, 'Detects empty answer');

// Range and symbol normalization tests
const resRange1 = Grading.evaluateAnswer('40 sampai 80', '40 - 80');
assert(resRange1.isCorrect, 'Accepts "sampai" when official answer is "-"');

const resRange2 = Grading.evaluateAnswer('40 - 80', '40 sampai 80');
assert(resRange2.isCorrect, 'Accepts "-" when official answer is "sampai"');

const resAmp1 = Grading.evaluateAnswer('generator & alternator', 'generator dan alternator');
assert(resAmp1.isCorrect, 'Accepts "&" when official answer is "dan"');

const resAmp2 = Grading.evaluateAnswer('generator dan alternator', 'generator & alternator');
assert(resAmp2.isCorrect, 'Accepts "dan" when official answer is "&"');

const resCombined = Grading.evaluateAnswer('40-80 psi & 20-30 c', '40 sampai 80 psi dan 20 sampai 30 c');
assert(resCombined.isCorrect, 'Accepts complex combined "&" and "-" for "DAN" and "SAMPAI"');

// Dual unit slash answer tests (e.g. 109 MPH/ 95 KTS)
const dualAnswer = '109 MPH/ 95 KTS';
assert(Grading.evaluateAnswer('109', dualAnswer).isCorrect, 'Accepts single side 109 when official answer is dual 109 MPH/ 95 KTS');
assert(Grading.evaluateAnswer('95', dualAnswer).isCorrect, 'Accepts single side 95 when official answer is dual 109 MPH/ 95 KTS');
assert(Grading.evaluateAnswer('109/95', dualAnswer).isCorrect, 'Accepts 109/95 when official answer is dual 109 MPH/ 95 KTS');

// Multi-parameter subQuestions check
const s300cData = JSON.parse(fs.readFileSync(path.join(ROOT_DIR, 'data/sikorsky-s300c.json'), 'utf8'));
const s300OilTemp = s300cData.questions.find(q => q.id === 'S300C-LIM-004');
const resSubQ = Grading.evaluateQuestion(s300OilTemp, { sub_a: '260', sub_b: '100-250' });
assert(resSubQ.isCorrect, 'Evaluates multi-input subQuestions accurately for S300C Oil Temp');

// Overall exam calculation
const sampleQuestions = [
  { id: 'Q1', question: 'Gross weight', answer: '11900 Lbs', acceptedAnswers: ['11900'], category: 'Weight', points: 1 },
  { id: 'Q2', question: 'Vne', answer: '140 KIAS', acceptedAnswers: ['140'], category: 'Speed', points: 1 },
  { id: 'Q3', question: 'Airspeed limit', answer: '105 KIAS', acceptedAnswers: ['105'], category: 'Speed', points: 1 }
];
const sampleAnswers = {
  'Q1': '11900',
  'Q2': '140 KIAS',
  'Q3': 'wrong answer'
};
const examResult = Grading.calculateExamResults(sampleQuestions, sampleAnswers, 70);
assert(examResult.finalScore === 67, `Exam score calculated correctly: ${examResult.finalScore}% (expected 67%)`);
assert(examResult.correctCount === 2, 'Correct count is 2');
assert(examResult.wrongCount === 1, 'Wrong count is 1');
assert(examResult.categories.length === 2, 'Category breakdown calculated');

// ----------------------------------------------------
// TEST 4: ANKA Authentic Boldface Layout & Validation
// ----------------------------------------------------
console.log('\n--- Test 4: ANKA Authentic Boldface Layout & Validation ---');
const AnkaRenderer = require(path.join(ROOT_DIR, 'assets/js/anka-renderer.js'));
assert(Boolean(AnkaRenderer), 'AnkaRenderer module loaded');
const ankaTabs = AnkaRenderer.getTabs();
assert(ankaTabs.length === 6, 'AnkaRenderer provides 6 authentic tabs');
const ankaTabCounts = ankaTabs.map(t => t.count);
assert(ankaTabCounts.reduce((a, b) => a + b, 0) === 132, 'All 132 ANKA questions are represented in tabs');

const renderedTab1 = AnkaRenderer.renderSections('tab-1');
assert(renderedTab1.includes('BOLD FACE LIMITATIONS'), 'Tab 1 contains authentic title BOLD FACE LIMITATIONS');
assert(renderedTab1.includes('TRAINING ONLY'), 'Header contains authentic military TRAINING ONLY tag');
assert(renderedTab1.includes('wind-table'), 'Contains authentic Wind table');
assert(renderedTab1.includes('ku-band-table'), 'Contains authentic Ku-Band 2D table');
assert(renderedTab1.includes('limitation-table'), 'Contains authentic System Limitation table');
assert(AnkaRenderer.isAnswerCorrect('108 KIAS', '108 kias'), 'AnkaRenderer normalizes 108 kias to 108 KIAS');
assert(AnkaRenderer.isAnswerCorrect('<= 20 KTS', '20'), 'AnkaRenderer matches 20 to <= 20 KTS');

const indexHtml = fs.readFileSync(path.join(ROOT_DIR, 'index.html'), 'utf8');
assert(indexHtml.includes('anka-renderer.js'), 'index.html includes anka-renderer.js script');

const styleCss = fs.readFileSync(path.join(ROOT_DIR, 'assets/css/style.css'), 'utf8');
assert(styleCss.includes('.boldface-app-shell.is-anka'), 'style.css defines .boldface-app-shell.is-anka styling');
assert(styleCss.includes('repeating-linear-gradient'), 'style.css defines authentic hazard candy-cane border');

// ----------------------------------------------------
// TEST 5: Local HTTP Server Status Check
// ----------------------------------------------------
console.log('\n--- Test 5: HTTP Server Endpoints Check ---');

function testEndpoint(pathname) {
  return new Promise((resolve) => {
    http.get(`http://localhost:8080/${pathname}`, (res) => {
      assert(res.statusCode === 200, `Endpoint http://localhost:8080/${pathname} returned HTTP 200`);
      resolve();
    }).on('error', (err) => {
      assert(false, `Endpoint http://localhost:8080/${pathname} failed: ${err.message}`);
      resolve();
    });
  });
}

(async () => {
  const isServerUp = await new Promise((resolve) => {
    const req = http.get('http://localhost:8080/', () => resolve(true));
    req.on('error', () => resolve(false));
    req.setTimeout(400, () => { req.destroy(); resolve(false); });
  });

  if (isServerUp) {
    await testEndpoint('');
    await testEndpoint('data/aircraft-index.json');
    await testEndpoint('data/mi-17v5.json');
    await testEndpoint('data/bell-412-ep.json');
    await testEndpoint('data/fennec-as550.json');
    await testEndpoint('data/sikorsky-s300c.json');
    await testEndpoint('assets/css/style.css');
    await testEndpoint('assets/js/app.js');
  } else {
    console.log('  ℹ️ INFO: Local HTTP server on :8080 is not running; skipping live endpoint probe.');
  }

  console.log('\n====================================================');
  console.log(`SUMMARY: ${passedTests} / ${totalTests} tests passed (${failedTests} failed)`);
  console.log('====================================================');

  if (failedTests > 0) {
    process.exit(1);
  } else {
    process.exit(0);
  }
})();
