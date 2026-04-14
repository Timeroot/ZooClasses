---
name: coUP
properties:
  - complement
---
Complement of {lang:UP}. A language L is in coUP if and only if its complement L̄ is in UP. Equivalently, there exists a nondeterministic polynomial-time machine such that:
1. If x ∉ L (the "no" case for L), exactly one computation path accepts.
2. If x ∈ L (the "yes" case for L), all computation paths reject.

The name "coUP" reflects this: UP enforces uniqueness of accepting witnesses for "yes" instances; coUP enforces uniqueness of rejecting witnesses (equivalently, accepting witnesses on the complement) for "no" instances.

Contains {lang:coRP} and is contained in {lang:coNP}. Contains P. Known to equal UP relative to a random oracle.

One-way permutations exist (in the worst-case sense) if and only if P ≠ UP ∩ coUP {ref:ht03}.
