"""
Reads per-entry markdown files from data/ and produces the JSON files that
the frontend expects, writing them to generated/.

    data/classes/<type-subfolder>/<Name>.md  ->  generated/classes.json
    data/theorems/<Name>.md                  ->  generated/theorems.json
    data/conjectures/<Name>.md               ->  generated/conjectures.json
    data/references/<Name>.md                ->  generated/references.json
    data/problems/<Name>.md                  ->  generated/problems.json

Also copies the two small JSON-only files that stay as-is:
    data/properties.json     ->  generated/properties.json
    data/problem_types.json  ->  generated/problem_types.json

Usage:
    python generate_json.py
"""

import json
import os
import re
import shutil

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(REPO_ROOT, "data")
OUT_DIR = os.path.join(REPO_ROOT, "generated")

SUBFOLDER_TO_TYPE = {
    "language": "Language",
    "promise": "Promise Problem",
    "function": "Function Problem",
    "parameterized": "Parameterized Language",
    "distributional": "Distributional Problem",
    "sampling": "Sampling Problem",
    "integer": "Integer Problem",
    "optimization": "Optimization Problem",
    "approximation": "Approximation Problem",
}


def parse_md(path: str) -> tuple[dict, str]:
    """Parse a markdown file with YAML frontmatter.

    Returns (frontmatter_dict, body_string).
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.startswith("---"):
        raise ValueError(f"{path}: expected YAML frontmatter (---) at start of file")

    end = text.index("---", 3)
    yaml_block = text[3:end].strip()
    body = text[end + 3:].strip()

    fm = parse_yaml_frontmatter(yaml_block)
    return fm, body


def parse_yaml_frontmatter(text: str) -> dict:
    """Minimal YAML parser sufficient for the frontmatter we generate.

    Handles:
      key: scalar
      key: "multi-line
       quoted scalar"
      key:
        - item1
        - item2
      key: []
    Scalars may be bare or double-quoted (including across multiple lines).
    """
    result = {}
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        m = re.match(r'^(\w[\w_]*)\s*:\s*(.*)', line)
        if not m:
            raise ValueError(f"Cannot parse YAML line: {line!r}")

        key = m.group(1)
        rest = m.group(2).strip()

        if rest == "[]":
            result[key] = []
            i += 1
        elif rest == "":
            items = []
            i += 1
            while i < len(lines) and lines[i].startswith("  - "):
                item_str = lines[i][4:]
                items.append(parse_yaml_scalar(item_str))
                i += 1
            result[key] = items
        else:
            # Handle double-quoted strings that span multiple lines
            if rest.startswith('"') and not _is_closed_quote(rest):
                i += 1
                while i < len(lines):
                    rest += "\n" + lines[i]
                    if _is_closed_quote(rest):
                        break
                    i += 1
            result[key] = parse_yaml_scalar(rest)
            i += 1

    return result


def _is_closed_quote(s: str) -> bool:
    """Check whether a string starting with \" has a matching closing \"."""
    if not s.startswith('"'):
        return True
    # Walk through, tracking escapes
    i = 1
    while i < len(s):
        if s[i] == '\\':
            i += 2
            continue
        if s[i] == '"':
            return True
        i += 1
    return False


def parse_yaml_scalar(s: str):
    """Parse a YAML scalar value — bare or double-quoted."""
    s = s.strip()
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1].replace('\\"', '"').replace('\\\\', '\\')
    if s in ("true", "True"):
        return True
    if s in ("false", "False"):
        return False
    if s in ("null", "~"):
        return None
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s


def collect_md_files(directory: str) -> list[str]:
    """Return sorted list of .md file paths in a directory (non-recursive)."""
    if not os.path.isdir(directory):
        return []
    return sorted(
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.endswith(".md")
    )


