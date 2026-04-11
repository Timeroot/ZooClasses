---
name: OMA
related:
  - BPP
  - EXP
  - MA
  - NP
  - P/poly
properties:
  - protocol
---
Oblivious MA. The class of problems solvable in randomized polynomial time with a shared, untrusted witness for each input size (the input-oblivious version of {lang:MA}).

L ∈ OMA if there is a randomized polynomial-time verifier V and a polynomial-size witness per input length n, such that: for every input of length n that is in L, V accepts; and for inputs not in L, V rejects with probability ≥ 1/2 for any witness.

NP ⊆ OMA iff NP ⊆ P/poly {ref:fsw09}. EXP ⊆ P/poly iff EXP = OMA {ref:fsw09}. BPP ⊆ OMA {ref:gm15}.

OMA/1 does not have circuits of size n^k for any k > 0 {ref:san07}.
