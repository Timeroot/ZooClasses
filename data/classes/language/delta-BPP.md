---
name: "δ-BPP"
related:
  - BPP
  - P
---
δ-Semi-Random BPP. Same as BPP, except that the random bit source is biased: each bit may depend arbitrarily on all previous bits, but the only promise is that each bit is 1 with probability in the range [δ, 1-δ] conditioned on all previous bits.

So 0-BPP = P and (1/2)-BPP = BPP. For any δ > 0, δ-BPP = BPP {ref:vv85} {ref:zuc91}.
