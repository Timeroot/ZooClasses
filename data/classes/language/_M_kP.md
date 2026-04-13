---
name: (M_k)P
related:
  - NP
  - PSPACE
  - Mod_kP
concrete: false
---
Acceptance Mechanism by Monoid M_k. A monoid is a set with an associative operation and an identity element (like a group but without requiring inverses).

(M_k)P is the class of decision problems solvable by an NP machine where the i-th computation path outputs an element m_i of M_k, and the machine accepts iff m_1·m_2·...·m_s is the identity (where s is the number of paths).

Defined by {ref:her97}. For the special case where M is a group:
- If G is any nonsolvable group (e.g., S_5), then (G)P = PSPACE.
- (Z_k)P = coMod_kP, where Z_k is the cyclic group on k elements.
- If |G| = k, then (G)P contains coMod_kP.
