# Robust Estimation of the Intrinsic Dimension of Data Sets with Quantum Cognition Machine Learning

| | |
|---|---|
| **Authors** | Luca Candelori; Alexander G. Abanov; Jeffrey Berger; Cameron J. Hogan; Vahagn Kirakosyan; Kharen Musaelian; Ryan Samson; James E. T. Smith; Dario Villani; Martin T. Wells; Mengjia Xu (Qognitive, Wayne State, Stony Brook, Cornell, NJIT, MIT, King's College London) |
| **Year** | 2025 |
| **Type** | Paper — *Scientific Reports* 15, 6933. Open access, CC BY-NC-ND 4.0. DOI 10.1038/s41598-025-91676-8 |
| **PDF** | `candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml.pdf` (in this folder) |
| **BibTeX** | `candelori2025robust` |
| **Status** | To read |

## What it is

A new intrinsic-dimension estimator built on QCML. Of the Qognitive papers, it makes the
claim that is easiest to check directly against classical methods.

- **Model the whole data manifold first.** For data with D features, train D Hermitian
  N × N matrices A₁…A_D (a "matrix configuration"). Each point x gets a quantum state ψ₀(x):
  the ground state of the error Hamiltonian H(x) = ½ Σ (A_k − x_k·I)². The state's expected
  position A(ψ₀(x)) gives a cleaned-up point cloud X_A. Because the matrices are fitted to all
  the data, each point's representation carries global information rather than only its
  neighbourhood.
- **The loss is bias-only.** The ground-state energy splits into squared distance plus
  quantum fluctuation, which is a bias–variance split. Minimising the full energy pushes the
  matrices to commute, which collapses the model into N-means clustering. So they minimise
  only the distance term, with an optional weight w on the fluctuation term.
- **Read the dimension off a spectral gap.** At each point the *quantum metric* g(x), a D × D
  positive semi-definite matrix computed by perturbation theory, has eigenvalues near 1 in
  directions along the manifold and near 0 across it. The estimate d is the location of the
  largest gap in that spectrum. A random-matrix (Marchenko–Pastur hard-threshold) rule is
  offered as an alternative. The rank of g is at most 2(N − 1), so N has to be large enough.
- **Results:**
  - On a noisy sphere it gives d = 2 at every noise level up to 0.2 and every sample size
    tried (250, 2,500 and 25,000 points). DANCo, MLE, CorrInt and TwoNN drift to 3, treating
    the noise as a "shadow dimension".
  - On the hard synthetic benchmarks (M10b, Mβ, M_N1) it is flat in noise. The classical
    estimators first underestimate (sparse data in high dimension) and then overestimate as
    noise grows.
  - ISOMAP faces give d = 3. MNIST digit "1" gives 9–12, depending on N. The Wisconsin
    breast-cancer data gives d = 2 at every noise level, against published estimates of
    3.5–6.
- **Proposed change to benchmarking:** test estimators on noise robustness rather than on
  ever more curved, noise-free synthetic manifolds.

## Why it's in the library

- **It gives a third answer to a question two notes already ask.** [[levina-bickel-2004]]
  (maximum likelihood) and [[facco-et-al-2017]] (TwoNN) are both local nearest-neighbour
  estimators, which are exactly what this paper claims noise breaks. Running all three on the
  same noisy return or feature panel is a concrete experiment. A real market panel is the
  noisy case the paper says matters.
- **Shadow dimensions are a real risk with financial data.** Noise that inflates estimated
  dimension also inflates how many factors you think you need. The useful question is whether
  an estimate stays put as noise is added, not just what number it gives.
- **It is the clearest written account of the QCML machinery** — matrix configurations,
  quasi-coherent states and the bias-only loss — that the finance papers in this folder take
  as given.

## Links

- [[levina-bickel-2004]], [[facco-et-al-2017]] — the classical estimators it benchmarks
  against (MLE and TwoNN)
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — why nearest-neighbour methods
  struggle in high dimension, which is the failure this paper exploits
- [[busemeyer-bruza-2012]] — the Hilbert-space cognition models QCML builds on
- [[gu-kelly-xiu-2021]] — the nonlinear latent-factor benchmark QCML has to beat in finance
