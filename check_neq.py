import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# Same setup as generate_json.py
_HASSE_REL_RE = re.compile(r'[⊆⊇⊂⊃⊊⊋⊈⊉=]')
_CANONICAL_FORMS = {'P', 'NP', 'PSPACE', 'L', 'NL', 'BPP', 'BQP', 'ZPP', 'IP', 'MIP', 'ALL', 'NONE'}

with open('generated/classes.json', encoding='utf-8') as f:
    classes_data = json.load(f)
with open('generated/theorems.json', encoding='utf-8') as f:
    theorems_data = json.load(f)

type_classes = [c for c in classes_data
                if c.get('type') == 'Language' and c.get('concrete') is not False]
class_names = {c['name'] for c in type_classes}

# Parse edges
edges = []
for thm in theorems_data:
    content = thm.get('content', '')
    for part in content.split('&&'):
        part = part.strip()
        if part.startswith('{'):
            continue
        m = _HASSE_REL_RE.search(part)
        if not m:
            continue
        rel = m.group(0)
        lhs = part[:m.start()].strip()
        rhs = part[m.end():].strip()
        if lhs not in class_names or rhs not in class_names:
            continue
        if rel == '\u228A': rel = '\u2282'
        if rel in ('\u2283', '\u2287'): lhs, rhs = rhs, lhs; rel = '\u2286'
        if rel == '\u2289': lhs, rhs = rhs, lhs; rel = '\u2288'
        if rel in ('\u2286', '\u2282'):
            edges.append((lhs, rhs))
        elif rel == '=':
            edges.append((lhs, rhs))
            edges.append((rhs, lhs))

print(f"Total edges: {len(edges)}")

# Transitive closure
def _tc(names, edges):
    adj = {n: [] for n in names}
    for lhs, rhs in edges:
        if lhs in adj:
            adj[lhs].append(rhs)
    reachable = {}
    for start in names:
        reached = {start}
        queue = list(adj[start])
        for n in queue:
            reached.add(n)
        idx = 0
        while idx < len(queue):
            for nxt in adj.get(queue[idx], []):
                if nxt not in reached:
                    reached.add(nxt)
                    queue.append(nxt)
            idx += 1
        reachable[start] = reached
    return reachable

reachable = _tc(list(class_names), edges)

target = 'S^\u2260'
print(f"\nreachable[{target!r}] has ALL: {'ALL' in reachable.get(target, set())}")
print(f"reachable[{target!r}] size: {len(reachable.get(target, set()))}")
print(f"reachable[{target!r}] = {sorted(reachable.get(target, set()))}")

# Check canonicals
assigned = set()
canon_rep = {}
equiv_members = {}
for name in sorted(class_names):
    if name in assigned:
        continue
    eq_class = [n for n in class_names
                if name in reachable[n] and n in reachable[name]]
    canon = next((n for n in eq_class if n in _CANONICAL_FORMS), None)
    if not canon:
        canon = min(eq_class)
    for member in eq_class:
        canon_rep[member] = canon
        assigned.add(member)
    equiv_members[canon] = eq_class

canonicals = list(equiv_members.keys())

print(f"\ncanon_rep[{target!r}] = {canon_rep.get(target, 'NOT FOUND')!r}")
c = canon_rep.get(target, target)
print(f"reachable[canon={c!r}] has ALL: {'ALL' in reachable.get(c, set())}")
