"""
Find theorem files where content has inclusion edges that fail to parse
(one or both sides not in class_names). These are content-name mismatches.
"""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

_UNICODE_RE = re.compile(r'[\u2282\u2286\u2283\u2287\u2288\u2289\u228A]')

with open('generated/classes.json', encoding='utf-8') as f:
    classes_data = json.load(f)
with open('generated/theorems.json', encoding='utf-8') as f:
    theorems_data = json.load(f)

type_classes = [c for c in classes_data
                if c.get('type') == 'Language' and c.get('concrete') is not False]
class_names = {c['name'] for c in type_classes}

broken = []
for thm in theorems_data:
    content = thm.get('content', '')
    if not content or content.startswith('{'):
        continue
    for part in content.split('&&'):
        part = part.strip()
        if part.startswith('{'):
            continue
        m = _UNICODE_RE.search(part)
        if not m:
            m = re.search(r'=', part)
        if not m:
            continue
        rel = m.group(0)
        lhs = part[:m.start()].strip()
        rhs = part[m.end():].strip()
        lhs_ok = lhs in class_names
        rhs_ok = rhs in class_names
        if not lhs_ok or not rhs_ok:
            if rel in '\u2282\u2286\u2283\u2287\u228A':  # ⊆/⊂ etc
                broken.append((thm['name'], lhs, rel, rhs, lhs_ok, rhs_ok))
            elif rel == '=':
                if not part.startswith('{'):
                    broken.append((thm['name'], lhs, rel, rhs, lhs_ok, rhs_ok))

# Print broken ones, excluding trivially expected ones (like X = P∩coP etc.)
for thm_name, lhs, rel, rhs, lhs_ok, rhs_ok in sorted(broken, key=lambda x: x[0]):
    problems = []
    if not lhs_ok:
        problems.append(f"lhs {lhs!r} not in classes")
    if not rhs_ok:
        problems.append(f"rhs {rhs!r} not in classes")
    print(f"  {thm_name!r}: {', '.join(problems)}")

print(f"\nTotal broken: {len(broken)}")
