---
name: ONP
related:
  - E
  - NE
  - NP
  - NP_cap_coNP
  - P
  - P/poly
  - YP
  - O_2P
---
Oblivious NP. The class of problems solvable in polynomial time with a shared, untrusted witness for each input size (the input-oblivious version of NP).

L ∈ ONP if there is a polynomial-time verifier V and a polynomial-size witness per input length n, such that: all inputs of length n in L are accepted (with that witness), and all inputs not in L are rejected for any witness.

Defined in {ref:fsw09}, where it was shown NP has n^k-size circuits for some k iff ONP/1 has n^j-size circuits for some j.

ONP ⊆ P/poly and ONP ⊆ NP {ref:fsw09}. ONP = NP iff NP ⊆ P/poly {ref:fsw09}. If NE ≠ E then ONP ≠ P {ref:gm15}.
