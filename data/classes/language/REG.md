---
name: REG
related:
  - CFL
  - NC^1
  - DSPACE
---
Regular Languages. The class of decision problems solvable by deterministic finite automata (DFAs), equivalently nondeterministic finite automata (NDFAs).

Equals DSPACE(O(1)) {ref:she59}, which equals DSPACE(o(log log n)) {ref:hls65}.

Can recognize "Is the parity of the input odd?" but not "Are the majority of bits in the input 1's?" (finite automata cannot count).

Contained in {lang:NC^1}.
