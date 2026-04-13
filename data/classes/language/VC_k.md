---
name: VC_k
related:
  - VC_or
  - NP
properties:
  - circuit
concrete: false
---
Verification Class with a Circuit of Depth k:
- VC_0 is the class of compressible languages.
- VC_1 is the class of languages with local verification: they can be verified by testing only a small part of the instance (polynomial in witness length and log of instance length).
- VC_k for k ≥ 2 is the class of languages verifiable by a circuit of depth k, with size polynomial in witness length and instance length.

VC_0 ⊆ VC_or ⊆ VC_1 ⊆ VC_2 ⊆ VC_3 ⊆ ...

Introduced in {ref:hn06}; see there for formal definitions.
