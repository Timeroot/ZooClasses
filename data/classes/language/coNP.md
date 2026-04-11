---
name: coNP
related:
  - NP
  - P
  - PH
properties:
  - complement
---
Complement of NP. The class of decision problems whose "no" instances have polynomial-time checkable certificates (i.e., problems of the form "for all witnesses, ..."). Equivalently, problems whose complements are in NP.

If NP = coNP, then any inconsistent Boolean formula of size n has a proof of inconsistency of size polynomial in n. If NP ≠ coNP, then P ≠ NP (but the converse is not known).

Every problem in coNP has an IP interactive proof system {ref:sha92}.
