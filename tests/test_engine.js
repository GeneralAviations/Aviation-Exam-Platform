/**
 * Exam Engine and Storage Integration Test
 */
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');

console.log('--- Test: Exam Engine & Storage Simulation ---');

// Mock localStorage in Node
const storageMap = {};
global.localStorage = {
  getItem: (k) => storageMap[k] || null,
  setItem: (k, v) => { storageMap[k] = String(v); },
  removeItem: (k) => { delete storageMap[k]; },
  clear: () => { Object.keys(storageMap).forEach(k => delete storageMap[k]); }
};

// Load modules
eval(fs.readFileSync(path.join(ROOT_DIR, 'assets/js/storage.js'), 'utf8'));
eval(fs.readFileSync(path.join(ROOT_DIR, 'assets/js/grading.js'), 'utf8'));
eval(fs.readFileSync(path.join(ROOT_DIR, 'assets/js/question-loader.js'), 'utf8'));
eval(fs.readFileSync(path.join(ROOT_DIR, 'assets/js/exam-engine.js'), 'utf8'));

// Test question set
const b412Data = JSON.parse(fs.readFileSync(path.join(ROOT_DIR, 'data/bell-412-ep.json'), 'utf8'));

console.log(`Starting mock exam session for ${b412Data.aircraft} with ${b412Data.questions.length} questions...`);

let stateUpdates = 0;
let finalResult = null;

ExamEngine.startSession({
  aircraft: b412Data.aircraft,
  aircraftData: b412Data,
  mode: 'exam',
  timerMinutes: 30,
  questions: b412Data.questions,
  resume: false
}, (state) => {
  stateUpdates++;
}, (result) => {
  finalResult = result;
});

let st = ExamEngine.getState();
console.log(`Session initialized. Current Q: #${st.currentIndex + 1} (${st.currentQuestion.id})`);

// Answer question 1
ExamEngine.setAnswer(st.currentQuestion.id, '1 pilot who shall operate helicopter on right crew seat');
// Flag question 1
ExamEngine.toggleFlag(st.currentQuestion.id);

st = ExamEngine.getState();
console.log(`Q1 answered: '${st.currentAnswer}', flagged: ${st.isFlagged}`);
console.log(`Draft answers saved in LocalStorage:`, Storage.getDraftAnswers(b412Data.aircraft));

// Advance to Q2
ExamEngine.nextQuestion();
st = ExamEngine.getState();
console.log(`Advanced to Q2: #${st.currentIndex + 1} (${st.currentQuestion.id}) - Question: ${st.currentQuestion.question}`);

// Navigate directly to Q10
ExamEngine.jumpTo(9);
st = ExamEngine.getState();
console.log(`Jumped to index 9: Q #${st.currentIndex + 1} (${st.currentQuestion.id})`);

// Save answer for Q10
ExamEngine.setAnswer(st.currentQuestion.id, '140 KIAS');

// Complete and submit exam
console.log('\nSubmitting exam session...');
const examSummary = ExamEngine.submitExam();

console.log('Exam completed successfully!');
console.log(`Final Score: ${examSummary.finalScore}%`);
console.log(`Status: ${examSummary.isPassed ? 'PASSED (LULUS)' : 'FAILED (TIDAK LULUS)'}`);
console.log(`Correct: ${examSummary.correctCount}, Wrong: ${examSummary.wrongCount}, Empty: ${examSummary.emptyCount}`);
console.log(`History records in LocalStorage:`, Storage.getHistory().length);

if (examSummary.finalScore >= 0 && examSummary.totalQuestions === b412Data.questions.length) {
  console.log('✓ PASS: Exam Engine simulation test passed completely.');
  process.exit(0);
} else {
  console.error('✕ FAIL: Exam Engine simulation state incorrect.');
  process.exit(1);
}
