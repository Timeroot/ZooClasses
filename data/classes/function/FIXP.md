---
name: FIXP
related:
  - PPAD
  - PSPACE
---
Fixed Point. The class of fixed-point problems: an instance I is associated with a continuous function F_I, and a solution is a fixed point. F_I is represented by an algebraic circuit over {+, -, *, /, max, min} with rational constants; a polynomial-time algorithm computes the circuit from I.

Every FIXP problem has partial computation, decision, approximation, and existence versions, all solvable in PSPACE. The Nash equilibrium for 3+ players is FIXP-complete. Linear-FIXP = PPAD.

Defined in {ref:ey07}.
