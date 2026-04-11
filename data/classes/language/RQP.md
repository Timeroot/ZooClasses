---
name: RQP
related:
  - coRQP
  - EQP
  - ZQP
  - RBQP
properties:
  - quantum
---
One-sided Randomized Quantum Polynomial time.
The class of questions that can be answered by a QTM that accepts with probability 0 when the true answer is no, and accepts with probability at least 1/2 when the true answer is yes. (TODO: What are the precise requirements on runtime or termination?) Since one of the probabilities has to vanish, RQP has the same technical caveats as {lang:EQP}. Complement is {lang:coRQP}.

## Notes

todo: complement of coRQP
