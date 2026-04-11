---
name: HamiltonianPath
---
Given a graph, does there exist a path that visits each vertex exactly once?

## Variants

### HamiltonianPathLanguage

- **Type:** Language
- **Description:** Given a graph, does there exist a path that visits each vertex exactly once?

NP-Complete

### HamiltonianPathFunction

- **Type:** Function Problem
- **Description:** Given a graph, output a Hamiltonian path if one exists, or output 'NO' if none exist.

In {lang:FNP}. Reduces to {prob:GraphColoringLanguage} by standard search-to-decision.
