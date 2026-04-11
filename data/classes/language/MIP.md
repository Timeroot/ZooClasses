---
name: MIP
related:
  - AM
  - IP
  - QIP
  - "MIP*"
  - MIPco
  - NEXP
properties:
  - protocol
---
Multiple-player Interactive Proofs. In general, MIP[p,r] means a proof with p player who cannot communicate, and r rounds of interaction with a referee. (The final round is always a message to the referee, as a final message to a player cannot be useful.) As it turns out, MIP[p,r]=MIP[2,1] for any p>=2 and r>=1, so the distinction is largely unnecessary. MIP[1,r] is better known as AM[r], see AM for more. 
 And of course MIP[p,0] is just P. :)

MIP[p,r]=MIP[2,poly] is proved in {ref:BFL91}. I can't find a source for the statement that MIP[2,poly]=MIP[2,1].
