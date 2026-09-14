# Kernel PCA

| | |
|---|---|
| **Source** | [Unraveling the Mysteries of Kernel PCA: A Leap Beyond Conventional PCA](https://medium.com/@juanc.olamendy/unraveling-the-mysteries-of-kernel-pca-a-leap-beyond-conventional-pca-bb0f0ef8cf13) — Juan C. Olamendy, Dec 2023 |
| **Primary reference** | Schölkopf, Smola & Müller (1998), *Nonlinear Component Analysis as a Kernel Eigenvalue Problem*, Neural Computation 10(5) |
| **Status** | To read |

## What it is

PCA finds directions of maximum variance — but only **linear** ones. Kernel PCA performs
the same operation in a feature space induced by a kernel, so the directions it recovers are
linear *there* and curved in the original space.

The mechanism is the kernel trick. Map $x \mapsto \varphi(x)$ into a high- (possibly
infinite-) dimensional space, but never compute $\varphi$. Instead eigendecompose the
centred Gram matrix

$$K_{ij} = k(x_i, x_j)$$

whose entries are kernel evaluations between pairs of *observations*. Common choices are the
Gaussian/RBF kernel, polynomial, and sigmoid. Principal components come out as expansions in
kernel evaluations, which means — unlike t-SNE or UMAP — **kernel PCA has a genuine
out-of-sample projection.**

## Why it's in the library

It bears directly on a distinction the market-structure work has to get right: **linear PCA
and RMT measure a linear *subspace*; "manifold" implies something possibly curved.** If
equity return structure is genuinely nonlinear, the linear rank *overstates* the true
dimension, and the eigenvalue count is an upper bound rather than the answer. Kernel PCA is
one of the standard ways to check that.

## ⚠️ The catch that matters most

**Going nonlinear costs you the null hypothesis.**

The entire rigour of the Marchenko–Pastur approach is that there is a closed-form
distribution for the eigenvalues of a *pure-noise* correlation matrix, so "more structure
than chance" is testable. **There is no comparable, well-established null for the spectrum
of a kernel matrix.** Kernel eigenvalues will always show decay, and without a noise
benchmark you cannot say how much of it is real.

So kernel PCA can suggest that structure is curved. It cannot, on its own, tell you the
curved structure is more than sampling artefact — which is precisely the discipline the
linear analysis was built to enforce.

Secondary caveats:

- **Hyperparameters.** Kernel choice and bandwidth are free parameters, tuned on the same
  data the result is read from. Classic overfitting surface.
- **Scaling.** The Gram matrix is *n_samples × n_samples*, so cost grows with the length of
  the sample, not the number of assets — the opposite of ordinary PCA's bottleneck.
- **Interpretability.** Components are expansions in kernel evaluations, not weights on
  assets. There is no "eigenportfolio" to read economically, so the sector-identification
  and macro-coupling analysis that makes linear modes meaningful has no direct analogue.

## Links

- [[coifman-lafon-2006]] — diffusion maps, the other nonlinear method with out-of-sample
  extension and stronger theoretical grounding
- [[facco-et-al-2017]] — intrinsic-dimension estimation, the cheaper way to ask whether the
  nonlinear dimension is lower than the linear rank
- [[marchenko-pastur-1967]] — the null that kernel methods give up
