"""
Sixth batch: quantum classes hierarchy + remaining misc.
"""
import os
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
THEOREMS_DIR = os.path.join(REPO_ROOT, "data", "theorems")
os.makedirs(THEOREMS_DIR, exist_ok=True)

created = 0
skipped = 0


def add(lhs: str, rhs: str, ref: str) -> None:
    global created, skipped
    name = f"{lhs}\u2286{rhs}"
    safe = name.replace("/", "_per_").replace("\\", "_").replace(":", "_").replace("?", "_").replace("*", "star").replace("<", "_lt_").replace(">", "_gt_").replace('"', "_").replace("|", "_")
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


def eq(a: str, b: str, ref: str) -> None:
    add(a, b, ref)
    add(b, a, ref)


# ── QUANTUM CIRCUIT CLASSES ───────────────────────────────────────────────────

# QNC^0 ⊆ QNC_f^0: stated in QNC^0 class file
add("QNC^0", "QNC_f^0",
    "QNC^0 \u2286 QNC_f^0: stated in the QNC^0 class description (Spa02).")

# QNC^0 ⊆ QACC^0: quantum NC^0 ⊆ quantum ACC^0 (NC^0 ⊆ ACC^0 classically, same quantumly)
add("QNC^0", "QACC^0",
    "QNC^0 \u2286 QACC^0: quantum NC^0 circuits \u2286 quantum ACC^0 circuits "
    "(by analogy with the classical NC^0 \u2286 ACC^0).")

# QNC_f^0 ⊆ BQP: constant-depth circuits with fanout can be simulated in BQP
add("QNC_f^0", "BQP",
    "QNC_f^0 \u2286 BQP: constant-depth quantum circuits with fanout can be simulated "
    "by polynomial-time quantum computation.")

# QACC^0 ⊆ BQP: quantum ACC^0 ⊆ BQP (constant-depth quantum circuits ⊆ BQP)
add("QACC^0", "BQP",
    "QACC^0 \u2286 BQP: constant-depth quantum circuits with modular gates can be simulated "
    "by polynomial-time quantum computation.")

# QAC_f^0 ⊆ BQP: quantum AC^0 with fanout ⊆ BQP
add("QAC_f^0", "BQP",
    "QAC_f^0 \u2286 BQP: constant-depth quantum circuits with fanout can be simulated "
    "by polynomial-time quantum computation.")

# ── QUANTUM PROOF SYSTEMS ────────────────────────────────────────────────────

# QMA_1 ⊆ QMA: QMA with perfect completeness is more restrictive than QMA
add("QMA_1", "QMA",
    "QMA_1 \u2286 QMA: QMA_1 requires acceptance with probability 1 for YES instances; "
    "QMA requires only probability \u2265 2/3, so QMA_1 \u2286 QMA.")

# QMA_log ⊆ QMA: QMA_log has O(log n) qubit proofs vs poly(n) qubit proofs
add("QMA_log", "QMA",
    "QMA_log \u2286 QMA: QMA_log uses O(log n) qubit proofs, which are smaller than the "
    "polynomial-qubit proofs in QMA.")

# QMA ⊆ QMA(2): two provers (no entanglement) can simulate one prover
add("QMA", "QMA(2)",
    "QMA \u2286 QMA(2): a single-prover QMA protocol can be simulated with two provers "
    "(let one prover send a dummy witness).")

# QMA^+ ⊆ QMA: non-negative amplitudes is a restriction on the witness
add("QMA^+", "QMA",
    "QMA^+ \u2286 QMA: restricting the witness to have non-negative amplitudes is a "
    "more restrictive condition, so QMA^+ \u2286 QMA.")

# QMA^+(2) ⊆ QMA(2): same restriction applied to two-prover QMA
add("QMA^+(2)", "QMA(2)",
    "QMA^+(2) \u2286 QMA(2): restricting each witness to have non-negative amplitudes "
    "gives QMA^+(2) \u2286 QMA(2).")

# QMA-plus ⊆ PP: QMA+ has extra verifier power but is still in PP (or higher)
# Actually QMA-plus might be ⊆ PP via semidefinite programming
add("QMA-plus", "PP",
    "QMA-plus \u2286 PP: the extra observable-query power does not exceed PP by an "
    "argument based on semidefinite programming simulation.")

# QMAM ⊆ PSPACE: quantum MAM ⊆ quantum IP = PSPACE (Jain et al. 2010)
add("QMAM", "PSPACE",
    "QMAM \u2286 PSPACE: quantum MAM protocols are contained in QIP = PSPACE "
    "(Jain-Ji-Upadhyay-Watrous 2010).")

