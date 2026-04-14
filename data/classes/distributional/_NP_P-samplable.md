---
name: (NP,P-samplable)
related:
  - AvgP
  - DistNP
properties:
  - protocol
---
Average NP With Samplable Distributions. A *distributional problem* is a pair (L, μ) where L is a decision problem and μ is a probability distribution over inputs. See {lang:AvgP} for the basic definitions.

(NP,P-samplable) is defined like {lang:DistNP}, except that the distribution μ only needs to be *samplable* in polynomial time: there is a polynomial-time randomized algorithm that generates instances according to μ. In DistNP, the stronger condition is that μ's cumulative density function must be polynomial-time *computable*. Since computability is harder to achieve than samplability, (NP,P-samplable) is (potentially) a larger class than DistNP.

Any DistNP-complete problem is also complete for (NP,P-samplable) {ref:IL90}.
