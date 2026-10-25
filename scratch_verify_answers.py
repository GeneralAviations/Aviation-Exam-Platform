import re
import json

with open('anka_full_original.html', 'r', encoding='utf-8') as f:
    html = f.read()

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

sections = re.findall(r'<section class="page-section[^"]*" data-page="([^"]+)">(.*?)</section>', html, re.DOTALL)
for spage, scontent in sections:
    sname = sec_map.get(spage)
    qs = [q for q in d['questions'] if q['section'] == sname]
    inputs = re.findall(r'<input\b([^>]*)>', scontent)
    print(f"\nChecking {spage} ({sname}): {len(inputs)} inputs vs {len(qs)} JSON questions")
    for idx, (inp_attrs, q) in enumerate(zip(inputs, qs)):
        ans_match = re.search(r'data-answer="([^"]*)"', inp_attrs)
        raw_ans = ans_match.group(1) if ans_match else ""
        # Check first 3 items
        if idx < 3 or idx == len(inputs) - 1:
            print(f"  [{idx+1}] QID: {q['id']} | HTML answer: '{raw_ans}' | JSON answer: '{q['answer']}'")
