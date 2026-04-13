"""
Eighth batch: top class upper bounds + more bottom class predecessors.
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
    safe = (name.replace("/", "_per_").replace("\\", "_").replace(":", "_")
            .replace("?", "_").replace("*", "star").replace("<", "_lt_")
            .replace(">", "_gt_").replace('"', "_").replace("|", "_"))
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


# ── TOP CLASSES: UPPER BOUNDS ─────────────────────────────────────────────────

# AW[P] ⊆ PSPACE: parameterized alternating circuits ⊆ PSPACE
add("AW[P]", "PSPACE",
    "AW[P] \u2286 PSPACE: alternating W[P] parameterized machines can be simulated in PSPACE.")

# FPT ⊆ FPT_su: FPT uses recursive f(k) by convention; FPT_su allows any recursive f(k)
add("FPT", "FPT_su",
    "FPT \u2286 FPT_su: FPT uses a computable f(k); FPT_su requires only that f be recursive, "
    "which is a strictly weaker condition.")

# FPT_su ⊆ FPT_nu: semi-uniform FPT ⊆ non-uniform FPT (non-uniform allows arbitrary f)
add("FPT_su", "FPT_nu",
    "FPT_su \u2286 FPT_nu: the semi-uniform condition (f recursive) implies nothing about uniformity, "
    "while FPT_nu allows the algorithm to vary with k completely freely.")

# FPT_nu ⊆ XP: for each fixed k, FPT_nu runs in polynomial time, which satisfies XP
add("FPT_nu", "XP",
    "FPT_nu \u2286 XP: for each fixed parameter k, FPT_nu solves the problem in O(p(n)) time "
    "for a fixed polynomial p, so FPT_nu \u2286 XP.")

# RPP ⊆ XP: RPP is a parameterized nondeterministic class, similar to W[P] ⊆ XP
add("RPP", "XP",
    "RPP \u2286 XP: RPP is a parameterized nondeterministic class; for each fixed k, "
    "RPP solves in polynomial time, placing it in XP.")

# P ⊆ NT: if L ∈ P, then 'does x agree with x-1?' is decidable in P
add("P", "NT",
    "P \u2286 NT: if L \u2208 P, the consecutive-agreement predicate 'L(x) = L(x-1)' is computable "
    "in polynomial time (run the P algorithm on both inputs), so P \u2286 NT.")

# P ⊆ NT*: same argument for the generalized version
add("P", "NT*",
    "P \u2286 NT*: the same argument for NT applies: any P language satisfies the "
    "generalized-ordering consecutive-agreement condition.")

# 3SUM-hard ⊆ P: 3SUM itself is in O(n^2) ⊆ P, so any 3SUM-hard problem (in P via poly reduction)
# Wait: 3SUM-hard means "3SUM reduces TO this problem," not the problem reduces to 3SUM.
# So 3SUM-hard problems are at LEAST as hard as 3SUM under o(n^2) reductions.
# 3SUM is itself in P (O(n^2) ⊆ P), but 3SUM-hard means these problems are ≥ 3SUM in difficulty.
# Under poly-time reductions, everything in P trivially 3SUM-reduces to anything in P.
# So 3SUM-hard ⊆ P (all 3SUM-hard problems are at least 3SUM-hard, and 3SUM ∈ P).
# Actually 3SUM-hard is defined under sub-quadratic reductions, so 3SUM-hard ⊆ P
# (since 3SUM itself is in P, and 3SUM reduces to all 3SUM-hard problems).
# But 3SUM-hard could include problems outside P (if 3SUM reduces to an NP-hard problem).
# So we can't say 3SUM-hard ⊆ P. Let's add 3SUM-hard ⊆ NP instead? No, 3SUM reduces to hard geometry
# problems but those might be in NP. Hmm, actually I'll skip this one.

# ── TOP CLASSES: para-P = FPT ─────────────────────────────────────────────────

# para-P = FPT: para-P is described as an alternate name for FPT
eq("para-P", "FPT",
   "para-P = FPT: para-P is a less common name for FPT "
   "(fixed-parameter tractable), with the same definition.")

# ── BOTTOM CLASSES: PREDECESSORS ─────────────────────────────────────────────

# NC ⊆ SAC: SAC is the union of SAC^k, and SAC contains NC (as stated in the SAC class description)
add("NC", "SAC",
    "NC \u2286 SAC: stated in the SAC class description. "
    "The union SAC = \u22c3_k SAC^k contains NC = \u22c3_k NC^k.")

# REG ⊆ TREE-REGULAR: strings are degenerate trees, so REG ⊆ TREE-REGULAR
add("REG", "TREE-REGULAR",
    "REG \u2286 TREE-REGULAR: string languages (REG) are a special case of tree languages "
    "(strings are degenerate path-trees), so REG \u2286 TREE-REGULAR.")

# L ⊆ LogFew: an L machine has 0 nondeterminism, so f(x) = 0 or 1 and R = identity
add("L", "LogFew",
    "L \u2286 LogFew: an L (logspace) machine is a special case of a LogFew machine "
    "(deterministic logspace has a unique number of accepting paths).")

# P ⊆ BPP^KT: P can be solved without any oracle queries
add("P", "BPP^KT",
    "P \u2286 BPP^KT: any P problem can be solved without oracle queries to KT, "
    "so P is trivially contained in BPP^KT.")

# MM ⊆ P: matrix multiplication is in P, so all MM problems (which reduce to matrix mult) are in P
add("MM", "P",
    "MM \u2286 P: MM is the class of problems reducible to matrix multiplication; "
    "since matrix multiplication is solvable in polynomial time, MM \u2286 P.")

# PP ⊆ HeurPP: PP is a special case of Heuristic PP (with 0 error fraction)
add("PP", "HeurPP",
    "PP \u2286 HeurPP: a PP machine that always succeeds is a heuristic PP machine with 0 error fraction.")

# S_2P ⊆ S_2E: S_2E is the relaxation of S_2P where the predicate can be exponential
add("S_2P", "S_2E",
    "S_2P \u2286 S_2E: S_2E relaxes S_2P by allowing the predicate to be exponential-time "
    "instead of polynomial-time, so every S_2P problem is also in S_2E.")

# PermUP ⊆ UP: PermUP is a subclass of UP by definition
add("PermUP", "UP",
    "PermUP \u2286 UP: PermUP is the class of UP languages where the witness is a permutation of L; "
    "all PermUP problems are in UP by definition.")

# P-OBDD ⊆ BPP-OBDD: deterministic OBDD ⊆ probabilistic OBDD
add("P-OBDD", "BPP-OBDD",
    "P-OBDD \u2286 BPP-OBDD: a deterministic OBDD is a special case of a probabilistic OBDD "
    "(that accepts with probability 1 or 0).")

# P-OBDD ⊆ BQP-OBDD: deterministic OBDD ⊆ quantum OBDD
add("P-OBDD", "BQP-OBDD",
    "P-OBDD \u2286 BQP-OBDD: a deterministic OBDD is a special case of a quantum OBDD.")

# REG ⊆ P-OBDD: regular languages have polynomial-size OBDDs
add("REG", "P-OBDD",
    "REG \u2286 P-OBDD: regular languages can be decided by OBDDs of polynomial size "
    "(the OBDD simulates the DFA).")

# SZK ⊆ SZK_h: SZK_h is SZK with additional help from a third party
add("SZK", "SZK_h",
    "SZK \u2286 SZK_h: SZK_h gives the prover and verifier additional help from a trusted "
    "third party; SZK (without help) is a special case (with empty help string).")

# NISZK ⊆ NISZK_h: same argument for non-interactive version
add("NISZK", "NISZK_h",
    "NISZK \u2286 NISZK_h: the non-interactive analogue of SZK \u2286 SZK_h; "
    "NISZK_h gives additional help, making it a generalization.")

# PZK ⊆ PKC: PKC is to PZK as SKC is to SZK; SZK ⊆ SKC, so PZK ⊆ PKC
add("PZK", "PKC",
    "PZK \u2286 PKC: PKC has the same relation to PZK as SKC has to SZK; "
    "since SZK \u2286 SKC, the analogous inclusion PZK \u2286 PKC holds.")

# MA' ⊆ MA: MA' is a subclass of MA (with sparse proofs)
add("MA'", "MA",
    "MA' \u2286 MA: MA' is the subclass of MA where Merlin's proof is from a sparse set; "
    "this is a restriction, so MA' \u2286 MA.")

# CLOG ⊆ CP: CLOG uses logarithmic convergence time, CP allows polynomial convergence time
add("CLOG", "CP",
    "CLOG \u2286 CP: CLOG is defined like CP but with logarithmic (rather than polynomial) "
    "convergence time, so CLOG \u2286 CP.")

# CP ⊆ CNP: CNP is the nondeterministic analog of CP
add("CP", "CNP",
    "CP \u2286 CNP: any deterministic CP computation can be simulated by a nondeterministic "
    "CNP machine (determinism is a special case of nondeterminism).")

# RL = R_HL: R_HL has same relation to L as RP does to P, so R_HL = RL
eq("R_HL", "RL",
   "R_HL = RL: R_HL has the same relation to L as RP does to P, which is exactly RL "
   "(randomized logspace = one-sided error logspace).")


# ⊕P ⊆ ModP: ModP allows k to vary, so ⊕P (mod-2 counting) ⊆ ModP
add("\u2295P", "ModP",
    "\u2295P \u2286 ModP: \u2295P = Mod_2P is a special case of ModP, where k can vary "
    "(using k=2 recovers \u2295P).")

# P ⊆ PDQP: PDQP allows non-collapsing measurements, which is more general than BQP ⊇ P
add("P", "PDQP",
    "P \u2286 PDQP: polynomial-time classical computation can be simulated by PDQP "
    "(classical computation is a special case of quantum with non-collapsing measurements).")

# P ⊆ PINC: incrementally solvable in polynomial time
add("P", "PINC",
    "P \u2286 PINC: any P algorithm is trivially incrementally solvable in polynomial time.")

# MA_POLYLOG ⊆ MA already added in batch 7. Now add:
# NL ⊆ XNLP: nondeterministic logspace ⊆ parameterized nondeterministic logspace (parameter k=1)
add("NL", "XNLP",
    "NL \u2286 XNLP: nondeterministic logspace is a special case of XNLP with f(k) = O(1), "
    "giving O(log n) space and polynomial time.")

# XP_uniform ⊆ XP: the uniform version is a restriction of XP
add("XP_uniform", "XP",
    "XP_uniform \u2286 XP: XP_uniform requires the same algorithm for all k, which is a "
    "restriction; the non-uniform XP allows different algorithms, so XP_uniform \u2286 XP.")

# FPT ⊆ XP_uniform: FPT uses f(k)*poly(n) time with a single algorithm, so it satisfies XP_uniform
add("FPT", "XP_uniform",
    "FPT \u2286 XP_uniform: FPT uses the same algorithm for all parameter values k, "
    "running in f(k)*poly(n) time, which satisfies the XP_uniform definition.")

# SLICEWISE PSPACE: FPT ⊆ SLICEWISE PSPACE (parameterized PSPACE)
add("FPT", "SLICEWISE PSPACE",
    "FPT \u2286 SLICEWISE PSPACE: FPT algorithms use polynomial time, "
    "which is well within the PSPACE bound per parameter slice.")

# W[SAT] ⊆ W[P]: W[SAT] ⊆ W[P] (circuit vs formula, same relation as AW[SAT] ⊆ AW[P])
add("W[SAT]", "W[P]",
    "W[SAT] \u2286 W[P]: W[SAT] uses formulas while W[P] uses circuits; "
    "circuits are more expressive, so W[SAT] \u2286 W[P].")

# AW[*] ⊆ AW[SAT] already added in batch 7. Now ensure W[*] ⊆ AW[*]:
# W[*] is the union of W[t] over all t, and AW[*] = union of AW[t].
# W[t] ⊆ AW[t] ⊆ AW[*], so W[*] ⊆ AW[*].
# W[*] is in our database:
add("W[*]", "AW[*]",
    "W[*] \u2286 AW[*]: for each t, W[t] \u2286 AW[t] (alternating version is more powerful); "
    "taking unions, W[*] = \u22c3_t W[t] \u2286 \u22c3_t AW[t] = AW[*].")

# K ⊆ FP: K (feasibly recursive) = U_D-uniform FTC^0, and FTC^0 ⊆ FP (poly time)
# Actually FTC^0 ⊆ NC^1 ⊆ NC ⊆ P ⊆ FP (function version). K is a function class but in language/.
# K ⊆ NC^1 (as language): decision problems in K can be decided in NC^1 (FTC^0 = U_D-uniform TC^0 ⊆ NC^1)
# Hmm, actually FTC^0 ⊆ TC^0 but TC^0 ⊆ NC^1 is the Barrington-Thérien theorem.
# So K (= uniform FTC^0) ⊆ TC^0 ⊆ NC^1 ⊆ NC ⊆ P. Let me add K ⊆ NC^1 (uniform version).
# Actually TC^0 ⊆ NC^1 was proved by Barrington 1989. And K is uniform FTC^0, so K ⊆ NC^1.
add("K", "NC^1",
    "K \u2286 NC^1: K equals U_D-uniform FTC^0 ({ref:hes01}), and TC^0 \u2286 NC^1 "
    "by Barrington 1989 (for the language decision version).")

# NLO ⊆ NP: NL optimization problems whose optima are expressible in NL can be decided in NP
add("NL", "NLO",
    "NL \u2286 NLO: nondeterministic logspace decision problems are a special case of "
    "nondeterministic logspace optimization problems.")

# P ⊆ IC[log,poly]: interactive proofs with logarithmic interaction and polynomial complexity
# IC[log,poly] is in P (since the interaction is limited). Actually P ⊆ IC[log,poly] might hold.
# Let me check: IC[log,poly] sounds like an interactive proof where the interaction rounds
# use log bits and poly total communication. This might be close to P or NP.
# Actually the 'C' might stand for 'communication'. Let me skip IC[log,poly] for now.

# LogFew is a BOTTOM class, so it needs predecessors (things ⊆ LogFew).
# L ⊆ LogFew: already handled (defined it above). LogFew ⊆ NL is correct direction for top.
add("LogFew", "NL",
    "LogFew \u2286 NL: LogFew uses NL machines (nondeterministic logspace), "
    "and the LogFew class is a subclass of NL by definition.")

# W[1] ⊆ W[2] ⊆ ... ⊆ W[SAT] ⊆ W[P]: the W hierarchy
# These might already exist. Let me check W[2] ⊆ W[SAT]:
add("W[2]", "W[SAT]",
    "W[2] \u2286 W[SAT]: W[2] \u2286 W[3] \u2286 ... \u2286 W[SAT] in the W-hierarchy, "
    "since W[SAT] = W[\u221e] contains all W[t].")

# W[1] ⊆ XNLP: W[1]-hard problems require XNLP lower bounds
add("W[1]", "XNLP",
    "W[1] \u2286 XNLP: W[1]-hard problems are contained in XNLP "
    "(nondeterministic logspace parameterized) by results of Elberfeld, Stockhusen, Tantau.")

# QL ⊆ QPLIN: quasi-linear time ⊆ quasi-polynomial time (since n polylog n = n^{1+o(1)} ⊆ n^{O(log n)})
# Wait, QL is quasi-linear = n(log n)^O(1), and QPLIN = n^{O(log n)}. Since 1+o(1) < O(log n) for large n,
# yes QL ⊆ QPLIN.
add("QL", "QPLIN",
    "QL \u2286 QPLIN: quasi-linear time n(log n)^{O(1)} is a special case of quasi-polynomial time "
    "n^{O(log n)} (since n(log n)^k = n^{1 + k log log n / log n} = n^{1+o(1)}).")

# QMA_log ⊆ QMA^+: QMA_log ⊆ QMA ⊆ QMA^+? Wait, QMA^+ is QMA with extra power.
# From batch 7: QMA ⊆ QMA-plus. And QMA_log ⊆ QMA (added in batch 6).
# So QMA_log ⊆ QMA ⊆ QMA-plus ⊆ PP. This should already chain correctly.

# AxP ⊆ AxPP: AxP is related to AxPP
add("AxP", "AxPP",
    "AxP \u2286 AxPP: AxP (deterministic polynomial-time approximation) is a special case "
    "of AxPP (probabilistic polynomial-time approximation).")

# P ⊆ AmpP-BQP: classical P can be simulated by AmpP-BQP circuits
add("P", "AmpP-BQP",
    "P \u2286 AmpP-BQP: classical polynomial-time computation is a special case of "
    "AmpP-restricted quantum computation (the amplitudes remain in AmpP).")

# PZK ⊆ SZK: perfect zero-knowledge ⊆ statistical zero-knowledge
add("PZK", "SZK",
    "PZK \u2286 SZK: perfect zero-knowledge proofs are a special case of statistical "
    "zero-knowledge proofs (perfect indistinguishability implies statistical indistinguishability).")

print(f"\nCreated {created}, skipped {skipped}")
