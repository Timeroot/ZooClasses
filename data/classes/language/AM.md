---
name: AM
related:
  - NP
  - MA
  - IP
properties:
  - protocol
---
Arthur-Merlin games. In general, AM[k] is k-round interactive protocols between am omniscient Merlin and a polytime Arthur. Arthur has randomness, but Merlin can see all of Arthur's randomness, and they exchange polynomial size messages, and Arthur becomes convinced with 2/3 soundness and completeness. It turns out that AM[k]=AM[2] for any constant k, TODO reference, and then the class AM is defined as AM[2]. This doesn't translate to polynomial k, as the message sizes grows by at least a constant factor with each removed round, leading to exponential slowdown if you tried to run AM[poly] as a AM[2] protocol. As other cases, there are AM[0]=BPP, AM[1]=MA, and AM[poly(n)]=IP. There is also the odd one AM[polylog(n)].
 Compare with IP[k], which has private coins: Merlin can't see Arthur's random choices.

## Notes

todo def
