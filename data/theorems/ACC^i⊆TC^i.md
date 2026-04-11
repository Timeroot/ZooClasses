---
name: ACC^i⊆TC^i
content: "{i}ACC^i⊆TC^i"
ref: "ACC has 'mod m' gates while TC has threshold gates. A 'w' treshold gate and a 'w+1' threshold gate let you build an 'equals w' threshold gate in constant depth. A mod m gate with n inputs can be decomposed into an OR of floor(n/m) many equality gates, so an ACC^i circuit can be mapped to a TC^i circuit with only a constant factor increase in depth and an O(n) increase in size. See for instance [here](https://cs.stackexchange.com/a/85656/11900)"
---
