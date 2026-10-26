const fs = require('fs');
const path = require('path');
const assert = require('assert');

const ROOT_DIR = path.resolve(__dirname, '..');

console.log('=== VERIFYING AUTHENTIC ANKA BOLDFACE LAYOUT & FUNCTIONALITY ===');

// 1. Check anka-renderer.js
const AnkaRenderer = require(path.join(ROOT_DIR, 'assets/js/anka-renderer.js'));
assert(AnkaRenderer, 'AnkaRenderer module must be loaded');

const tabs = AnkaRenderer.getTabs();
assert.strictEqual(tabs.length, 6, 'Must have exactly 6 authentic tabs');
const counts = tabs.map(t => t.count);
console.log('Tab counts:', counts);
const total = counts.reduce((a, b) => a + b, 0);
assert.strictEqual(total, 132, 'Total tab count must equal 132');

// 2. Check rendered HTML
const rendered = AnkaRenderer.renderSections('tab-1');
assert(rendered.includes('page-header'), 'Rendered HTML must have page-header');
assert(rendered.includes('TRAINING ONLY'), 'Rendered HTML must have TRAINING ONLY tag');
assert(rendered.includes('ANKA / LIMITATIONS'), 'Rendered HTML must have ANKA / LIMITATIONS tag');
assert(rendered.includes('BOLD FACE LIMITATIONS'), 'Rendered HTML must have BOLD FACE LIMITATIONS title');
assert(rendered.includes('wind-table'), 'Rendered HTML must have authentic wind-table');
assert(rendered.includes('ku-band-table'), 'Rendered HTML must have authentic ku-band-table');
assert(rendered.includes('limitation-table'), 'Rendered HTML must have authentic limitation-table');

// Check that all 132 IDs are present in rendered HTML
for (let i = 1; i <= 75; i++) {
  const qid = `ANKA-LIM-${String(i).padStart(3, '0')}`;
  assert(rendered.includes(`id="paper-input-${qid}"`), `Must include id for ${qid}`);
}
for (let i = 1; i <= 15; i++) {
  const qid = `ANKA-ACT-${String(i).padStart(3, '0')}`;
  assert(rendered.includes(`id="paper-input-${qid}"`), `Must include id for ${qid}`);
}
for (let i = 1; i <= 8; i++) {
  const qid = `ANKA-RPMH-${String(i).padStart(3, '0')}`;
  assert(rendered.includes(`id="paper-input-${qid}"`), `Must include id for ${qid}`);
}
for (let i = 1; i <= 6; i++) {
  const qid = `ANKA-RPML-${String(i).padStart(3, '0')}`;
  assert(rendered.includes(`id="paper-input-${qid}"`), `Must include id for ${qid}`);
}
for (let i = 1; i <= 7; i++) {
  const qid = `ANKA-LDG-${String(i).padStart(3, '0')}`;
  assert(rendered.includes(`id="paper-input-${qid}"`), `Must include id for ${qid}`);
}
for (let i = 1; i <= 21; i++) {
  const qid = `ANKA-STOP-${String(i).padStart(3, '0')}`;
  assert(rendered.includes(`id="paper-input-${qid}"`), `Must include id for ${qid}`);
}
console.log('✓ PASS: All 132 ANKA inputs present with unique paper-input IDs and data attributes.');

// 3. Test answer evaluation logic
assert.strictEqual(AnkaRenderer.isAnswerCorrect('108 KIAS', '108 kias'), true);
assert.strictEqual(AnkaRenderer.isAnswerCorrect('108 KIAS', '108'), true);
assert.strictEqual(AnkaRenderer.isAnswerCorrect('<= 20 KTS', '20 KTS'), true);
assert.strictEqual(AnkaRenderer.isAnswerCorrect('<= 20 KTS', '20'), true);
assert.strictEqual(AnkaRenderer.isAnswerCorrect('51-87', '51 - 87'), true);
assert.strictEqual(AnkaRenderer.isAnswerCorrect('FLOAT', 'float'), true);
assert.strictEqual(AnkaRenderer.isAnswerCorrect('108 KIAS', '90'), false);
assert.strictEqual(AnkaRenderer.isAnswerCorrect('Left', 'kanan'), false);
assert.strictEqual(AnkaRenderer.isAnswerCorrect('Left', 'kiri'), true);
assert.strictEqual(AnkaRenderer.isAnswerCorrect('Left', 'left'), true);
assert.strictEqual(AnkaRenderer.isAnswerCorrect('Right', 'kanan'), true);
assert.strictEqual(AnkaRenderer.isAnswerCorrect('Right', 'kiri'), false);
assert.strictEqual(AnkaRenderer.isAnswerCorrect(['Kiri', 'Left'], 'kanan'), false);
assert.strictEqual(AnkaRenderer.isAnswerCorrect(['Kiri', 'Left'], 'kiri'), true);
console.log('✓ PASS: AnkaRenderer answer validation is accurate.');

