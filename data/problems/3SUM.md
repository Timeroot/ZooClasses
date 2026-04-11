---
name: 3SUM
---
Given a list of n integers, are there three that sum to zero? Standard problem in fine-grained complexity.

## Variants

### 3SUMLanguage

- **Type:** Language
- **Description:** Given a list of n integers in binary, are there three that sum to zero?

Often written `3SUM` for the language. Known to be in DTIME(n^2 / polylog(n)) in the Word RAM model (with O(log n)-bit words), conjectured to require n^{2-o(1)} time, i.e. there is no O(n^{2-epsilon}) time algorithm for any epsilon>0.

### 3SUMFunction

- **Type:** Function Problem
- **Description:** Given a list of n integers, output three that sum to zero, or output 'NO' if none exist.

Can be reduced to {prob:3SUMLanguage} using a search-to-decision in 3 log_2 n oracle queries.

### #3SUM

- **Type:** Integer Problem
- **Description:** Given a list of n integers, count how many subsets of three that sum to zero.

### Approximate#3SUM

- **Type:** Approximation Problem
- **Description:** Given a list of n integers, count how many subsets of three that sum to zero, to within a factor of 1±epsilon.

If {prob:3SUMLanguage} requires T(n) time, then this approximation can be computed in T(n)*polylog(n)/epsilon^2 time, see Theorem 4 of https://arxiv.org/pdf/1707.04609 .
