---
name: P⊆C_eqP
content: P⊆C_eqP
ref: "Simple enough to be usually stated without proof, but here's the proof. Take any deterministic machine M for the language in {lang:P}. Add an initial state that nondeterministically transitions to (option A) the initial state of the original machine, or (option B) a new state that immediately rejects. This machine has one accepting path and one rejecting path if M accepts, and two rejecting paths if M rejects, so this is a valid {lang:C_eqP} machine."
impliedby: ObviousConstruction
---
