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
    print("Generating JSON from markdown files...")
    generate_classes()
    generate_theorems()
    generate_conjectures()
    generate_references()
    generate_problems()
    copy_static()
    print(f"Done. Output in {OUT_DIR}/")
