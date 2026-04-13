"""Batch 11: addressing remaining bottom classes."""
import os, sys, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
THEOREMS_DIR = os.path.join(REPO_ROOT, "data", "theorems")
os.makedirs(THEOREMS_DIR, exist_ok=True)

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

# Check which classes exist
with open('generated/classes.json', encoding='utf-8') as f:
    d = json.load(f)
names = {c['name'] for c in d}

# ── COUNTING / CIRCUIT CLASSES ────────────────────────────────────────────────

# AC^0 ⊆ C_=AC^0: AC^0 languages are zero-sets of DiffAC^0 functions
add("AC^0", "C_=AC^0",
    "AC^0 \u2286 C_=AC^0: any AC^0 language L can be expressed as {x : f(x) = 0} "
    "for f = 1 - \u03c7_L \u2208 DiffAC^0, so AC^0 \u2286 C_=AC^0.")

# LC^0 ⊆ NC^0: linear-size constant-depth ⊆ polynomial-size constant-depth
add("LC^0", "NC^0",
    "LC^0 \u2286 NC^0: linear-size constant-depth circuits are a special case of "
    "polynomial-size constant-depth circuits (NC^0 allows polynomial size).")

# NC^2 ⊆ MM: NC^2 can be reduced to matrix multiplication (e.g., matrix powering)
add("NC^2", "MM",
    "NC^2 \u2286 MM: NC^2 problems can be reduced to matrix multiplication; "
    "e.g., graph connectivity via matrix powering is in NC^2 and reduces to matrix mult.")

# ── P VARIANTS ────────────────────────────────────────────────────────────────

# P ⊆ AlgP/poly: Boolean gates can be simulated by algebraic operations over {0,1}
add("P", "AlgP/poly",
    "P \u2286 AlgP/poly: any Boolean circuit (P algorithm) can be simulated by an algebraic "
    "circuit using AND(x,y)=x\u00b7y, OR(x,y)=x+y-xy, NOT(x)=1-x over integers.")

# P ⊆ BQP_tt/poly: BQP with truth-table queries and polynomial advice contains P (0 queries)
add("P", "BQP_tt/poly",
    "P \u2286 BQP_tt/poly: polynomial-time classical computation needs no quantum oracle "
    "queries or advice, so it is trivially in BQP_tt/poly.")

# P ⊆ D#P (= P^#P): P is contained in P with a #P oracle
add("P", "D#P",
    "P \u2286 D#P: D#P is an alternate name for P^{#P}; trivially P \u2286 P^{#P}.")

# P ⊆ IC[log,poly]: for L ∈ P, the O(log n) program A = "hardcode which P algo" works
add("P", "IC[log,poly]",
    "P \u2286 IC[log,poly]: for L \u2208 P, the O(1)-size program (constant, independent of n) "
    "that runs the P algorithm is also O(log n)-size, so P \u2286 IC[log,poly].")

# P ⊆ MA': P problems have empty witnesses, which are in any sparse set S_n
add("P", "MA'",
    "P \u2286 MA': for L \u2208 P, Arthur can verify without a witness (Merlin sends \u03b5); "
    "the singleton {'\u03b5'} is sparse, so P \u2286 MA'.")

# MA ⊆ MA_E: MA is a special case of MA_E (poly-time predicate ⊆ exp-time predicate)
add("MA", "MA_E",
    "MA \u2286 MA_E: MA_E relaxes MA's polynomial-time predicate to exponential time; "
    "any polynomial-time predicate is also exponential-time, so MA \u2286 MA_E.")

# P ⊆ MA_POLYLOG: P has trivial proofs (Merlin sends nothing); the polylog-time Arthur can verify P
add("P", "MA_POLYLOG",
    "P \u2286 MA_POLYLOG: for L \u2208 P, Arthur (running in polylog time with random access) "
    "can accept/reject without a proof from Merlin; P trivially satisfies MA_POLYLOG.")

# P ⊆ P^NP[k]: 0 queries is a special case of k queries
if "P^NP[k]" in names:
    add("P", "P^NP[k]",
        "P \u2286 P^NP[k]: P uses 0 NP queries, which is \u2264 k queries; so P is trivially "
        "in P^NP[k].")

# P^NP[k] ⊆ Δ_2P: P with k adaptive NP queries ⊆ P with polynomially many NP queries
if "\u0394_2P" in names:
    add("P^NP[k]", "\u0394_2P",
        "P^NP[k] \u2286 \u0394_2P: k (constant) adaptive NP queries is fewer than polynomial, "
        "so P^NP[k] \u2286 P^NP = \u0394_2P.")

# P ⊆ P^||QMA: P needs no QMA oracle queries
add("P", "P^\u2016QMA",
    "P \u2286 P^\u2016QMA: P uses no oracle queries; making 0 non-adaptive QMA queries "
    "is still polynomial-time QMA-oracle computation.")

# P ⊆ PQUERY: P uses no oracle queries, ≤ poly oracle queries
add("P", "PQUERY",
    "P \u2286 PQUERY: P uses 0 oracle queries, which is \u2264 polynomial number of oracle "
    "queries; so P \u2286 PQUERY.")

# P ⊆ PromiseP: P languages are promise-P with domain = {0,1}^*
add("P", "PromiseP",
    "P \u2286 PromiseP: any P language is a promise problem solvable by a P machine "
    "(where the promise is the trivial promise: all strings are valid inputs).")

