# Landscape and Training Regimes in Deep Learning

| | |
|---|---|
| **Authors** | Mario Geiger, Leonardo Petrini, Matthieu Wyart (EPFL, Institute of Physics) |
| **Year** | 2021 (arXiv v1 30 December 2020) |
| **Type** | Review with new experiments — *Physics Reports* 924, 1–18 (2021), doi:10.1016/j.physrep.2021.04.001. The arXiv version (2012.15110) is titled "Perspective: A Phase Diagram for Deep Learning unifying Jamming, Feature Learning and Lazy Training", 29pp |
| **PDF** | `geiger-petrini-wyart-2021-landscape-and-training-regimes-in-deep-learning.pdf` (in this folder; the published *Physics Reports* version, open access under CC BY 4.0) |
| **Link** | [Physics Reports (open access)](https://doi.org/10.1016/j.physrep.2021.04.001) · [arXiv:2012.15110](https://arxiv.org/abs/2012.15110) |
| **BibTeX** | `geiger2021landscape` |
| **Status** | Reference — read in full (arXiv and published versions) |

## What it is

A physicist's review of three puzzles about deep nets, organised around one picture: a
**phase diagram** in the plane of network width h and the rescaled output scale at
initialisation α̃ = √h·α (α is Chizat and Bach's multiplier on the output,
f = α[f̃_θ − f̃_θ₀]). The puzzles are why training does not get stuck in bad minima, why
adding parameters past the point of fitting the data keeps helping, and how deep nets beat
the curse of dimensionality.

- **New data (Fig. 4).** Fully connected nets with two hidden layers, trained by gradient
  flow on binary MNIST (projected to 10 principal components) and binary CIFAR-10
  (30 components), 5,000 training points, test error of the average of 15 nets per point
  of the (h, α̃) plane. Code is public (Zenodo).
- **Under- vs over-parametrised: a jamming transition (§2).** Below a critical number of
  parameters N\*, the hinge loss cannot reach zero and the landscape is glassy. Above it,
  zero loss is reached and the landscape has many flat directions. The boundary is a
  line of critical points, like the jamming of repulsive particles as density rises.
  - **The universality class is that of ellipses, not spheres.** A counting argument gives
    N_Δ ≤ N, where N_Δ is the number of unfitted data (data with margin below one, like
    support vectors). Hessian stability gives N_Δ ≥ N⁻, the number of negative
    eigenvalues of the curvature term.
    - For spheres N⁻ = N, so N_Δ = N at jamming (isostatic).
    - For a ReLU net, N⁻ ≈ N/2, so N_Δ < N (hypostatic). The Hessian at jamming then
      shows a delta peak at zero, a gap and a continuous band, as measured on MNIST (Fig. 7).
  - **N\*(P) is linear in the number of training points P for random data and sub-linear
    for structured data.** The bound N\* ≤ P/C₀ guarantees zero loss with a number of
    parameters linear in P, if C₀ stays positive (a conjecture).
  - **The test error peaks at jamming (the cusp of "double descent").** The norm of the
    predictor diverges as an inverse power law there. Early stopping, SGD noise or
    weight decay all remove the divergence, so regularisation matters most near jamming.
- **Why more parameters keep helping (§3).** Past jamming, the infinite-width limits are
  well-defined algorithms, and finite width adds noise from the random initialisation.
  The learnt function fluctuates as ‖f_N − ⟨f_N⟩‖ ∼ N^(−1/4), so the test error is
  inflated by ∼ N^(−1/2) over the ensemble average. This holds in both regimes.
  **Averaging nets trained from different initial weights removes the second descent**
  and gives most of the gain of a much wider net (Fig. 5).
- **Lazy (kernel) vs feature learning (§4).** Over-parametrised nets cross over smoothly
  between two regimes at α√h = O(1), with the neural tangent kernel (NTK) changing by
  ‖ΔΘ‖/‖Θ₀‖ ≈ 1 on the boundary.
  - **At large α̃, lazy training.** The NTK barely moves, so the net is a kernel method.
  - **At small α̃, feature learning (mean-field).** The weights move a lot and the kernel
    changes.
  - **The boundary bends up near jamming**, where the output norm explodes, so nets near
    jamming are always feature learners.
  - **Which regime wins depends on the architecture.** For fully connected nets, lazy
    training usually performs better on MNIST, Fashion-MNIST and CIFAR-10; the exception
    is MNIST-10PCA, best near α̃ ∼ 1. For CNNs, feature learning wins, with a steeper
    learning-curve exponent (β ≈ ½ vs ≈ ⅓ on CIFAR-10).
- **How invariants beat the curse of dimensionality (§5).** For Lipschitz targets the
  test error can only fall as P^(−1/d). Low intrinsic dimension helps but is not enough:
  MNIST has d_int ≈ 14 and CIFAR-10 d_int ≈ 30, and Laplace/Gaussian kernels give
  β ≈ 0.4 and β ≈ 0.1. The working hypothesis (Mallat–Bruna) is that nets learn to ignore
  label-preserving deformations of images.
  - **Stripe model.** The label depends only on d_∥ of the d input directions. Lazy
    training gives β = d/(3d−2), while feature learning gives β = (d + d_⊥/2)/(3d−2).
    Neurons align with the informative direction, compressing the uninformative ones by
    a factor Λ ∼ √P. Compressing the input by Λ and then training lazily matches feature
    learning (Fig. 9).
  - **Kernel PCA of the NTK.** After training, the top kernel principal components carry
    more information about the labels, both in the stripe model and for a CNN on MNIST.
    The improved kernel alone performs as well as the trained net.

## Why it's in the library

**It ties together the rest of this folder on one map.** NTK and linearised-network results
([[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]],
[[wikipedia-neural-tangent-kernel]]) live in the lazy corner. Mean-field and µP results
([[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]],
[[bordelon-pehlevan-2023-dynamics-of-finite-width-kernel-and-prediction-fluctuations-in-mean-field-neural-networks]])
live in the feature-learning corner. Memorisation and double descent
([[zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization]]) live on
the jamming line. Karkada's single "richness" knob is this paper's α√h.

**Two practical points for small networks.**
- **Ensembles of moderately wide nets** past the jamming point recover most of the benefit
  of width, because what width removes is initialisation noise. This argues for averaging
  several seeds rather than training one very wide model.
- **Initialisation scale is a real hyperparameter.** For fully connected nets, lazy
  training did better in most of these experiments. Feature learning helped where the
  architecture builds in the right invariance (CNNs).

**On the curse of dimensionality** ([[altman-krzywinski-2018-the-curses-of-dimensionality]],
[[facco-et-al-2017]]), it says plainly that low intrinsic dimension alone does not explain
learnability: CIFAR-10's ≈30 dimensions still give a kernel exponent of about 0.1. What
helps is learning which directions do not matter, and the stripe model makes that
quantitative. Its own conclusion is that the invariance-to-deformations hypothesis is not
established, even empirically.

**Limits.** The experiments are fully connected nets with 2–3 hidden layers, gradient flow,
hinge loss, binary tasks and 5,000 points projected to 10–30 principal components. The
stripe-model exponents assume a smooth decision boundary with non-vanishing data density
there. The diffeomorphism-invariance story is a hypothesis, not a result.

## Links

- [[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]] — the lazy/rich axis
  derived from scaling arguments; its richness r plays the role of α√h here
- [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]] — the lazy
  limit: wide networks as linear models in their weights
