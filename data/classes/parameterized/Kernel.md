---
name: Kernel
related:
  - FPT
---
Problems that admit kernelization: languages (x,k) for which there is a _kernelization algorithm_ that processes the original instance in time poly(n,k) = (n+k)^{O(1)}, and produces an output string K of size f(k) for a computable function f, so that the original instance can be decided by running some (computable) algorithm on K. See [Wikipedia](https://en.wikipedia.org/wiki/Kernelization#Downey%E2%80%93Fellows_notation) for more details. This is a stronger requirement than being FPT, by essentially saying that the "slow" part of the algorithm that depends on k shouldn't need the whole input.
