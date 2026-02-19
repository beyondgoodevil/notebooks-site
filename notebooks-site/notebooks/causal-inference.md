---
title: Causal Inference
date: 06 Feb 2026 14:20
---

# Causal Inference

How do we learn cause-and-effect relationships from data?

## The Fundamental Problem

We can never observe the same unit under both treatment and control simultaneously. All causal inference therefore requires some untestable assumption about counterfactuals.

## Frameworks

### Potential Outcomes (Rubin)

Each unit *i* has potential outcomes Y_i(1) and Y_i(0) — the outcome under treatment and under control. The average treatment effect is E[Y(1) - Y(0)]. The observed outcome is Y_i = T_i · Y_i(1) + (1 - T_i) · Y_i(0).

### Directed Acyclic Graphs (Pearl)

Causal structure encoded as a DAG. The *do*-calculus provides rules for computing interventional distributions from observational data, when possible. The key tool: d-separation determines which conditional independences hold.

### Key Assumptions

- **Ignorability / unconfoundedness**: treatment assignment is independent of potential outcomes, conditional on observed covariates
- **SUTVA**: no interference between units; well-defined treatment
- **Overlap / positivity**: every unit has nonzero probability of each treatment level

## Methods

- **Randomized experiments**: gold standard, eliminates confounding by design
- **Instrumental variables**: find a variable that affects treatment but not outcome directly
- **Regression discontinuity**: exploit sharp thresholds in treatment assignment
- **Difference-in-differences**: compare before/after changes across treated and untreated groups

## See Also

- [Statistics](statistics.html)
- [Graphical Models](graphical-models.html)