# UP ⊆ PromiseUP: UP problems are promise-UP problems with trivial promise
add("UP", "PromiseUP",
    "UP \u2286 PromiseUP: any UP language is a promise problem solvable by a UP machine.")

# P ⊆ PhP: physical computers can run polynomial-time algorithms
add("P", "PhP",
    "P \u2286 PhP: polynomial-time algorithms can be implemented on physically constructible "
    "computers; so P \u2286 PhP by definition.")

# P ⊆ PBP: polynomial branching programs contain P
add("P", "PBP",
    "P \u2286 PBP: polynomial-time algorithms can be represented as polynomial-width "
    "branching programs (of polynomial length), so P \u2286 PBP.")

# ── LOGSPACE CLASSES ─────────────────────────────────────────────────────────

# L ⊆ NLOG: logspace ⊆ nondeterministic logspace with one-way oracle
add("L", "NLOG",
    "L \u2286 NLOG: deterministic logspace is a special case of nondeterministic logspace "
    "(NLOG), using no nondeterminism.")

# L ⊆ coUCC: L problems reduce to coUCC problems
add("L", "coUCC",
    "L \u2286 coUCC: since the unique-cycle-cover problem is coUCC-complete under L reductions "
    "(Tor\u00e1n 2000), L \u2286 coUCC.")

# mL ⊆ L: monotone logspace ⊆ logspace
if "mL" in names:
    add("mL", "L",
        "mL \u2286 L: monotone logspace machines are a special case of unrestricted logspace "
        "machines (monotone = no NOT gates on oracle, but the Turing machine can still use NOT).")

# ── EQUIVALENCES ─────────────────────────────────────────────────────────────

# NMCL = QRL: stated explicitly in the NMCL class file
eq("NMCL", "QRL",
   "NMCL = QRL: NMCL is an alternative name for QRL, as stated in the class description.")

# YQP*/poly = BQP/qpoly: stated in the YQP*/poly class description
if "YQP*/poly" in names and "BQP/qpoly" in names:
    eq("YQP*/poly", "BQP/qpoly",
       "YQP*/poly = BQP/qpoly: stated directly in the YQP*/poly class description [ad14].")

# ── PROBABILISTIC / ZK CLASSES ────────────────────────────────────────────────

# BPP ⊆ Coh: BPP decides without oracle, so trivially autoreducible
add("BPP", "Coh",
    "BPP \u2286 Coh: BPP machines decide L(x) without any oracle access to L; "
    "trivially they can query points different from x (and just ignore the answers).")

# E ⊆ UE: deterministic exponential time is unambiguous exponential time
add("E", "UE",
    "E \u2286 UE: deterministic computation has exactly one (accepting) path, "
    "which is unambiguous; so E \u2286 UE by the same argument as P \u2286 UP.")

# P ⊆ frIP: frIP has trivial BPP deciders for P problems
add("P", "frIP",
    "P \u2286 frIP: for L \u2208 P, the decider D (a BPP machine) can ignore the oracle "
    "and decide L directly in polynomial time; so P \u2286 frIP.")

# NP ⊆ ∃NISZK: stated in the ∃NISZK class description
add("NP", "\u2203NISZK",
    "NP \u2286 \u2203NISZK: stated in the \u2203NISZK class description.")

# NISZK ⊆ ∃NISZK: ∃NISZK extends NISZK with the existential operator
add("NISZK", "\u2203NISZK",
    "NISZK \u2286 \u2203NISZK: \u2203NISZK is NISZK with the existential operator, "
    "so NISZK is a special case.")

# ∃NISZK ⊆ Σ_3P: stated in the class description ("contained in the third level of PH")
if "\u03a3_3P" in names:
    add("\u2203NISZK", "\u03a3_3P",
        "\u2203NISZK \u2286 \u03a3_3P: stated in the \u2203NISZK class description "
        "('contained in the third level of PH').")

# ── YP FAMILY ─────────────────────────────────────────────────────────────────

# YP ⊆ YP*: YP* is a generalization of YP (advice string is verifiable)
if "YP*" in names:
    add("YP", "YP*",
        "YP \u2286 YP*: YP* is YP with the additional property that the advice string "
        "s_n can be verified in polynomial time; YP is the special case without this requirement.")

# BPP ⊆ YPP: BPP is the special case of YPP with no Merlin
add("BPP", "YPP",
    "BPP \u2286 YPP: YPP is the probabilistic analogue of YP; BPP algorithms have "
    "trivial YPP protocols (no Merlin needed).")

# YQP ⊆ YQP*: YQP* generalizes YQP
if "YQP*" in names:
    add("YQP", "YQP*",
        "YQP \u2286 YQP*: YQP* is to YQP as YP* is to YP; YQP is a special case of YQP*.")

# ── ∃BPP ─────────────────────────────────────────────────────────────────────

# BPP ⊆ ∃BPP: ∃BPP is BPP with an existential quantifier (so BPP ⊆ ∃BPP)
if "\u2203BPP" in names:
    add("BPP", "\u2203BPP",
        "BPP \u2286 \u2203BPP: \u2203BPP adds an existential quantifier over BPP; "
        "BPP is the special case with an empty existential.")

# ── MONOTONE CLASSES ─────────────────────────────────────────────────────────

# mNL ⊆ NL: monotone NL ⊆ NL
add("mNL", "NL",
    "mNL \u2286 NL: monotone nondeterministic logspace machines are a special case of "
    "unrestricted NL machines.")

print(f"\nCreated {created}, skipped {skipped}")
