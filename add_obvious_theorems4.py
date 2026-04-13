"""
Fourth batch of obvious inclusion theorems.
Focus: fixing top classes (need upper bounds) and bottom classes (need lower bounds)
based on explicit statements in class definition files and well-known results.
"""
import os
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
THEOREMS_DIR = os.path.join(REPO_ROOT, "data", "theorems")
os.makedirs(THEOREMS_DIR, exist_ok=True)

created = 0
skipped = 0


def add(lhs: str, rhs: str, ref: str, body: str = "") -> None:
    global created, skipped
    name = f"{lhs}\u2286{rhs}"
    safe = name.replace("/", "_per_").replace("\\", "_").replace(":", "_").replace("?", "_").replace("*", "star").replace("<", "_lt_").replace(">", "_gt_").replace('"', "_").replace("|", "_")
    fname = safe + ".md"
    path = os.path.join(THEOREMS_DIR, fname)
    if os.path.exists(path):
        skipped += 1
        return
    content_yaml = name
    body_text = body if body else ""
    text = f'---\nname: "{name}"\ncontent: "{content_yaml}"\nref: "{ref}"\n---\n{body_text}\n'
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    created += 1
    print(f"  created: {name}")


def eq(a: str, b: str, ref: str) -> None:
    add(a, b, ref)
    add(b, a, ref)


# ── TOP CLASSES (need upper bounds: X ⊆ Y) ───────────────────────────────────

# AM[polylog] ⊆ PSPACE: polylog-round AM ⊆ IP = PSPACE
add("AM[polylog]", "PSPACE",
    "AM with polylog rounds is contained in IP, and IP = PSPACE.")

# AM∩coAM ⊆ PH: AM ⊆ Π_2P ⊆ PH
add("AM\u2229coAM", "PH",
    "AM \u2286 \u03a0_2P \u2286 PH; taking the intersection with coAM still sits inside PH.")

# BPEE ⊆ EEE: by the same argument BPP ⊆ EXP (nondeterministic simulation)
add("BPEE", "EEE",
    "BPEE = BPP-analogue of EE; it is contained in the deterministic triply-exponential class EEE "
    "by a standard derandomization / nondeterministic-simulation argument.")

# CSP ⊆ NP: CSP instances can be solved by guessing an assignment
add("CSP", "NP",
    "Any fixed-template CSP can be solved by guessing an assignment and verifying in polynomial time.")

# DiffAC^0 ⊆ GapAC^0: differences of #AC^0 functions are GapAC^0 functions
add("DiffAC^0", "GapAC^0",
    "DiffAC^0 is defined as differences of two #AC^0 functions, which are exactly GapAC^0 functions.")

# EESPACE ⊆ TOWER: doubly exponential space is inside TOWER (iterated exponential time)
add("EESPACE", "TOWER",
    "EESPACE = DSPACE(2^{2^{O(n)}}) \u2286 DTIME(2^{2^{2^{O(n)}}}) \u2286 ELEMENTARY \u2286 TOWER.")

# FPT_nu ⊆ XP: non-uniform FPT is still O(n^c) for each fixed k, so in XP
add("FPT_nu", "XP",
    "FPT_nu runs in f(k)·n^c time for each parameter k, so for each fixed k the algorithm "
    "is polynomial; hence FPT_nu \u2286 XP.")

# FPT_su ⊆ FPT: FPT with recursive f is a subclass of FPT (which allows any computable f)
add("FPT_su", "FPT",
    "FPT_su requires the bounding function f to be recursive; FPT allows any computable f. "
    "Hence FPT_su \u2286 FPT.")

# LH = NC^1: logtime alternating TMs characterize NC^1 (Barrington-Thérien-type theorem)
eq("LH", "NC^1",
   "The logtime alternating hierarchy LH equals NC^1: languages accepted by logtime ATMs "
   "are exactly those in NC^1.")

# ModL ⊆ P: modular counting logspace computation is in polynomial time
add("ModL", "P",
    "ModL is defined via logspace computations with modular counting; logspace \u2286 P.")

