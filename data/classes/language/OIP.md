---
name: OIP
related:
  - IP
  - P/poly
properties:
  - protocol
---
Oblivious IP. {lang:IP} where only the input size (not the specific input) is known during the interaction with the prover; after the interaction, the verifier gets the actual input.

L ∈ OIP if there is a randomized polynomial-time interrogator I (taking input size) and a polynomial-time verifier V (taking input and witness), such that: for any length-n input in L, I with a suitable prover produces a witness accepted by V; and for inputs not in L, any prover interaction yields a witness rejected by V with probability ≥ 2/3.

OIP = IP ∩ P/poly {ref:gm15}.
