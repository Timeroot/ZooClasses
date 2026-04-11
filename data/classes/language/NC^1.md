---
name: NC^1
related:
  - AC^1
  - TC^0
  - NC^0
  - NC
  - L
  - k-PBP
  - k-EQBP
  - ALOGTIME
properties:
  - circuit
---
Level 1 of NC. The class of decision problems solvable by uniform Boolean circuits with depth O(log n) and fan-in 2. See {lang:NC} for context.

Equals 5-PBP {ref:bar89}; width 5 is necessary unless NC^1 = ACC^0 {ref:bt88}.

NC^1 can be simulated on a quantum computer with a single qubit initialized to a pure state {ref:amp02}: NC^1 ⊆ 2-EQBP.

Is contained in {lang:L} {ref:bor77}. Contains {lang:TC^0}.

Contains integer division even under L-uniformity {ref:bch86} {ref:cdl01}.

U_{E*}-uniform NC^1 = {lang:ALOGTIME} {ref:ruz81}.
