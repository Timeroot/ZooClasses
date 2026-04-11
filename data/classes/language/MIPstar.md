---
name: "MIP*"
related:
  - MIP
  - MIPco
  - RE
properties:
  - protocol
  - quantum
---
Multiple-player Interactive Proofs, with entanglement. Traditionally defined with polynomially many players and rounds, but it turns out that MIP*[poly,poly]=MIP*[2,1], so one can just think of as two players and one round. 
 When the provers are allowed to have (unbounded) entanglement, this allows them to cheat at some games, so it is not obvious that MIP* is as big as {lang:MIP}; it is only clear that one can ignore all but one player and get the class IP as a lower bound. But, having entanglement also means we can ask more from the players -- much more, and it turns out that {thm:MIP*=RE}, and includes undecidable problems.
