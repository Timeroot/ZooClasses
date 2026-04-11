---
name: SBP
related:
  - AM
  - MA
  - WAPP
  - ExistsBPP
  - A_0PP
  - BPPpath
---
Small Bounded-Error Probability. The class of decision problems for which the following holds: there exists a #P function f and an FP function g such that, for all inputs x:
1. If the answer is "yes," f(x) > g(x).
2. If the answer is "no," f(x) < g(x)/2.

Defined in {ref:bgm02}, where it was also shown that:
- SBP contains {lang:MA}, WAPP, and {lang:ExistsBPP}.
- SBP is contained in {lang:AM} and BPP_path.
- SBP is closed under union.
- There exists an oracle relative to which SBP ⊄ Σ_2P.

There exists an oracle relative to which SBP is not closed under intersection {ref:glm15}.

If SAT can be solved by an NP-machine with a subexponential number of accepting paths, then SBP = AM {ref:vol20}.
