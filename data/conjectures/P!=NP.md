---
name: "P!=NP"
content: P⊂NP
implies:
  - "P!=PSPACE"
  - "No sparse NP-complete languages"
---
The class of problems solvable in polynomial time is strictly contained within the class of problems solvable in nondeterministic polynomial time. It is logically equivalent to saying that there is an NP-complete problem that cannot be solved in polynomial time, or that *some* NP problem (not necessarily NP-complete.) cannot be solved in polynomial time.

## Notes

One of the Millenium Prize Problems.
The fact that this implies {conj:No sparse NP-complete languages} is known as Mahaney's theorem. The fact that this is implied by {conj:No sparse NP-complete language} is relatively trivial, since there are sparse languages in P, and P=NP implies that all nontrivial languages in P are NP-complete.
Logically equivalent to the statement that P!={lang:PH}: if P=PH, then in particular P=NP since NP sits between P and PH; conversely, if P=NP, then each level of PH is just NP with an oracle to NP, which is just NP again, so PH=NP=P.
