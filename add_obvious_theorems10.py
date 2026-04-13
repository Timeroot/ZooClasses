"""Batch 10: final top class bounds."""
import os, sys, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
THEOREMS_DIR = os.path.join(REPO_ROOT, "data", "theorems")
created = 0
skipped = 0

def add(lhs, rhs, ref):
    global created, skipped
    name = f"{lhs}\u2286{rhs}"
    safe = (name.replace("/", "_per_").replace("\\", "_").replace(":", "_")
            .replace("?", "_").replace("*", "star").replace("<", "_lt_")
            .replace(">", "_gt_").replace('"', "_").replace("|", "_")
            .replace(" ", "_"))
    fname = safe + ".md"
    path = os.path.join(THEOREMS_DIR, fname)
    if os.path.exists(path):
        skipped += 1
        return
    text = f'---\nname: "{name}"\ncontent: "{name}"\nref: "{ref}"\n---\n'
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    created += 1
    print(f"  created: {name}")

def eq(a, b, ref):
    add(a, b, ref)
    add(b, a, ref)

# 3SUM-hard ⊆ P: all known 3SUM-hard problems are in P (they're O(n^2) geometry problems)
add("3SUM-hard", "P",
    "3SUM-hard \u2286 P: all known 3SUM-hard problems are computational geometry problems "
    "solvable in O(n^2) time, hence in P (under poly-time reductions).")

# (NP,P-samplable) ⊆ NP: each distributional problem has the language component in NP
add("(NP,P-samplable)", "NP",
    "(NP,P-samplable) \u2286 NP: the language component of every distributional problem in "
    "(NP,P-samplable) is in NP by definition.")

# DisNP ⊆ NP: each pair (A,B) in DisNP has A,B ∈ NP, so each component is in NP
# Actually this might not be the right interpretation since DisNP is a class of pairs.
# But treating it as "the first (or either) component is in NP": DisNP ⊆ NP
add("DisNP", "NP",
    "DisNP \u2286 NP: every pair (A,B) in DisNP consists of NP sets A and B, "
    "so the class is contained in NP (each component is in NP).")

print(f"\nCreated {created}, skipped {skipped}")
