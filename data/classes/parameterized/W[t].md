---
name: "W[t]"
related:
  - "W[1]"
  - "W[SAT]"
  - "W^*[t]"
  - FPT
  - XP
---
Nondeterministic Fixed-Parameter Hierarchy. The class of decision problems of the form (x, k) (k a parameter), fixed-parameter reducible to:

**Weighted Weft-t Depth-h Circuit-SAT**: Given a Boolean circuit C with a mixture of fanin-2 and unbounded-fanin gates, where the number of unbounded-fanin gates on any path to the root is at most t, and the total depth (fanin-2 and unbounded-fanin) is at most h. Does C have a satisfying assignment of Hamming weight k?

See {lang:W[1]} for the definition of fixed-parameter reducibility. Defined in {ref:df99}.

Contained in {lang:W[SAT]} and in W^*[t]. Generalizes W[1] (t=1) and W[2] (t=2).
