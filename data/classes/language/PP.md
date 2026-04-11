---
name: PP
related:
  - NP
  - BPP
  - BQP
  - QMA
  - PH
  - P^SharpP
  - PostBQP
  - PQP
  - CH
---
Probabilistic Polynomial-Time. The class of decision problems solvable by an NP machine such that:
1. If the answer is "yes," at least 1/2 of computation paths accept.
2. If the answer is "no," fewer than 1/2 of computation paths accept.

Defined in {ref:gil77}. PP is closed under union and intersection {ref:brs91} (open for 14 years). More generally, P^{PP[log]} = PP; PP is closed under polynomial-time truth-table reductions.

Contains P^{NP[log]} {ref:bhw89} and QMA {ref:mw05}. BPP, BQP, and YQP* are all low for PP {ref:kst89b} {ref:fr98} {ref:yir24}. PH ⊆ P^PP {ref:tod89}.

Equals PostBQP {ref:aar05b}. Equals PQP {ref:wat09}.

For any fixed k, PP contains a language without circuits of size n^k {ref:vin04b}; even without quantum circuits of size n^k with quantum advice {ref:aar06}.
