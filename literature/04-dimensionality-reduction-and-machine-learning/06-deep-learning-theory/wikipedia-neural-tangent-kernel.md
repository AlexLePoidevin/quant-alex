# Neural Tangent Kernel (Wikipedia)

| | |
|---|---|
| **Author** | Wikipedia contributors |
| **Year** | 2026 (revision of 11 August 2026) |
| **Type** | Encyclopedia article — English Wikipedia, CC BY-SA 4.0 |
| **Link** | https://en.wikipedia.org/wiki/Neural_tangent_kernel (permanent revision: https://en.wikipedia.org/w/index.php?oldid=1368847382) |
| **BibTeX** | `wiki2026ntk` |
| **Status** | Explainer and reading map — cite the primary papers, not this page |

## What it covers

- **Definition.** For a network f(x; θ), the NTK is Θ(x, x′; θ) = ∇θ f(x; θ) · ∇θ f(x′; θ): the
  inner product of the parameter gradients at two inputs. It is symmetric and positive
  semi-definite, so it is a valid kernel. Introduced by Jacot, Gabriel & Hongler (NeurIPS 2018).
- **Function-space dynamics.** Under gradient flow on a loss C(f) = Σᵢ c(f(xᵢ), zᵢ),
  ∂ₜ f(x) = −Σᵢ Θ(x, xᵢ) ∂c/∂f(xᵢ). Each training point moves the prediction at *x* in
  proportion to the kernel between them, so the NTK says how learning on one input spreads
  to another.
- **The infinite-width limit** (fully connected, NTK parameterisation W/√n):
  - the kernel becomes deterministic (independent of the random initialisation) and stays
    constant during training;
  - individual weights barely move, but together they change the output by a finite amount;
  - the network is linear in its parameters (still nonlinear in its inputs), as in
    [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]];
  - training is kernel gradient descent with the NTK.
  The limiting kernel follows a layer-by-layer recursion,
  Θ⁽ˡ⁺¹⁾ = Θ⁽ˡ⁾ Σ̇⁽ˡ⁺¹⁾ + Σ⁽ˡ⁺¹⁾, built from the NNGP activation kernels Σ⁽ˡ⁾.
- **What it is used for:**
  - **Ridgeless kernel regression.** With squared loss, the trained ensemble's mean equals
    ŷ(x) = Θ(x, X) Θ(X, X)⁻¹ y, so a wide network **interpolates its training data**: the
    minimum-RKHS-norm interpolant (implicit regularisation).
  - **Overparameterisation and generalisation.** Kernel-regression theory (Jacot et al.
    2020, Canatar et al. 2021, Simon et al. 2021) explains why wide converged networks can
    fit training data exactly and still generalise; links to double descent.
  - **Convergence proofs.** If the NTK stays positive definite, a convex loss converges to
    its global minimum, which gave the early global-convergence results for wide networks
    (Du et al. 2019, Allen-Zhu et al. 2019).
- **Limitation: no feature learning.** Because the kernel is fixed, an infinite-width network
  in this regime learns no representations. Other scalings allow feature learning
  (mean-field: Mei–Montanari–Nguyen 2018, Chizat & Bach 2018; μP: Yang & Hu 2021), and the
  neural tangent hierarchy (Huang & Yau 2019) describes finite-width corrections.
- **Software.** Neural Tangents (Google) for exact infinite-width NTK/NNGP inference;
  scikit-ntk for an NTK Gaussian-process kernel in scikit-learn.

## Read with care

- **A Wikipedia article can change.** The permanent link above pins the version read here.
  Check equations against Jacot et al. (2018) and Lee et al. (2019) before quoting them.
- **The "always interpolates" result is a warning for noisy targets.** Ridgeless kernel
  regression fits every training label exactly. On returns, where most of each label is
  noise, that means fitting the noise unless training is stopped early or a ridge term is
  added.

## Why it's in the library

**It is the quickest map of the NTK literature**, from the definition through convergence,
generalisation and the feature-learning debate, with the key papers on each.

**It makes the "is my network just a kernel?" check concrete.** A kernel ridge regression
with the network's NTK (one call in Neural Tangents) is the baseline a trained network has
to beat before it can claim to have learned features. If it doesn't beat it, the model is
in the lazy regime and a cheaper kernel method would do.

## Links

- [[nikolaou-et-al-2026-spectral-reach-neural-scaling-as-progress-into-the-spectral-tail]]
  — empirical NTK spectra during training; feature learning extends reach into the tail
- [[zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization]] — networks
  interpolate even random labels; the experiment behind the interpolation debate
- [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]] — the
  linearisation and Gaussian-process results this article summarises
- [[kernel-pca]] — kernel methods and feature maps
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — the smoothness bias of networks on tabular data
- [[conklin-et-al-2026-learning-is-forgetting]] — representation change during training,
  the feature-learning side of the debate
