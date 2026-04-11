---
name: AP
related:
  - PSPACE
  - PH
  - AL
---
Alternating P. An alternating Turing machine is a nondeterministic machine with two kinds of states: AND states and OR states. It accepts if and only if the AND-OR tree of all computation paths evaluates to 1 (Accept = 1, Reject = 0).

AP is the class of problems solvable in polynomial time by an alternating Turing machine.

AP = PSPACE {ref:cks81}.

Note: "AP" is also used in the literature for "Approximable in Polynomial Time"; that class is called {lang:AxP} here to avoid ambiguity.
