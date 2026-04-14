---
name: coMod_kP
properties:
  - complement
concrete: false
---
Complement of {lang:Mod_kP}, parameterized by an integer k > 1. A language L is in coMod_kP if and only if its complement L̄ is in Mod_kP.

Equivalently, L ∈ coMod_kP if there is a nondeterministic polynomial-time machine such that the number of accepting paths is divisible by k if and only if the answer is "yes." (For Mod_kP the divisibility-by-k condition signals "no"; for coMod_kP it signals "yes.")
