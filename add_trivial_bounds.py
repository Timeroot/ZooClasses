"""
add_trivial_bounds.py

Generates NONE⊆X.md and X⊆ALL.md theorem files for every concrete Language
class X (except NONE⊆NONE and ALL⊆ALL).

Skips files that already exist so it is safe to re-run.

Usage:
    python add_trivial_bounds.py
"""

import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
CLASSES_JSON = os.path.join(REPO_ROOT, "generated", "classes.json")
THEOREMS_DIR = os.path.join(REPO_ROOT, "data", "theorems")

REF_NONE = "NONE is the empty language, trivially contained in every complexity class."
REF_ALL  = "ALL is the class of all languages, trivially containing every complexity class."


def safe_filename(name: str) -> str:
    """Convert a class name to a legal Windows filename component."""
    # Replace Windows-illegal characters
    s = name
    s = s.replace("*",  "star")
    s = s.replace("/",  "_")
    s = s.replace("|",  "_")
    s = s.replace("\\", "_")
    s = s.replace(":",  "_")
    s = s.replace("?",  "_")
    s = s.replace('"',  "_")
    s = s.replace("<",  "_lt_")
    s = s.replace(">",  "_gt_")
    return s


def write_theorem(path: str, name: str, content: str, ref: str) -> bool:
    """Write a theorem file.  Returns True if written, False if already existed."""
    if os.path.exists(path):
        return False
    body = f'---\nname: "{name}"\ncontent: "{content}"\nref: "{ref}"\n---\n'
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    return True


def main():
    with open(CLASSES_JSON, encoding="utf-8") as f:
        classes = json.load(f)

    lang_classes = [
        c["name"] for c in classes
        if c.get("type") == "Language" and c.get("concrete") is not False
    ]
    lang_classes.sort()

    created_none = 0
    created_all  = 0
    skipped_none = 0
    skipped_all  = 0

    for name in lang_classes:
        safe = safe_filename(name)

        # NONE ⊆ X  (skip X = NONE)
        if name != "NONE":
            rel_content = f"NONE\u2286{name}"
            rel_name    = rel_content
            fname = f"NONE\u2286{safe}.md"
            path  = os.path.join(THEOREMS_DIR, fname)
            if write_theorem(path, rel_name, rel_content, REF_NONE):
                created_none += 1
            else:
                skipped_none += 1

        # X ⊆ ALL  (skip X = ALL)
        if name != "ALL":
            rel_content = f"{name}\u2286ALL"
            rel_name    = rel_content
            fname = f"{safe}\u2286ALL.md"
            path  = os.path.join(THEOREMS_DIR, fname)
            if write_theorem(path, rel_name, rel_content, REF_ALL):
                created_all += 1
            else:
                skipped_all += 1

    total_lang = len(lang_classes)
    print(f"Language classes: {total_lang}")
    print(f"NONE⊆X : created {created_none}, already existed {skipped_none}")
    print(f"X⊆ALL  : created {created_all},  already existed {skipped_all}")


if __name__ == "__main__":
    main()
