# Machine learning

Model families and the theory of why they work: what a neural network actually learns,
when trees beat deep nets, and how representations are learned and
compressed.

| Folder | What's in it |
|---|---|
| `deep-learning-theory` | *A network learns features* → *a wide network is a fixed kernel*: the neural tangent kernel, lazy vs rich (µP) training, finite-width fluctuations; why networks that can memorise random labels still generalise; scaling as learning from the NTK spectral tail; Hessian, gradient and weight spectra explained by neural collapse; depth separation, where one extra layer can beat exponential width; the jamming transition and the lazy-versus-feature-learning phase diagram; a survey of kernel, sparse-coding, matrix-factorisation and manifold explanations of what networks learn |
| `tree-ensembles-and-tabular-data` | *Learn a representation first* → *split on the raw features*: gradient-boosted trees against deep nets on tabular data and on windowed time series, a proof of what a single tree cannot generalise to and why sums of trees do better, why CART has small bias and what MDI feature importance measures, a controlled test of trees and networks when most features are pure noise, forests that split on contiguous patches of structured inputs, and forests for curved (hyperbolic, spherical, product-manifold) embeddings |
| `representation-learning` | What a model should keep: the 2013 review of representation learning (autoencoders, Boltzmann machines, manifold learning, disentangling factors), energy-based models and LeCun's joint embedding predictive architecture (JEPA), the Information Bottleneck measured on LLMs as they train, and common sense as a representation problem for language models (COMET, ATOMIC) |
| `quantum-cognition-ml` | Data as states in a Hilbert space (Qognitive's QCML programme and its cognitive-science foundation) |

The geometry these models run into (the curse of dimensionality, intrinsic dimension,
manifold learning, PCA and ICA) is in `../high-dimensional-geometry/`. The finance-specific
nonlinear factor models (IPCA, autoencoders) are in
`../factor-models-and-asset-pricing/machine-learning-factor-models/`. They are the
benchmark that any method here has to beat on returns.
