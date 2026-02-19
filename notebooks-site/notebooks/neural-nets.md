---
title: Neural Nets, Connectionism, Perceptrons, etc.
date: 12 Feb 2026 11:40
---

# Neural Nets, Connectionism, Perceptrons, etc.

Notes on artificial neural networks — from perceptrons to deep learning.

## Historical Background

The perceptron (Rosenblatt, 1958) was the first trainable neural network. Minsky & Papert's *Perceptrons* (1969) showed its limitations (it can't learn XOR), dampening enthusiasm for two decades.

The backpropagation algorithm (Rumelhart, Hinton, Williams, 1986) enabled training of multi-layer networks, reviving the field.

## Why Deep Learning Works (Partial Answers)

- **Representation learning**: hidden layers learn useful feature representations
- **Lottery ticket hypothesis**: large networks contain well-initialized sub-networks
- **Implicit regularization**: SGD has a bias toward "simpler" solutions
- **Double descent**: generalization can improve even as models interpolate training data

## Architecture Zoo

- **MLP**: fully connected layers; the baseline
- **CNN**: convolutional layers exploit spatial locality and translational equivariance
- **RNN/LSTM**: handle sequences with recurrent connections; largely supplanted by Transformers
- **Transformer**: attention mechanisms; now dominant in language, vision, and much else
- **GNN**: extend deep learning to graph-structured data

## Concerns

Adversarial examples, overconfident predictions, poor calibration, brittleness to distribution shift. The gap between benchmark performance and real-world reliability remains large in many domains.

## See Also

- [Artificial Intelligence](ai.html)
- [Statistics](statistics.html)