def write_json(path: str, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write("\n")


# ── Classes ──────────────────────────────────────────────────────────────

def generate_classes():
    classes_root = os.path.join(DATA_DIR, "classes")
    entries = []

    for subfolder in sorted(os.listdir(classes_root)):
        subfolder_path = os.path.join(classes_root, subfolder)
        if not os.path.isdir(subfolder_path):
            continue

        problem_type = SUBFOLDER_TO_TYPE.get(subfolder)
        if problem_type is None:
            print(f"  WARNING: unknown subfolder data/classes/{subfolder}/, skipping")
            continue

        for md_path in collect_md_files(subfolder_path):
            fm, body = parse_md(md_path)
            entry = {}
            entry["name"] = fm["name"]
            entry["type"] = problem_type

            if fm.get("concrete") is False or str(fm.get("concrete", "")).lower() == "false":
                entry["concrete"] = False

            desc, notes = split_body_notes(body)
            entry["desc"] = desc
            if fm.get("related"):
                entry["related"] = fm["related"]
            if fm.get("properties"):
                entry["properties"] = fm["properties"]
            if notes:
                entry["notes"] = notes

            entries.append(entry)

    out_path = os.path.join(OUT_DIR, "classes.json")
    write_json(out_path, entries)
    print(f"  classes.json: {len(entries)} entries")


# ── Theorems ─────────────────────────────────────────────────────────────

def generate_theorems():
    thm_dir = os.path.join(DATA_DIR, "theorems")
    entries = []

    for md_path in collect_md_files(thm_dir):
        fm, body = parse_md(md_path)
        entry = {}
        entry["name"] = fm["name"]
        if "content" in fm:
            entry["content"] = fm["content"]
        else:
            entry["content"] = ""
        if "ref" in fm:
            entry["ref"] = fm["ref"]
        if "impliedby" in fm:
            entry["impliedby"] = fm["impliedby"]
        if "priority" in fm:
            entry["priority"] = fm["priority"]
        if fm.get("related"):
            entry["related"] = fm["related"]
        if body:
            entry["notes"] = body

        entries.append(entry)

    out_path = os.path.join(OUT_DIR, "theorems.json")
    write_json(out_path, entries)
    print(f"  theorems.json: {len(entries)} entries")


# ── Conjectures ──────────────────────────────────────────────────────────

def generate_conjectures():
    conj_dir = os.path.join(DATA_DIR, "conjectures")
    entries = []

    for md_path in collect_md_files(conj_dir):
        fm, body = parse_md(md_path)
        entry = {}
        entry["name"] = fm["name"]
        if "content" in fm:
            entry["content"] = fm["content"]
        else:
            entry["content"] = ""

        desc, notes = split_body_notes(body)
        if desc:
            entry["desc"] = desc
        if fm.get("implies"):
            entry["implies"] = fm["implies"]
        if fm.get("not_implies"):
            entry["not_implies"] = fm["not_implies"]
        if notes:
            entry["notes"] = notes

        entries.append(entry)

    out_path = os.path.join(OUT_DIR, "conjectures.json")
    write_json(out_path, entries)
    print(f"  conjectures.json: {len(entries)} entries")


# ── References ───────────────────────────────────────────────────────────

def generate_references():
    ref_dir = os.path.join(DATA_DIR, "references")
    entries = []

    for md_path in collect_md_files(ref_dir):
        fm, body = parse_md(md_path)
        entry = {}
        entry["name"] = fm["name"]
        entry["desc"] = body
        if fm.get("url"):
            entry["url"] = fm["url"]
        else:
            entry["url"] = []

        entries.append(entry)

    out_path = os.path.join(OUT_DIR, "references.json")
    write_json(out_path, entries)
    print(f"  references.json: {len(entries)} entries")


# ── Problems ─────────────────────────────────────────────────────────────

def generate_problems():
    prob_dir = os.path.join(DATA_DIR, "problems")
    entries = []

    for md_path in collect_md_files(prob_dir):
        fm, body = parse_md(md_path)
        entry = {}
        entry["name"] = fm["name"]

        description, variants_text = split_body_variants(body)
        if description:
            entry["description"] = description
        if variants_text is not None:
            entry["variants"] = parse_variants(variants_text)

        entries.append(entry)

    out_path = os.path.join(OUT_DIR, "problems.json")
    write_json(out_path, entries)
    print(f"  problems.json: {len(entries)} entries")


def split_body_notes(body: str) -> tuple[str, str]:
    """Split a body into (desc, notes) on the '## Notes' heading."""
    marker = "## Notes"
    idx = body.find(marker)
    if idx == -1:
        return body.strip(), ""
    desc = body[:idx].strip()
    notes = body[idx + len(marker):].strip()
    return desc, notes


def split_body_variants(body: str) -> tuple[str, str | None]:
    """Split a body into (description, variants_block) on '## Variants'."""
    marker = "## Variants"
    idx = body.find(marker)
    if idx == -1:
        return body.strip(), None
    desc = body[:idx].strip()
    variants_text = body[idx + len(marker):].strip()
    return desc, variants_text


def parse_variants(text: str) -> list[dict]:
    """Parse the variants section of a problem markdown file.

    Each variant starts with ### <id> and has bullet fields and optional notes.
    """
    chunks = re.split(r'^### ', text, flags=re.MULTILINE)
    variants = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue

        lines = chunk.split("\n", 1)
        var_id = lines[0].strip()
        rest = lines[1].strip() if len(lines) > 1 else ""

        variant = {"id": var_id}

        type_m = re.search(r'^\- \*\*Type:\*\*\s*(.+)$', rest, re.MULTILINE)
        if type_m:
            variant["type"] = type_m.group(1).strip()

        desc_m = re.search(r'^\- \*\*Description:\*\*\s*(.+)$', rest, re.MULTILINE)
        if desc_m:
            variant["desc"] = desc_m.group(1).strip()

        bullet_lines = [l for l in rest.split("\n") if l.startswith("- **")]
        non_bullet = []
        past_bullets = False
        for line in rest.split("\n"):
            if line.startswith("- **"):
                past_bullets = True
                continue
            if past_bullets or (not line.startswith("- **") and non_bullet):
                past_bullets = True
                non_bullet.append(line)

        notes_text = "\n".join(non_bullet).strip()
        if notes_text:
            variant["notes"] = notes_text

        variants.append(variant)

    return variants


# ── Reference validation ─────────────────────────────────────────────────

_LANG_RE = re.compile(r'\{lang:([^}]+)\}')
_THM_RE  = re.compile(r'\{thm:([^}]+)\}')
_REF_RE  = re.compile(r'\{ref:([^}]+)\}')


def validate_references(classes_data, theorems_data, references_data):
    """Check that all {lang:}, {thm:}, {ref:} pointers in content resolve."""
    class_names = {c['name'] for c in classes_data}
    thm_names   = {t['name'] for t in theorems_data}
    ref_names   = {r['name'] for r in references_data}

    warnings = []

    def check(text, label):
        for m in _LANG_RE.finditer(text):
            if m.group(1) not in class_names:
                warnings.append(f"  WARN {label}: {{lang:{m.group(1)}}} — class not found")
        for m in _THM_RE.finditer(text):
            if m.group(1) not in thm_names:
                warnings.append(f"  WARN {label}: {{thm:{m.group(1)}}} — theorem not found")
        for m in _REF_RE.finditer(text):
            if m.group(1) not in ref_names:
                warnings.append(f"  WARN {label}: {{ref:{m.group(1)}}} — reference not found")

    for c in classes_data:
        lbl = f"class '{c['name']}'"
        check(c.get('desc', ''), lbl)
        check(c.get('notes', ''), lbl)

    for t in theorems_data:
        lbl = f"theorem '{t['name']}'"
        check(t.get('content', ''), lbl)
        check(t.get('ref', ''), lbl)
        check(t.get('notes', ''), lbl)

    return warnings


# ── Hasse diagram analysis ────────────────────────────────────────────────

# Matches any inclusion/equality/strict relation symbol
_HASSE_REL_RE     = re.compile(r'[\u2282\u2286\u2283\u2287\u2288\u2289\u228A\u2260=]')
# Unicode subset/superset symbols only (no =) — used to avoid = in class names confusing the parser
_HASSE_UNICODE_RE = re.compile(r'[\u2282\u2286\u2283\u2287\u2288\u2289\u228A]')

_CANONICAL_FORMS = frozenset([
    "PSPACE", "BPP", "NC", "L", "NL", "NLINSPACE",
    "NC^0", "QAC", "RE", "NEXP", "SAC^1", "coNQP",
])


def _parse_inclusion_edges(theorems_data, class_names):
    """Extract (lhs ⊆ rhs) directed edges from theorem content strings.

    Mirrors the parsing logic in process.js buildPosetFromTheorems.
    """
    edges = []
    for thm in theorems_data:
        content = thm.get('content', '')
        if not content or content.startswith('{'):
            continue
        for part in content.split('&&'):
            part = part.strip()
            if part.startswith('{'):
                continue
            # Prefer Unicode ⊆/⊂/etc. first; only fall back to = (equality) if none found.
            # This avoids '=' inside class names like C_=AC^0 being mistaken for a relation.
            m = _HASSE_UNICODE_RE.search(part)
            if not m:
                m = re.search(r'=', part)
            if not m:
                continue
            rel = m.group(0)
            lhs = part[:m.start()].strip()
            rhs = part[m.end():].strip()
            if lhs not in class_names or rhs not in class_names:
                continue
            # Normalise direction so we always have lhs ⊆ rhs
            if rel == '\u228A':                        rel = '\u2282'          # ⊊ → ⊂
            if rel in ('\u2283', '\u2287'):            lhs, rhs = rhs, lhs; rel = '\u2286'
            if rel == '\u2289':                        lhs, rhs = rhs, lhs; rel = '\u2288'
            if rel in ('\u2286', '\u2282'):            # ⊆ or ⊂
                edges.append((lhs, rhs))
            elif rel == '=':
                edges.append((lhs, rhs))
                edges.append((rhs, lhs))
            # ⊈ / ≠ edges are intentionally ignored for the inclusion poset
    return edges


def _transitive_closure(names, edges):
    """BFS transitive closure.  Returns dict: name -> frozenset of reachable names."""
    adj = {n: [] for n in names}
    for lhs, rhs in edges:
        if lhs in adj:
            adj[lhs].append(rhs)

    reachable = {}
    for start in names:
        reached = {start}
        queue = list(adj[start])
        idx = 0
        for n in queue:
            reached.add(n)
        while idx < len(queue):
            for nxt in adj.get(queue[idx], []):
                if nxt not in reached:
                    reached.add(nxt)
                    queue.append(nxt)
            idx += 1
        reachable[start] = reached
    return reachable


def analyse_hasse(classes_data, theorems_data, class_type='Language'):
    """Compute the inclusion poset and print a diagnostic report.

    In a *finite* poset, 'has no covering parent' is equivalent to 'is a
    minimal element', so we only need the transitive closure — no O(n³)
    covering-relation scan needed.
    """
    type_classes = [c for c in classes_data
                    if c.get('type') == class_type and c.get('concrete') is not False]
    class_names = {c['name'] for c in type_classes}

    edges    = _parse_inclusion_edges(theorems_data, class_names)
    reachable = _transitive_closure(list(class_names), edges)

    # ── Equivalence classes (mutual reachability) ─────────────────────────
    assigned     = set()
    canon_rep    = {}
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

    # ── Minimals / maximals of the quotient poset ─────────────────────────
    minimals = {x for x in canonicals
                if not any(y != x and x in reachable[y] and y not in reachable[x]
                           for y in canonicals)}
    maximals = {x for x in canonicals
                if not any(y != x and y in reachable[x] and x not in reachable[y]
                           for y in canonicals)}

    # ── Isolation check ───────────────────────────────────────────────────
    isolated = {x for x in class_names
                if len(reachable[x]) == 1
                and not any(x in reachable[y] and y != x for y in class_names)}

    none_canonical = canon_rep.get('NONE', 'NONE')
    all_canonical  = canon_rep.get('ALL',  'ALL')

    # Connected minimals that aren't NONE (have successors but no predecessor)
    real_minimals = sorted(
        x for x in minimals
        if any(y != x and y in reachable[x] and x not in reachable[y] for y in canonicals)
        and x != none_canonical
    )
    # Connected maximals that aren't ALL (have predecessors but no successor)
    real_maximals = sorted(
        x for x in maximals
        if any(y != x and x in reachable[y] and y not in reachable[x] for y in canonicals)
        and x != all_canonical
    )

    # "Bottom" classes: non-NONE classes whose ONLY strict canonical predecessor is NONE.
    # These sit just above NONE — things like SF are fine here; others may need work.
    bottom_classes = sorted(
        x for x in canonicals
        if x not in (none_canonical, all_canonical)
        and {y for y in canonicals
             if x in reachable[y] and y not in reachable[x] and y != x} == {none_canonical}
    )
    # "Top" classes: non-ALL classes whose ONLY strict canonical successor is ALL.
    top_classes = sorted(
        x for x in canonicals
        if x not in (none_canonical, all_canonical)
        and {y for y in canonicals
             if y in reachable[x] and x not in reachable[y] and y != x} == {all_canonical}
    )

    # ── Report ────────────────────────────────────────────────────────────
    n_connected = len(class_names) - len(isolated)
    print(f"\nHasse ({class_type}): {len(class_names)} concrete classes, "
          f"{len(edges)} inclusion edges")
    print(f"  {n_connected} classes in at least one inclusion; "
          f"{len(isolated)} completely isolated")

    # NONE must be the only minimal
    if 'NONE' not in class_names:
        print(f"  ASSERT FAIL: NONE class not present")
    elif real_minimals:
        print(f"  ASSERT FAIL: {len(real_minimals)} classes have successors but no predecessor "
              f"(NONE⊆X theorems missing):")
        for name in real_minimals:
            print(f"    {name}")
    else:
        none_reach = reachable.get(none_canonical, {none_canonical}) - {none_canonical}
        print(f"  NONE is the only minimal ({len(none_reach)} known successors) ✓")

    # ALL must be the only maximal
    if 'ALL' not in class_names:
        print(f"  ASSERT FAIL: ALL class not present")
    elif real_maximals:
        print(f"  ASSERT FAIL: {len(real_maximals)} classes have predecessors but no successor "
              f"(X⊆ALL theorems missing):")
        for name in real_maximals:
            print(f"    {name}")
    else:
        all_pred = [y for y in canonicals
                    if all_canonical in reachable[y] and y not in reachable[all_canonical]
                    and y != all_canonical]
        print(f"  ALL is the only maximal ({len(all_pred)} known predecessors) ✓")

    # Bottom and top classes are "work needed" items
    if bottom_classes:
        print(f"\n  {len(bottom_classes)} bottom classes (just above NONE — add lower bounds):")
        for name in bottom_classes:
            print(f"    {name}")

    if top_classes:
        print(f"\n  {len(top_classes)} top classes (just below ALL — add upper bounds):")
        for name in top_classes:
            print(f"    {name}")


# ── Copy static JSON ─────────────────────────────────────────────────────

def copy_static():
    for filename in ("properties.json", "problem_types.json"):
        src = os.path.join(DATA_DIR, filename)
        dst = os.path.join(OUT_DIR, filename)
        if os.path.isfile(src):
            os.makedirs(OUT_DIR, exist_ok=True)
            shutil.copy2(src, dst)
            print(f"  {filename}: copied")
        else:
            print(f"  WARNING: {src} not found")


# ── Main ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    import argparse
    # Ensure UTF-8 output on Windows consoles
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    parser = argparse.ArgumentParser(description="Generate JSON from markdown data files.")
    parser.add_argument('--quiet-refs', action='store_true',
                        help="Suppress {ref:} broken-pointer warnings (they are often expected gaps).")
    parser.add_argument('--all-warnings', action='store_true',
                        help="Show all {ref:} warnings (overrides default truncation).")
    args = parser.parse_args()
    print("Generating JSON from markdown files...")
    generate_classes()
    generate_theorems()
    generate_conjectures()
    generate_references()
    generate_problems()
    copy_static()
    print(f"Done. Output in {OUT_DIR}/")

    # ── Post-generation validation ─────────────────────────────────────────
    with open(os.path.join(OUT_DIR, "classes.json"),    encoding="utf-8") as f:
        _classes   = json.load(f)
    with open(os.path.join(OUT_DIR, "theorems.json"),   encoding="utf-8") as f:
        _theorems  = json.load(f)
    with open(os.path.join(OUT_DIR, "references.json"), encoding="utf-8") as f:
        _refs      = json.load(f)

    print("\nValidating references...")
    _warnings = validate_references(_classes, _theorems, _refs)
    if _warnings:
        lang_warns = [w for w in _warnings if '{lang:' in w]
        thm_warns  = [w for w in _warnings if '{thm:' in w]
        ref_warns  = [w for w in _warnings if '{ref:' in w]
        print(f"  {len(_warnings)} broken pointer(s): "
              f"{len(lang_warns)} {{lang:}}, {len(thm_warns)} {{thm:}}, "
              f"{len(ref_warns)} {{ref:}}")
        # {lang:} and {thm:} are structural — always show them
        for w in lang_warns + thm_warns:
            print(w)
        # {ref:} are often just gaps in reference import
        if ref_warns and not args.quiet_refs:
            shown = len(ref_warns) if args.all_warnings else min(20, len(ref_warns))
            for w in ref_warns[:shown]:
                print(w)
            if len(ref_warns) > shown:
                print(f"  ... and {len(ref_warns) - shown} more {{ref:}} warnings "
                      f"(pass --all-warnings to see all, or --quiet-refs to silence)")
        elif ref_warns and args.quiet_refs:
            print(f"  ({len(ref_warns)} {{ref:}} warnings suppressed by --quiet-refs)")
    else:
        print("  All {lang:}, {thm:}, {ref:} pointers OK ✓")

    analyse_hasse(_classes, _theorems, "Language")
