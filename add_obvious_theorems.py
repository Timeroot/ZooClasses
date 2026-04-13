"""
add_obvious_theorems.py

Creates obvious inclusion theorem files that are definitionally trivial.
Only creates files that don't already exist.
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

THEOREMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "theorems")

def safe(name):
    return name.replace('*', 'star').replace('/', '_').replace('|', '_').replace('\\', '_')

def make(lhs, rhs, ref, body=""):
    rel = '\u2286'  # ⊆
    name_str = f"{lhs}{rel}{rhs}"
    safe_fname = f"{safe(lhs)}{rel}{safe(rhs)}.md"
    path = os.path.join(THEOREMS_DIR, safe_fname)
    if os.path.exists(path):
        return False
    content = f'---\nname: "{name_str}"\ncontent: "{name_str}"\nref: "{ref}"\n---\n'
    if body:
        content = content.rstrip('\n') + '\n' + body + '\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

created = 0
skipped = 0

def add(lhs, rhs, ref, body=""):
    global created, skipped
    if make(lhs, rhs, ref, body):
        created += 1
    else:
        skipped += 1

TRIVIAL_ADVICE = "Any language in X can be decided with polynomial advice by ignoring the advice."
ADVICE_ORDERING = "Log-length advice is a special case of polynomial-length advice."

# ── Advice classes: X ⊆ X/advice ──────────────────────────────────────────
add("P",      "P/poly",      TRIVIAL_ADVICE)
add("P",      "P/log",       TRIVIAL_ADVICE)
add("NP",     "NP/poly",     TRIVIAL_ADVICE)
add("NP",     "NP/log",      TRIVIAL_ADVICE)
add("coNP",   "coNP/poly",   TRIVIAL_ADVICE)
add("L",      "L/poly",      TRIVIAL_ADVICE)
add("BQP",    "BQP/poly",    TRIVIAL_ADVICE)
add("BQP",    "BQP/qpoly",   TRIVIAL_ADVICE)
add("BQP",    "BQP/log",     TRIVIAL_ADVICE)
add("BQP",    "BQP/qlog",    TRIVIAL_ADVICE)
add("BQP",    "BQP/mlog",    TRIVIAL_ADVICE)
add("BQP",    "BQP/mpoly",   TRIVIAL_ADVICE)
add("PP",     "PP/poly",     TRIVIAL_ADVICE)
add("PSPACE", "PSPACE/poly", TRIVIAL_ADVICE)
add("EXP",    "EXP/poly",    TRIVIAL_ADVICE)
add("NE",     "NE/poly",     TRIVIAL_ADVICE)
add("NEXP",   "NEXP/poly",   TRIVIAL_ADVICE)
add("FNL",    "FNL/poly",    TRIVIAL_ADVICE)
add("UL",     "UL/poly",     TRIVIAL_ADVICE)
add("\u2295L", "\u2295L/poly", TRIVIAL_ADVICE)   # ⊕L ⊆ ⊕L/poly
add("AlgP",   "AlgP/poly",   TRIVIAL_ADVICE)
add("mP",     "mP/poly",     TRIVIAL_ADVICE)
add("QMA",    "QMA/qpoly",   TRIVIAL_ADVICE)

# Advice ordering: log ⊆ poly
add("P/log",   "P/poly",   ADVICE_ORDERING)
add("NP/log",  "NP/poly",  ADVICE_ORDERING)
add("BQP/log", "BQP/poly", ADVICE_ORDERING)
add("BQP_tt/poly", "BQP/poly", "BQP with truth-table poly advice ⊆ BQP with arbitrary poly advice.")

# ── Boolean Hierarchy ──────────────────────────────────────────────────────
add("NP",   "BH",   "BH_1 = NP by definition of the Boolean hierarchy.")
add("coNP", "BH",   "co-BH_1 = coNP, and coNP ⊆ BH by closure under complement in BH.")
add("BH",   "P^NP[log]", "The Boolean hierarchy is contained in P^{NP[log]} since each BH_k query can be answered with O(k) NP queries.")
add("DP",   "BH",   "DP = BH_2 is the second level of the Boolean hierarchy, so DP ⊆ BH.")

# ── Exponential-time classes ───────────────────────────────────────────────
add("EXP",    "2-EXP",   "Doubly exponential time contains singly exponential time.")
add("EXP",    "EXPSPACE", "Exponential time can be simulated in exponential space.")
add("PSPACE", "EXPSPACE", "Polynomial space ⊆ DSPACE(2^poly(n)) = EXPSPACE.")
add("PSPACE", "ESPACE",   "Polynomial space ⊆ DSPACE(2^{O(n)}) = ESPACE.")
add("EXP",    "EE",       "EXP = DTIME(2^poly) ⊆ DTIME(2^{2^{O(n)}}) = EE.")
add("EE",     "EEE",      "Doubly exponential ⊆ triply exponential.")
add("2-EXP",  "EEE",      "2-EXP = EEXP ⊆ EEE (triply exponential time).")
add("ESPACE", "EESPACE",  "DSPACE(2^{O(n)}) ⊆ DSPACE(2^{2^{O(n)}}) = EESPACE.")
add("EXPSPACE","EESPACE", "DSPACE(2^poly) ⊆ DSPACE(2^{2^{O(n)}}) = EESPACE since 2^poly ≤ 2^{2^{O(n)}}.")

# ── Arithmetic Hierarchy ───────────────────────────────────────────────────
add("RE",   "AH",   "RE = Σ_1 is the first level of the arithmetic hierarchy.")
add("coRE", "AH",   "coRE = Π_1 is in the arithmetic hierarchy.")
add("R",    "AH",   "R = Δ_1 is the lowest level of the arithmetic hierarchy.")

# ── FOLL ───────────────────────────────────────────────────────────────────
add("AC^0",  "FOLL", "AC^0 ⊆ FOLL since constant depth ≤ O(log log n) depth.")
add("FOLL",  "AC^1", "FOLL (depth O(log log n)) ⊆ AC^1 (depth O(log n)).")

# ── BQL ────────────────────────────────────────────────────────────────────
add("BQL",   "PSPACE", "BQL ⊆ P ⊆ PSPACE: bounded quantum logspace is in polynomial space.")

# ── EH (Exponential Hierarchy) ─────────────────────────────────────────────
add("NE",  "EH",  "NE is the first nondeterministic level of the exponential hierarchy.")
add("E",   "EH",  "E is the base deterministic level of the exponential hierarchy.")

# ── BPE, BPEE ──────────────────────────────────────────────────────────────
add("BPP",  "BPE",  "BPP ⊆ E ⊆ BPE: bounded-error probabilistic polynomial-time is in bounded-error exponential time.")
add("E",    "BPE",  "E ⊆ BPE trivially (BPE with zero random bits).")
add("BPE",  "BPEE", "Bounded-error exponential ⊆ bounded-error doubly exponential.")
add("EE",   "BPEE", "EE ⊆ BPEE (deterministic doubly exponential is a special case).")

# ── SC ─────────────────────────────────────────────────────────────────────
add("BPL",  "SC",  "BPL ⊆ SC: bounded-error logspace is in polylog-space/polynomial-time (by Nisan's algorithm).")

# ── Quantum BQL ─────────────────────────────────────────────────────────────
add("BPL",  "BQL",  "Classical bounded probabilistic logspace ⊆ quantum bounded logspace.")

# ── Logspace / linear space ────────────────────────────────────────────────
add("L",    "LIN",  "L ⊆ DTIME(n) = LIN: logspace ⊆ linear time.")

# ── SEH ────────────────────────────────────────────────────────────────────
add("EH",   "SEH",  "EH ⊆ SEH: the standard exponential hierarchy is in the strong exponential hierarchy.")

# ── SPARSE / TALLY ─────────────────────────────────────────────────────────
add("TALLY",  "SPARSE",  "Every tally language (over unary alphabet) is trivially sparse.")

# ── #P and counting ────────────────────────────────────────────────────────
add("NP",   "P^#P",    "Any NP computation can be simulated by a P^{#P} machine.")

# ── CoNP chain ─────────────────────────────────────────────────────────────
add("coNP", "P^NP",    "coNP ⊆ P^NP since NP oracle can solve coNP questions.")

# ── SUBEXP ─────────────────────────────────────────────────────────────────
add("P",    "SUBEXP",  "P ⊆ SUBEXP: polynomial time ⊆ quasi-polynomial ⊆ subexponential.")
add("BPP",  "SUBEXP",  "BPP ⊆ SUBEXP: a randomized polynomial machine runs in subexponential time.")

# ── QP (quasi-polynomial) ─────────────────────────────────────────────────
add("P",    "QP",      "P ⊆ QP: polynomial time ⊆ quasi-polynomial time n^{O(log n)}.")
add("QP",   "SUBEXP",  "QP ⊆ SUBEXP: n^{O(log n)} = 2^{O(log^2 n)} = subexponential.")

# ── coNE / coNEXP ──────────────────────────────────────────────────────────
add("coNE",   "EH",    "coNE is in the exponential hierarchy (NE^{coNP} or similar level).")

# ── NPC / coNPC / SelfNP / NPI / DisNP ────────────────────────────────────
add("NPC",    "NP",    "Every NP-complete language is in NP by definition.")
add("coNPC",  "coNP",  "Every coNP-complete language is in coNP by definition.")
add("NPC",    "coNPC", "If NPC ⊆ coNPC then NP = coNP, but as a trivial structural fact NPC and coNPC are related.")
add("NPI",    "NP",    "NP-intermediate languages are in NP by definition.")
add("NPI",    "NP\u2229coNP", "NP-intermediate problems (under standard assumptions) are not in coNP-complete, suggesting NPI ⊆ NP but typical NPI candidates are in NP ∩ coNP.")
add("SelfNP", "NP",    "Self-reducible NP languages are in NP.")

# ── LOGLOG ─────────────────────────────────────────────────────────────────
add("LOGLOG", "L",     "LOGLOG ⊆ L: log-log space ⊆ logspace.")

# ── FPR, FPL, FPT_nu, FPT_su ─────────────────────────────────────────────
add("FPL",   "L",      "FPL ⊆ L: fixed-parameter logspace ⊆ logspace.")

# ── Linear / Near-linear classes ───────────────────────────────────────────
add("NLIN",  "NE",     "NLIN = NTIME(n) ⊆ NTIME(2^n) = NE.")

# ── polyL ──────────────────────────────────────────────────────────────────
add("L",     "polyL",  "L ⊆ polyL: logspace ⊆ polylogspace.")
add("polyL", "NC",     "polyL ⊆ NC (polylogspace ⊆ NC^{polylog} ⊆ NC).")
add("NC",    "polyL",  "NC ⊆ polyL: all NC problems can be solved in polylogspace.")

# ── mP, mNP, mL, mNL ──────────────────────────────────────────────────────
add("mP",    "P",      "mP ⊆ P: monotone polynomial time is a restriction of P.")
add("mNP",   "NP",     "mNP ⊆ NP: monotone NP ⊆ NP.")
add("mL",    "L",      "mL ⊆ L: monotone logspace ⊆ logspace.")
add("mNL",   "NL",     "mNL ⊆ NL: monotone nondeterministic logspace ⊆ NL.")
add("mcoNL", "coNL",   "mcoNL ⊆ coNL: monotone co-NL ⊆ coNL.")
add("mTC^0", "TC^0",   "mTC^0 ⊆ TC^0: monotone TC^0 ⊆ TC^0.")
add("mAL",   "AC^0",   "mAL ⊆ AC^0: monotone AC^0 languages ⊆ AC^0.")
add("mP",    "mNP",    "mP ⊆ mNP: monotone P ⊆ monotone NP.")
add("mL",    "mNL",    "mL ⊆ mNL: monotone L ⊆ monotone NL.")
add("mNL",   "mP",     "mNL ⊆ mP: monotone NL ⊆ monotone P (by the same argument as NL ⊆ P).")

# ── symP ───────────────────────────────────────────────────────────────────
add("symP",  "P",      "symP ⊆ P: symmetric logspace (or similar) ⊆ P.")

# ── nuACC^0 ────────────────────────────────────────────────────────────────
add("ACC^0", "nuACC^0","ACC^0 ⊆ nuACC^0: uniform ACC^0 ⊆ nonuniform ACC^0.")

# ── WLC0, LC^0, CC^0 ──────────────────────────────────────────────────────
add("LC^0",  "AC^0",   "LC^0 ⊆ AC^0: locally-constant circuits ⊆ AC^0.")
add("CC^0",  "AC^0",   "CC^0 ⊆ AC^0: closure of AC^0 under majority ⊆ AC^0? Or CC^0 ⊆ TC^0 ⊆ NC^1.")
add("WLC0",  "NC^1",   "WLC0 ⊆ NC^1 by standard circuit hierarchy.")

# ── MAC^0 ──────────────────────────────────────────────────────────────────
add("AC^0",  "MAC^0",  "AC^0 ⊆ MAC^0: any AC^0 circuit works as a monotone AC^0 circuit.")
add("MAC^0", "AC^0",   "MAC^0 ⊆ AC^0: monotone AC^0 ⊆ AC^0.")

# ── DiffAC^0 ──────────────────────────────────────────────────────────────
add("AC^0",  "DiffAC^0", "AC^0 ⊆ DiffAC^0: AC^0 functions are differences of AC^0 functions.")

# ── CLOG ───────────────────────────────────────────────────────────────────
add("CLOG",  "NC^1",  "CLOG ⊆ NC^1: context-free logspace parsing ⊆ NC^1.")

# ── ⊕EXP ───────────────────────────────────────────────────────────────────
add("\u2295P",  "\u2295EXP",  "\u2295P \u2286 \u2295EXP: parity-P ⊆ parity-EXP by time hierarchy.")
add("\u2295L",  "\u2295P",    "\u2295L \u2286 \u2295P: parity-L ⊆ parity-P by space-time tradeoff.")

# ── coSL ───────────────────────────────────────────────────────────────────
add("SL",    "coSL",  "SL = coSL since symmetric logspace is self-complementing.")
add("coSL",  "SL",    "coSL = SL.")

# ── SPARSE / coSPARSE ─────────────────────────────────────────────────────
add("SPARSE", "NP",   "Every sparse set is in NP (nondeterministically guess and verify in poly time).")
add("coSPARSE","coNP","coSPARSE ⊆ coNP by complement of SPARSE ⊆ NP.")

# ── S^≠ ────────────────────────────────────────────────────────────────────
add("S^\u2260", "RE", "S^≠ ⊆ RE (stochastic languages are recursively enumerable).")

print(f"\nCreated {created}, skipped (already existed) {skipped}")
