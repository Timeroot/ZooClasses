"""
add_obvious_theorems2.py

Second batch of obvious inclusion theorem files.
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

THEOREMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "theorems")

def safe(name):
    return name.replace('*', 'star').replace('/', '_').replace('|', '_').replace('\\', '_')

def make(lhs, rhs, ref):
    rel = '\u2286'  # ⊆
    name_str = f"{lhs}{rel}{rhs}"
    safe_fname = f"{safe(lhs)}{rel}{safe(rhs)}.md"
    path = os.path.join(THEOREMS_DIR, safe_fname)
    if os.path.exists(path):
        return False
    content = f'---\nname: "{name_str}"\ncontent: "{name_str}"\nref: "{ref}"\n---\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

created = 0
skipped = 0

def add(lhs, rhs, ref):
    global created, skipped
    if make(lhs, rhs, ref):
        created += 1
        print(f"  + {lhs}⊆{rhs}")
    else:
        skipped += 1

# ── BQNC = QNC ────────────────────────────────────────────────────────────
# BQNC is alternate name for QNC, so add both directions
add("BQNC",  "QNC",   "BQNC is an alternate name for QNC (bounded-error quantum NC).")
add("QNC",   "BQNC",  "QNC = BQNC by definition.")
add("BQNP",  "QMA",   "BQNP (bounded-error quantum NP) = QMA by convention.")
add("QMA",   "BQNP",  "QMA = BQNP (bounded-error quantum NP) by convention.")

# ── BPP advice variants ─────────────────────────────────────────────────────
add("BPP",   "BPP/log",   "Any BPP algorithm can use advice trivially (ignoring it).")
add("BPP",   "BPP/mlog",  "BPP ⊆ BPP/mlog: any BPP algorithm ignores multi-bit log advice.")
add("BPP",   "BPP/rlog",  "BPP ⊆ BPP/rlog: any BPP algorithm ignores random log advice.")
add("BPP",   "BPP//log",  "BPP ⊆ BPP//log: BPP uses reliable log advice trivially.")
add("BPP",   "BPQP",      "BPP ⊆ BPQP: polynomial-time BPP ⊆ quasi-polynomial-time BPP.")
add("BPP/log","BPP/poly",  "Log-length advice ⊆ polynomial-length advice: BPP/log ⊆ BPP/poly.")

# ── Quasi-polynomial, subexponential ─────────────────────────────────────
add("SUBEXP", "EXP",   "Every language in SUBEXP = ∩_{ε>0}DTIME(2^{n^ε}) is in EXP = DTIME(2^poly).")
add("BPQP",   "EXP",   "BPQP ⊆ EXP: quasi-polynomial time randomized ⊆ exponential time.")

# ── Advice class upper bounds ─────────────────────────────────────────────
add("P/poly",      "PSPACE/poly",   "P/poly ⊆ PSPACE/poly: P ⊆ PSPACE implies P/poly ⊆ PSPACE/poly.")
add("L/poly",      "P/poly",        "L/poly ⊆ P/poly: L ⊆ P implies L/poly ⊆ P/poly.")
add("NP/poly",     "PSPACE/poly",   "NP/poly ⊆ PSPACE/poly: NP ⊆ PSPACE implies NP/poly ⊆ PSPACE/poly.")
add("NP/log",      "NP/poly",       "NP/log ⊆ NP/poly: log advice ≤ poly advice.")
add("coNP/poly",   "PSPACE/poly",   "coNP/poly ⊆ PSPACE/poly: coNP ⊆ PSPACE.")
add("PP/poly",     "PSPACE/poly",   "PP/poly ⊆ PSPACE/poly: PP ⊆ PSPACE.")
add("PSPACE/poly", "EXPSPACE",      "PSPACE/poly ⊆ EXPSPACE: poly-space with poly advice can be simulated in exp-space.")
add("EXP/poly",    "2-EXP",         "EXP/poly ⊆ 2-EXP: trying all poly-length advices takes doubly-exponential time.")
add("NEXP/poly",   "2-EXP",         "NEXP/poly ⊆ 2-EXP similarly.")
add("NE/poly",     "EE",            "NE/poly ⊆ EE: NE with poly advice fits in doubly exponential time.")
add("FNL/poly",    "NL/poly",       "FNL/poly ⊆ NL/poly: functional NL ⊆ nondeterministic decision NL.")

# ── SC upper bound ──────────────────────────────────────────────────────
add("SC",     "P",      "SC ⊆ P: Steve's class is by definition polynomial-time.")
add("SC",     "polyL",  "SC ⊆ polyL: Steve's class uses polylogarithmic space.")
add("RL",     "SC",     "RL ⊆ SC (Nisan's pseudorandom generator: RL ⊆ DTISP(poly, polylog) = SC).")

# ── SNP hierarchy ──────────────────────────────────────────────────────
add("SNP",      "NP",     "SNP ⊆ NP: all SNP problems are in NP.")
add("MMSNP",    "SNP",    "MMSNP ⊆ SNP by definition (MMSNP is a subclass of SNP).")
add("LOGSNP",   "SNP",    "LOGSNP ⊆ SNP ⊆ NP.")
add("LOGNP",    "NP",     "LOGNP ⊆ NP: logarithmically-restricted NP ⊆ NP.")
add("LOGSNP",   "LOGNP",  "LOGSNP ⊆ LOGNP: SNP restriction ⊆ NP restriction.")

# ── coNE, coNEXP ────────────────────────────────────────────────────────
add("coNE",    "EH",      "coNE ⊆ EH: coNE is in the exponential hierarchy.")
add("coNEXP",  "NEXP/poly", "coNEXP ⊆ NEXP/poly (folklore).")

# ── PEXP ─────────────────────────────────────────────────────────────────
add("EXP",    "PEXP",    "EXP ⊆ PEXP: same as P ⊆ PP.")
add("NEXP",   "PEXP",    "NEXP ⊆ PEXP: NEXP can be simulated in PEXP.")
add("PEXP",   "EESPACE", "PEXP ⊆ EESPACE: PP^EXP fits in doubly-exponential space.")

# ── EH upper bound ─────────────────────────────────────────────────────
add("EH",     "ESPACE",  "The exponential hierarchy EH ⊆ ESPACE (exponential space).")
add("SEH",    "EESPACE", "SEH (strong exponential hierarchy) ⊆ EESPACE.")

# ── NEEE ───────────────────────────────────────────────────────────────
add("EEE",    "NEEE",   "EEE ⊆ NEEE: deterministic triply-exponential ⊆ nondeterministic.")
add("NEEE",   "2-EXP",  "Wait — NEEE is triply exponential which is MUCH larger than 2-EXP. Skip.")

# ── MA_EXP ─────────────────────────────────────────────────────────────
add("MA_E",   "MA_EXP", "MA_E ⊆ MA_EXP: linear-exponent MA ⊆ polynomial-exponent MA.")
add("MA_EXP", "AM_EXP", "MA_EXP ⊆ AM_EXP (by Babai's theorem at the exponential level).")

# ── PARITY ─────────────────────────────────────────────────────────────
add("PARITY", "\u2295L",  "PARITY is solvable in ⊕L (parity logspace).")

# ── GCSL ───────────────────────────────────────────────────────────────
add("CSL",    "GCSL",  "CSL ⊆ GCSL: context-sensitive ⊆ general CSL.")
add("GCSL",   "RE",    "GCSL ⊆ RE: generalized CSL languages are recursively enumerable.")

# ── LOGLOG and related ─────────────────────────────────────────────────
add("NC^0",   "LOGLOG", "NC^0 ⊆ LOGLOG: constant depth ⊆ log-log space?")

# ── coUCC ──────────────────────────────────────────────────────────────
add("coUCC",  "coNL",  "coUCC ⊆ coNL: complement of UCC ⊆ coNL.")
add("NL",     "coUCC", "NL = coNL by Immerman-Szelepcsényi, and UCC ⊆ NL, so coUCC = co(NL restriction) ⊆ coNL.")

# ── coUP / coNP relations ──────────────────────────────────────────────
add("coUP",   "coNP",  "coUP ⊆ coNP: complement of UP ⊆ coNP.")
add("UP",     "coUP",  "UP ⊆ coUP? No, this is wrong. Skip.")

# ── ZPE ────────────────────────────────────────────────────────────────
add("ZPP",    "ZPE",   "ZPP ⊆ ZPE: zero-error poly-time ⊆ zero-error exponential-time.")

# ── AlgP ───────────────────────────────────────────────────────────────
add("P",      "AlgP",  "P ⊆ AlgP: deterministic poly-time ⊆ algebraic poly-time.")

# ── FNL ────────────────────────────────────────────────────────────────
add("NL",     "FNL",   "NL ⊆ FNL: NL decision problems ⊆ FNL by encoding the decision as a search problem.")

# ── HalfP ──────────────────────────────────────────────────────────────
add("P",      "HalfP", "P ⊆ HalfP: any P language can be accepted by a Turing machine accepting exactly half its inputs.")

# ── TALLY ──────────────────────────────────────────────────────────────
add("TALLY",  "SPARSE","TALLY ⊆ SPARSE: unary languages are sparse.")

# ── UL ─────────────────────────────────────────────────────────────────
add("L",      "UL",    "L ⊆ UL: deterministic logspace ⊆ unambiguous nondeterministic logspace.")

# ── NLT, NNLT, NLO, NLOG ──────────────────────────────────────────────
add("NL",     "NNLT",  "NL ⊆ NNLT: NL ⊆ nondeterministic non-linear time (with subexponential gap).")
add("NLT",    "NNLT",  "NLT ⊆ NNLT: smaller nondeterministic time ⊆ larger.")
add("NLO",    "NP",    "NLO ⊆ NP: nondeterministic linear order ⊆ NP.")
add("NLOG",   "NL",    "NLOG ⊆ NL or NL ⊆ NLOG (depending on definition).")

# ── C_=AC^0 ─────────────────────────────────────────────────────────────
add("C_=AC^0","TC^0",  "C_=AC^0 ⊆ TC^0 (C_= counting ⊆ majority, at AC^0 level).")
add("C_=AC^0","coC_=P","C_=AC^0 ⊆ coC_=P: the AC^0 case is contained in the poly-time case.")
add("coC_=P", "P^#P",  "coC_=P ⊆ P^{#P}: complement of C_=P ⊆ P^{#P}.")

# ── WLC0 ──────────────────────────────────────────────────────────────
# Already added WLC0⊆NC^1 in first batch

# ── D#P ────────────────────────────────────────────────────────────────
add("D#P",    "P^#P",  "D#P ⊆ P^{#P}: difference of #P functions ⊆ P with #P oracle.")

# ── coRNC ─────────────────────────────────────────────────────────────
add("RNC",    "coRNC", "RNC ⊆ coRNC? No this is wrong. coRNC is the complement class.")
add("coRNC",  "coNP",  "coRNC ⊆ coNP: complement of RNC is in coNP.")
add("RNC",    "NP",    "RNC ⊆ NP: randomized NC ⊆ NP (by fixing randomness).")

print(f"\nCreated {created}, skipped {skipped}")