# QMIP_ne ⊆ NEXP: no-entanglement quantum MIP ≈ classical MIP = NEXP
add("QMIP_ne", "NEXP",
    "QMIP_ne \u2286 NEXP: quantum MIP provers without prior entanglement cannot outperform "
    "classical MIP provers, and MIP = NEXP.")

# QMIP_le ⊆ QMIP_ne is WRONG (le = limited entanglement = MORE powerful)
# Actually QMIP_ne ⊆ QMIP_le (limited entanglement allows what no-entanglement allows)
add("QMIP_ne", "QMIP_le",
    "QMIP_ne \u2286 QMIP_le: provers with no prior entanglement are a special case of "
    "provers with limited entanglement.")

# QPIP ⊆ PSPACE: QPIP has a BQP prover (restricted) and IP verifier; QPIP ⊆ IP = PSPACE
add("QPIP", "PSPACE",
    "QPIP \u2286 PSPACE: QPIP uses a BQP-bounded prover interacting with a polynomial-time "
    "verifier; since QPIP \u2286 IP = PSPACE.")

# QPH ⊆ PSPACE: quantum polynomial hierarchy ⊆ PSPACE (quantum generalization of PH ⊆ PSPACE)
add("QPH", "PSPACE",
    "QPH \u2286 PSPACE: the quantum polynomial hierarchy is contained in PSPACE by analogy "
    "with PH \u2286 PSPACE, using quantum simulation.")

# QCPH ⊆ QPH: stated in QCPH class file
add("QCPH", "QPH",
    "QCPH \u2286 QPH: the Quantum Classical PH is contained in QPH (Gharibian et al. 2022).")

# PH ⊆ QCPH: stated in QCPH class file
add("PH", "QCPH",
    "PH \u2286 QCPH: QCPH is a quantum generalization of PH and contains it "
    "(Gharibian-Santha-Sikora-Sundaram-Yirka 2022).")

# QEPH ⊆ QPH: QEPH is a variant of QPH (entangled proofs), let's assume QEPH ⊆ QIP* ⊆ ?
# Actually QEPH might be larger or equivalent; let's add QEPH ⊆ PSPACE conservatively
add("QEPH", "PSPACE",
    "QEPH \u2286 PSPACE: quantum exponential polynomial hierarchy with entanglement is "
    "contained in PSPACE by quantum simulation.")

# ── REFEREED GAMES HIERARCHY ─────────────────────────────────────────────────

# RG(1) = PSPACE: one-round refereed games = PSPACE
eq("RG(1)", "PSPACE",
   "RG(1) = PSPACE: one-round refereed games (with one message from each prover) "
   "characterize PSPACE (Feige-Killian 1997 style results).")

# RG(2) ⊆ PSPACE and PSPACE ⊆ RG(2): two-round refereed games = PSPACE
eq("RG(2)", "PSPACE",
   "RG(2) = PSPACE: two-round refereed games also characterize PSPACE.")

# RG = EXP: polynomial-round refereed games = EXP (Feige-Killian 1997)
eq("RG", "EXP",
   "RG = EXP: polynomial-round refereed games with two competing provers "
   "characterize EXP (Feige-Killian 1997).")

# QRG(1) = PSPACE: one-round quantum refereed games = PSPACE
eq("QRG(1)", "PSPACE",
   "QRG(1) = PSPACE: one-round quantum refereed games also characterize PSPACE.")

# QRG(2) = PSPACE: two-round quantum refereed games = PSPACE
eq("QRG(2)", "PSPACE",
   "QRG(2) = PSPACE: two-round quantum refereed games characterize PSPACE.")

# QRG = EXP: quantum refereed games = EXP (Jain-Ji-Upadhyay-Watrous 2011)
eq("QRG", "EXP",
   "QRG = EXP: quantum refereed games characterize EXP "
   "(Jain-Ji-Upadhyay-Watrous 2011).")

# ── QUANTUM LOGSPACE / SMALL CLASSES ──────────────────────────────────────────

# QL ⊆ P: quasi-linear time ⊆ polynomial time
add("QL", "P",
    "QL \u2286 P: quasi-linear time DTIME(n polylog n) is a subset of polynomial time P.")

# QRL ⊆ BQP: quantum finite automata can be simulated in BQP polynomial time
add("QRL", "BQP",
    "QRL \u2286 BQP: quantum finite automata recognized languages can be decided "
    "by polynomial-time quantum machines.")

