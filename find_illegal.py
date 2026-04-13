import json, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('generated/classes.json', encoding='utf-8') as f:
    d = json.load(f)
ILLEGAL = set('/\\:*?"<>|')
problem = [(c['name'], sorted(set(ch for ch in c['name'] if ch in ILLEGAL)))
           for c in d if c.get('type') == 'Language' and c.get('concrete') is not False
           if any(ch in ILLEGAL for ch in c['name'])]
for name, chars in sorted(problem):
    print(repr(name), '->', chars)
print('Total with illegal chars:', len(problem))
