---
name: PosSLP
---
Given a division-free straight-line program that computes an integer, determine whether the integer is positive.

## Variants

### PosSLPLanguage

- **Type:** Language
- **Description:** Given a division-free straight-line program that computes an integer, determine whether the integer is positive.

See https://arxiv.org/pdf/2307.08008 for overview of recent results. In the 4th level of the polynomial hierarchy, specifically `P^PP^PP^PP`. Important problem in numerical computation. In Exists-Real (TODO lang).

### DegSLP

- **Type:** Integer Problem
- **Description:** Given a division-free straight-line program, determine the degree of the polynomial that it computes.

Representing the polynomial itself can be exponentially large, so we only ask for the degree.

### SuccinctIntegerInequality

- **Type:** Language
- **Description:** See https://arxiv.org/abs/1304.5429

Reduces to {prob:PosSLPLanguage}. Conjectured to be in {lang:P}.
