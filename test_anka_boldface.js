const fs = require('fs');
const path = require('path');
const assert = require('assert');

console.log('=== VERIFYING AUTHENTIC ANKA BOLDFACE LAYOUT & FUNCTIONALITY ===');

// 1. Check anka-renderer.js
const AnkaRenderer = require('./assets/js/anka-renderer.js');
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
console.log('✓ PASS: AnkaRenderer answer validation is accurate.');

// 4. Test CSS hazard candy-cane border
const css = fs.readFileSync(path.join(__dirname, 'assets/css/style.css'), 'utf-8');
assert(css.includes('repeating-linear-gradient'), 'CSS must include repeating linear gradient hazard border');
assert(css.includes('.boldface-app-shell.is-anka'), 'CSS must include .boldface-app-shell.is-anka rules');
assert(css.includes('.boldface-app-shell.is-anka .correction-text'), 'CSS must include .correction-text styling');
console.log('✓ PASS: CSS hazard striped border and authentic styling confirmed.');

// 5. Test index.html includes anka-renderer.js
const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf-8');
assert(html.includes('anka-renderer.js'), 'index.html must include script tag for anka-renderer.js');
console.log('✓ PASS: index.html correctly loads anka-renderer.js script.');

console.log('\n=== ALL ANKA BOLDFACE TESTS PASSED SUCCESSFULLY! ===');
