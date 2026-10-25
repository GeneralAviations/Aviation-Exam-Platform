/**
 * Automated Verification & Test Suite for Aviation Examination & Training Platform
 */
const fs = require('fs');
const path = require('path');
const http = require('http');

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
  const fullPath = path.join(__dirname, file);
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
  const content = JSON.parse(fs.readFileSync(path.join(__dirname, df), 'utf8'));
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
const Grading = require('./assets/js/grading.js');
assert(typeof Grading.evaluateAnswer === 'function', 'Grading.evaluateAnswer exists');

// Exact matching
const res1 = Grading.evaluateAnswer('11.900 Lbs', '11.900 Lbs', ['11900 lbs', '11900'], 'Lbs');
assert(res1.isCorrect && res1.status === 'correct', 'Exact match evaluates as correct');

// Accepted variants matching
const res2 = Grading.evaluateAnswer('11900', '11.900 Lbs', ['11900 lbs', '11900'], 'Lbs');
assert(res2.isCorrect, 'Numeric variation matches accepted answer');

// Whitespace and case-insensitivity
const res3 = Grading.evaluateAnswer('   1 PILOT   ', '1 pilot', [], '');
assert(res3.isCorrect, 'Trims and normalizes casing correctly');

// Unit mismatch detection (1000 ft vs 1000 m)
const res4 = Grading.evaluateAnswer('1000 m', '1000 ft', [], 'ft');
assert(!res4.isCorrect, 'Rejects conflicting units (1000 m vs 1000 ft)');

// Speed unit mismatch detection (100 km/h vs 100 knots)
const res5 = Grading.evaluateAnswer('100 knots', '100 km/h', [], 'km/h');
assert(!res5.isCorrect, 'Rejects conflicting speed units (100 knots vs 100 km/h)');

// Empty answer
const res6 = Grading.evaluateAnswer('', '4000 kg', [], 'kg');
assert(!res6.isCorrect && res6.status === 'empty', 'Detects empty answer');

// 'sampai' <-> '-' equivalence
const resSampai1 = Grading.evaluateAnswer('980 sampai 2320', '980-2320', []);
assert(resSampai1.isCorrect, 'Accepts "sampai" when official answer is "-"');
const resSampai2 = Grading.evaluateAnswer('980-2320', '980 sampai 2320', []);
assert(resSampai2.isCorrect, 'Accepts "-" when official answer is "sampai"');

// 'dan' <-> '&' equivalence
const resDan1 = Grading.evaluateAnswer('3000 & 3200', '3000 dan 3200', []);
assert(resDan1.isCorrect, 'Accepts "&" when official answer is "dan"');
const resDan2 = Grading.evaluateAnswer('3000 dan 3200', '3000 & 3200', []);
assert(resDan2.isCorrect, 'Accepts "dan" when official answer is "&"');

// Combined complex range and conjunction equivalence
const resComb = Grading.evaluateAnswer('55 & 115 / 55 - 95', '55 DAN 115 PSI / 55 SAMPAI 95 PSI', []);
assert(resComb.isCorrect, 'Accepts complex combined "&" and "-" for "DAN" and "SAMPAI"');

// Dual-unit and slash alternatives support
const resSlash1 = Grading.evaluateAnswer('109', '109 MPH/ 95 KTS', [], 'MPH / KTS');
assert(resSlash1.isCorrect, 'Accepts single side 109 when official answer is dual 109 MPH/ 95 KTS');
const resSlash2 = Grading.evaluateAnswer('95', '109 MPH/ 95 KTS', [], 'MPH / KTS');
assert(resSlash2.isCorrect, 'Accepts single side 95 when official answer is dual 109 MPH/ 95 KTS');
const resSlash3 = Grading.evaluateAnswer('109/95', '109 MPH/ 95 KTS', [], 'MPH / KTS');
assert(resSlash3.isCorrect, 'Accepts 109/95 when official answer is dual 109 MPH/ 95 KTS');

// Multi-parameter subQuestions check
const s300cData = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/sikorsky-s300c.json'), 'utf8'));
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
// TEST 4: Local HTTP Server Status Check
// ----------------------------------------------------
console.log('\n--- Test 4: HTTP Server Endpoints Check ---');

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
