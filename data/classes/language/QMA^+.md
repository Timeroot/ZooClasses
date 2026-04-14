---
name: QMA^+
concrete: false
properties:
  - quantum
  - protocol
---
QMA with the additional constraint that the witness state must have non-negative real amplitudes in the standard basis. Aaronson showed that QMA^+ = QMA for the standard (1/3, 2/3) gap [Aar09], but this proof does not extend to all gap choices.

Not concrete: the equivalence of different completeness/soundness gap parameters is not known, so this is a family of classes parameterized by the gap, not a single well-defined class.