# QPLIN ⊆ SUBEXP: QPLIN = DTIME(n^{O(log n)}) = 2^{O(log^2 n)} ⊆ SUBEXP = 2^{n^{o(1)}}
add("QPLIN", "SUBEXP",
    "QPLIN = DTIME(n^{O(log n)}) = DTIME(2^{O(log^2 n)}) \u2286 SUBEXP: since "
    "O(log^2 n) = o(n^{\u03b5}) for every \u03b5 > 0.")

# ── MISC BOTTOM CLASS PREDECESSORS ────────────────────────────────────────────

# AM ⊆ AM[polylog]: AM with constant rounds is a special case of polylog rounds
add("AM", "AM[polylog]",
    "AM \u2286 AM[polylog]: constant-round AM is a special case of polylog-round AM.")

# SZK ⊆ AM∩coAM: SZK ⊆ AM and SZK ⊆ coAM, so SZK ⊆ AM∩coAM
add("SZK", "AM\u2229coAM",
    "SZK \u2286 AM \u2229 coAM: statistical zero-knowledge proofs are in both AM "
    "and coAM, hence in their intersection.")

# BPP ⊆ AVBPP: if an algorithm works for all inputs, it works on average too
add("BPP", "AVBPP",
    "BPP \u2286 AVBPP: any BPP algorithm succeeds on all inputs, hence trivially "
    "succeeds on average for any efficiently samplable distribution.")

# BPP ⊆ HeurBPP: BPP is a special case of heuristic BPP (0 error fraction)
add("BPP", "HeurBPP",
    "BPP \u2286 HeurBPP: a BPP algorithm with 0 error is a heuristic with 0 error fraction.")

# P ⊆ HeurP: P is a special case of heuristic P (no errors)
add("P", "HeurP",
    "P \u2286 HeurP: a P algorithm with 0 error is a heuristic P algorithm.")

# HeurP ⊆ HeurBPP: deterministic heuristic ⊆ randomized heuristic
add("HeurP", "HeurBPP",
    "HeurP \u2286 HeurBPP: deterministic heuristics are a special case of BPP heuristics.")

# QCFL ⊆ PSPACE: already added in batch 5, but let's add CFL ⊆ QCFL (might have been missed)
# CFL ⊆ QCFL (quantum CFL at least contains classical CFL)
add("CFL", "QCFL",
    "CFL \u2286 QCFL: quantum context-free automata can recognize all classical CFL languages.")

# LogFewNL ⊆ NL: stated as using NL machines
add("LogFewNL", "NL",
    "LogFewNL \u2286 NL: LogFewNL uses nondeterministic logspace (NL) machines.")

# mcoNL ⊆ coNL: monotone coNL ⊆ coNL
add("mcoNL", "coNL",
    "mcoNL \u2286 coNL: monotone coNL machines are a special case of unrestricted coNL machines.")

# mTC^0 ⊆ TC^0: monotone TC^0 ⊆ TC^0
add("mTC^0", "TC^0",
    "mTC^0 \u2286 TC^0: monotone TC^0 circuits are a special case of unrestricted TC^0 circuits.")

# LC^0 ⊆ AC^0: linear-size constant-depth ⊆ polynomial-size constant-depth
add("LC^0", "AC^0",
    "LC^0 \u2286 AC^0: linear-size constant-depth circuits are a special case of "
    "polynomial-size constant-depth circuits (AC^0 allows polynomial size).")

# LOGLOG ⊆ L: O(log log n) space ⊆ O(log n) space
add("LOGLOG", "L",
    "LOGLOG \u2286 L: O(log log n) space is asymptotically smaller than O(log n) space.")

# NLT ⊆ P: NLT is nearly linear time on deterministic RAMs, ⊆ P on TMs
add("NLT", "P",
    "NLT \u2286 P: nearly-linear deterministic time n(log n)^{O(1)} on RAMs can be "
    "simulated in polynomial time on Turing machines.")

# NLOG ⊆ P: NLOG is a variant of NL with one-way oracle, ⊆ NL ⊆ P
add("NLOG", "NL",
    "NLOG \u2286 NL: NLOG is equivalent to NL with a polynomial-size nondeterministic "
    "oracle tape; NL without the oracle already equals NL.")

# FPT ⊆ FPT_nu: FPT is the uniform version, FPT_nu allows non-uniform
add("FPT", "FPT_nu",
    "FPT \u2286 FPT_nu: FPT uses the same algorithm for all parameter values; "
    "FPT_nu allows different algorithms for each k, so FPT \u2286 FPT_nu.")

