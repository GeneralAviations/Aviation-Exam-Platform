import re
import json

with open('anka_full_original.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('data/anka-male-uav.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

sec_map = {
    'tab-1': {
        'title': '1. BOLD FACE LIMITATIONS',
        'short': 'LIMITATIONS',
        'sectionName': 'BOLD FACE LIMITATIONS'
    },
    'tab-2': {
        'title': '2. EMER - ACT POSITION FAIL',
        'short': 'ACT POSITION FAIL',
        'sectionName': 'EMER - ACT POSITION FAIL'
    },
    'tab-3': {
        'title': '3. EMER - ENG RPM HIGH',
        'short': 'ENG RPM HIGH',
        'sectionName': 'EMER - ENG RPM HIGH'
    },
    'tab-4': {
        'title': '4. EMER - ENG RPM LOW',
        'short': 'ENG RPM LOW',
        'sectionName': 'EMER - ENG RPM LOW'
    },
    'tab-5': {
        'title': '5. EMER - LDG GR EXTENTION FAIL',
        'short': 'LDG GR EXTENTION FAIL',
        'sectionName': 'EMER - LDG GR EXTENTION FAIL'
    },
    'tab-6': {
        'title': '6. EMER - ENG STOPPED',
        'short': 'ENG STOPPED',
        'sectionName': 'EMER - ENG STOPPED'
    }
}

sections = re.findall(r'<section class="page-section[^"]*" data-page="([^"]+)">(.*?)</section>', content, re.DOTALL)

tab_data = []

for page, shtml in sections:
    meta = sec_map.get(page)
    sname = meta['sectionName']
    qs = [q for q in d['questions'] if q['section'] == sname]
    
    counter = [0]
    
    def replacer(match):
        idx = counter[0]
        if idx >= len(qs):
            return match.group(0)
        
        q = qs[idx]
        counter[0] += 1
        
        attrs = match.group(1)
        cls = "answer-input paper-answer-input"
        if "inline-input" in attrs:
            cls += " inline-input"
        
        maxl_m = re.search(r'maxlength="(\d+)"', attrs)
        maxl = maxl_m.group(1) if maxl_m else "40"
        
        accepted_list = q.get("acceptedAnswers", [q["answer"]])
        accepted_str = "|".join(accepted_list).replace('"', '&quot;')
        clean_ans = q["answer"].replace('"', '&quot;')
        
        return (f'<input class="{cls}" '
                f'id="paper-input-{q["id"]}" '
                f'type="text" '
                f'data-qid="{q["id"]}" '
                f'data-tab="{page}" '
                f'data-answer="{clean_ans}" '
                f'data-accepted="{accepted_str}" '
                f'maxlength="{maxl}" '
                f'autocomplete="off" '
                f'spellcheck="false" '
                f'oninput="App.onBoldFaceInput(\'{q["id"]}\')" '
                f'onkeydown="App.onBoldFaceKeyDown(event, \'{q["id"]}\')" />')
    
    # Strip any existing correction-text
    cleaned_shtml = re.sub(r'<span class="correction-text"[^>]*>.*?</span>', '', shtml)
    new_shtml = re.sub(r'<input\b([^>]*)>', replacer, cleaned_shtml)
    
    tab_data.append({
        'id': page,
        'title': meta['title'],
        'short': meta['short'],
        'sectionName': sname,
        'count': len(qs),
        'html': new_shtml.strip()
    })

js_content = """/**
 * ANKA MALE UAV - Dedicated Authentic Layout Renderer
 * Recreates the exact authentic document layout from https://generalaviations.github.io/Soal-latihan-anka/
 * Includes:
 *  - Candy-cane diagonal hazard striped border
 *  - Official military UAV section headers (TRAINING ONLY / ANKA / LIMITATIONS)
 *  - Dotted leader lines for Airspeed and Performance limits
 *  - Authentic gold-header tables (Wind limits, KU-Band 2D table, System limits)
 *  - Inline condition blanks (Takeoff, Landing, Weather avoidance)
 *  - All 6 authentic modules (Limitations + 5 Emergency Procedures)
 *  - Integrated live answer validation and correction display
 */
const AnkaRenderer = (() => {
  const tabs = """ + json.dumps(tab_data, indent=2, ensure_ascii=False) + """;

  function getTabs() {
    return tabs;
  }

  function renderSections(activeTab = 'tab-1') {
    return tabs.map(tab => {
      const isActive = activeTab === 'ALL' || activeTab === tab.id;
      return `
        <div class="anka-tab-section-wrapper" id="anka-sec-${tab.id}" style="display: ${isActive ? 'block' : 'none'};">
          <section class="page-section ${isActive ? 'active' : ''}" data-page="${tab.id}" data-section="${tab.sectionName}">
            ${tab.html}
          </section>
        </div>
      `;
    }).join('\\n');
  }

  function setActiveTab(tabId) {
    tabs.forEach(tab => {
      const wrap = document.getElementById(`anka-sec-${tab.id}`);
      if (wrap) {
        const show = tabId === 'ALL' || tabId === tab.id;
        wrap.style.display = show ? 'block' : 'none';
        const sec = wrap.querySelector('.page-section');
        if (sec) {
          sec.classList.toggle('active', show);
        }
      }
    });

    document.querySelectorAll('.bf-tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tabSec === tabId);
    });
  }

  function normalize(value) {
    return String(value || '')
      .replace(/\\u00A0/g, ' ')
      .trim()
      .toLowerCase()
      .replace(/[\\u00b0\\u00ba]/g, '')
      .replace(/[_-]/g, ' ')
      .replace(/kias|kts|knots?|deg|degrees|km|kgs?|kg|psi|bar|ft|msl|v|volts?|amps?|c|percent|vs|%/g, ' ')
      .replace(/[,]/g, '.')
      .replace(/\\./g, '')
      .replace(/[^0-9+\\-\\s]/g, ' ')
      .replace(/\\s+/g, ' ')
      .trim();
  }

  function exactAnswerMatch(answer, value) {
    return normalize(answer) === normalize(value);
  }

  function numericAnswerMatch(answer, value) {
    const answerDigits = String(answer || '').replace(/[^\\d-]/g, '');
    const valueDigits = String(value || '').replace(/[^\\d-]/g, '');
    return Boolean(answerDigits && valueDigits && answerDigits === valueDigits);
  }

  function isAnswerCorrect(acceptedAnswers, userValue) {
    if (!userValue || !userValue.trim()) return false;
    const list = Array.isArray(acceptedAnswers) ? acceptedAnswers : String(acceptedAnswers || '').split('|');
    return list.some(ans => {
      const clean = ans.trim();
      return exactAnswerMatch(clean, userValue) || numericAnswerMatch(clean, userValue);
    });
  }

  return {
    getTabs,
    renderSections,
    setActiveTab,
    isAnswerCorrect,
    normalize
  };
})();

if (typeof module !== 'undefined' && module.exports) {
  module.exports = AnkaRenderer;
}
"""

with open('assets/js/anka-renderer.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated assets/js/anka-renderer.js ({len(js_content)} characters)")
