---
name: QMA^+(2)
concrete: false
properties:
  - quantum
  - protocol
---
The two-prover variant of QMA^+: same as QMA(2), except each witness must be a state with non-negative real amplitudes in the standard basis. The relationship to QMA(2) is not well understood and may depend on the completeness/soundness gap.

Not concrete: the equivalence of different completeness/soundness gap parameters is not known, so this is a family of classes parameterized by the gap, not a single well-defined class.
