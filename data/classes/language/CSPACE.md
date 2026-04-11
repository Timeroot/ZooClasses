---
name: CSPACE
related:
  - CL
concrete: false
---
Catalytic Space. CSPACE(s, c) is the class of problems solvable by a catalytic Turing machine with work space s and catalytic space c. A catalytic Turing machine has an extra catalytic tape of size c, which must be returned to its initial configuration at the end of every computation path (regardless of the input).

Defined in {ref:bckls14}. In most works c is exponential in s, since that is the largest amount of catalytic space addressable by the worktape. The main studied variant is {lang:CL} = CSPACE(O(log n), n^{O(1)}).
