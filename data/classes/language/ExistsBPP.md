---
name: "∃BPP"
related:
  - BPP
  - MA
  - NP
  - SBP
---
BPP with Existential Operator. The class of problems for which there exists a BPP machine M such that for all inputs x: (1) if the answer is "yes", there exists a y such that M(x,y) accepts; (2) if the answer is "no", for all y, M(x,y) rejects. Alternatively defined as NP^BPP.

Contains NP and BPP, and is contained in {lang:MA} and {lang:SBP}.

∃BPP seems obviously equal to MA, yet {ref:ffk93} constructed an oracle separating them. The key difference: MA requires only that for "yes" instances, there exist a y such that M accepts for at least 2/3 of random strings r (but allows arbitrary acceptance for other y's). ∃BPP requires the acceptance probability to always be either ≤ 1/3 or ≥ 2/3 for every y.