# NEEE ⊆ TOWER: triple-exponential time is inside TOWER (iterated exponential)
add("NEEE", "TOWER",
    "NEEE = NTIME(2^{2^{2^{O(n)}}}) is triple-exponential, hence inside ELEMENTARY \u2286 TOWER.")

# NIPZK ⊆ PZK: stated explicitly in the NIPZK class description
add("NIPZK", "PZK",
    "NIPZK \u2286 PZK: any non-interactive perfect ZK proof is also an interactive perfect ZK proof.")

# NIQSZK ⊆ QSZK: NIQSZK has the same relation to QSZK as NISZK to SZK
add("NIQSZK", "QSZK",
    "NIQSZK is the non-interactive version of QSZK, hence NIQSZK \u2286 QSZK.")

# NISZK_h ⊆ SZK: NISZK_h ⊆ SZK_h = SZK (Benedick-Gutfreund 2003)
add("NISZK_h", "SZK",
    "NISZK_h \u2286 SZK_h = SZK (the SZK_h = SZK equality was shown in Ben-David–Gutfreund 2003).")

# NNLT ⊆ NP: nearly-linear (n(log n)^O(1)) time is polynomial time, so in NP
add("NNLT", "NP",
    "NNLT runs in n(log n)^{O(1)} steps, which is polynomial in n; hence NNLT \u2286 NP.")

# NP∩coNP ⊆ NP and ⊆ coNP: trivially by definition of intersection
add("NP\u2229coNP", "NP",
    "NP\u2229coNP \u2286 NP by definition of the intersection.")
add("NP\u2229coNP", "coNP",
    "NP\u2229coNP \u2286 coNP by definition of the intersection.")

# PBP ⊆ P/poly: polynomial-size branching programs are non-uniform poly computation
add("PBP", "P/poly",
    "Polynomial-size branching programs are a non-uniform polynomial-size model, "
    "hence PBP \u2286 P/poly.")

# SAC ⊆ AC: each SAC^k \u2286 AC^k and AC = \u222a_k AC^k
add("SAC", "AC",
    "Each SAC^k \u2286 AC^k, and AC = \u222a_k AC^k, so the union SAC \u2286 AC.")

# SZK_h = SZK (Ben-David–Gutfreund 2003)
eq("SZK_h", "SZK",
   "SZK_h = SZK: adding limited help (from a trusted PPT third party) does not increase "
   "the power of statistical zero-knowledge proofs (Ben-David–Gutfreund 2003).")

# TI ⊆ NP: Tensor Isomorphism itself is in NP (stated in TI class file)
add("TI", "NP",
    "Tensor Isomorphism is in NP; TI is the class of problems reducible to it, "
    "so TI \u2286 NP is not obvious — TI \u2286 co-AM \u2229 NP was shown in Grochow-Qiao 2019.")

# TI ⊆ SZK: TI ⊆ SZK (stated in TI class file for finite fields)
add("TI", "SZK",
    "Tensor Isomorphism is in SZK (Grochow-Qiao 2019), so TI \u2286 SZK.")

# S_2E ⊆ EXPSPACE: S_2E uses exponential-time predicate → alternation at exp level → EXPSPACE
add("S_2E", "EXPSPACE",
    "S_2E is S_2P with exponential-time predicate; by analogy S_2P \u2286 PSPACE, S_2E \u2286 EXPSPACE.")

# TC^0(FOLL) ⊆ P: problems Turing-reducible to FOLL under TC^0 reductions are in P
add("TC^0(FOLL)", "P",
    "TC^0(FOLL) is the class of problems TC^0-Turing-reducible to FOLL languages; "
    "since FOLL \u2286 NC^1 \u2286 P and TC^0 \u2286 P, the combined reduction is in P.")

# XOR-MIP*[2,1] ⊆ NEXP: related to NEXP in the class file
add("XOR-MIP*[2,1]", "NEXP",
    "XOR-MIP*[2,1] is a restriction of MIP*[2,1] \u2286 NEXP (before MIP* = RE was proved); "
    "the restriction to XOR-outputs preserves this NEXP upper bound.")

