# Dimensionality reduction and machine learning

Methods for finding low-dimensional structure in high-dimensional data, starting from PCA
and moving beyond it. PCA is the baseline: its eigenvectors are the principal axes from
`../01-mathematical-foundations/03-linear-algebra-and-eigenvectors/`. Each folder relaxes
one of its assumptions.

| Folder | What it relaxes |
|---|---|
| `01-component-analysis` | *Uncorrelated* → *independent* (ICA), and *linear* → *curved* (kernel PCA) |
| `02-manifolds-and-intrinsic-dimension` | Structure as a manifold rather than a subspace: diffusion maps, and estimators of how many dimensions the data really has (MLE, two-NN) |
| `03-quantum-cognition-ml` | Data as states in a Hilbert space (Qognitive's QCML programme and its cognitive-science foundation) |

The finance-specific nonlinear factor models (IPCA, autoencoders) are in
`../02-factor-models-and-asset-pricing/06-machine-learning-factor-models/`. They are the
benchmark that any method here has to beat on returns.
