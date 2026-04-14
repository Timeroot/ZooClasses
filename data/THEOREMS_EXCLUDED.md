# Excluded Theorems

These are theorem-like statements from the Complexity Zoo that were
not automatically extracted. Common reasons:

- **Conditional results**: "If NP ⊆ P/poly then PH collapses"
- **Oracle results**: "There exists an oracle relative to which X=Y"
- **Approximate/relative**: Results about specific problems, not class containments
- **Complex multi-clause**: Statements with too many moving parts
- **Unknown classes**: References to classes not in our data model

The automated extraction focused on clear, unconditional containment (⊆, ⊂)
and equality (=) relationships between known class names.


## Cross-type theorems (moved here pending type-system design)

These theorems compare classes of different types (Language vs Distributional,
Language vs Parameterized, Language vs Promise). They are factually correct but
violate the "same-type only" rule and need to be reconsidered once the type
system design is settled.

### BPP⊆HeurBPP

```
---
name: "BPP⊆HeurBPP"
content: "BPP⊆HeurBPP"
ref: "BPP ⊆ HeurBPP: a BPP algorithm with 0 error is a heuristic with 0 error fraction."
---
```

### HeurBPP⊆BPP

```
---
name: "HeurBPP⊆BPP"
content: "HeurBPP⊆BPP"
ref: "HeurBPP ⊆ BPP: heuristic BPP ⊆ BPP."
---
```

### P⊆HeurP

```
---
name: "P⊆HeurP"
content: "P⊆HeurP"
ref: "P ⊆ HeurP: a P algorithm with 0 error is a heuristic P algorithm."
---
```

### HeurP⊆P

```
---
name: "HeurP⊆P"
content: "HeurP⊆P"
ref: "HeurP ⊆ P: heuristic P problems are in P on typical inputs."
---
```

### PP⊆HeurPP

```
---
name: "PP⊆HeurPP"
content: "PP⊆HeurPP"
ref: "PP ⊆ HeurPP: a PP machine that always succeeds is a heuristic PP machine with 0 error fraction."
---
```

### HeurPP⊆PP

```
---
name: "HeurPP⊆PP"
content: "HeurPP⊆PP"
ref: "HeurPP ⊆ PP: heuristic PP ⊆ PP."
---
```

### (NP,P-samplable)⊆NP

```
---
name: "(NP,P-samplable)⊆NP"
content: "(NP,P-samplable)⊆NP"
ref: "(NP,P-samplable) ⊆ NP: the language component of every distributional problem in (NP,P-samplable) is in NP by definition."
---
```

### AW[P]⊆PSPACE

```
---
name: "AW[P]⊆PSPACE"
content: "AW[P]⊆PSPACE"
ref: "AW[P] ⊆ PSPACE: alternating W[P] parameterized machines can be simulated in PSPACE."
---
```

### FPL⊆L

```
---
name: "FPL⊆L"
content: "FPL⊆L"
ref: "FPL ⊆ L: fixed-parameter logspace ⊆ logspace."
---
```

### FPR⊆BPP

```
---
name: "FPR⊆BPP"
content: "FPR⊆BPP"
ref: "FPR (fixed-polynomial randomized) ⊆ BPP."
---
```

### NL⊆XNLP

```
---
name: "NL⊆XNLP"
content: "NL⊆XNLP"
ref: "NL ⊆ XNLP: nondeterministic logspace is a special case of XNLP with f(k) = O(1), giving O(log n) space and polynomial time."
---
```

### para-P⊆P

```
---
name: "para-P⊆P"
content: "para-P⊆P"
ref: "para-P (parametrized P) ⊆ P: fixed-parameter tractable ⊆ P."
---
```

### SLICEWISE PSPACE⊆NEXP

```
---
name: "SLICEWISE PSPACE⊆NEXP"
content: "SLICEWISE PSPACE⊆NEXP"
ref: "Slicewise PSPACE ⊆ NEXP."
---
```

### XNLP⊆NEXP

```
---
name: "XNLP⊆NEXP"
content: "XNLP⊆NEXP"
ref: "XNLP (XP for NL) ⊆ NEXP."
---
```

### XP_uniform⊆PSPACE

```
---
name: "XP_uniform⊆PSPACE"
content: "XP_uniform⊆PSPACE"
ref: "XP_uniform ⊆ PSPACE."
---
```

### P⊆PromiseP

```
---
name: "P⊆PromiseP"
content: "P⊆PromiseP"
ref: "P ⊆ PromiseP: any P language is a promise problem solvable by a P machine (where the promise is the trivial promise: all strings are valid inputs)."
---
```

### PromiseP⊆P

```
---
name: "PromiseP⊆P"
content: "PromiseP⊆P"
ref: "PromiseP ⊆ P: promise problems in P."
---
```

### UP⊆PromiseUP

```
---
name: "UP⊆PromiseUP"
content: "UP⊆PromiseUP"
ref: "UP ⊆ PromiseUP: any UP language is a promise problem solvable by a UP machine."
---
```

### PromiseUP⊆UP

```
---
name: "PromiseUP⊆UP"
content: "PromiseUP⊆UP"
ref: "PromiseUP ⊆ UP."
---
```


### PODN⊆NP

```
---
name: "PODN⊆NP"
content: "PODN⊆NP"
ref: "PODN (P with one-sided determinism) ⊆ NP."
---
```

### PSK⊆NP

```
---
name: "PSK⊆NP"
content: "PSK⊆NP"
ref: "PSK (P-settable k-wise NP) ⊆ NP."
---
```

### AW[star]⊆PSPACE

```
---
name: "AW[*]⊆PSPACE"
content: "AW[*]⊆PSPACE"
ref: "AW[*] ⊆ PSPACE (alternating Turing machine with all quantifiers)."
---
```
