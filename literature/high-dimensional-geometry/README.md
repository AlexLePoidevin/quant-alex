# High-dimensional geometry

What data looks like when it has many features, and how to find the few dimensions that
actually matter. Intuition built in two or three dimensions fails here: volume moves to
the corners, distances bunch together, a few points become everyone's nearest neighbour.
The same data usually lies near something much lower-dimensional, and the methods here
measure that structure and work on it directly.

PCA is the baseline. Its eigenvectors are the principal axes from
`../mathematical-foundations/linear-algebra-and-eigenvectors/`.

| Folder | What's in it |
|---|---|
| `curse-of-dimensionality` | Why nearest-neighbour methods break as dimension grows: distance concentration (Beyer et al.), how the choice of norm changes the rate (Aggarwal et al.), hubs that dominate neighbour lists (Radovanović et al.), the argument that they come from density gradients rather than dimension (Low et al.), a benchmark of the fixes for them (Feldbauer & Flexer), a two-page primer on the separate curses, and two blog explainers of where the volume goes and why distances bunch together |
| `intrinsic-dimension` | How many dimensions the data really has: what testing the manifold hypothesis means and costs (Fefferman et al.), the MLE and two-NN estimators, evidence that the number varies across parts of the data (the union of manifolds hypothesis), and controlled benchmarks for measuring curvature and reach and testing manifold-fitting rates |
| `manifold-learning-and-embeddings` | Working on the manifold instead of in the ambient space: diffusion maps, clustering separate manifolds and embedding each one (SMCE), how tree-like the data is (δ-hyperbolicity, tree and hyperbolic embeddings), geometric deep learning, and an optimal-transport view of generative models (why GANs drop modes) and piecewise-linear limits on which manifolds a ReLU autoencoder can flatten |
| `component-analysis` | Linear reduction beyond PCA: *uncorrelated* → *independent* (ICA), and *linear* → *curved* (kernel PCA) |

A QCML estimator of intrinsic dimension sits with the rest of that programme in
`../machine-learning/quantum-cognition-ml/`. The finance-specific nonlinear factor models
(IPCA, autoencoders) are in `../factor-models-and-asset-pricing/machine-learning-factor-models/`.
