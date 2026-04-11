---
name: APP
related:
  - FewP
  - GapP
  - PP
  - AWPP
---
Amplified PP. Roughly, the class of decision problems for which the following holds: for all polynomials p(n), there exist GapP functions f and g such that for all inputs x with n = |x|, (1) if the answer is "yes" then 1 > f(x)/g(1^n) > 1 - 2^{-p(n)}, and (2) if the answer is "no" then 0 < f(x)/g(1^n) < 2^{-p(n)}.

Defined in {ref:li93}, where it was also shown that APP is contained in {lang:PP} (and is low for PP), and is closed under intersection, union, and complement. APP contains {lang:AWPP} {ref:fen02} and {lang:FewP} {ref:li93}.

Note: "APP" is also used in the literature for "Approximable in Probabilistic Polynomial Time"; that class is called {lang:AxPP} here to avoid ambiguity.
