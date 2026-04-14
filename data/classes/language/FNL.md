---
name: FNL
related:
  - "#L"
  - NL
  - NP
  - UL
---
Function Nondeterministic Logspace. The class of function problems solvable by nondeterministic logspace computation: given an input x and a logspace-checkable predicate F(x,y), if there exists a y satisfying F(x,y) then output any such y, otherwise output 'no.'

Equivalently, FNL is to {lang:NL} as {lang:FNP} is to NP: it is the function analogue of nondeterministic logspace, where the output (the witness y) has length polynomial in n and can be verified in logspace.

Contained in #L and contains {lang:UL}.
