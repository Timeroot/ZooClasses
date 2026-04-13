"""Quick additions for NT, NT*, and other top class bounds."""
import os
import sys
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

# NT ⊆ ⊕P: stated in the Complexity Zoo (GHJ+91)
add("NT", "\u2295P",
    "NT \u2286 \u2295P: contained in \u2295P, defined in [GHJ+91] to study \u2295P-complete problems.")

# NT ⊆ E: contained in E (linear exponential time)
add("NT", "E",
    "NT \u2286 E: stated in the Complexity Zoo NT entry ([GHJ+91]).")

# NT ⊆ NT*: NT* is a generalization of NT
add("NT", "NT*",
    "NT \u2286 NT*: NT* is defined like NT but with a more general ordering on inputs.")

# NT* ⊆ ⊕P: contained in ⊕P
add("NT*", "\u2295P",
    "NT* \u2286 \u2295P: stated in the Complexity Zoo NT* entry ([GHJ+91]).")

# (NP ∩ coNP)/poly ⊆ S_2P: Cai's theorem
add("(NP \u2229 coNP)/poly", "S_2P",
    "(NP \u2229 coNP)/poly \u2286 S_2P: by Cai's result (from the class description).")

# DistNP check: (NP,P-samplable) = DistNP
# AvgP ⊆ (NP,P-samplable): any AvgP problem has a natural distribution (uniform or P-samplable)
# Let me check if DistNP is in database

# AH: RE ⊆ AH and coRE ⊆ AH (Σ_1 = RE ⊆ ⊆ AH, Π_1 = coRE ⊆ AH)
import json
with open('generated/classes.json', encoding='utf-8') as f:
    d = json.load(f)
names = {c['name'] for c in d}
print("RE in db:", 'RE' in names)
print("coRE in db:", 'coRE' in names)
print("DistNP in db:", 'DistNP' in names)
print("AvgP in db:", 'AvgP' in names)

if 'RE' in names:
    add("RE", "AH",
        "RE \u2286 AH: the recursively enumerable languages are \u03a3_1 = RE, "
        "which is a level of the arithmetic hierarchy AH.")

if 'coRE' in names:
    add("coRE", "AH",
        "coRE \u2286 AH: the co-recursively enumerable languages are \u03a0_1 = coRE, "
        "a level of the arithmetic hierarchy AH.")

if 'DistNP' in names:
    eq("(NP,P-samplable)", "DistNP",
       "(NP,P-samplable) = DistNP: DistNP is defined as NP problems with P-samplable "
       "distributions, which is exactly (NP,P-samplable).")

print(f"\nCreated {created}, skipped {skipped}")
