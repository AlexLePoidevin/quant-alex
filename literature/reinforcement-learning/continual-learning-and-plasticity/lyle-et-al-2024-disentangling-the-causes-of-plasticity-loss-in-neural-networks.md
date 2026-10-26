# Disentangling the Causes of Plasticity Loss in Neural Networks

| | |
|---|---|
| **Authors** | Clare Lyle, Zeyu Zheng, Khimya Khetarpal, Will Dabney, Hado van Hasselt, Razvan Pascanu, James Martens (Google DeepMind) |
| **Year** | 2024 |
| **Type** | Preprint — arXiv:2402.18762v1 [cs.LG], 29 February 2024, 32pp including appendices |
| **PDF** | `lyle-et-al-2024-disentangling-the-causes-of-plasticity-loss-in-neural-networks.pdf` (in this folder) |
| **BibTeX** | `lyle2024disentangling` |
| **Status** | Reference — read §3 (mechanisms) and §4.1; the practical answer is in the abstract: layer norm plus weight decay |

## What it is

Earlier work showed networks trained on changing data lose the ability to learn, and that
no single measured quantity (dead units, weight norm) explains every case. This paper's
answer: **there are several independent mechanisms**, each with its own fix, and **fixing them
together** — a "Swiss cheese" model — gives robust training.

- **Plasticity, defined (§2.2).** A network has lost plasticity if it optimises a new
  objective **worse than a freshly initialised network would**. It is a property of a point
  in parameter space (and optimiser state) as a *starting point*.
- **Two kinds of problem cause it (§3.1, Fig. 1).**
  - **Large regression targets.** Pre-training on targets with a big constant offset makes
    later fitting slower, with a clear dose–response. The network encodes the offset in one
    feature direction, and the features become badly conditioned. **Moving targets alone are
    not needed** — a growing target mean is enough.
  - **Sudden shifts.** Re-randomising 1% of labels at a time barely hurts; 10% or more
    sharply speeds the decline. **Abrupt change damages more than gradual change.**
- **Mechanisms inside the network (§3.2).**
  - **Pre-activation distribution shift**, which produces dead units, poor signal
    propagation, and a new pathology: **"zombie" units that have become effectively
    linear**, passing gradients but adding no expressive power.
  - **Parameter norm growth**, which sharpens the loss landscape and can saturate
    normalisation or attention layers; layers can grow at different rates.
  - Right after a task change there is an "erasing" phase with large gradients where many
    units die or linearise at once (Fig. 2).
- **A common signature (§3.3, Fig. 3).** Very different routes all produce a degenerate
  **empirical neural tangent kernel**: off-diagonal structure close to low rank. The eNTK is
  proposed as a diagnostic.
- **Fixes (§4.1, Fig. 4).** Layer or batch normalisation for pre-activation shift; **L2
  (weight decay)** for norm growth; **distributional / "two-hot" classification losses** for
  large targets. Resetting dead units (ReDo) helps but can slow convergence. Gradient-norm
  penalties, Shampoo and feature regularisation did not beat **layer norm + L2**.
- **Evaluation (§5).** Layer norm + L2 keeps plasticity across many synthetic shifts on
  CIFAR-10 with MLPs, CNNs and ResNet-18 — accuracy often *improves* across tasks — and gives
  modest gains for C51 and Rainbow on Atari and SAC on DeepMind Control. L2 and batch norm
  interfered with the RL agents, so layer norm alone was used there.

## Read with care

- **Not an exhaustive list.** The authors do not claim to have found every mechanism.
- **Mostly synthetic benchmarks.** Random labels and permuted classes are clean but extreme.
  The natural distribution-shift results are fewer.
- **L2 costs speed.** The conclusion notes weight decay slows single-task convergence, and
  better norm control may exist.
- **Preprint version.** This copy is arXiv v1; check for a published version before citing
  exact numbers.

## Why it's in the library

**Return targets are a large-target regression problem.** Many forecasting models regress on
returns, cumulative returns or value-like quantities whose mean shifts across regimes. The
target-offset result says that fitting a target with a large or drifting mean can by
itself damage a network's later ability to learn. Demeaning targets per window, or using a
classification or two-hot loss over return bins, is a cheap guard.

**Abrupt regime changes are the damaging case.** The sudden-versus-gradual finding matches
markets: a crash or policy shift is a large, sudden label change. A model warm-started
through such a break may lose more plasticity than one that saw only drift.

**It gives a default recipe.** For a neural model that is retrained in place on a rolling
window, layer normalisation before each nonlinearity plus a small weight decay is the
first thing to try, before more complex resets.

**It connects plasticity to kernel theory.** The eNTK diagnostic ties this folder to the NTK
notes elsewhere in the library: a network that has lost plasticity is one whose tangent
kernel has collapsed toward low rank.

## Links

- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — the phenomenon at
  scale; this paper explains its correlates
- [[sokar-et-al-2023-the-dormant-neuron-phenomenon-in-deep-reinforcement-learning]] — dead
  units, one of the mechanisms here, and ReDo, one of the fixes compared
- [[bellemare-dabney-munos-2017-a-distributional-perspective-on-reinforcement-learning]] —
  C51; the paper suggests distributional losses help partly by avoiding large-target
  ill-conditioning
- [[chiley-et-al-2019-online-normalization-for-training-neural-networks]] — normalisation
  for streaming data, relevant to the pre-activation-shift fix
- [[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]] — the NTK and
  parameterisation background behind the eNTK diagnostic
- [[khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives]]
  — the continual RL framing (Khetarpal is a co-author of both)
