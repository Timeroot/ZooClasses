---
name: MinimumCircuitSize
---
Given the truth table of a Boolean function, what is the size of the smallest Boolean circuit that computes it?

## Variants

### MCSLanguage

- **Type:** Language
- **Description:** Given the truth table of a Boolean function and an integer s, does there exist a Boolean circuit (with any fanin-2 gates) of size at most s that computes the function?

Called `MCSP` for the language. Not known to be in NP, nor known to be NP-hard. Believed to be a very hard problem, as it is closely related to proving circuit lower bounds.

### MCSFunction

- **Type:** Integer Problem
- **Description:** Given the truth table of a Boolean function, output the size of the smallest Boolean circuit that computes it.

### MCSOptimization

- **Type:** Optimization Problem
- **Description:** Given the truth table of a Boolean function, find the smallest Boolean circuit possible that computes it.
