---
name: AH
related:
  - PH
  - R
  - RE
  - coRE
---
Arithmetic Hierarchy. The analog of {lang:PH} in computability theory.

Let Δ_0 = Σ_0 = Π_0 = R. Then for i > 0:
- Δ_i = R with Σ_{i-1} oracle.
- Σ_i = RE with Σ_{i-1} oracle.
- Π_i = coRE with Σ_{i-1} oracle.

AH is the union of these classes for all nonneg i.

Each level strictly contains the levels below it. Equivalently, Σ_{i+1} consists of sets validating a formula ∃X_1...∃X_n φ with φ ∈ Δ_i, and Π_i is the complement of Σ_i.
