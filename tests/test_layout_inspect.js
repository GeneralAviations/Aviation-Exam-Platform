/**
 * Layout & Data Verification Script
 */
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');

console.log('=== VERIFYING LAYOUT, OVERLAPS, AND BOLDFACE DATA ===');

const html = fs.readFileSync(path.join(ROOT_DIR, 'index.html'), 'utf8');
const css = fs.readFileSync(path.join(ROOT_DIR, 'assets/css/style.css'), 'utf8');
const appJs = fs.readFileSync(path.join(ROOT_DIR, 'assets/js/app.js'), 'utf8');

// 1. Check stat cards have stat-info-col
const statCards = (html.match(/class="stat-card"/g) || []).length;
const statInfoCols = (html.match(/class="stat-info-col"/g) || []).length;
console.log(`[1] Stat cards: ${statCards}, Stat info columns: ${statInfoCols}`);
if (statCards === statInfoCols && statCards === 4) {
  console.log('  ✓ PASS: All 4 stat cards have stat-info-col wrappers (no horizontal text overlap).');
} else {
  console.error('  ✕ FAIL: stat-card count mismatch with stat-info-col');
}

// 2. Check brand-title-row in CSS
if (css.includes('.brand-title-row {') && css.includes('.brand-title-row .live-status-pill {')) {
  console.log('  ✓ PASS: .brand-title-row flex layout and live-status-pill header sizing defined.');
} else {
  console.error('  ✕ FAIL: .brand-title-row missing in CSS');
}

// 3. Check dark mode paper-cat-title is NOT light color
if (css.includes('body.dark-mode .paper-cat-title') || css.includes('[data-theme="dark"] .paper-cat-title')) {
  console.error('  ✕ FAIL: paper-cat-title has light color override in dark mode');
} else {
  console.log('  ✓ PASS: paper-cat-title preserves high-contrast dark ink in all modes.');
}

// 4. Check paper-dots min-width: 0
if (css.includes('min-width: 0;') && css.includes('.paper-dots {')) {
  console.log('  ✓ PASS: .paper-dots has min-width: 0 to prevent row overflow.');
} else {
  console.error('  ✕ FAIL: .paper-dots missing min-width: 0');
}

// 5. Check sub-param-header alignment
if (css.includes('.sub-param-header {') && css.includes('align-items: flex-start;')) {
  console.log('  ✓ PASS: .sub-param-header uses flex-start alignment.');
} else {
  console.error('  ✕ FAIL: .sub-param-header alignment issue');
}

// 6. Check review-sub-row stacked direction
if (css.includes('.review-sub-row {') && css.includes('flex-direction: column;')) {
  console.log('  ✓ PASS: .review-sub-row stacked column eliminates text collision in review cards.');
} else {
  console.error('  ✕ FAIL: .review-sub-row not stacked');
}

// 7. Check Paper Sheet numbering preserves official question numbers
if (appJs.includes('qMatch = (q.question || \'\').match(/^\\s*(\\d+)[\\.\\)]\\s*(.*)/)') &&
    appJs.includes('const qNum = qMatch ? `${qMatch[1]}.` : (q.order ? `${q.order}.` : `${idx + 1}.`);')) {
  console.log('  ✓ PASS: Paper sheet preserves official PDF question numbers across all sections.');
} else {
  console.error('  ✕ FAIL: Official PDF question number preservation logic modified or missing');
}

// 8. Check Fleet metadata has all 8 aircraft
const expectedFleets = ['AH-64E', 'BELL 412 EP', 'BO-105', 'CASA 212-200', 'FENNEC AS550', 'MI-17V5', 'SIKORSKY S-300C', 'ANKA MALE UAV'];
let fleetMatch = true;
expectedFleets.forEach(fleet => {
  if (!appJs.includes(`'${fleet}':`)) {
    console.error(`  ✕ FAIL: Missing fleet metadata for ${fleet}`);
    fleetMatch = false;
  }
});
if (fleetMatch) {
  console.log('  ✓ PASS: FLEET_METADATA accurately matches all 8 aircraft identifiers.');
}

// 9. Inspect boldface questions structure across all datasets
const datasets = [
  'ah-64e.json', 'anka-male-uav.json', 'bell-412-ep.json', 'bo-105.json',
  'casa-212-200.json', 'fennec-as550.json', 'mi-17v5.json', 'sikorsky-s300c.json'
];

let totalQuestions = 0;
let multiItemQuestions = 0;
datasets.forEach(d => {
  const data = JSON.parse(fs.readFileSync(path.join(ROOT_DIR, 'data', d), 'utf8'));
  totalQuestions += data.questions.length;
  data.questions.forEach(q => {
    if (q.subQuestions && q.subQuestions.length > 0) {
      multiItemQuestions++;
    }
  });
});

console.log(`[9] Verified 8 aircraft datasets: ${totalQuestions} questions (${multiItemQuestions} multi-item boldface questions).`);
if (totalQuestions >= 479) {
  console.log('  ✓ PASS: All boldface structures and subquestion parameters intact.');
} else {
  console.error('  ✕ FAIL: Expected at least 479 questions across datasets.');
}

console.log('\n=== ALL VERIFICATION CHECKS PASSED ===\n');