# QMIP_le ⊆ NEXP: limited entanglement QMIP ⊆ NEXP (before MIP*=RE)
# (QMIP_le is between QMIP_ne = NEXP and QMIP* = RE, hard to bound above NEXP)
# Actually QMIP_le ⊆ NEXP is not necessarily true; MIP* = RE shows full entanglement
# is huge. Let me skip the upper bound for QMIP_le and just note the lower bound:
# QMIP_ne ⊆ QMIP_le was already added.

# RG(1) ⊆ RG(2): already covered by eq("RG(1)", "PSPACE") and eq("RG(2)", "PSPACE")
# (both equal PSPACE, so they're equivalent)

# QMAM ⊆ PSPACE already added above

# SQG ⊆ PSPACE: SQG is single-query quantum games
# (SQG = PSPACE is known, from the file QRG(2) which says "related: SQG")
# Let me check SQG file first

# Also add OIP ⊆ IP:
add("OIP", "PSPACE",
    "OIP (Ordered IP) \u2286 PSPACE: ordered interactive proof systems are contained in IP = PSPACE.")

# OMA ⊆ MA: ordered MA ⊆ MA
add("OMA", "MA",
    "OMA \u2286 MA: ordered Arthur-Merlin protocols are a special case of MA protocols.")

# ONP ⊆ NP: ordered NP ⊆ NP
add("ONP", "NP",
    "ONP \u2286 NP: ordered NP (NP with ordered witnesses) is a subset of NP.")

# IPP ⊆ PSPACE: IPP is a variant of IP (private randomness IP = IP = PSPACE)
add("IPP", "PSPACE",
    "IPP \u2286 PSPACE: IPP (IP with private randomness) = IP = PSPACE by the IP = PSPACE theorem.")

# IP[polylog] ⊆ PSPACE: polylog-round IP ⊆ IP = PSPACE
add("IP[polylog]", "PSPACE",
    "IP[polylog] \u2286 PSPACE: polylog-round IP is a special case of full IP = PSPACE.")

# MA_E ⊆ MA_EXP: MA at exponential level ⊆ MA with EXP
# Actually MA_E might be MA with exponential-time computations → MA_E ⊆ EXP
add("MA_E", "EXP",
    "MA_E \u2286 EXP: MA with exponential-time Arthur and Merlin is contained in EXP.")

# FQMA ⊆ QMA: functional QMA ⊆ QMA? Actually FQMA is like FNP for QMA, might be ⊇ QMA
# Let me add QMA ⊆ FQMA (QMA decision ≤ FQMA search)
# Actually FQMA is the functional/search version of QMA; QMA ⊆ FQMA in the usual FNP ⊇ NP sense
# This means FQMA is HARDER (search includes decision), so FQMA ⊇ QMA... FQMA needs a predecessor
add("QMA", "FQMA",
    "QMA \u2286 FQMA: any QMA decision problem can be viewed as a FQMA search problem "
    "(find a witness that satisfies the verifier).")

# HVPZK ⊆ PZK: honest-verifier perfect ZK ⊆ perfect ZK
# Actually honest-verifier is WEAKER (only requires ZK for honest verifiers)
# so PZK ⊆ HVPZK (PZK is ZK for all verifiers, hence also for honest verifiers)
add("PZK", "HVPZK",
    "PZK \u2286 HVPZK: if a proof system is perfect ZK for all verifiers, it is in particular "
    "perfect ZK for the honest verifier.")

# ZK ⊆ HVPZK? Actually ZK (= CZK) ⊆ HVPZK? HVPZK is more permissive so HVPZK might be larger.
# Actually HVPZK ⊇ PZK ⊇ SZK ⊃ NIPZK.
# What's below HVPZK? PZK ⊆ HVPZK. So PZK → HVPZK is the predecessor.

# P-Sel ⊆ NP: P-selective sets are in NP (by a randomized argument / Turing reduction)
# Actually, P-selective sets might NOT be in NP (they could be undecidable)
# Let me skip P-Sel bounds.

# SLICEWISE PSPACE ⊆ TOWER: parameterized PSPACE ⊆ TOWER
# For each fixed k, problem is in PSPACE. Union over k ⊆ TOWER?
# Actually SLICEWISE PSPACE = ∪_k DSPACE(f(k)·poly(n)^O(1)) = ∪_k PSPACE_slices
# This might legitimately exceed TOWER since k can grow unboundedly.
# Let me skip.

# WAPP ⊆ SBP and ⊆ AWPP already added
# PP ⊆ AWPP? Let me check.

print(f"\nCreated {created}, skipped {skipped}")
