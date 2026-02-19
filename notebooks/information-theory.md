---
title: Information Theory
date: 07 Jul 2025 13:35
---

# Information Theory

Shannon's theory of communication and its extensions.

## Fundamentals

**Entropy**: H(X) = -Σ p(x) log p(x). The average uncertainty, or equivalently, the minimum average code length for lossless compression.

**Mutual information**: I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X). How much knowing Y reduces uncertainty about X.

**KL divergence**: D_KL(P‖Q) = Σ p(x) log(p(x)/q(x)). Not a metric (asymmetric), but measures how much P differs from Q. Always ≥ 0, equals 0 iff P = Q.

## Shannon's Theorems

- **Source coding theorem**: you can compress an i.i.d. source X to H(X) bits per symbol, but no further
- **Channel coding theorem**: you can communicate reliably at any rate below channel capacity C = max_{p(x)} I(X;Y), but not above

## Connections

- To statistics: KL divergence is the excess code length when using the wrong distribution; related to likelihood ratios and hypothesis testing
- To physics: entropy in thermodynamics and information-theoretic entropy are the same concept (Jaynes)
- To learning theory: MDL (minimum description length) connects model selection to compression

## See Also

- [Algorithmic Information Theory](algorithmic-information-theory.html)
- [Statistics](statistics.html)
