---
name: UL
related:
  - "#L"
  - FNL
  - L
  - NL
  - P
---
Unambiguous Logspace. The class of decision problems solvable by a nondeterministic Turing machine using O(log n) space such that:
1. If the answer is "yes," there is exactly one accepting computation path.
2. If the answer is "no," there are no accepting computation paths.

This is the logspace analogue of {lang:UP}: the nondeterminism is "unambiguous" in the sense of unique witnesses. Contained in {lang:NL} and contains {lang:L}.