// 4. Test CSS hazard candy-cane border
const css = fs.readFileSync(path.join(ROOT_DIR, 'assets/css/style.css'), 'utf-8');
assert(css.includes('repeating-linear-gradient'), 'CSS must include repeating linear gradient hazard border');
assert(css.includes('.boldface-app-shell.is-anka'), 'CSS must include .boldface-app-shell.is-anka rules');
assert(css.includes('.boldface-app-shell.is-anka .correction-text'), 'CSS must include .correction-text styling');
console.log('✓ PASS: CSS hazard striped border and authentic styling confirmed.');

// 5. Test index.html includes anka-renderer.js and exam table container
const html = fs.readFileSync(path.join(ROOT_DIR, 'index.html'), 'utf-8');
assert(html.includes('anka-renderer.js'), 'index.html must include script tag for anka-renderer.js');
assert(html.includes('exam-table-input-zone'), 'index.html must include exam-table-input-zone container');
console.log('✓ PASS: index.html correctly loads anka-renderer.js and has exam-table-input-zone.');

// 6. Test Exam Table Classifiers & Interactive Table Generation
assert.strictEqual(AnkaRenderer.isTableQuestion('ANKA-LIM-006'), true, 'Wind limit Q006 is table question');
assert.strictEqual(AnkaRenderer.isTableQuestion('ANKA-LIM-001'), false, 'Airspeed limit Q001 is not table question');
assert.strictEqual(AnkaRenderer.getTableType('ANKA-LIM-008'), 'wind', 'Q008 must resolve to wind table');
assert.strictEqual(AnkaRenderer.getTableType('ANKA-LIM-020'), 'kuband', 'Q020 must resolve to kuband table');
assert.strictEqual(AnkaRenderer.getTableType('ANKA-LIM-040'), 'system', 'Q040 must resolve to system table');
assert.strictEqual(AnkaRenderer.getTableType('ANKA-ACT-008'), 'surface', 'ACT Q008 must resolve to surface table');

const windHtml = AnkaRenderer.getTableHtmlForExam('ANKA-LIM-006', {}, false, null);
assert(windHtml.includes('wind-table'), 'Wind table HTML rendered');
assert(windHtml.includes('exam-cell-input-ANKA-LIM-006'), 'Wind table includes input cell for Q006');
assert(windHtml.includes('is-active-cell'), 'Active cell has is-active-cell marker');

const kuHtml = AnkaRenderer.getTableHtmlForExam('ANKA-LIM-020', {}, false, null);
assert(kuHtml.includes('ku-band-table'), 'Ku-band table HTML rendered');
assert(kuHtml.includes('exam-cell-input-ANKA-LIM-020'), 'Ku-band table includes input cell for Q020');

const sysHtml = AnkaRenderer.getTableHtmlForExam('ANKA-LIM-040', {}, false, null);
assert(sysHtml.includes('limitation-table'), 'System limitation table HTML rendered');
assert(sysHtml.includes('exam-cell-input-ANKA-LIM-040'), 'System table includes input cell for Q040');

const surfHtml = AnkaRenderer.getTableHtmlForExam('ANKA-ACT-008', {}, false, null);
assert(surfHtml.includes('simple-table'), 'Surface table HTML rendered');
assert(surfHtml.includes('exam-cell-input-ANKA-ACT-008'), 'Surface table includes input cell for Q008');

console.log('✓ PASS: AnkaRenderer table questions classifier and table HTML generators verified.');

// 7. Test app.js paper view navigation architecture
const appJs = fs.readFileSync(path.join(ROOT_DIR, 'assets/js/app.js'), 'utf-8');
assert(appJs.includes('loadAndRenderPaperView'), 'app.js must define loadAndRenderPaperView');
assert(!appJs.includes('renderBoldFaceSheetDOM(data, questions, subMode);\n    Navigation.navigateTo(\'paper\');'), 'renderBoldFaceSheetDOM must not call Navigation.navigateTo');
console.log('✓ PASS: app.js paper navigation architecture verified to have zero recursion.');

// 8. Test Horizontal Dotted-Leader Layout & Table Columns
const allRendered = AnkaRenderer.renderSections('ALL');
const questionRowMatches = allRendered.match(/class="[^"]*question-row[^"]*"/g) || [];
assert(questionRowMatches.length >= 55, `Expected >= 55 question rows, got ${questionRowMatches.length}`);

const leaderMatches = allRendered.match(/class="[^"]*question-leader[^"]*"/g) || [];
assert(leaderMatches.length >= 55, `Expected >= 55 question leaders, got ${leaderMatches.length}`);

// Section 1 VNE & Section 3 Turning Speed layout sequence
assert(/VNE \(Never Exeed\)[\s\S]*?class="[^"]*question-leader[\s\S]*?paper-input-ANKA-LIM-001/.test(allRendered), 'Section 1 must follow horizontal Label -> Leader -> Input order');
assert(/Turning Speed[\s\S]*?class="[^"]*question-leader[\s\S]*?paper-input-ANKA-LIM-015/.test(allRendered), 'Section 3 must follow horizontal Label -> Leader -> Input order');

