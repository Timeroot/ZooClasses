---
name: "TC^0"
related:
  - AC^0
  - ACC^0
  - NC^1
  - TC
properties:
  - circuit
---
Constant-Depth Threshold Circuits. See {lang:TC} for the definition.

Contains {lang:ACC^0} and is contained in {lang:NC^1}.

TC^0 circuits of depth 3 are strictly more powerful than depth 2 {ref:hmp93}.

TC^0 circuits of depth 3 and quasipolynomial size can simulate all of {lang:ACC^0} {ref:yao90}.

There is a function in AC^0 whose computation with TC^0 depth-2 circuits requires exponentially many gates {ref:she08}.

A candidate pseudorandom function family computable in TC^0 exists under a subexponential lower bound on factoring {ref:nr97} {ref:nrr01}. Under this assumption, there is no natural proof separating TC^0 from P/poly {ref:rr97}.

The permanent of a 0-1 matrix cannot be computed in uniform TC^0 {ref:all99}.

Integer division is in U_D-uniform TC^0 and is complete for this class under AC^0 reductions {ref:hes01}.
