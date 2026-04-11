---
name: SumOfSquareRoots
---
Given a list of integers, determine whether the sum of their square roots is at least a given target value.

## Variants

### SumOfSquareRootsLanguage

- **Type:** Language
- **Description:** Given a list of integers a_1, a_2, ..., a_n in binary and a target integer T, determine whether sqrt(a_1) + sqrt(a_2) + ... + sqrt(a_n) >= T.

In PSPACE, not known to be in NP or co-NP. Conjectured to be in P. Equivalent to the problem where T is a rational number instead of an integer. Reducible to {prob:PosSLPLanguage} by (TODO ref: Eric Allender, Peter B¨urgisser, Johan Kjeldgaard-Pedersen, and Peter Bro Miltersen. On the complexity of numerical analysis.). In Exists-Real (TODO lang).

### SumOfSignedSquareRootsLanguage

- **Type:** Language
- **Description:** Given a list of integers a_1, a_2, ..., a_n in binary, and a set of signs s_1, s_2, ..., s_n in binary, determine whether sqrt(a_1)*s_1 + sqrt(a_2)*s_2 + ... + sqrt(a_n)*s_n >= 0. In Exists-Real (TODO lang).

### SumOfRootsLanguage

- **Type:** Language
- **Description:** Given a list of integers a_1, a_2, ..., a_n in binary, and a set of rational powers p_1, p_2, ..., p_n as pairs of integers, and a target integer T, determine whether a_1^{p_1} + a_2^{p_2} + ... + a_n^{p_n} >= T. In Exists-Real (TODO lang).
