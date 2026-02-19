---
title: Statistics
date: 15 Oct 2025 13:12
---

# Statistics

Notes on statistical theory, methods, and foundations.

## Core References

- Cox, D.R. *Principles of Statistical Inference* (2006)
- Lehmann, E.L. & Casella, G. *Theory of Point Estimation*
- Wasserman, L. *All of Statistics* (2004) — excellent modern overview

## Topics

### Estimation

Point estimation, interval estimation, and the tradeoffs between bias and variance. The James-Stein estimator shows that even seemingly natural estimators (like the sample mean in 3+ dimensions) can be uniformly improved upon — a result that was deeply counterintuitive when first proved.

### Hypothesis Testing

The Neyman-Pearson framework: fix a significance level α, maximize power against alternatives. The difficulty is that "significance" is easily confused with "importance," and p-values are frequently misinterpreted.

> The most common error: confusing the probability of the data given the null hypothesis with the probability of the null hypothesis given the data.

### Bayesian vs. Frequentist

Both frameworks have their uses. Bayesian methods give you coherent probability statements about parameters; frequentist methods give you procedures with guaranteed long-run performance. Often the practical differences are smaller than the philosophical ones.

## See Also

- [Probability Theory](probability.html)
- [Model Selection](model-selection.html)
- [Causal Inference](causal-inference.html)
