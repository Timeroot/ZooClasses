---
name: ModL
related:
  - GapL
  - FL
  - Mod_kL
---
Mod Logspace. A language L is in ModL if there exist functions f ∈ GapL and g ∈ FL such that for all strings x: there exist a prime p and natural number α such that g(x) = 0^{p^α}, and x ∈ L iff f(x) ≡ 0 (mod |g(x)|).

Thus Mod_{p^α}L ⊆ ModL for any prime p and natural number α. Moreover, FL^{ModL} = FL^{GapL} {ref:av04}.

Defined in {ref:av04}.
