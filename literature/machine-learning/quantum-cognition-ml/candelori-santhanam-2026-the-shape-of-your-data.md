# The Shape of Your Data (Data Cleaning White Paper)

| | |
|---|---|
| **Authors** | Luca Candelori, Nag Santhanam (Qognitive, Inc.) |
| **Year** | 2026 |
| **Type** | White paper — Qognitive, 7pp. Not peer-reviewed |
| **Link** | [qognitiveai.com/papers/Data_Cleaning_Whitepaper.pdf](https://www.qognitiveai.com/papers/Data_Cleaning_Whitepaper.pdf) |
| **Find it** | Use the link above, or [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Shape+of+Your+Data+%28Data+Cleaning+White+Paper%29%22+Candelori) for the title and authors |
| **BibTeX** | `candelori2026shape` |
| **Status** | Reference — short; pp. 3–5 (energy, the Hilbert-space dimension, imputation as energy minimisation) carry the method |

## What it is

Qognitive's pitch for using QCML to fill in missing values and flag anomalies in tabular
data. The argument: real data sit near a low-dimensional manifold (the manifold
hypothesis), so a missing value should be inferred from the global shape of the data, not
patched from nearby records or column averages.

- **Imputation as energy minimisation.** An energy-based model (EBM) gives every possible
  input a score: low on the data, high away from it. To fill a gap, choose the missing
  coordinates that give the lowest energy, given the ones observed. Points with high
  energy are anomalies.
- **The problem with ordinary EBMs.** Training them by maximum likelihood needs the
  normalising constant Z, an integral of e^(−E(x)) over all inputs, which is intractable
  when E is a generic neural network. They fall back on contrastive divergence or score
  matching, which are hard to scale, and on mixed continuous and categorical tabular data
  few EBMs exist at all (TabEBM is the example given).
- **The QCML version.** Each data point is a quantum state, a vector in a small Hilbert
  space; each feature is an operator (an observable). States and operators are learned
  together. A state's energy is built to be proportional to its squared distance from the
  data, so far from the data the energy grows like ‖x‖²/2 and Z is finite (it behaves like
  a Gaussian). Imputation then finds the state that minimises the energy of the
  partially observed point and reads off its expected position.
- **Small Hilbert spaces.** The 2D examples need a 16-dimensional space (4 qubits) and train
  in seconds on a laptop. The authors say 8–32 dimensions suffice for the financial and
  other datasets in their published work, and that they have trained on genetics data
  with 20,000 features.
- **Multi-modal imputation.** On the two half-moons with half the coordinates removed, a
  deep autoencoder fills gaps with values between the two arcs (it minimises squared
  error, so it averages). The QCML imputation snaps each point onto one arc or the other.
- **Categorical data.** Swapping Euclidean distance for cross-entropy on categorical
  features lets one model handle both kinds; a toy example with two 20-level categorical
  variables arranged in a ring is imputed correctly.
- **Claims without numbers.** The paper also claims linear scaling in the number of
  features, against exponential for MICE (chained-equations imputation), and that
  correlated features need no special handling. The authors state that they deliberately
  leave out benchmarks: the evidence is the 2D figures.

## Why it's in the library

**Imputation by projection onto the data's shape is the right idea, whoever implements
it.** Mean-filling and column-by-column regression ignore the joint structure; an
autoencoder trained on squared error averages across modes. Choosing the value most
consistent with the whole record is the principle, and the half-moons figure is a clean
picture of why averaging fails when the data have more than one mode.

**It ties together two threads already in the library.** The energy-based view of
[[dawid-lecun-2023-introduction-to-latent-variable-energy-based-models]] and the
manifold view in `../../high-dimensional-geometry/` meet here: low energy means on the
manifold, and distance from it is both the anomaly score and the imputation criterion.

**It shows how the QCML programme is being productised.** The intrinsic-dimension paper
[[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] is the
peer-reviewed method; this is the commercial application. The scaling and accuracy claims
would need a benchmark against MICE, k-nearest-neighbour imputation and an autoencoder on
real data before they count as results.

## Links

- [[samson-et-al-2024-quantum-cognition-machine-learning-financial-forecasting]] — the
  same model applied to forecasting US stock returns
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — the
  peer-reviewed QCML method this builds on, applied to intrinsic dimension
- [[dawid-lecun-2023-introduction-to-latent-variable-energy-based-models]] — energy-based
  models, the framework used here, and their training difficulties
- [[busemeyer-bruza-2012]] — the Hilbert-space cognition models behind QCML
- [[fefferman-mitter-narayanan-2016-testing-the-manifold-hypothesis]] — what "the data lie
  on a manifold" means formally
- [[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]]
  — why models built from connected noise fill in the gap between separate modes, the
  same failure the half-moons figure shows for autoencoders
- [[freytsis-perelstein-san-2024-anomaly-detection-in-the-presence-of-irrelevant-features]]
  — density-based anomaly detection with trees, an alternative to an energy landscape
- [[gu-kelly-xiu-2021]] — the nonlinear latent-factor benchmark QCML has to beat in finance
