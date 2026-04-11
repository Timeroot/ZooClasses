---
name: QIP
related:
  - IP
  - QMA
  - PSPACE
  - QSZK
  - QAM
  - QMAM
properties:
  - quantum
  - protocol
---
Quantum Interactive Proof Systems. Like {lang:IP}, but the verifier is a BQP (quantum polynomial-time) algorithm, and messages can be quantum states. The prover has unbounded resources (but obeys quantum mechanics). The verifier and prover may become entangled.

Defined in {ref:wat99}, where PSPACE ⊆ QIP[3] was shown. KW00 showed that for k > 3, QIP[k] = QIP[3] = QIP. QIP ⊆ EXP {ref:kw00}.

QIP = IP = PSPACE {ref:jjuw09}; quantum computing adds no power to single-prover interactive proofs.

QIP(1) is known as {lang:QMA}.
