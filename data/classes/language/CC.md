---
name: CC
related:
  - NC
  - NL
  - P
properties:
  - circuit
---
Comparator Circuits. A comparator gate takes two inputs and outputs the minimum on one wire and the maximum on the other, with fanout-1 restriction on outputs. The Comparator Circuit Value Problem (CCVP) asks, given a circuit of comparator gates, specified inputs, and a specified output, what is the value of that output?

CC is the class of problems log-space many-one reducible to CCVP {ref:ms89}. Known: NL ⊆ CC ⊆ P {ref:ms89}. CC is not known to be in NC nor known to be P-complete.

Natural complete problems include Stable Marriage, Stable Roommate, and Lex-first Maximal Matching {ref:sub94}.
