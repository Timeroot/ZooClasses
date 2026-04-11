---
name: GraphColoring
---
Given a graph and an integer k, can the graph be colored with k colors such that no two adjacent vertices share the same color?

## Variants

### GraphColoringLanguage

- **Type:** Language
- **Description:** Given a graph and an integer k, can the graph be colored with k colors such that no two adjacent vertices share the same color?

NP-Complete.

### ChromaticNumberFunction

- **Type:** Integer Problem
- **Description:** Given a graph, output its chromatic number (the minimum number of colors needed to color the graph).

Not necessarily in {lang:FNP}, because the chromatic number alone is not enough of a witness to check the existence of a coloring. Reduces to {prob:GraphColoringLanguage} by standard search-to-decision.

### GraphColoringFunction

- **Type:** Function Problem
- **Description:** Given a graph and an integer k, output a valid k-coloring of the graph, or output 'NO' if none exists.

In {lang:FNP}. Reduces to {prob:GraphColoringLanguage} by standard search-to-decision.

### GraphColoringOptimization

- **Type:** Optimization Problem
- **Description:** Given a graph, find a valid graph coloring with as few colors as possible.

Reduces to {prob:GraphColoringLanguage} by standard search-to-decision.

### #kCOL

- **Type:** Integer Problem
- **Description:** Given a graph, count the number of distinct valid k-colorings of the graph.

#P-Complete. {prob:GraphColoringLanguage} reduces to this problem by checking if the count is greater than zero.
