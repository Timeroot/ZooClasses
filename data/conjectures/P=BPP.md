---
name: P=BPP
content: P=BPP
not_implies:
  - "P!=NP"
---
## Notes

A type of a derandomization conjecture. {thm:Adleman's theorem} says that BPP⊆P/poly, in other words that BPP has polynomial-size circuits; this conjecture is a stronger statement that BPP has polynomial-time algorithms, or polynomial-size uniform circuits.
If this conjecture is true, then many other derandomization conjectures follow, such as BPP=RP and BPP=ZPP.
If this conjecture is false, then it implies that {conj:P!=NP}: P=NP implies that P=PH (collapse), and the {thm:Sipser–Lautemann theorem} says that BPP⊆PH.
