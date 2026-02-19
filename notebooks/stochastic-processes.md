---
title: Stochastic Processes
date: 06 Feb 2026 14:20
---

# Stochastic Processes

A stochastic process is a collection of random variables indexed by time (or space).

## Key Texts

- Karatzas & Shreve, *Brownian Motion and Stochastic Calculus*
- Rogers & Williams, *Diffusions, Markov Processes and Martingales* (2 vols.)
- Revuz & Yor, *Continuous Martingales and Brownian Motion*

## Types

### Discrete-Time Processes

- **Random walks**: sums of i.i.d. increments; recurrent in d ≤ 2, transient in d ≥ 3
- **Markov chains**: next state depends only on current state; characterized by transition matrix
- **Martingales**: conditional expectation of future equals present; model "fair games"

### Continuous-Time Processes

- **Brownian motion / Wiener process**: continuous paths, independent Gaussian increments
- **Poisson process**: counting process with independent increments; model arrivals
- **Lévy processes**: processes with stationary, independent increments; generalize both

### Stochastic Differential Equations

dX_t = μ(X_t, t) dt + σ(X_t, t) dW_t

Itô's lemma is the chain rule for stochastic calculus — the extra term (the Itô correction) arises because Brownian paths have nonzero quadratic variation.

## See Also

- [Probability Theory](probability.html)
- [Markov Models](markov.html)