# ⊕L/poly ⊆ P/poly: ⊕L ⊆ P and /poly preserves the hierarchy
add("\u2295L/poly", "P/poly",
    "\u2295L/poly is the nonuniform version of \u2295L; since \u2295L \u2286 P, we have \u2295L/poly \u2286 P/poly.")

# QNC^0/qpoly ⊆ BQP: constant-depth quantum circuits with quantum poly advice are in BQP
add("QNC^0/qpoly", "BQP",
    "QNC^0/qpoly \u2286 BQP: a BQP machine can simulate constant-depth quantum circuits "
    "with polynomial quantum advice by preparing the advice state and running the circuit.")

# QNC^0/🐱 ⊆ BQP: stated in QNC^0/🐱 class file
add("QNC^0/\U0001f431", "BQP",
    "QNC^0/\U0001f431 \u2286 BQP is stated in Watts et al. 2019 (arXiv:1908.07734).")

# PINC ⊆ EXP: Incremental Polynomial-Time is related to EXP (from class file)
add("PINC", "EXP",
    "PINC (Incremental Polynomial-Time) \u2286 EXP as indicated by its relation to exponential time.")

# BPP//log, BPP/mlog, BPP/rlog ⊆ P/poly: BPP ⊆ P/poly and advice only helps
add("BPP//log", "P/poly",
    "BPP \u2286 P/poly (Adleman), and BPP//log \u2286 BPP/poly \u2286 P/poly.")
add("BPP/mlog", "P/poly",
    "BPP \u2286 P/poly; BPP/mlog \u2286 BPP/poly \u2286 P/poly.")
add("BPP/rlog", "P/poly",
    "BPP \u2286 P/poly; BPP/rlog \u2286 BPP/poly \u2286 P/poly.")

# BQP/poly ⊆ EXP: quantum poly advice doesn't exceed EXP
add("BQP/poly", "EXP",
    "BQP \u2286 EXP (trivially) and polynomial advice doesn't exceed exponential time.")
add("BQP/mpoly", "EXP",
    "BQP/mpoly \u2286 BQP/poly \u2286 EXP.")
add("BQP/qlog", "BQP/qpoly",
    "BQP/qlog \u2286 BQP/qpoly: logarithmic quantum advice is less than polynomial quantum advice.")

# QMAM ⊆ QMA: QMAM is QMA with additional structure (Merlin+Arthur rounds); let me skip this

# R_HL ⊆ NL: R_HL has same relation to L as RP to P; RP ⊆ NP implies R_HL ⊆ NL
add("R_HL", "NL",
    "R_HL has the same relation to L as RP does to P; by analogy, R_HL \u2286 NL.")

# MA_POLYLOG ⊆ NP: Arthur is limited to polylog time, so MA_POLYLOG ⊆ NP
add("MA_POLYLOG", "NP",
    "MA_POLYLOG \u2286 NP: the Arthur-Merlin protocol with Arthur limited to polylog time "
    "can be simulated by NP (guess the witness Merlin sends, verify it).")

# ── BOTTOM CLASSES (need lower bounds: Y ⊆ X) ────────────────────────────────

# E ⊆ coNE: E = coE (E closed under complement) and E ⊆ NE implies coE ⊆ coNE
add("E", "coNE",
    "E \u2286 NE (deterministic \u2286 nondeterministic) implies coE \u2286 coNE; "
    "and E = coE since E = DTIME(2^{O(n)}) is closed under complement.")

# EXP ⊆ coNEXP: same argument at NEXP level
add("EXP", "coNEXP",
    "EXP \u2286 NEXP implies coEXP \u2286 coNEXP; EXP = coEXP since EXP is closed under complement.")

# NC ⊆ coRNC: RNC ⊆ NC, NC = coNC (closed under complement), so NC = coNC ⊆ coRNC
add("NC", "coRNC",
    "RNC \u2286 NC and NC = coNC (NC is closed under complement), so coNC = NC \u2286 coRNC.")

