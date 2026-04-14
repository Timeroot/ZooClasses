---
name: YP
related:
  - BPP
  - NP
  - NP ∩ coNP
  - ONP
  - P
  - P/poly
  - TALLY
  - ZPP
  - coNP
---
The class of decision problems for which there exists a polynomial-time machine M such that:
1. For all input sizes n, there exists a polynomial-size advice string s_n such that M(x, s_n) outputs the correct answer for all inputs x of size n.
2. For all inputs x and advice strings s, M(x, s) outputs either the correct answer or "I don't know."

The name stands for "Your Polynomial-time" or "Yaroslav-Percival." Defined in a blog post by Scott Aaronson.

Contains {lang:ZPP} (by the same argument placing BPP in P/poly) and P with a TALLY ∩ NP ∩ coNP oracle. Contained in NP ∩ coNP and {lang:YPP}. Equals ONP ∩ coONP.
