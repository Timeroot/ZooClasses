---
name: SPP
related:
  - C_eqP
  - FP
  - FewP
  - LWPP
  - Mod_kP
  - NP
  - PP
  - WPP
  - GapP
---
Stoic PP. The class of decision problems solvable by an NP machine such that:
1. If the answer is "no," the number of accepting paths equals the number of rejecting paths.
2. If the answer is "yes," these numbers differ by exactly 1 (or, in the all-paths-equal variant, by 2).

Defined in {ref:ffk94}, where it was shown that SPP is low for PP, C_=P, Mod_kP, and SPP itself (adding SPP as oracle does not increase their power). Independently defined in {ref:oh93} (called XP there).

Contained in {lang:LWPP}, C_=P, and {lang:WPP}. Contains {lang:FewP}; FewP is low for SPP.

Contains the problem of deciding if a graph has any nontrivial automorphisms {ref:kst92}. Contains Graph Isomorphism {ref:ak02}. Contains many problems for solvable black-box groups: solvability, membership, subgroup testing, order, nilpotence, group isomorphism, and intersection {ref:vin04}. The Hidden Subgroup Problem for permutation groups is in FP^SPP {ref:ak02}.
