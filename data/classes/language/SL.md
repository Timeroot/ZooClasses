---
name: SL
related:
  - DSPACE
  - L
  - Mod_kL
  - NL
  - coSL
---
Symmetric Logarithmic-Space. The class of problems solvable by a nondeterministic Turing machine in logarithmic space, such that:
1. If the answer is "yes," one or more computation paths accept.
2. If the answer is "no," all paths reject.
3. If the machine can make a nondeterministic transition from configuration A to configuration B, then it can also transition from B to A. (This is what "symmetric" means.)

Defined in {ref:lp82}.

The undirected s-t connectivity problem (USTCON: is there a path from vertex s to vertex t in an undirected graph?) is complete for SL under L-reductions.

SL contains {lang:L} and is contained in {lang:NL}. Contained in L/poly {ref:akl79}. Contained in ⊕L and Mod_kL for every prime k {ref:kw93}. Contained in DSPACE(log^{3/2} n) {ref:nsw92} and DSPACE(log^{4/3} n) {ref:atw00}.

SL = coSL, and SL^SL = SL (the symmetric logspace hierarchy collapses) {ref:nt95}.

Reingold ultimately showed SL = L {ref:rei04}, even relative to an oracle.
