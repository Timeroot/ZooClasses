---
name: SNP
related:
  - MMSNP
  - MaxSNP
  - NP
---
Strict NP. {ref:fag74} showed that NP is precisely the class of decision problems reducible to a graph-theoretic property expressible in second-order existential logic.

SNP is the class of decision problems reducible to a graph-theoretic predicate with only universal quantifiers over vertices and no existential quantifiers. As an example, k-SAT (CNF satisfiability with at most k literals per clause, for k a constant) is in SNP. General SAT is not in SNP, because we need to say "there exists a literal in this clause that satisfies the clause."

Contains {lang:MMSNP}. See also {lang:MaxSNP}.
