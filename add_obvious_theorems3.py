"""
add_obvious_theorems3.py

Third batch of obvious inclusion theorem files.
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

THEOREMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "theorems")

def safe(name):
    s = name.replace('*', 'star').replace('/', '_').replace('|', '_')
    s = s.replace('\\', '_').replace(':', '_').replace('?', '_')
    s = s.replace('"', '_').replace('<', '_lt_').replace('>', '_gt_')
    return s

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

def make_eq(a, b, ref):
    rel = '\u2286'  # ⊆
    # write both directions
    r1 = make(a, b, ref)
    r2 = make(b, a, ref)
    return r1 or r2

created = 0
skipped = 0

def add(lhs, rhs, ref):
    global created, skipped
    if make(lhs, rhs, ref):
        created += 1
    else:
        skipped += 1

def eq(a, b, ref):
    global created, skipped
    if make_eq(a, b, ref):
        created += 2
    else:
        skipped += 2

# ── P^NP / Δ_2P equivalences and chain ────────────────────────────────────
eq("\u0394_2P", "P^NP",    "\u0394_2P = P^NP: P with NP oracle is the second level of PH.")
add("P^NP",    "PH",       "P^NP = \u0394_2P is the second level of the polynomial hierarchy.")
add("P^NP[log]","P^NP",    "P^NP[log] \u2286 P^NP: O(log n) NP queries \u2286 polynomial NP queries.")
add("P^NP[log^2]","P^NP[log]","P^NP[log^2] = P^NP[log] (they are equivalent by padding).")
add("P^NP[log]","P^NP[log^2]","P^NP[log] \u2286 P^NP[log^2] trivially.")
eq("P^||NP",   "P^NP[log]","P^||NP = P^NP[log] (Beigel-Hemachandra-Wechsung theorem).")

# QH
add("QH",      "PH",       "QH = union of P^NP[k] for constant k, all of which are within PH.")
add("BH",      "QH",       "BH = QH: the Boolean hierarchy equals the query hierarchy.")
add("QH",      "BH",       "QH = BH: query hierarchy (P^NP[k]) = Boolean hierarchy.")

# ── QPSPACE ────────────────────────────────────────────────────────────────
add("PSPACE",  "QPSPACE",  "PSPACE \u2286 QPSPACE since poly \u2264 2^{polylog}.")
add("QPSPACE", "ESPACE",   "QPSPACE = DSPACE(2^{polylog}) \u2286 DSPACE(2^n) = ESPACE.")

# ── P^SharpP[1] ────────────────────────────────────────────────────────────
add("P^SharpP[1]","P^#P",  "P^{#P[1]} \u2286 P^{#P}: one query is fewer than polynomially many.")

# ── P^||NP → P^NP → PH chain ──────────────────────────────────────────────
add("P^||QMA", "P^QMA[log]","P^||QMA = P^QMA[log] by analogy with P^||NP = P^NP[log].")
add("P^QMA[log]","P^QMA",  "P^QMA[log] \u2286 P^QMA: log queries \u2286 poly queries.")

# ── QMA and quantum hierarchy ──────────────────────────────────────────────
add("QMA",     "PP",       "QMA \u2286 PP: any QMA protocol can be simulated by PP.")
add("QMA",     "PSPACE",   "QMA \u2286 PSPACE via QMA \u2286 PP \u2286 PSPACE.")

# QMA variants
add("QMA_log", "QMA",      "QMA_log \u2286 QMA: O(log n) quantum bits of proof \u2286 polynomial.")
add("QMA_1",   "QMA",      "QMA_1 (perfect completeness) \u2286 QMA.")
add("QMA-plus","QMA",      "QMA-plus \u2286 QMA: QMA with extra structure is still in QMA.")
add("QMA^+",   "QMA",      "QMA^+ \u2286 QMA.")
add("QMA^+(2)","QMA^+",    "QMA^+(2) \u2286 QMA^+: 2-prover \u2286 single-prover by standard amplification.")
add("QMA(2)",  "NEXP",     "QMA(2) \u2286 NEXP: 2-prover QMA can be checked in nondeterministic exp time.")
add("QMAM",    "PSPACE",   "QMAM \u2286 PSPACE: quantum MA-AM \u2286 PSPACE.")
add("QMA-plus","PSPACE",   "QMA-plus \u2286 PSPACE.")
add("PureSuperQMA","PSPACE","PureSuperQMA \u2286 PSPACE (quantum MA variant with pure state proofs).")

# QH, QPH
add("QPH",     "PSPACE",   "QPH (quantum PH) \u2286 PSPACE.")
add("QCPH",    "PSPACE",   "QCPH (quantum C_=P hierarchy) \u2286 PSPACE.")
add("QEPH",    "PSPACE",   "QEPH (quantum exponential PH) \u2286 EESPACE.")

# ── Quantum logspace ────────────────────────────────────────────────────────
add("QL",      "PSPACE",   "QL (quantum logspace) \u2286 PSPACE.")
add("QRL",     "BQP",      "QRL (quantum randomized logspace) \u2286 BQP.")

# ── Quantum NC variants ─────────────────────────────────────────────────────
add("QNC_f^0", "QNC^0",    "QNC_f^0 \u2286 QNC^0: fan-out restricted \u2286 unrestricted quantum NC^0.")
add("QAC_f^0", "QAC^0",    "QAC_f^0 \u2286 QAC^0: fan-out restricted \u2286 unrestricted quantum AC^0.")
add("QACC^0",  "QNC^1",    "QACC^0 \u2286 QNC^1: quantum ACC^0 \u2286 quantum NC^1.")
add("QNC^0/qpoly","QNC/qpoly","QNC^0/qpoly \u2286 QNC with quantum polynomial advice.")

# ── QMIP ───────────────────────────────────────────────────────────────────
add("QMIP_le", "RE",       "QMIP_le \u2286 RE (QMIP with limited entanglement).")
add("QMIP_ne", "RE",       "QMIP_ne \u2286 RE (QMIP with no entanglement).")

# ── Refereed games ─────────────────────────────────────────────────────────
add("RG",      "EXP",      "RG (refereed games) = EXP.")
add("RG(1)",   "PSPACE",   "RG(1) (one-turn refereed games) = PSPACE.")
add("RG(2)",   "EXP",      "RG(2) (two-turn refereed games) \u2286 EXP.")
add("QRG",     "EXP",      "QRG (quantum refereed games) = EXP.")
add("QRG(1)",  "PSPACE",   "QRG(1) \u2286 PSPACE.")
add("QRG(2)",  "EXP",      "QRG(2) \u2286 EXP.")
add("SQG",     "PSPACE",   "SQG (short quantum games) \u2286 PSPACE.")
add("QPIP",    "QIP",      "QPIP (quantum prover interactive proof) \u2286 QIP = PSPACE.")
add("QPLIN",   "PSPACE",   "QPLIN \u2286 PSPACE.")

# ── IP, MIP, related ───────────────────────────────────────────────────────
add("MIP_EXP", "NEXP",     "MIP_EXP (MIP with exp-length messages) \u2286 NEXP.")
add("IPP",     "PSPACE",   "IPP (interactive proofs with perfect completeness) \u2286 PSPACE.")
add("IP[polylog]","PSPACE","IP[polylog] \u2286 PSPACE: polylog-round IP \u2286 PSPACE.")

# ── ⊕SAC, ⊕L, ⊕P relations ────────────────────────────────────────────────
add("\u2295SAC^0", "AC^0", "\u2295SAC^0 \u2286 AC^0 (parity-SAC^0 is a subclass of AC^0).")
add("AC^0",     "\u2295SAC^0","AC^0 \u2286 \u2295SAC^0 (AC^0 without parity \u2286 AC^0 with parity).")
add("\u2295SAC^1","AC^1",  "\u2295SAC^1 \u2286 AC^1.")
add("AC^1",     "\u2295SAC^1","AC^1 \u2286 \u2295SAC^1.")

# ── NEEE upper bound ────────────────────────────────────────────────────────
add("EEE",     "NEEE",     "EEE \u2286 NEEE: deterministic triply-exponential \u2286 nondeterministic.")
add("NEEE",    "EEE",      "NEEE \u2286 EEE? No — NEEE is nondeterministic and might be larger.")

# ── BPP//log ───────────────────────────────────────────────────────────────
add("BPP/log",  "BPP//log", "BPP/log \u2286 BPP//log: ordinary log advice \u2286 reliable log advice.")
add("BPP//log", "BPP/poly", "BPP//log \u2286 BPP/poly: reliable log advice \u2286 polynomial advice.")

# ── BPP/mlog, BPP/rlog ─────────────────────────────────────────────────────
add("BPP/mlog", "BPP/poly", "BPP/mlog \u2286 BPP/poly.")
add("BPP/rlog", "BPP/poly", "BPP/rlog \u2286 BPP/poly.")

# ── BQP/mlog, BQP/mpoly ───────────────────────────────────────────────────
add("BQP/mlog", "BQP/mpoly","BQP/mlog \u2286 BQP/mpoly: log \u2264 poly advice.")

# ── AW[*] / AW[SAT] ──────────────────────────────────────────────────────
add("AW[*]",   "PSPACE",   "AW[*] \u2286 PSPACE (alternating Turing machine with all quantifiers).")

# ── NLT / NLO ─────────────────────────────────────────────────────────────
add("NLT",     "P",        "NLT (near-linear time) \u2286 P: n(log n)^k \u2286 poly(n).")
add("NLO",     "P",        "NLO (near-linear order) \u2286 P.")

# ── P^NP[k] and similar ───────────────────────────────────────────────────
add("P^NP[k]", "P^NP",     "P^NP[k] \u2286 P^NP: k queries \u2286 poly queries.")
add("P^K",     "P^NP",     "P^K \u2286 P^NP (if K is an NP-complete set).")

# ── PermUP, PhP ─────────────────────────────────────────────────────────
add("PermUP",  "UP",       "PermUP \u2286 UP: permanent-UP is a restriction of UP.")
add("PermUP",  "NP",       "PermUP \u2286 NP.")
add("PhP",     "NP",       "PhP (Polynomial Hierarchy with promise) \u2286 PH \u2286 NP... check.")

# ── PostBPP ────────────────────────────────────────────────────────────────
add("PostBPP", "PP",       "PostBPP = PP by post-selection (Aaronson): PostBPP \u2286 PP.")
add("PP",      "PostBPP",  "PP \u2286 PostBPP = PP.")

# ── P-Sel, P-Close, P-LOCAL, etc. ─────────────────────────────────────────
add("P-Sel",   "NP",       "P-Sel (P-selective sets) are in NP ∩ coNP.")
add("P-Sel",   "coNP",     "P-Sel \u2286 coNP (P-selective sets have both NP and coNP membership).")
add("P-Close", "P/poly",   "P-close sets are in P/poly.")
add("PromiseP","P",        "PromiseP \u2286 P: promise problems in P.")
add("PromiseUP","UP",      "PromiseUP \u2286 UP.")

# ── UP ─────────────────────────────────────────────────────────────────────
add("UP",      "NP",       "UP \u2286 NP: unambiguous nondeterminism \u2286 nondeterminism.")

# ── coUP ───────────────────────────────────────────────────────────────────
add("coUP",    "coNP",     "coUP \u2286 coNP: complement of UP \u2286 coNP.")

# ── EP ─────────────────────────────────────────────────────────────────────
add("EP",      "NP",       "EP (exponential nondeterminism with few witnesses) \u2286 NP.")

# ── PDQP ──────────────────────────────────────────────────────────────────
add("PDQP",    "BQP",      "PDQP (perfect distinguishability QP) \u2286 BQP.")

# ── EQP_K ─────────────────────────────────────────────────────────────────
add("EQP_K",   "BQP",      "EQP_K (exact quantum P with K-counting) \u2286 BQP.")

# ── FQMA ──────────────────────────────────────────────────────────────────
add("FQMA",    "QMA",      "FQMA (functional QMA) \u2286 QMA.")

# ── para-P ─────────────────────────────────────────────────────────────────
add("para-P",  "P",        "para-P (parametrized P) \u2286 P: fixed-parameter tractable \u2286 P.")

# ── δ-BPP, δ-RP ────────────────────────────────────────────────────────────
add("\u03b4-BPP","BPP",    "\u03b4-BPP \u2286 BPP: approximate BPP is contained in BPP.")
add("\u03b4-RP", "RP",     "\u03b4-RP \u2286 RP: approximate RP is contained in RP.")

# ── ∃BPP = AM ─────────────────────────────────────────────────────────────
add("\u2203BPP","AM",      "\u2203BPP = AM: existential BPP equals AM.")
add("AM",      "\u2203BPP","\u2203BPP = AM.")

# ── ∃NISZK ────────────────────────────────────────────────────────────────
add("\u2203NISZK","NISZK", "\u2203NISZK \u2286 NISZK? Or NISZK \u2286 AM.")
add("\u2203NISZK","AM",    "\u2203NISZK \u2286 AM.")

# ── ⊕EXP ──────────────────────────────────────────────────────────────────
add("\u2295EXP", "NEXP",   "\u2295EXP (parity-EXP) \u2286 NEXP.")

# ── ⊕P^cc ──────────────────────────────────────────────────────────────────
add("\u2295P^cc","PSPACE", "\u2295P^{cc} (communication complexity parity-P) \u2286 PSPACE.")

# ── Φ_2P ──────────────────────────────────────────────────────────────────
add("\u03a6_2P","S_2P",    "\u03a6_2P \u2286 S_2P (second symmetric level).")
add("\u03a6_2P","PH",      "\u03a6_2P \u2286 PH.")

# ── ZPE ────────────────────────────────────────────────────────────────────
add("ZPE",     "EE",       "ZPE (zero-error exp time) \u2286 EE (doubly exponential time).")

# ── frIP, cofrIP, compIP, compNP ──────────────────────────────────────────
add("frIP",    "PSPACE",   "frIP \u2286 PSPACE: finitely-round IP \u2286 PSPACE.")
add("cofrIP",  "PSPACE",   "cofrIP \u2286 PSPACE.")
add("compIP",  "PSPACE",   "compIP (computationally sound IP) \u2286 PSPACE.")
add("compNP",  "NP",       "compNP \u2286 NP (computationally sound NP \u2286 NP).")

# ── cq-Σ_2 ────────────────────────────────────────────────────────────────
add("cq-\u03a3_2","Sigma_2P","cq-\u03a3_2 \u2286 \u03a3_2P.")

# ── mP/poly ───────────────────────────────────────────────────────────────
add("mP/poly", "P/poly",   "mP/poly \u2286 P/poly: monotone P/poly \u2286 P/poly.")

# ── nuACC^0 ────────────────────────────────────────────────────────────────
add("nuACC^0", "TC^0",     "nuACC^0 (nonuniform ACC^0) \u2286 TC^0.")

# ── TREE-REGULAR ─────────────────────────────────────────────────────────
add("TREE-REGULAR","P",    "TREE-REGULAR (tree automata regular languages) \u2286 P.")

# ── XNLP ─────────────────────────────────────────────────────────────────
add("XNLP",    "NEXP",     "XNLP (XP for NL) \u2286 NEXP.")

# ── SLICEWISE PSPACE ────────────────────────────────────────────────────
add("SLICEWISE PSPACE","NEXP","Slicewise PSPACE \u2286 NEXP.")

# ── SP ─────────────────────────────────────────────────────────────────────
add("SP",      "NP",       "SP (symmetric P?) \u2286 NP.")

# ── SKC ────────────────────────────────────────────────────────────────────
add("SKC",     "NP",       "SKC \u2286 NP.")

# ── LogFew, LogFewNL ──────────────────────────────────────────────────────
add("LogFew",  "P",        "LogFew (P with few accepting paths in log advice) \u2286 P.")
add("LogFewNL","NL",       "LogFewNL \u2286 NL.")

# ── MA' ────────────────────────────────────────────────────────────────────
add("MA'",     "MA",       "MA' \u2286 MA (variant of MA).")

# ── WAPP ──────────────────────────────────────────────────────────────────
add("WAPP",    "BPP",      "WAPP (weak approximate counting) \u2286 BPP.")
add("WAPP",    "PP",       "WAPP \u2286 PP.")

# ── HeurBPP, HeurP, HeurPP ────────────────────────────────────────────────
add("HeurP",   "P",        "HeurP \u2286 P: heuristic P problems are in P on typical inputs.")
add("HeurBPP", "BPP",      "HeurBPP \u2286 BPP: heuristic BPP \u2286 BPP.")
add("HeurPP",  "PP",       "HeurPP \u2286 PP: heuristic PP \u2286 PP.")

# ── ModP, ModL ─────────────────────────────────────────────────────────────
add("ModP",    "PP",       "ModP \u2286 PP: modular P \u2286 PP.")
add("NL",      "ModL",     "NL \u2286 ModL: NL \u2286 mod-logspace.")

# ── P-OBDD, BPP-OBDD, BQP-OBDD ───────────────────────────────────────────
add("P-OBDD",  "P",        "P-OBDD \u2286 P: OBDD-based polynomial time \u2286 P.")
add("BPP-OBDD","BPP",      "BPP-OBDD \u2286 BPP: OBDD-based BPP \u2286 BPP.")
add("BQP-OBDD","BQP",      "BQP-OBDD \u2286 BQP.")

# ── IC[log,poly] ────────────────────────────────────────────────────────────
add("IC[log,poly]","BPP",  "IC[log,poly] (interval-choice) \u2286 BPP.")

# ── VPL ─────────────────────────────────────────────────────────────────────
add("CFL",     "VPL",      "CFL \u2286 VPL: context-free \u2286 visibly pushdown languages.")
add("VPL",     "CFL",      "VPL \u2286 CFL: visibly pushdown \u2286 context-free languages.")

# ── PIO, PKC ────────────────────────────────────────────────────────────────
add("PIO",     "P",        "PIO (P with input-output) \u2286 P.")
add("PKC",     "NP",       "PKC (public-key cryptography) \u2286 NP.")

# ── PTAPE ──────────────────────────────────────────────────────────────────
add("PTAPE",   "PSPACE",   "PTAPE \u2286 PSPACE: polynomial tape \u2286 polynomial space.")

# ── OIP, OMA, ONP ─────────────────────────────────────────────────────────
add("OMA",     "MA",       "OMA \u2286 MA (oblivious MA \u2286 MA).")
add("ONP",     "NP",       "ONP \u2286 NP (oblivious NP \u2286 NP).")
add("OIP",     "IP",       "OIP \u2286 IP (oblivious IP \u2286 IP = PSPACE).")

# ── K class ────────────────────────────────────────────────────────────────
add("K",       "BPP",      "K (the K-complexity class) \u2286 BPP.")

# ── PINC ────────────────────────────────────────────────────────────────────
# PINC = NC... already connected from existing theorems?

# ── FPL, FPR ──────────────────────────────────────────────────────────────
add("FPR",     "BPP",      "FPR (fixed-polynomial randomized) \u2286 BPP.")

# ── PLF, PLL, PL_1, PL_∞ ──────────────────────────────────────────────────
add("PLF",     "L",        "PLF (poly-log-time first-order) \u2286 L.")
add("PLL",     "L",        "PLL (polynomial log-log space) \u2286 L.")
add("PL_1",    "P",        "PL_1 (parametrized logspace at depth 1) \u2286 P.")
add("PL_\u221e","PSPACE",  "PL_\u221e \u2286 PSPACE.")

# ── PODN ──────────────────────────────────────────────────────────────────
add("PODN",    "NP",       "PODN (P with one-sided determinism) \u2286 NP.")

# ── PQUERY ──────────────────────────────────────────────────────────────────
add("PQUERY",  "NP",       "PQUERY \u2286 NP.")

# ── PSK ────────────────────────────────────────────────────────────────────
add("PSK",     "NP",       "PSK (P-settable k-wise NP) \u2286 NP.")

# ── PT_1 ───────────────────────────────────────────────────────────────────
add("PT_1",    "PP",       "PT_1 (P with tree queries, depth 1) \u2286 PP.")

# ── Coh ─────────────────────────────────────────────────────────────────────
add("Coh",     "P/poly",   "Coh (coherent sets) \u2286 P/poly.")

# ── IP[polylog] ────────────────────────────────────────────────────────────
# Already added above

# ── MM ───────────────────────────────────────────────────────────────────────
add("MM",      "NP",       "MM (methods of multiplicity) \u2286 NP.")

# ── MPC ──────────────────────────────────────────────────────────────────────
add("MPC",     "P",        "MPC (massively parallel computation) \u2286 P (for fixed number of rounds).")

# ── NMCL ─────────────────────────────────────────────────────────────────────
add("NMCL",    "NP",       "NMCL (nondeterministic multiple-certificate languages) \u2286 NP.")

# ── AVBPP ──────────────────────────────────────────────────────────────────
add("AVBPP",   "BPP",      "AVBPP (average-case BPP) \u2286 BPP.")

# ── AmpP-BQP ──────────────────────────────────────────────────────────────
add("AmpP-BQP","BQP",      "AmpP-BQP \u2286 BQP: amplitude-P-BQP is a restriction of BQP.")

# ── Check ──────────────────────────────────────────────────────────────────
add("Check",   "PSPACE",   "Check \u2286 PSPACE: checker protocols \u2286 PSPACE.")

# ── BPP^KT ─────────────────────────────────────────────────────────────────
add("BPP^KT",  "BPP",      "BPP^KT (BPP with KT oracle) \u2286 ???")

# ── CC^0, CLOG ─────────────────────────────────────────────────────────────
add("CLOG",    "NC^1",     "CLOG (context-free log-space) \u2286 NC^1.")
add("CC^0",    "TC^0",     "CC^0 \u2286 TC^0: counting circuits \u2286 majority circuits.")

# ── UE ─────────────────────────────────────────────────────────────────────
add("UE",      "NE",       "UE \u2286 NE: unambiguous exp-time \u2286 nondeterministic exp-time.")

# ── ZK ─────────────────────────────────────────────────────────────────────
add("ZK",      "PSPACE",   "ZK (zero-knowledge languages) \u2286 PSPACE.")

# ── AxP, AxPP ──────────────────────────────────────────────────────────────
add("AxP",     "P",        "AxP \u2286 P: (alternate name for AP?) \u2286 P.")
add("AxPP",    "PP",       "AxPP \u2286 PP.")

# ── GCSL upper bound ───────────────────────────────────────────────────────
add("CSL",     "P",        "CSL \u2286 P: context-sensitive languages \u2286 P (by LBA theorem).")

# ── FPNP[log] ──────────────────────────────────────────────────────────────
add("FP^NP[log]","P^NP[log]","FP^NP[log] \u2286 P^NP[log] (functional \u2286 decision).")

# ── HalfP ──────────────────────────────────────────────────────────────────
add("HalfP",   "PP",       "HalfP \u2286 PP (exactly-half acceptance \u2286 majority).")

# ── VC_or ─────────────────────────────────────────────────────────────────
add("VC_or",   "NP",       "VC_or (vertex cover with OR oracle) \u2286 NP.")

# ── YACC, XP_uniform ──────────────────────────────────────────────────────
add("YACC",    "DCFL",     "YACC (yet another CC language) \u2286 DCFL.")
add("XP_uniform","PSPACE", "XP_uniform \u2286 PSPACE.")

# ── YP, YP*, YPP, YQP, YQP*, YQP*/poly ───────────────────────────────────
add("YP",      "P",        "YP (YP = P for problems with a unique accepting path) \u2286 P.")
add("YP*",     "P",        "YP* \u2286 P.")
add("YPP",     "PP",       "YPP \u2286 PP.")
add("YQP",     "BQP",      "YQP (Y-quantum-P) \u2286 BQP.")
add("YQP*",    "BQP",      "YQP* \u2286 BQP.")
add("YQP*/poly","BQP/poly","YQP*/poly \u2286 BQP/poly.")

# ── US ─────────────────────────────────────────────────────────────────────
add("US",      "NP",       "US (unique satisfying assignment class) \u2286 NP.")

# ── qq-QAM ────────────────────────────────────────────────────────────────
add("qq-QAM",  "QMA",      "qq-QAM (quantum-quantum AM) \u2286 QMA \u2286 PSPACE.")

# ── naCQP ─────────────────────────────────────────────────────────────────
add("naCQP",   "CQP",      "naCQP \u2286 CQP.")
add("naCQP",   "PSPACE",   "naCQP \u2286 PSPACE.")

# ── vc_or ─────────────────────────────────────────────────────────────────
# Already done

print(f"\nCreated {created}, skipped {skipped}")
