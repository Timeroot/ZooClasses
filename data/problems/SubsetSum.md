---
name: SubsetSum
---
Given a set of integers and a target integer T, is there a subset that sums to T?

## Variants

### SubsetSumLanguage

- **Type:** Language
- **Description:** Given a set of integers and a target integer T, is there a subset that sums to T?

Often written `SUBSETSUM` for the language. NP-Complete.

### SubsetSumFunction

- **Type:** Function Problem
- **Description:** Given a set of integers and a target integer T, output a subset that sums to T, or output 'NO' if none exist.

In {lang:FNP}. Reduces to {prob:SubsetSumLanguage} by standard search-to-decision.

### SubsetSumClosest

- **Type:** Optimization Problem
- **Description:** Given a set of integers, output a nonempty subset with a nonnegative sum as close as possible to zero.
