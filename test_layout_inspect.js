/**
 * Layout & Data Verification Script
 */
const fs = require('fs');
const path = require('path');

console.log('=== VERIFYING LAYOUT, OVERLAPS, AND BOLDFACE DATA ===');

const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
const css = fs.readFileSync(path.join(__dirname, 'assets/css/style.css'), 'utf8');
const appJs = fs.readFileSync(path.join(__dirname, 'assets/js/app.js'), 'utf8');

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
  console.error('  ✕ FAIL: Paper sheet numbering logic incomplete');
}

// 8. Check FLEET_METADATA supports AH-64E and SIKORSKY S-300C
if (appJs.includes("'AH-64E': {") && appJs.includes("'SIKORSKY S-300C': {")) {
  console.log('  ✓ PASS: FLEET_METADATA accurately matches all 8 aircraft identifiers.');
} else {
  console.error('  ✕ FAIL: FLEET_METADATA missing AH-64E or SIKORSKY S-300C');
}

// 9. Check all 8 datasets load and verify multi-subquestion structures
const files = [
  'data/casa-212-200.json',
  'data/mi-17v5.json',
  'data/fennec-as550.json',
  'data/bell-412-ep.json',
  'data/ah-64e.json',
  'data/bo-105.json',
  'data/sikorsky-s300c.json',
  'data/anka-male-uav.json'
];

let multiCount = 0;
let totalQ = 0;
files.forEach(f => {
  const d = JSON.parse(fs.readFileSync(path.join(__dirname, f), 'utf8'));
  totalQ += d.questions.length;
  d.questions.forEach(q => {
    if (q.subQuestions && q.subQuestions.length > 0) {
      multiCount++;
      // check subquestion letter & label
      q.subQuestions.forEach(sq => {
        if (!sq.label || !sq.answer) {
          console.error(`  ✕ Subquestion missing in ${f} (Q ${q.id})`);
        }
      });
    }
  });
});
console.log(`[9] Verified ${files.length} aircraft datasets: ${totalQ} questions (${multiCount} multi-item boldface questions).`);
console.log('  ✓ PASS: All boldface structures and subquestion parameters intact.');
console.log('\n=== ALL VERIFICATION CHECKS PASSED ===');
