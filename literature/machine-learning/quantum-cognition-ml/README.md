# Quantum cognition machine learning

The Qognitive research programme: representing data as states in a Hilbert space and
learning a Hamiltonian over them, so that structure is recovered from the geometry of the
state space rather than from a covariance matrix. Quantum-*inspired* and classical to run —
density matrices and POVMs on ordinary hardware — except where a paper says otherwise.

All ten papers below (plus one blog post) were published by Qognitive at
[qognitiveai.com/research](https://www.qognitiveai.com/research/). Several have appeared in
peer-reviewed venues; the PDFs carry the venue where there is one.

For a spoken introduction, Kharen Musaelian's January 2025 IBM Research talk on QCML is
listed under his name in `../../podcasts-and-videos/`.


---

## The programme

| Year | Title | Authors | Link |
|---|---|---|---|
| 2024 | *Quantum Cognition Machine Learning: AI Needs Quantum* — the founding position paper: why classical probability falls short and why represent data in a Hilbert space; no model equations or results; note [[musaelian-et-al-2024-quantum-cognition-machine-learning-ai-needs-quantum]] | Musaelian, Abanov, Berger, Candelori, Kirakosyan, Samson, Smith, Villani | [PDF](https://www.qognitiveai.com/papers/QCML%20-%20Qognitive,%20Inc.pdf) |
| 2025 | *Quantum Geometry of Data* — QCML as matrix geometry: quantum metric, Berry curvature, Chern numbers and matrix-Laplacian eigenmaps, with synthetic checks and a breast-cancer example; arXiv:2507.21135; note [[abanov-et-al-2025-quantum-geometry-of-data]] | Abanov, Candelori, Steinacker, Wells, Busemeyer, Hogan, Kirakosyan, Marzari, Pinnamaneni, Villani, Xu, Musaelian | [PDF](https://www.qognitiveai.com/papers/quantum-geometry.pdf) |

## Estimators and method

| Year | Title | Authors | Link |
|---|---|---|---|
| 2025 | *Robust estimation of the intrinsic dimension of data sets with QCML* — *Scientific Reports* 15, 6933; note [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] | Candelori, Abanov, Berger, Hogan, Kirakosyan, Musaelian, Samson, Smith, Villani, Wells, Xu | [PDF](candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml.pdf) |
| 2026 | *Shallow-circuit Supervised Learning on a Quantum Processor* — a QCML classifier trained with ground states sampled on up to 50 qubits of an IBM Heron processor; arXiv:2601.03235; note [[candelori-et-al-2026-shallow-circuit-supervised-learning-on-a-quantum-processor]] | Candelori, Majumder, Mezzacapo, Robledo Moreno, Musaelian, Nagarajan, Pinnamaneni, Sharma, Villani | [PDF](candelori-et-al-2026-shallow-circuit-supervised-learning-on-a-quantum-processor.pdf) |
| 2025 | *Breaking the curse of dimensionality: QCML vs. tree-based models* (blog post) — QCML against tree ensembles on synthetic high-dimensional data; note [[candelori-santhanam-2025-breaking-the-curse-of-dimensionality-qcml-vs-tree-based-models]] | Candelori, Santhanam | [Post](https://www.qognitiveai.com/blog/tree-benchmarks/) |
| 2026 | *The Shape of Your Data* (Data Cleaning White Paper) — imputation and anomaly detection as energy minimisation; note [[candelori-santhanam-2026-the-shape-of-your-data]] | Candelori, Santhanam | [PDF](https://www.qognitiveai.com/papers/Data_Cleaning_Whitepaper.pdf) |

## Finance applications

| Year | Title | Authors | Link |
|---|---|---|---|
| 2024 | *Quantum Cognition Machine Learning: Financial Forecasting* — QCML against a neural network on US stock returns; note [[samson-et-al-2024-quantum-cognition-machine-learning-financial-forecasting]] | Samson, Berger, Candelori, Kirakosyan, Musaelian, Villani | [PDF](https://www.qognitiveai.com/papers/Qognitive_Financial_Forecasting.pdf) |
| 2025 | *Supervised Similarity for High-Yield Corporate Bonds with QCML* — *Risk.net*, May 2025 (arXiv:2502.01495); QCML state overlap as a learned distance between bonds, against random-forest proximity; note [[rosaler-et-al-2025-supervised-similarity-for-high-yield-bonds]] | Rosaler, Candelori, Kirakosyan, Musaelian, Samson, Wells, Mehta, Pasquali | [PDF](https://www.qognitiveai.com/papers/RiskBondSimilarity.pdf) |
| 2025 | *Supervised Similarity for Firm Linkages* — *Risk.net*, October 2025; firms linked by similar characteristics, with plain and QCML-learned distance, tested for return spillover; note [[samson-et-al-2025-supervised-similarity-for-firm-linkages]] | Samson, Banner, Candelori, Cottrell, Di Matteo, Duchnowski, Kirakosyan, Marques, Musaelian, Pasquali, Stever, Villani | [PDF](https://www.qognitiveai.com/papers/firm_linkages.pdf) |

## Other domains

| Year | Title | Authors | Link |
|---|---|---|---|
| 2025 | *QCML for Forecasting Chromosomal Instability* — supervised QCML and a POVM density forecast on 227 tumour-cell images, against ten classical models; note [[di-caro-et-al-2025-quantum-cognition-machine-learning-for-forecasting-chromosomal-instability]] | Di Caro, Kirakosyan, Abanov, Candelori, Hartmann, Lam, Musaelian, Samson, Wells, Wenstrup, Xu | [PDF](https://www.qognitiveai.com/papers/epic-paper.pdf) |
| 2025 | *On the Impossibility of an AI Mathematician Being Both Autonomous and Useful* — a halting-problem argument that no Turing machine can do mathematics that is both autonomous and useful, in reply to the Birch test; working paper, no longer on the Qognitive site; note [[musaelian-2025-on-the-impossibility-of-an-ai-mathematician-being-both-autonomous-and-useful]] | Musaelian | [Archived PDF](https://web.archive.org/web/20260615202433/https://www.qognitiveai.com/papers/Birch_Test_paper.pdf) |

---

## Cross-topic

**[[busemeyer-bruza-2012]]**, in this folder, is the
foundation this programme builds on — Hilbert-space representations of human judgement,
where non-commuting observables model the order effects and interference that Kolmogorov
probability cannot. Busemeyer is a co-author on *Quantum Geometry of Data*.

**Intrinsic dimension is the sharpest point of comparison in the whole repo.**
`../../high-dimensional-geometry/intrinsic-dimension/` already holds two classical estimators of the same quantity — **[[levina-bickel-2004-maximum-likelihood-estimation-of-intrinsic-dimension]]**
(maximum-likelihood) and **[[facco-et-al-2017]]** (two-NN) — and the 2025 QCML paper claims
a more robust one ([[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]]). Three estimators, one target, on data you have. That is a runnable
comparison rather than a reading exercise.

`../../factor-models-and-asset-pricing/machine-learning-factor-models/` holds the finance-legitimate nonlinear
alternative, **[[gu-kelly-xiu-2021]]**, the conditional autoencoder. If QCML is to earn its
place over a nonlinear latent-factor model, that is the benchmark it has to beat.
