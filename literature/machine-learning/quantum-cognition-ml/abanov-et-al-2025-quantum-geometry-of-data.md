# Quantum Geometry of Data

| | |
|---|---|
| **Authors** | Alexander G. Abanov, Luca Candelori, Harold C. Steinacker, Martin T. Wells, Jerome R. Busemeyer, Cameron J. Hogan, Vahagn Kirakosyan, Nicola Marzari, Sunil Pinnamaneni, Dario Villani, Mengjia Xu, Kharen Musaelian (Qognitive; Stony Brook; Wayne State; Vienna; Cornell; Indiana; EPFL; King's College London; NJIT; MIT) |
| **Year** | 2025 |
| **Type** | Preprint — arXiv:2507.21135, July 2025, 31pp. The PDF here is a later revision hosted by Qognitive (adds a timing check, a two-spheres stability study and a classical comparison on the breast-cancer data). Not peer-reviewed |
| **Link** | [arxiv.org/abs/2507.21135](https://arxiv.org/abs/2507.21135); revised PDF at [qognitiveai.com/papers/quantum-geometry.pdf](https://www.qognitiveai.com/papers/quantum-geometry.pdf); code and trained operators at [github.com/camhogan/Quantum_Geometry_of_Data](https://github.com/camhogan/Quantum_Geometry_of_Data) |
| **BibTeX** | `abanov2025geometry` |
| **Status** | Reference — §3 (the model), §4.1–4.4 (the geometric tools) and §5.4 (the real-data example) carry the paper; §4 can be skimmed on a first pass |

## What it is

The full mathematical write-up of QCML. It shows that the matrices QCML learns define a
*matrix* (or *fuzzy*) geometry of the kind studied in mathematical physics, and turns the
tools of that field into data-analysis diagnostics: intrinsic dimension, connectivity,
curvature and topological invariants. The authors say plainly that this is a new
representation, not a benchmarked algorithm.

- **The model.** A dataset of T points with D features. Each feature a gets a learned
  N × N Hermitian matrix X_a (N is small, often 8). For a data point x, the displacement
  Hamiltonian is H(x) = ½ Σ_a (X_a − x_a I)², and the point is represented by its ground
  state |x⟩ (the eigenvector with the lowest eigenvalue), called a quasi-coherent state.
  The point's image is the vector of expectations ⟨x|X_a|x⟩.
- **The loss.** Training minimises the squared gap between each point and its image, plus
  w times the spread (variance) of the observables in that state. w sets the resolution.
  Too large a w pushes the matrices to commute, and then the model collapses to N-means
  clustering with N centroids; small w gives smoother, more "quantum" geometries. There is
  no rule for picking w.
- **The geometric tools.**
  - *Quantum metric and Berry curvature.* The quasi-coherent states sit in complex
    projective space, which gives every point a metric (how fast the state changes as x
    moves) and a curvature. Counting the large eigenvalues of the metric gives a local
    intrinsic dimension, as in the earlier Candelori et al. paper.
  - *Chern numbers.* Where the ground state becomes degenerate, the curvature has
    point-like sources ("monopoles") with integer charges, found by integrating the
    curvature over a small sphere around them. These are topological invariants of the
    learned geometry.
  - *Matrix Laplacian.* Δ = Σ_a [X_a, [X_a, ·]], the matrix analogue of the
    Laplace–Beltrami operator. Its near-zero eigenvalues count disconnected pieces, the
    growth of its eigenvalue count (Weyl's law, N(λ) ~ λ^(d/2)) gives a global dimension,
    and its low eigenvectors (eigenmaps) give a smooth low-dimensional embedding, the
    matrix counterpart of Laplacian eigenmaps and diffusion maps.
- **Size.** For fixed N, the parameter count and training cost grow linearly in D (the
  total is DN² + 2T(N − 1) real numbers). One run on a 2,000 × 200 dataset with N = 8
  took 5.4 minutes on a laptop CPU.
- **Synthetic checks.** On a uniform sphere with N = 4, the learned matrices are close to
  the textbook fuzzy sphere (angular-momentum matrices), and the Laplacian spectrum
  matches the exact one. On two noisy spheres, two near-zero Laplacian eigenvalues show
  two components, and a seventh monopole flags a noise-made "neck" between them. On a
  non-uniform sphere, the learned surface is less certain where data are sparse. On 2,000
  conformal maps of the disk encoded as 200-dimensional vectors, the metric shows a clear
  gap after two eigenvalues (true dimension 2), and the first two eigenmaps recover the
  map's complex parameter without being told it. The same works for maps of balls in
  C² to C⁵.
- **Breast-cancer data (569 samples, 30 features, N = 8).** The estimated dimension falls
  as w rises: 7, 5, 4, 3, 2, 1 for w = 0.02, 0.05, 0.10, 0.20, 0.50, 0.80. Classical rules
  give a similar spread (2 to 17 depending on the criterion), so neither picks one answer;
  w at least has a geometric meaning. Three eigenmaps, learned without labels, reach 0.960
  AUC and 0.885 accuracy separating benign from malignant; three principal components
  reach 0.990 and 0.948, and all 30 features 0.992 and 0.962. The authors' own verdict:
  the example supports claims about representation, not diagnostic advantage. At
  w = 0.5 the Laplacian suggests three components, but this may be the early collapse to
  clustering, so they call it provisional.

## Why it's in the library

**It is the reference text for the whole QCML programme.** The other QCML papers here
(the forecasting white paper, the intrinsic-dimension paper, the imputation white paper)
all use this ground-state model; this paper defines it fully and shows what the learned
matrices mean geometrically.

**It is unusually honest about its limits.** The PCA comparison is reported even though
PCA wins at the same dimension, the dimension estimate is shown to depend on w across a
wide range, and the three-cluster reading is flagged as possibly an artefact. Those are
the right checks to carry over to any use of these tools.

**The connection to known methods is explicit.** In the commuting limit QCML is N-means
clustering. Its Laplacian eigenmaps are a matrix version of graph Laplacian eigenmaps and
diffusion maps ([[coifman-lafon-2006]]). Its dimension estimate targets the same quantity
as [[levina-bickel-2004-maximum-likelihood-estimation-of-intrinsic-dimension]]. So it can
be tested against those baselines directly rather than taken on its own terms.

**The resolution parameter is a useful idea in itself.** Intrinsic dimension depends on
the scale it is measured at. Here that scale is one explicit parameter, and sweeping it
shows how the data look at different resolutions: the same lesson as running the MLE
estimator at several neighbour counts.

## Links

- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — the
  quantum-metric dimension estimate used here, introduced and tested
- [[musaelian-et-al-2024-quantum-cognition-machine-learning-ai-needs-quantum]] — the
  first description of QCML, which this paper formalises
- [[samson-et-al-2024-quantum-cognition-machine-learning-financial-forecasting]] — the
  same model applied to stock-return forecasting
- [[candelori-santhanam-2026-the-shape-of-your-data]] — the same model applied to
  imputation and anomaly detection
- [[candelori-et-al-2026-shallow-circuit-supervised-learning-on-a-quantum-processor]] —
  running QCML-style models on quantum hardware
- [[busemeyer-bruza-2012]] — the quantum-cognition models QCML is named after;
  Busemeyer is a co-author here
- [[coifman-lafon-2006]] — diffusion maps, the graph-based counterpart of the matrix
  Laplacian eigenmaps
- [[levina-bickel-2004-maximum-likelihood-estimation-of-intrinsic-dimension]] — the
  classical intrinsic-dimension estimator to compare against
- [[fefferman-mitter-narayanan-2016-testing-the-manifold-hypothesis]] — what fitting a
  manifold to data means formally
