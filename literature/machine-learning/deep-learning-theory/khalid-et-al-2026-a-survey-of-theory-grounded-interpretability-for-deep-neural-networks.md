# A Survey of Theory-Grounded Interpretability for Deep Neural Networks

| | |
|---|---|
| **Authors** | Muhammad Usman Khalid, Abeer A. K. Alharbi, Shariq Bashir, Shafiq ur Rehman (Imam Mohammad Ibn Saud Islamic University, Riyadh) |
| **Year** | 2026 |
| **Type** | Survey — *Journal of King Saud University Computer and Information Sciences* 38, article 835 (2026), doi:10.1007/s44443-026-01061-2, 49pp |
| **PDF** | `khalid-et-al-2026-a-survey-of-theory-grounded-interpretability-for-deep-neural-networks.pdf` (in this folder; the published version, open access under CC BY 4.0) |
| **Link** | [Journal page (open access)](https://doi.org/10.1007/s44443-026-01061-2) |
| **BibTeX** | `khalid2026survey` |
| **Status** | Reference — read the framing, the four critical-analysis sections and the conclusion; skimmed the application catalogues |

## What it is

A systematic review of 203 papers (2016–2026) that explain *why* deep networks learn what they
learn using four classical theories, rather than using post-hoc tools like SHAP or saliency maps.
The corpus came from a PRISMA-style search of Web of Science, Scopus and IEEE Xplore (3,310
records after filters, 179 kept after full-text screening, plus 24 from citation tracking).

The four lenses, with their share of the corpus:
- **Kernel methods / neural tangent kernel (40%).** Wide networks near initialisation behave
  like kernel regression, which gives convergence and generalisation guarantees and a spectral
  account of which functions are learned first. The catch is that real networks train in the
  rich, feature-learning regime, where the kernel moves and the guarantees no longer hold.
- **Sparse representations (29%).** Algorithm unrolling (LISTA and its descendants) turns an
  iterative sparse-coding solver into network layers, giving networks that are interpretable by
  design. Sparse autoencoders on language models are mentioned as a related but theoretically
  separate line.
- **Matrix factorisation (23%).** Gradient descent on factorised and deep linear models has an
  implicit bias toward low rank that norm minimisation does not fully capture. Extensions cover
  tensor factorisation (depth induces locality bias in CNNs), dropout as nuclear-norm
  regularisation, and NMF for concept-based explanations.
- **Manifold learning (8%).** Classification capacity explained by manifold radius,
  dimension and correlation shrinking through the layers; error rates governed by intrinsic
  rather than ambient dimension; curvature linked to long-tail bias and adversarial examples.

The synthesis argues that the four are views of one phenomenon: gradient-based training tends
to push networks toward low-complexity structure (minimum norm, sparsity, low rank, low
intrinsic dimension). It names three bridges: sparse coding is matrix factorisation with an L1
penalty; NTK and manifold analyses both read learned geometry off eigendecompositions; low rank
corresponds to low intrinsic manifold dimension.

## Why it's in the library

**It is a map of the theory side of this folder.** The kernel section covers the lazy-regime
results already here ([[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]],
[[wikipedia-neural-tangent-kernel]], [[bordelon-pehlevan-2023-dynamics-of-finite-width-kernel-and-prediction-fluctuations-in-mean-field-neural-networks]]),
and its main caveat, that practical networks live in the rich regime, is the lazy/rich split of
[[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]] and
[[geiger-petrini-wyart-2021-landscape-and-training-regimes-in-deep-learning]]. The manifold
section leans on the manifold hypothesis that
[[fefferman-mitter-narayanan-2016-testing-the-manifold-hypothesis]] tries to test.

**Its most useful line is the stated tension:** the theories with the strongest guarantees
(infinite-width NTK) apply to the least realistic networks, and the most practical tools
(unrolling, sparse autoencoders) have the weakest theory. Each framework's section ends with a
"best suited to" statement and a list of failure modes, which is a quick way to check whether a
given theoretical explanation applies to a given model.

**Limits.** It is a literature synthesis with no new results; the "unifying" bridges are
analogies argued in prose rather than theorems. Inclusion used citation-count thresholds, which
favour established lines of work, and a large share of the sparse-coding and factorisation
material is signal-processing applications (image reconstruction, hyperspectral imaging) far
from tabular or financial data.

## Links

- [[geiger-petrini-wyart-2021-landscape-and-training-regimes-in-deep-learning]] — the lazy
  versus feature-learning phase diagram behind this survey's main NTK caveat
- [[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]] — the lazy/rich
  regimes derived from scaling arguments
- [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]] — the
  infinite-width linearisation the kernel section is built on
- [[wikipedia-neural-tangent-kernel]] — the kernel itself
- [[bordelon-pehlevan-2023-dynamics-of-finite-width-kernel-and-prediction-fluctuations-in-mean-field-neural-networks]]
  — finite-width corrections, one of the survey's named open problems
- [[nikolaou-et-al-2026-spectral-reach-neural-scaling-as-progress-into-the-spectral-tail]] —
  learning order from the kernel spectrum
- [[garrod-keating-2026-unifying-low-dimensional-spectra-in-deep-learning]] — low-rank
  spectra and neural collapse, the factorisation section's terminal-phase story
- [[fefferman-mitter-narayanan-2016-testing-the-manifold-hypothesis]] — whether the manifold
  hypothesis holds, the manifold section's stated weak point
- [[elhamifar-vidal-2011-sparse-manifold-clustering-and-embedding]] — sparse coding and
  manifold learning in one method
- [[lei-et-al-2020-a-geometric-understanding-of-deep-learning]] — the optimal-transport view of GANs this survey cites under manifold learning
