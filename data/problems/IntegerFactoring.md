---
name: IntegerFactoring
---
Determine the prime factors of a given integer.

## Variants

### FactoringLanguage

- **Type:** Language
- **Description:** Given an integer N in binary, and integers A and B in binary, does N have a prime factor betwween A and B?

Often written `FACTORING` for the language, sometimes this instead asks if N has any factor - not just a prime factor - between A and B. In NP and co-NP, but not known to be in P or NP-complete. In {lang:NP} and {lang:coNP} (because {prob:PrimalityLanguage} is in {lang:P}), and {lang:BQP} by Shor's algorithm.

### AllFactorsFunction

- **Type:** Function Problem
- **Description:** Given an integer N in binary, output its prime factorization.

Reduces to {prob:FactoringLanguage} by standard search-to-decision. In {lang:FNP} and {lang:FcoNP} since {prob:PrimalityLanguage} is in {lang:P}, and in {lang:FBQP} by Shor's algorithm.

### SmallestFactorFunction

- **Type:** Function Problem
- **Description:** Given an integer N in binary, output its smallest prime factor.

Not necessarily in {lang:FNP}, because the smallest prime factor alone is not enough of a witness to prove that there is no smaller prime factor. Still in {lang:FBQP} by Shor's algorithm though. Reduces to {prob:FactoringLanguage} by standard search-to-decision.