- [[wikipedia-neural-tangent-kernel]] — the kernel that stops moving in the lazy regime
- [[bordelon-pehlevan-2023-dynamics-of-finite-width-kernel-and-prediction-fluctuations-in-mean-field-neural-networks]]
  — finite-width fluctuations of the kernel and predictions, the noise behind the N^(−1/4) law
- [[zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization]] —
  over-parametrised nets fit random labels yet generalise
- [[nikolaou-et-al-2026-spectral-reach-neural-scaling-as-progress-into-the-spectral-tail]] —
  learning-curve exponents from the kernel spectrum
- [[garrod-keating-2026-unifying-low-dimensional-spectra-in-deep-learning]] — Hessian and
  weight spectra, the other side of the landscape geometry
- [[altman-krzywinski-2018-the-curses-of-dimensionality]] — why distance-based learning
  fails in high dimension
- [[facco-et-al-2017]] — measuring the intrinsic dimension this review cites for MNIST and
  CIFAR-10
- [[bronstein-bruna-cohen-velickovic-2021-geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges]]
  — symmetry and invariance as the architectural answer to the curse
- [[khalid-et-al-2026-a-survey-of-theory-grounded-interpretability-for-deep-neural-networks]] — a 2026 survey of NTK, sparse-coding, factorisation and manifold explanations of deep nets, with this lazy/rich split as its main caveat