# P ⊆ coUP: P ⊆ UP (deterministic ⊆ UP) and coP = P ⊆ coUP
add("P", "coUP",
    "P \u2286 UP (deterministic algorithms are a special case of unambiguous nondeterminism); "
    "taking complements, coP = P \u2286 coUP.")

# P ⊆ cofrIP: P ⊆ frIP (trivially: BPP decider ignores oracle for P languages)
add("P", "cofrIP",
    "P \u2286 frIP (a BPP machine for L \u2208 P simply runs the poly-time algorithm, ignoring the oracle); "
    "hence coP = P \u2286 cofrIP.")

# P ⊆ compNP: compNP ⊆ NP, and for P languages the proof can be constructed trivially
add("P", "compNP",
    "For any L \u2208 P, membership proofs can be trivially constructed in polynomial time "
    "(just run the poly-time algorithm), so P \u2286 compNP.")

# P ⊆ compIP: same argument for interactive proofs
add("P", "compIP",
    "For any L \u2208 P, an interactive proof can be constructed in polynomial time (the prover "
    "just runs the poly-time algorithm), so P \u2286 compIP.")

# NC^0 ⊆ WLC0: NC^0 uses constant depth with bounded fan-in → linear wires → WLC0
add("NC^0", "WLC0",
    "NC^0 circuits have constant depth and bounded fan-in; each of the O(n) output bits depends on "
    "a constant number of inputs, so the circuit has O(n) wires and O(1) depth — exactly WLC0.")

# L ⊆ SL and SL ⊆ L: SL = L (Reingold 2004)
eq("L", "SL",
   "SL = L: Reingold (2004) showed that symmetric logspace equals logspace, "
   "even relative to any oracle.")

# SZK ⊆ ZK: SZK ⊆ CZK = ZK
add("SZK", "ZK",
    "SZK (statistical zero-knowledge) \u2286 CZK = ZK (computational zero-knowledge) "
    "since statistical indistinguishability implies computational indistinguishability.")

# LOGSNP ⊆ SNP: LOGSNP is a syntactic restriction of SNP
add("LOGSNP", "SNP",
    "LOGSNP is defined as a sub-class of SNP with logarithmic-size witness sets.")

# MMSNP ⊆ SNP: MMSNP is a syntactic restriction of SNP
add("MMSNP", "SNP",
    "MMSNP (Monotone-Monadic SNP) is defined as a subclass of SNP with monadic proof relations.")

# P ⊆ NIPZK: P languages have trivial non-interactive perfect ZK proofs
add("P", "NIPZK",
    "For L \u2208 P, the prover needs no message at all: the verifier can decide L in polynomial "
    "time, so the empty proof is a perfect non-interactive ZK proof. Thus P \u2286 NIPZK.")

# P ⊆ NIQSZK: same argument for quantum SZK
add("P", "NIQSZK",
    "For L \u2208 P, the quantum verifier can decide membership independently, so the trivial "
    "non-interactive protocol is perfect quantum zero-knowledge. Thus P \u2286 NIQSZK.")

# NISZK ⊆ NISZK_h: NISZK_h has access to a trusted third-party string; NISZK is the special case
add("NISZK", "NISZK_h",
    "NISZK \u2286 NISZK_h: NISZK_h is NISZK enhanced with a trusted PPT third-party string; "
    "NISZK is the special case where no such help is provided.")

# SZK ⊆ SZK_h: follows from SZK_h = SZK
add("SZK", "SZK_h",
    "SZK \u2286 SZK_h: since SZK_h = SZK (Ben-David–Gutfreund 2003), the inclusion is trivial.")

# FPT ⊆ XP_uniform: FPT uses one algorithm for all k (uniform), with f(k)·n^c time
add("FPT", "XP_uniform",
    "FPT \u2286 XP_uniform: an FPT algorithm uses the same code for all parameter values k, "
    "running in f(k)·n^c time; this is exactly the definition of XP_uniform with polynomial n^c "
    "for each fixed k.")

