---
name: NIPZK
related:
  - PZK
  - SBP
  - NISZK
properties:
  - protocol
---
Non-Interactive PZK. Defined in {ref:m08} based on {ref:ddp98} and {ref:bfm88}.

Contained in {lang:PZK} and coSBP. There are oracles separating NIPZK from PZK, coNIPZK, and {lang:SBP} {ref:bchtv17} {ref:dgpv20}.

A complete promise-problem for NIPZK is Uniform (UN): instances are circuits with n+1 output bits, where the first n bits represent the uniform distribution and the last bit is 1 with probability ≥ 2/3 (YES instance) or ≤ 1/3 (NO instance). UN is in co{lang:SBP} {ref:dgpv20}.
