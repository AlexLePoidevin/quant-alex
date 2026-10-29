# The Data Manifold under the Microscope

| | |
|---|---|
| **Authors** | Marios Koulakis (independent researcher), Constantin Seibold (Diagnostic and Interventional Radiology, University Clinic Heidelberg) |
| **Year** | 2026 |
| **Type** | Conference paper — ICML 2026 (poster); arXiv:2606.15760v1, CC BY 4.0 |
| **PDF** | `koulakis-seibold-2026-the-data-manifold-under-the-microscope.pdf` (in this folder; the arXiv paper) |
| **Slides** | [ICML 2026 talk slides with speaker script](https://icml.cc/media/icml-2026/Slides/66403.pdf) — not committed |
| **Code** | [github.com/koulakis/manifold-microscope](https://github.com/koulakis/manifold-microscope) |
| **BibTeX** | `koulakis2026data` |
| **Status** | Reference — §3 (definitions) and §5 (the two use cases); the slides are a 10-minute summary |

## What it is

A benchmark for the **manifold hypothesis**: the idea that high-dimensional data sit
near a low-dimensional curved surface. Theory about learning such surfaces depends on
quantities like intrinsic dimension, curvature and **reach** (how close the surface
comes to touching itself), but on real data these can only be guessed. The paper
builds image data sets where they can be measured almost exactly.

- **Controlled image manifolds.** Two disentanglement data sets are re-rendered on
  dense, regular grids of known transformations: dSprites (scale, rotation, x, y;
  d = 4) and COIL-20 (view angle, rotation, scale; d = 3), both as 64×64 images
  (D = 4096). The grid is a known chart from a few parameters to pixel space.
- **Geometry by finite differences.** Because the grid is known, tangent vectors are
  just differences between neighbouring images. From them come the metric, volume,
  scalar curvature, reach and distances between classes. On manifolds with known
  curvature this beats a general-purpose curvature estimator, even when that
  estimator is given its best radius at every point.
- **Use case 1 — do the theoretical rates hold?** Manifold-fitting theory gives the
  rate at which error falls with sample size n. The authors fit the manifold from
  1% to 100% of the data, using moving least squares (MMLS) or a β-VAE, and fit a
  power law to the error. The Fefferman et al. rate, roughly n^(−1/d), matches the
  observed slope better than the Genovese et al. rate. The β-VAE curve is flatter: it
  is not learning the surface as efficiently as a simple local fit.
- **Use case 2 — geometry inside a β-VAE.** Layer by layer, curvature rises, reach
  falls and classes move further apart towards the latent space. The network separates
  classes at the cost of a more folded intermediate surface.

## Read with care

- **A testbed, not a tool for real data.** The method needs a known grid of
  transformations and works only up to about 4–5 intrinsic dimensions and simple
  shapes (boxes times circles). It cannot be pointed at an arbitrary data set.
- **The bounds are fitted after the fact.** "Closer to Fefferman" compares slopes
  only. The theoretical constants are chosen to wrap the empirical curves, so nothing
  here tests the bounds' actual size.
- **Small experiments.** Three repetitions per sample size, two data sets, one
  architecture family. Fine grids on fixed-resolution images also create aliasing
  that distorts curvature.
- **New and unreplicated.** A first version (v1, June 2026) with no independent
  follow-up yet; no finance data.

## Why it's in the library

**It gives the sample-size cost of learning a manifold.** Error that falls like
n^(−1/d) means the data needed grows exponentially with intrinsic dimension. A few
years of daily returns is a few thousand rows, so any nonlinear factor structure we
hope to learn has to be very low-dimensional. That is why the dimension estimates in
[[levina-bickel-2004]] and [[facco-et-al-2017]] matter before fitting anything.

**It is a check on general-purpose estimators.** The authors find standard curvature
estimators unreliable even on easy manifolds. Treat any single estimate of dimension,
curvature or tree-likeness
([[sonthalia-gilbert-2020-tree-i-am-no-tree-i-am-a-low-dimensional-hyperbolic-embedding]])
on noisy market data as rough.

**It questions autoencoders as manifold learners.** The β-VAE did not fit the surface
the way theory expects of an efficient fitter. That is a useful prior for
autoencoder factor models such as [[gu-kelly-xiu-2021]]: do not assume the encoder has
found the underlying structure.

## Links

- [[levina-bickel-2004]], [[facco-et-al-2017]] — intrinsic-dimension estimators, the
  d that sets the sample-size cost here
- [[coifman-lafon-2006]] — diffusion maps, another way of recovering a manifold from samples
- [[sonthalia-gilbert-2020-tree-i-am-no-tree-i-am-a-low-dimensional-hyperbolic-embedding]]
  — measuring another geometric property (tree-likeness) from distances
- [[bronstein-bruna-cohen-velickovic-2021-geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges]]
  — the case for building known geometry into models
- [[gu-kelly-xiu-2021]] — autoencoders as factor models, the finance case of a learned manifold
- [[bengio-courville-vincent-2013-representation-learning-a-review-and-new-perspectives]] — the manifold prior
  and autoencoders as manifold learners, the claims this benchmark tests
