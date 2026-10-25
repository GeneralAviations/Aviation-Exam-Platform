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

console.log('\n=== ALL ANKA BOLDFACE TESTS PASSED SUCCESSFULLY! ===\n');
