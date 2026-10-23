# The Lazy (NTK) and Rich (µP) Regimes: A Gentle Tutorial

| | |
|---|---|
| **Author** | Dhruva Karkada (UC Berkeley) |
| **Year** | 2024 (v2, 7 October) |
| **Type** | Tutorial — arXiv:2404.19719v2 [cs.LG], 23pp including appendices |
| **PDF** | `karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial.pdf` (in this folder) |
| **BibTeX** | `karkada2024lazy` |
| **Status** | Reference — the best entry point to this folder; read before the NTK and mean-field papers |

## What it is

A non-rigorous, scaling-argument derivation of one fact: **for a wide network to train well,
there is only one free choice in how initial weights and learning rates scale with width.**
That choice sets how much the network learns features.

- **Training criteria (§2.2).** Using a 3-layer linear network, the tutorial requires that, as
  width n → ∞, the outputs move toward the labels in finite time, the hidden representations
  update without exploding or stalling, and training is as fast as these allow. Solving
  these constraints fixes every layer's initial scale and gradient multiplier except one.
- **The richness scale (Fig. 1).** That remaining freedom is r, how fast the hidden
  representation updates ‖Δh‖ grow with width (‖Δh‖ ∼ nʳ):
  - **r = 0, lazy / NTK.** Features barely move. The network is a fixed-kernel machine, as in
    [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]].
  - **r = ½, rich / µP** (maximal update parameterisation). Features change substantially,
    even at infinite width.
  - In between, behaviour changes smoothly at finite width, but at infinite width there is
    a sharp transition: anything below r = ½ is lazy.
- **Intuitions it justifies (§2.3).**
  - Weight updates are rank-one and **align with the layer's input** (§2.3.1).
  - **Standard PyTorch / TensorFlow initialisation is not on the scale** (§2.3.3): the
    readout and first layer are scaled wrongly, so training becomes unstable once width is
    large enough (Fig. 5).
  - **Lazy if and only if linearised** (§2.3.4): the second-order term of the Taylor expansion
    scales like ‖Δh‖²/n, so it vanishes unless the network is at µP. This is the Yang–Hu
    "dynamical dichotomy": kernel behaviour and feature learning exclude each other at
    infinite width.
  - **Feature learning needs small outputs at initialisation** (§2.3.5); the readout layer
    aligns after the first step and outputs reach the right scale.
  - **Rescaling the output by γ = nʳ** (with learning rate γ²), the approach of
    [[bordelon-pehlevan-2023-dynamics-of-finite-width-kernel-and-prediction-fluctuations-in-mean-field-neural-networks]],
    is equivalent to choosing richness r (§2.3.6).
  - **Layerwise learning rates and gradient multipliers are interchangeable** (§2.3.7). That
    "gauge freedom" is why the literature has several names (µP, mean-field, NTK
    parameterisation) for what are the same few choices.
- **Evidence (§2.3.8).** A Myrtle-5 CNN on CIFAR-10 with minibatch SGD and momentum: training
  is well behaved for 0 ≤ r ≤ ½ and diverges or stalls outside it, more so as width grows.

## Read with care

- **Non-rigorous by design.** The rigorous versions are Yang & Hu (2021), *Feature Learning in
  Infinite-Width Neural Networks*. The derivation uses a 3-layer linear network trained on one
  example.
- **Says where training is stable, not which r generalises best.** The tutorial argues rich
  training is closer to practice, but whether more feature learning helps a given task is
  left open, and it is the question that matters on noisy data.
- **Width-scaling arguments.** The guidance is about how to scale hyperparameters as width
  grows. For a fixed, small network the practical differences between parameterisations are
  smaller, and ordinary tuning may hide them.

## Why it's in the library

**It is the map for the rest of this folder.** The NTK papers
([[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]],
[[wikipedia-neural-tangent-kernel]]) sit at r = 0. Bordelon & Pehlevan's γ and Nikolaou et
al.'s feature-learning results sit toward r = ½. This tutorial puts them on one axis.

**It turns "lazy vs rich" into a hyperparameter you set.** How much a network learns features
is decided by initial scales and learning rates, not by the architecture alone. Two practical
points for small networks on tabular features:
- the framework default initialisation is neither lazy nor µP, so behaviour can change as
  width changes even with the learning rate held fixed;
- a zero or small-scale readout initialisation is what allows feature learning. With a
  large initial output the network trains lazily, and a kernel method with the same NTK
  is the right baseline.

**Choose the regime deliberately.** On low-signal targets, lazy training is effectively
regularised kernel regression with early stopping, while rich training can find structure,
and also noise. Treat richness as something to compare on held-out data, not a default.

## Links

- [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]] — the r = 0 end:
  wide networks as linear models
- [[wikipedia-neural-tangent-kernel]] — NTK definitions, and the mean-field / µP alternatives
- [[bordelon-pehlevan-2023-dynamics-of-finite-width-kernel-and-prediction-fluctuations-in-mean-field-neural-networks]]
  — finite-width fluctuations along the same richness axis (their γ = nʳ)
- [[nikolaou-et-al-2026-spectral-reach-neural-scaling-as-progress-into-the-spectral-tail]] —
  what feature learning buys at scale, measured in µP and standard settings
- [[zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization]] — the
  generalisation question that neither regime fully answers
