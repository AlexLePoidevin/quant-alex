# Dynamics of Finite Width Kernel and Prediction Fluctuations in Mean Field Neural Networks

| | |
|---|---|
| **Authors** | Blake Bordelon, Cengiz Pehlevan (Harvard SEAS, Center for Brain Science, Kempner Institute) |
| **Year** | 2023 |
| **Type** | Paper — *Advances in Neural Information Processing Systems* 36 (NeurIPS 2023). 44pp including appendices; code at github.com/Pehlevan-Group/dmft_fluctuations |
| **PDF** | `bordelon-pehlevan-2023-dynamics-of-finite-width-kernel-and-prediction-fluctuations-in-mean-field-neural-networks.pdf` (in this folder) |
| **BibTeX** | `bordelon2023finite` |
| **Status** | Reference — physics-style theory; read §1, §5–6 and §9 |

## What it is

The infinite-width limit gives a clean, deterministic description of training. Real networks
are finite, so two networks trained on the same data from different random seeds disagree.
This paper computes **how large that seed-to-seed disagreement is, and how it changes during
training**, in the regime where networks learn features.

- **Setting (§2).** Networks in the mean-field / μP parameterisation, with a parameter γ
  setting feature-learning strength: γ → 0 is the lazy (NTK) regime of
  [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]], large γ is
  rich feature learning. At infinite width, training is described by a **dynamical mean
  field theory** (DMFT): kernels and predictions follow deterministic equations.
- **Method (§3–4).** Treat width N as large but finite and expand around the DMFT solution.
  Kernels and predictions then fluctuate across initialisations with variance of order 1/N
  (deviations of order 1/√N), and the paper gives equations for that variance throughout
  training. The expansion is perturbative in 1/width but **not** in feature-learning strength,
  which earlier finite-width analyses (the neural tangent hierarchy) required.
- **Lazy limit (§5).** The NTK is random but fixed, so its seed variance never changes. The
  variance of the prediction errors follows a simple differential equation over the kernel's
  eigenmodes (Proposition 3). It rises as the model starts fitting, then falls as errors
  shrink.
- **Rich regime, two-layer networks (§6).** Kernel and prediction fluctuations are coupled
  and must be solved together. **Feature learning reduces the variance**: larger γ gives a
  lower-variance final kernel and final predictions, a higher signal-to-noise ratio, and a
  network closer to its infinite-width limit. Larger training sets (relative to width)
  make finite-width effects bigger; richer training partly offsets this.
- **Deeper networks (§7).** Kernel variance can **accumulate layer by layer** at strong feature
  learning, yet the signal-to-noise ratio of the feature kernels still improves.
- **Large learning rates (§8).** Edge-of-stability dynamics are captured by the
  infinite-width theory, and initialisation variance can shrink during training.
- **CIFAR-10 CNNs (§9).** Wider networks have lower error, lower bias (from averaging the
  logits of 8 seeds) and, compared at equal training accuracy, lower variance. **Ensembling
  does not remove the finite-width penalty**: even averaged over seeds, narrow networks
  train more slowly. The fitted training rate falls roughly linearly in 1/N, with a
  quadratic term below N ≈ 100.

## Read with care

- **Physics rigour, not proofs.** The authors say so (§10). The expansion keeps only the
  leading 1/N term and breaks down when the number of samples approaches the width.
- **Not computable at scale.** The full equations need a Hessian with O(T⁴P⁴) entries over
  training time and samples, so they are solved only for toy models: one training point,
  two-layer networks, deep linear networks. The CIFAR results are empirical checks, not
  solutions of the theory.
- **Only initialisation noise.** SGD minibatch noise, data-order effects and distribution shift
  are outside the analysis. In practice they also produce seed-to-seed disagreement.
- **Toy targets.** Mostly Gaussian random data or single points. Nothing on noisy,
  low-signal targets, where variance across seeds could be large relative to the signal.

## Why it's in the library

**It explains seed variance and what ensembling can and cannot fix.** Two models trained on
the same data from different seeds pick different things. This paper splits the effect of
finite size into two parts:
- **Variance**: seed-to-seed scatter, which averaging over seeds removes, and which wider
  networks and stronger feature learning reduce;
- **Bias**: a shift in the *average* model, including slower training, which averaging over
  seeds does not remove; only more width does.

A seed ensemble is therefore worth building, but it does not turn a narrow model into a wide
one. Report how much predictions disagree across seeds alongside any backtest, and compare
an ensemble against a single wider model at equal compute.

**It connects the lazy and rich pictures.** Read after the NTK papers:
[[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]] says what happens
at infinite width with no feature learning; this paper adds finite width and feature
learning. Its finding that feature learning moves the network toward its infinite-width
limit fits [[nikolaou-et-al-2026-spectral-reach-neural-scaling-as-progress-into-the-spectral-tail]],
where feature learning is what sustains progress.

## Links

- [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]] — the lazy,
  infinite-width baseline this paper perturbs around (γ → 0)
- [[wikipedia-neural-tangent-kernel]] — lazy vs mean-field / μP scalings and the neural tangent
  hierarchy this paper improves on
- [[nikolaou-et-al-2026-spectral-reach-neural-scaling-as-progress-into-the-spectral-tail]] —
  feature learning as the thing that keeps training progressing
- [[zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization]] — the
  generalisation puzzle that infinite-width theories try to explain
