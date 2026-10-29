# Dimensionality reduction and machine learning

Methods for finding low-dimensional structure in high-dimensional data, starting from PCA
and moving beyond it. PCA is the baseline: its eigenvectors are the principal axes from
`../mathematical-foundations/linear-algebra-and-eigenvectors/`. Each folder relaxes
one of its assumptions.

| Folder | What it relaxes |
|---|---|
| `component-analysis` | *Uncorrelated* → *independent* (ICA), and *linear* → *curved* (kernel PCA) |
| `manifolds-and-intrinsic-dimension` | Structure as a manifold rather than a subspace: diffusion maps, estimators of how many dimensions the data really has (MLE, two-NN) and evidence that it varies across parts of the data (the union of manifolds hypothesis) along with a method that clusters the separate manifolds and embeds each one (SMCE), why it matters for nearest-neighbour methods (distance concentration), how tree-like the data is (δ-hyperbolicity, tree and hyperbolic embeddings), and controlled benchmarks for measuring curvature and reach and testing manifold-fitting rates |
| `quantum-cognition-ml` | Data as states in a Hilbert space (Qognitive's QCML programme and its cognitive-science foundation) |
| `information-bottleneck-and-compression` | *Keep the variance* → *keep what predicts the target*: the Information Bottleneck, measured on LLMs as they train |
| `tree-ensembles-and-tabular-data` | *Learn a representation first* → *split on the raw features*: gradient-boosted trees against deep nets on tabular data and on windowed time series, forests that split on contiguous patches of structured inputs, and forests for curved (hyperbolic, spherical, product-manifold) embeddings |
| `deep-learning-theory` | *A network learns features* → *a wide network is a fixed kernel*: the neural tangent kernel, lazy vs rich (µP) training, finite-width fluctuations; why networks that can memorise random labels still generalise; scaling as learning from the NTK spectral tail; Hessian, gradient and weight spectra explained by neural collapse; depth separation, where one extra layer can beat exponential width |
| `commonsense-reasoning-and-language-models` | *Choose from fixed labels* → *generate an explanation*: why common sense defeated logic-based AI, defeasible and abductive inference, and language models as the representation (COMET, ATOMIC) |
| `energy-based-models-and-self-supervised-learning` | *Predict the output* → *predict a representation of it*: the 2013 review of representation learning (autoencoders, Boltzmann machines, manifold learning, disentangling factors), energy-based models, collapse and how contrastive or regularised training prevents it, and LeCun's joint embedding predictive architecture (JEPA) |
| `ml-trading-strategies` | *Predict each return* → *learn the portfolio*: end-to-end training on net-of-cost Sharpe for futures, and an intraday decision-tree paper kept as a backtest-audit example |

The finance-specific nonlinear factor models (IPCA, autoencoders) are in
`../factor-models-and-asset-pricing/machine-learning-factor-models/`. They are the
benchmark that any method here has to beat on returns.