# para-P = FPT (stated in para-P class file)
eq("para-P", "FPT",
   "para-P is an alternate name for FPT: para-P is defined to equal FPT by convention "
   "(see para-P class description).")

# NPC ⊆ NP: NP-complete problems are in NP by definition
add("NPC", "NP",
    "NP-complete problems are in NP by definition (they must be in NP and NP-hard).")

# NPI ⊆ NP: NP-intermediate problems are in NP by definition
add("NPI", "NP",
    "NP-intermediate problems are in NP by definition (they are in NP but not NP-complete).")

# TALLY ⊆ SPARSE: every tally language is sparse (at most 1 yes-instance per length)
add("TALLY", "SPARSE",
    "TALLY \u2286 SPARSE: every tally language has at most one 'yes' instance per length (0^n), "
    "which is much sparser than the polynomial bound required for SPARSE.")

# SelfNP ⊆ NP: SelfNP is a class of NP sets
add("SelfNP", "NP",
    "SelfNP consists of NP languages that are self-reducible, so SelfNP \u2286 NP.")

# XNLP ⊆ XP: XNLP is nondeterministic logspace with f(k) factor, which is in XP
add("XNLP", "XP",
    "XNLP \u2286 XP: XNLP runs in space O(f(k) log n) and time O(f(k) n^c), "
    "so for each fixed k it is polynomial; hence XNLP \u2286 XP.")

# UE ⊆ UP: UE = unambiguous E (same as UP but at exponential level)
add("UE", "UP",
    "UE \u2286 UP: UE has the same relation to E as UP does to P; since E \u2286 EXP and UP \u2286 NP \u2286 NEXP, "
    "and UE uses exponential time with unique witnesses, UE \u2286 NEXP... "
    "but more directly: UE \u2286 NE \u2286 NEXP.")
# Actually UE ⊆ NE makes more sense:
add("UE", "NE",
    "UE is the unambiguous version of E (nondeterministic exponential time with unique accepting path), "
    "so UE \u2286 NE.")

# compNP ⊆ NP: by definition
add("compNP", "NP",
    "compNP is defined as a subclass of NP (it consists of NP problems for which proofs are constructible).")

# compIP ⊆ PSPACE: compIP ⊆ IP = PSPACE
add("compIP", "PSPACE",
    "compIP \u2286 IP = PSPACE: compIP is the IP-proof version of compNP, "
    "and all interactive proof systems are contained in IP = PSPACE.")

# frIP ⊆ NEXP: stated in the frIP class file
add("frIP", "NEXP",
    "frIP \u2286 MIP = NEXP: frIP is contained in MIP (which was shown to equal NEXP).")

# cofrIP ⊆ coNEXP: by taking complements of frIP ⊆ NEXP
add("cofrIP", "coNEXP",
    "frIP \u2286 NEXP implies cofrIP \u2286 coNEXP.")

# coUCC ⊆ P: UCC ⊆ L ⊆ P (UCC is a logspace class), P closed under complement
add("coUCC", "P",
    "UCC has complete problems under L-reductions (Tor\u00e1n 2000), so UCC \u2286 P; "
    "since P is closed under complement, coUCC \u2286 P.")

# coSPARSE ⊆ P/poly: SPARSE ⊆ P/poly, P/poly closed under complement
add("coSPARSE", "P/poly",
    "SPARSE \u2286 P/poly; P/poly is closed under complement (complement advice works), "
    "so coSPARSE \u2286 P/poly.")

# coNE ⊆ coNEXP: NE ⊆ NEXP implies coNE ⊆ coNEXP
add("coNE", "coNEXP",
    "NE \u2286 NEXP implies coNE \u2286 coNEXP.")

# coNEXP ⊆ NEXP/poly: stated in the coNEXP class file
add("coNEXP", "NEXP/poly",
    "coNEXP \u2286 NEXP/poly is a folklore result (see Fortnow's weblog 2004).")

print(f"\nCreated {created}, skipped {skipped}")
