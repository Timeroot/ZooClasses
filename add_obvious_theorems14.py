"""Batch 14: final remaining bottom classes."""
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

with open('generated/classes.json', encoding='utf-8') as f:
    d = json.load(f)
names = {c['name'] for c in d}

# NC^0 ⊆ PL_1: NC^0 functions have at most 2^c Fourier terms, so the L_1 sum is O(1) ≤ poly(n)
add("NC^0", "PL_1",
    "NC^0 \u2286 PL_1: NC^0 functions depend on only O(1) input bits, so their Fourier "
    "expansion has at most 2^c terms each of magnitude \u2264 1; the sum of absolute "
    "Fourier coefficients is O(1) \u2264 poly(n), so NC^0 \u2286 PL_1.")

# BQP ⊆ QMA^+: QMA^+ with empty/dummy witness contains BQP (no proof needed)
add("BQP", "QMA^+",
    "BQP \u2286 QMA^+: BQP problems need no proof (0-qubit witness), which trivially "
    "has non-negative amplitudes; so BQP \u2286 QMA^+ with an empty witness.")

# P ⊆ VC_or: P problems can be expressed as OR of 1 SAT instance (trivially via Karp reduction)
add("P", "VC_or",
    "P \u2286 VC_or: any P problem can be expressed as the OR of a single SAT instance "
    "(via a Karp reduction to SAT followed by checking satisfiability).")

# P ⊆ WAPP: P problems have easy counting witnesses
add("P", "WAPP",
    "P \u2286 WAPP: for L \u2208 P, define f(x) = 2^{p-1} if x \u2208 L and 0 otherwise; "
    "f is in #P and satisfies the WAPP conditions with \u03b5 = 1/2.")

# P ⊆ naCQP: classical P ⊆ naCQP (quantum computation with non-adaptive measurements)
add("P", "naCQP",
    "P \u2286 naCQP: classical polynomial-time computation is a special case of "
    "quantum computation with non-adaptive measurements.")

# P ⊆ SelfNP: for P languages, use the input itself as a witness (self-witnessing)
# Actually this requires careful thought. For L ∈ P, every x ∈ L has a trivial witness
# (e.g., empty string). The SelfNP condition requires that the union of witnesses = L.
# For a P language, if we choose "witness for x = x", then the union of witnesses over x ∈ L is L.
# This satisfies the SelfNP condition! So P ⊆ SelfNP.
add("P", "SelfNP",
    "P \u2286 SelfNP: for L \u2208 P, use x as its own witness; then the union of witnesses "
    "over x \u2208 L equals L itself, satisfying the SelfNP condition.")

# Mark ⊕P^cc as concrete: false (communication complexity class, doesn't fit language hierarchy)
# (This will be done by editing the file directly, not by adding theorems)

print(f"\nCreated {created}, skipped {skipped}")
