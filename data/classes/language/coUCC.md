---
name: coUCC
related:
  - L
properties:
  - complement
---
Complement of UCC (Unique Connected Component). A language is in coUCC if and only if its complement is in UCC, which is the class of problems reducible in L to deciding whether an undirected graph has a unique connected component.

The following problem is complete for coUCC under L-reductions {ref:tor00}: given a colored graph G in which at most two vertices share any given color, does G have any nontrivial automorphism?

Since UCC = L {ref:rei04}, and L is closed under complement (a deterministic machine can just flip accept/reject states), coUCC = L as well.
