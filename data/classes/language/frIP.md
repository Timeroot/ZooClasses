---
name: frIP
related:
  - BPEE
  - BPP
  - Coh
  - MIP
  - NEE
  - NEXP
  - NP
  - compIP
  - Check
properties:
  - protocol
---
Function-Restricted IP Proof Systems. The class of problems L that have a decider: there exists a BPP machine D such that for all inputs x, (1) if the answer is "yes" then D^L(x) (D with oracle for L) accepts with probability ≥ 2/3, and (2) if the answer is "no" then D^A(x) accepts with probability ≤ 1/3 for all oracles A.

Contains {lang:compIP} {ref:bg94} and {lang:Check} {ref:bk89}. Contained in MIP = NEXP {ref:frs88}. Assuming NEE ⊄ BPEE, NP ∩ Coh is not contained in frIP {ref:bg94}.
