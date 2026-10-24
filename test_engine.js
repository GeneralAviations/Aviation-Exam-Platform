/**
 * Exam Engine and Storage Integration Test
 */
const fs = require('fs');

console.log('--- Test 5: Exam Engine & Storage Simulation ---');

// Mock localStorage in Node
const storageMap = {};
global.localStorage = {
  getItem: (k) => storageMap[k] || null,
  setItem: (k, v) => { storageMap[k] = String(v); },
  removeItem: (k) => { delete storageMap[k]; },
  clear: () => { Object.keys(storageMap).forEach(k => delete storageMap[k]); }
};

// Load modules
eval(fs.readFileSync('./assets/js/storage.js', 'utf8'));
eval(fs.readFileSync('./assets/js/grading.js', 'utf8'));
eval(fs.readFileSync('./assets/js/question-loader.js', 'utf8'));
eval(fs.readFileSync('./assets/js/exam-engine.js', 'utf8'));

// Test question set
const b412Data = JSON.parse(fs.readFileSync('./data/bell-412-ep.json', 'utf8'));

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

// Answer Q2
ExamEngine.setAnswer(st.currentQuestion.id, '11900 Lbs');

// Jump to Q10
ExamEngine.jumpTo(9);
st = ExamEngine.getState();
console.log(`Jumped to Q10: #${st.currentIndex + 1} (${st.currentQuestion.id})`);

// Submit exam
console.log('Submitting exam session...');
const submission = ExamEngine.submitExam(false);

console.log(`Exam submitted! Final Score: ${submission.finalScore}%`);
console.log(`Correct: ${submission.correctCount}, Wrong: ${submission.wrongCount}, Empty: ${submission.emptyCount}`);
console.log(`Categories evaluated: ${submission.categories.length}`);
console.log(`History records in LocalStorage: ${Storage.getHistory().length}`);

if (submission.finalScore > 0 && submission.correctCount >= 2 && Storage.getHistory().length === 1) {
  console.log('✓ PASS: Exam Engine lifecycle and storage persistence fully verified!');
  process.exit(0);
} else {
  console.error('✕ FAIL: Exam Engine unexpected state');
  process.exit(1);
}
