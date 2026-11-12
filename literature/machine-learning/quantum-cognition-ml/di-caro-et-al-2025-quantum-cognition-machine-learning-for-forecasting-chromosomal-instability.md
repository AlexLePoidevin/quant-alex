# Quantum Cognition Machine Learning for Forecasting Chromosomal Instability

| | |
|---|---|
| **Authors** | Giuseppe Di Caro, Vahagn Kirakosyan, Alexander G. Abanov, Luca Candelori, Nadine Hartmann, Ernest T. Lam, Kharen Musaelian, Ryan Samson, Martin T. Wells, Richard J. Wenstrup, Mengjia Xu (Qognitive; Epic Sciences; Stony Brook; Wayne State; Cornell; NJIT) |
| **Year** | 2025 |
| **Type** | Preprint — Qognitive / Epic Sciences, May 2025, 16pp. Not peer-reviewed |
| **Link** | [qognitiveai.com/papers/epic-paper.pdf](https://www.qognitiveai.com/papers/epic-paper.pdf) |
| **Find it** | Use the link above, or [search Google Scholar](https://scholar.google.com/scholar?q=%22Quantum+Cognition+Machine+Learning+for+Forecasting+Chromosomal+Instability%22+Caro) for the title and authors |
| **BibTeX** | `dicaro2025chromosomal` |
| **Status** | Reference — §2.3–2.4 (the supervised QCML model and the POVM extension) and Tables 1–2 carry the content; the rest is the biology |

## What it is

QCML applied to a small, wide medical data set. The task is to predict, from images of
circulating tumour cells (CTCs) taken from the blood of patients with metastatic breast
cancer, whether a cell is genomically unstable. Instability is measured by sequencing as
the number of large-scale state transitions (LST); a cell is called LST+ above 12.

- **The data.** 227 sequenced cells from 73 patients (about 3 per patient, at most 8). Each
  cell has 112 image features: 8 shape features, 44 stain-intensity features and 70 texture
  features. Hyperparameters were tuned on a 166-cell, 51-patient subset; all models were
  then scored by 5-fold cross-validation repeated 5 times on the full 227 cells. Cells are
  treated as independent, so cells from the same patient can sit on both sides of a split.
- **Supervised QCML.** Each feature k is a learned Hermitian matrix A_k and the target is a
  further matrix B. A cell's features define an error Hamiltonian
  H(x) = ½ Σ_k (A_k − x_k·I)², the cell is represented by its ground state |ψ⟩, and the
  forecast is ⟨ψ|B|ψ⟩. Training updates all matrices by gradient descent. The loss mixes an
  L1 regression term with a cross-entropy term on the LST > 12 label, each rescaled to
  equal weight, with the positive class down-weighted to 0.5 to favour specificity (false
  positives are the costly error clinically).
- **QCML POVM, introduced here.** Instead of a point forecast, the model outputs a whole
  probability density for the target: p(y) = ⟨ψ|Y†(y)Y(y)|ψ⟩, with Y(y) expanded in
  Legendre polynomials and learned matrices constrained so the density integrates to 1 (a
  positive operator-valued measure). This gives both a probability that LST exceeds 12 and
  a full predictive distribution.
- **Regression results (Table 1).** Out of sample, QCML has the highest balanced accuracy,
  70% ± 8% (sensitivity 84%, specificity 57%), against 68% ± 7% for a Gaussian-kernel SVM
  and 60–65% for the rest of the ten classical models. XGBoost and the neural network fit
  the training folds almost perfectly (100% and 95% balanced accuracy) and drop to 63% and
  62%; QCML goes from 78% in-sample to 70%.
- **Classification results (Table 2).** QCML POVM has the highest out-of-sample ROC AUC,
  0.763, against 0.747 for XGBoost, 0.744 for random forest and 0.737 for 32-nearest
  neighbours. Balanced accuracies are within a point or two of each other (QCML POVM 67%,
  random forest 67%, XGBoost 66%), with standard deviations of 7–8%.
- **Interpretation.** Gradient-based feature importance picks out DAPI (DNA stain)
  intensity, nuclear size and fractal shape features as signs of instability, which the
  authors match to known biology. A distance between cells defined from their quantum
  states, d = 1 − |⟨ψ₁|ψ₂⟩|², separates unstable from stable cells visibly better than
  Euclidean distance in a 2D multidimensional-scaling plot.
- **Stated next step.** The authors say future studies must validate the findings and
  test whether the predictions relate to patient survival.

## Why it's in the library

**It is the clearest statement of the supervised QCML recipe.** The model (feature matrices,
ground state, target matrix, gradient descent) is written out in full here, more plainly
than in the finance papers, and the POVM section is the method for forecasting a whole
distribution rather than a point. Both carry over directly to any tabular forecasting
problem.

**Small, wide, noisy data is where the claim should be tested.** 227 cells and 112
features is the regime where flexible models overfit: XGBoost and the network fit the
training data almost perfectly and lose 30+ points out of sample. QCML's smaller gap
between in-sample and out-of-sample is the most useful result here, more than its
headline lead.

**The margins are inside the noise.** The leads are 2 points of balanced accuracy and 0.016
of AUC, with fold-to-fold standard deviations of 7–11%, on cells that are not split by
patient and with tuning done on a subset of the evaluation data. Read it as "competitive
with the best classical models on a hard small data set", which is consistent with
[[candelori-santhanam-2025-breaking-the-curse-of-dimensionality-qcml-vs-tree-based-models]]
needing a linear baseline before its gap meant anything.

**The supervised distance is reusable.** Defining similarity from states trained on the
target, rather than raw feature distance, is the same idea the bond and firm-linkage papers
use for finance.

## Links

- [[musaelian-et-al-2024-quantum-cognition-machine-learning-ai-needs-quantum]] — the
  original QCML statement this model follows
- [[abanov-et-al-2025-quantum-geometry-of-data]] — the geometric theory behind the ground
  state representation
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — the
  unsupervised version of the same model, used for intrinsic dimension
- [[samson-et-al-2024-quantum-cognition-machine-learning-financial-forecasting]] — the
  same supervised model on stock returns
- [[rosaler-et-al-2025-supervised-similarity-for-high-yield-bonds]],
  [[samson-et-al-2025-supervised-similarity-for-firm-linkages]] — the target-trained
  state distance, applied to bonds and firms
- [[candelori-et-al-2026-shallow-circuit-supervised-learning-on-a-quantum-processor]] —
  supervised QCML run on quantum hardware
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — the tabular benchmark where tree ensembles usually win
