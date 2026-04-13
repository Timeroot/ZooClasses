---
name: IOP
related:
  - IP
  - NEXP
  - PCP_r_n_q_n
properties:
  - protocol
---
Interactive Oracle Proof. A proof system combining PCP and {lang:IP}. Both prover and verifier can send messages as in interactive proofs, but the verifier receives oracle access to the prover's messages (as in PCP). Instead of one fixed proof, the prover sends multiple rounds of proofs whose contents may depend on verifier messages, and the verifier randomly queries symbols from these.

The class of problems solvable by IOPs equals {lang:NEXP}, the same as PCP. Thus IOPs are not more powerful than PCPs, but can achieve better parameters (total proof length, alphabet size, query complexity). IOPs can be converted to IPs via Merkle trees using the BCS compiler.
