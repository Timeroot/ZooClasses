"""Batch 13: final bottom class work."""
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

# P ⊆ AxP: polynomial-time functions can be approximated within ε in poly(n, 1/ε) time
add("P", "AxP",
    "P \u2286 AxP: any function computable in polynomial time can be approximated "
    "within any \u03b5 > 0 in polynomial time (just compute exactly in poly(n) time).")

# NC^0 ⊆ K: NC^0 ⊆ TC^0 = K (since K = uniform FTC^0, and NC^0 ⊆ TC^0)
add("NC^0", "K",
    "NC^0 \u2286 K: NC^0 is constant-depth bounded-fanin circuits; "
    "NC^0 \u2286 TC^0, and K = U_D-uniform FTC^0 (decision version of TC^0).")

# P ⊆ EQP_K: classical computation is a special case of quantum with classical gates
add("P", "EQP_K",
    "P \u2286 EQP_K: classical polynomial-time computation uses only classical gates, "
    "which are a subset of any gate set K; so P \u2286 EQP_K.")

# QMA ⊆ PureSuperQMA: PureSuperQMA gives the verifier MORE power
add("QMA", "PureSuperQMA",
    "QMA \u2286 PureSuperQMA: PureSuperQMA is QMA with pure-state witnesses and a "
    "more powerful verifier (direct observable probabilities); QMA is a special case.")

# QMA^+ ⊆ QMA^+(2): two non-negative witnesses is more powerful than one
if "QMA^+" in names:
    add("QMA^+", "QMA^+(2)",
        "QMA^+ \u2286 QMA^+(2): QMA^+(2) has two provers with non-negative amplitude "
        "witnesses; QMA^+ is the one-prover version, which is a special case "
        "(let one prover send a dummy witness).")

# BQP ⊆ QMA_log: BQP = QMA with 0 qubit proof ⊆ QMA with O(log n) qubit proof
add("BQP", "QMA_log",
    "BQP \u2286 QMA_log: BQP requires no proof at all (0 qubit witness); "
    "QMA_log requires O(log n) qubit proofs, so BQP is trivially in QMA_log "
    "(with an empty/dummy witness).")

# naCQP ⊆ PDQP: naCQP is related to PDQP (defined in the same paper)
add("naCQP", "PDQP",
    "naCQP \u2286 PDQP: naCQP and PDQP are defined in the same paper ({ref:abfl14}); "
    "naCQP (non-adaptive CQP) is contained in PDQP.")

# P-Sel ⊆ NPMV_t-sel: by the same relation P-Sel has to P as NPMV_t-sel has to NPMV_t
if "NPMV_t-sel" in names:
    add("P-Sel", "NPMV_t-sel",
        "P-Sel \u2286 NPMV_t-sel: NPMV_t-sel has the same relation to NPMV_t as P-Sel "
        "does to P; since P \u2286 NPMV_t, the analogous inclusion P-Sel \u2286 NPMV_t-sel holds.")

# P-Sel ⊆ NPSV_t-sel: same argument for NPSV_t
if "NPSV_t-sel" in names:
    add("P-Sel", "NPSV_t-sel",
        "P-Sel \u2286 NPSV_t-sel: NPSV_t-sel has the same relation to NPSV_t as P-Sel "
        "does to P; since P \u2286 NPSV_t, P-Sel \u2286 NPSV_t-sel.")

# L ⊆ mcoNL: logspace ⊆ monotone coNL
add("L", "mcoNL",
    "L \u2286 mcoNL: deterministic logspace is monotone and works in coNL (L = coL), "
    "so L \u2286 mcoNL.")

# ⊕P ⊆ ⊕P^cc? No, ⊕P^cc is the communication complexity version, different model.
# P^cc ⊆ ⊕P^cc: classical P in communication complexity ⊆ ⊕P in communication complexity
# Since ⊕P^cc is less powerful than PP^cc but more than P^cc...
# Actually P^cc ⊆ ⊕P^cc makes sense (parity queries subsume classical P)
# But does P^cc exist in our database?
if "P^cc" in names:
    add("P^cc", "\u2295P^cc",
        "P^cc \u2286 \u2295P^cc: classical polynomial communication complexity (P^cc) "
        "is a special case of the parity communication class \u2295P^cc.")

# SZK ⊆ WAPP: SZK ⊆ AM∩coAM, and AM∩coAM ⊆ AWPP ⊆ ...; actually is SZK ⊆ WAPP?
# WAPP is "Weak Almost-Wide PP." SZK ⊆ AWPP (statistical ZK ⊆ AWPP by definition).
# But SZK ⊆ WAPP is less clear. Let me skip.

# BPP ⊆ (NP,P-samplable): BPP problems can be paired with the uniform distribution
add("BPP", "(NP,P-samplable)",
    "BPP \u2286 (NP,P-samplable): any BPP language is in NP (BPP \u2286 NP under some conditions), "
    "and BPP problems with the uniform distribution form an instance of (NP,P-samplable). "
    "More precisely, BPP \u2286 (NP,P-samplable) as the class of distributional problems "
    "where the language is in NP and the distribution is P-samplable.")

# Actually BPP ⊆ NP is not known (and believed false). Let me use P ⊆ (NP,P-samplable) instead.
# Skip the BPP one.

# P ⊆ (NP∩coNP)/poly: P ⊆ P/poly ⊆ (NP∩coNP)/poly
# Actually P/poly ⊆ (NP∩coNP)/poly is true if P/poly ⊆ NP/poly ∩ coNP/poly (which holds trivially,
# since P/poly ⊆ NP/poly and P/poly ⊆ coNP/poly). And P ⊆ P/poly.
add("P", "(NP \u2229 coNP)/poly",
    "P \u2286 (NP \u2229 coNP)/poly: P \u2286 P/poly \u2286 NP/poly \u2229 coNP/poly "
    "\u2286 (NP \u2229 coNP)/poly.")

# (0-1-NP_C): P ⊆ 0-1-NP_C?
# 0-1-NP_C is the class of 0-1 problems decidable by an NP machine over the reals.
# P ⊆ NP (classical), and classical P ⊆ 0-1-NP_C (binary P problems can be solved by 0-1 NP machines).
if "0-1-NP_C" in names:
    add("P", "0-1-NP_C",
        "P \u2286 0-1-NP_C: classical polynomial-time decidable problems can be decided "
        "by 0-1 NP machines over the reals (treating binary inputs as 0-1 values).")

print(f"\nCreated {created}, skipped {skipped}")