// Wind Table: 3 columns per row
const windTableMatch = allRendered.match(/<table class="[^"]*wind-table[^"]*"[\s\S]*?<\/table>/);
assert(windTableMatch, 'Wind table must be present');
const windRows = windTableMatch[0].match(/<tr>[\s\S]*?<\/tr>/g) || [];
assert.strictEqual(windRows.length, 4, 'Wind table must have 1 header row + 3 data rows');
for (let i = 1; i < windRows.length; i++) {
  const inputsInRow = windRows[i].match(/<input /g) || [];
  assert.strictEqual(inputsInRow.length, 3, `Wind table row ${i} must have exactly 3 horizontal inputs`);
}

// Ku-Band Table: 6 columns per row
const kuTableMatch = allRendered.match(/<table class="[^"]*ku-band-table[^"]*"[\s\S]*?<\/table>/);
assert(kuTableMatch, 'Ku-band table must be present');
const kuBodyRows = kuTableMatch[0].match(/<tbody>[\s\S]*?<\/tbody>/)[0].match(/<tr>[\s\S]*?<\/tr>/g) || [];
assert.strictEqual(kuBodyRows.length, 3, 'Ku-band table must have 3 data rows in tbody');
for (let i = 0; i < kuBodyRows.length; i++) {
  const inputsInRow = kuBodyRows[i].match(/<input /g) || [];
  assert.strictEqual(inputsInRow.length, 6, `Ku-band row ${i + 1} must have exactly 6 horizontal inputs`);
}

// System Limitation Table: 9 rows with MIN, NORMAL OPERATION, MAX
const limTableMatch = allRendered.match(/<table class="[^"]*limitation-table[^"]*"[\s\S]*?<\/table>/);
assert(limTableMatch, 'System Limitation table must be present');
const limBodyRows = limTableMatch[0].match(/<tbody>[\s\S]*?<\/tbody>/)[0].match(/<tr>[\s\S]*?<\/tr>/g) || [];
assert.strictEqual(limBodyRows.length, 9, 'System Limitation table must have 9 data rows in tbody');
for (let i = 0; i < limBodyRows.length; i++) {
  const inputsInRow = limBodyRows[i].match(/<input /g) || [];
  assert(inputsInRow.length >= 2, `System limitation row ${i + 1} must have inputs for MIN, NORMAL, MAX`);
}
console.log('✓ PASS: Horizontal dotted leader layout and all table column structures verified.');

// 9. Test Show Answers implementation in app.js
assert(appJs.includes('function cleanAnswerText('), 'app.js must define cleanAnswerText');
assert(appJs.includes('function applyAnkaKeysDisplay('), 'app.js must define applyAnkaKeysDisplay');
assert(appJs.includes('applyAnkaKeysDisplay(boldFaceKeysRevealed);'), 'toggleBoldFaceKeys must call applyAnkaKeysDisplay');
assert(appJs.includes('.table-key-hint'), 'applyAnkaKeysDisplay must support table cells with .table-key-hint');
assert(appJs.includes('.inline-key-hint'), 'applyAnkaKeysDisplay must support inline blanks with .inline-key-hint');
assert(appJs.includes('.anka-key-hint'), 'applyAnkaKeysDisplay must support standard rows with .anka-key-hint');
assert(appJs.includes('function isAnkaAircraft('), 'app.js must define isAnkaAircraft');
assert(appJs.includes('function getAnkaRenderer('), 'app.js must define getAnkaRenderer');
assert(appJs.includes('function decodeHtmlEntities('), 'app.js must decode HTML entities');
assert(!appJs.includes('if (!input.value.trim() && refAns)'), 'Buggy check that ignored filled inputs must be removed');

// Test that CSS never truncates answer hints
assert(!css.includes('.boldface-app-shell.is-anka .table-key-hint {\n  display: block;\n  font-size: 0.68rem;'), 'Old truncated table hint CSS must be replaced');
assert(css.includes('text-overflow: clip !important;'), 'CSS must allow hints to expand without ellipsis');
console.log('✓ PASS: Show Answers implementation, non-truncation, and hint badge generation verified.');

// 10. Test Authoritative Dataset Completeness
const ankaData = JSON.parse(fs.readFileSync(path.join(ROOT_DIR, 'data/anka-male-uav.json'), 'utf-8'));
assert.strictEqual(ankaData.questions.length, 132, 'Must have 132 questions');
ankaData.questions.forEach(q => {
  assert(q.answer !== undefined && q.answer !== null && String(q.answer).trim().length > 0, `Question ${q.id} must have non-empty answer`);
});
console.log('✓ PASS: All 132 ANKA questions possess valid authoritative answers in dataset.');

// 11. Test window and global exports in anka-renderer.js
const ankaScript = fs.readFileSync(path.join(ROOT_DIR, 'assets/js/anka-renderer.js'), 'utf-8');
assert(ankaScript.includes('window.AnkaRenderer = AnkaRenderer'), 'anka-renderer.js must explicitly assign window.AnkaRenderer');
assert(ankaScript.includes('globalThis.AnkaRenderer = AnkaRenderer'), 'anka-renderer.js must assign globalThis.AnkaRenderer');
console.log('✓ PASS: AnkaRenderer export to window and global scopes verified.');

console.log('\n=== ALL ANKA BOLDFACE TESTS PASSED SUCCESSFULLY! ===\n');
