import re
import json

with open('anka_full_original.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('data/anka-male-uav.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

sec_map = {
    'tab-1': 'BOLD FACE LIMITATIONS',
    'tab-2': 'EMER - ACT POSITION FAIL',
    'tab-3': 'EMER - ENG RPM HIGH',
    'tab-4': 'EMER - ENG RPM LOW',
    'tab-5': 'EMER - LDG GR EXTENTION FAIL',
    'tab-6': 'EMER - ENG STOPPED'
}

sections = re.findall(r'<section class="page-section[^"]*" data-page="([^"]+)">(.*?)</section>', content, re.DOTALL)

processed_sections = []

for page, shtml in sections:
    sname = sec_map.get(page)
    qs = [q for q in d['questions'] if q['section'] == sname]
    
    counter = [0]
    
    def replacer(match):
        idx = counter[0]
        if idx >= len(qs):
            print(f"Warning: more inputs than questions in {page} at {idx}")
            return match.group(0)
        
        q = qs[idx]
        counter[0] += 1
        
        attrs = match.group(1)
        cls = "answer-input paper-answer-input"
        if "inline-input" in attrs:
            cls += " inline-input"
        
        maxl_m = re.search(r'maxlength="(\d+)"', attrs)
        maxl = maxl_m.group(1) if maxl_m else "40"
        
        accepted_str = "|".join(q.get("acceptedAnswers", [q["answer"]]))
        
        return (f'<input class="{cls}" '
                f'id="paper-input-{q["id"]}" '
                f'type="text" '
                f'data-qid="{q["id"]}" '
                f'data-tab="{page}" '
                f'data-answer="{q["answer"]}" '
                f'data-accepted="{accepted_str}" '
                f'maxlength="{maxl}" '
                f'autocomplete="off" '
                f'spellcheck="false" '
                f'oninput="App.onBoldFaceInput(\'{q["id"]}\')" '
                f'onkeydown="App.onBoldFaceKeyDown(event, \'{q["id"]}\')" />')
    
    new_shtml = re.sub(r'<input\b([^>]*)>', replacer, shtml)
    processed_sections.append((page, sname, new_shtml))
    print(f"Processed {page} ({sname}): replaced {counter[0]} inputs (expected {len(qs)})")

total_len = sum(len(s[2]) for s in processed_sections)
print(f"Total processed HTML length: {total_len} characters")
