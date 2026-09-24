# Quantum cognition machine learning

The Qognitive research programme: representing data as states in a Hilbert space and
learning a Hamiltonian over them, so that structure is recovered from the geometry of the
state space rather than from a covariance matrix. Quantum-*inspired* and classical to run —
density matrices and POVMs on ordinary hardware — except where a paper says otherwise.

All ten papers below are published by Qognitive at
[qognitiveai.com/research](https://www.qognitiveai.com/research/). Several have appeared in
peer-reviewed venues; the PDFs carry the venue where there is one.

**✓** marks a PDF already downloaded to the Vinland Saga project directory.

---

## The programme

| Year | Title | Authors | Link |
|---|---|---|---|
| 2024 | *Quantum Cognition Machine Learning: AI Needs Quantum* ✓ | Musaelian, Abanov, Berger, Candelori, Kirakosyan, Samson, Smith, Villani | [PDF](https://www.qognitiveai.com/papers/QCML%20-%20Qognitive,%20Inc.pdf) |
| 2025 | *Quantum Geometry of Data* ✓ | Abanov, Candelori, Steinacker, Wells, Busemeyer, Hogan, Kirakosyan, Marzari, Pinnamaneni, Villani, Xu, Musaelian | [PDF](https://www.qognitiveai.com/papers/quantum-geometry.pdf) |

## Estimators and method

| Year | Title | Authors | Link |
|---|---|---|---|
| 2025 | *Robust estimation of the intrinsic dimension of data sets with QCML* ✓ | Candelori, Abanov, Berger, Hogan, Kirakosyan, Musaelian, Samson, Smith, Villani, Wells, Xu | [PDF](https://www.qognitiveai.com/papers/Nature-IntrinsicDimension.pdf) |
| 2026 | *Shallow-circuit Supervised Learning on a Quantum Processor* | Candelori, Majumder, Mezzacapo, Robledo Moreno, Musaelian, Nagarajan, Pinnamaneni, Sharma, Villani | [PDF](https://www.qognitiveai.com/papers/quantum.pdf) |
| 2026 | *Data Cleaning White Paper* | Candelori, Santhanam | [PDF](https://www.qognitiveai.com/papers/Data_Cleaning_Whitepaper.pdf) |

## Finance applications

| Year | Title | Authors | Link |
|---|---|---|---|
| 2024 | *Quantum Cognition Machine Learning: Financial Forecasting* ✓ | Samson, Berger, Candelori, Kirakosyan, Musaelian, Villani | [PDF](https://www.qognitiveai.com/papers/Qognitive_Financial_Forecasting.pdf) |
| 2025 | *Supervised Similarity for High-Yield Corporate Bonds with QCML* ✓ | Rosaler, Candelori, Kirakosyan, Musaelian, Samson, Wells, Mehta, Pasquali | [PDF](https://www.qognitiveai.com/papers/RiskBondSimilarity.pdf) |
| 2025 | *Supervised Similarity for Firm Linkages* | Samson, Banner, Candelori, Cottrell, Di Matteo, Duchnowski, Kirakosyan, Marques, Musaelian, Pasquali, Stever, Villani | [PDF](https://www.qognitiveai.com/papers/firm_linkages.pdf) |

## Other domains

| Year | Title | Authors | Link |
|---|---|---|---|
| forthcoming | *QCML for Forecasting Chromosomal Instability* | Di Caro, Kirakosyan, Abanov, Candelori, Hartmann, Lam, Musaelian, Samson, Wells, Wenstrup, Xu | [PDF](https://www.qognitiveai.com/papers/epic-paper.pdf) |
| 2025 | *On the Impossibility of an AI Mathematician Being Both Autonomous and Useful* | Musaelian | [PDF](https://www.qognitiveai.com/papers/Birch_Test_paper.pdf) |

---

## Cross-topic

**[[busemeyer-bruza-2012]]** in `../market-structure/04-nonlinear-and-quantum/` is the
foundation this programme builds on — Hilbert-space representations of human judgement,
where non-commuting observables model the order effects and interference that Kolmogorov
probability cannot. Busemeyer is a co-author on *Quantum Geometry of Data*.

**Intrinsic dimension is the sharpest point of comparison in the whole repo.** That folder
already holds two classical estimators of the same quantity — **[[levina-bickel-2004]]**
(maximum-likelihood) and **[[facco-et-al-2017]]** (two-NN) — and the 2025 QCML paper claims
a more robust one. Three estimators, one target, on data you have. That is a runnable
comparison rather than a reading exercise.

`../market-structure/04-nonlinear-and-quantum/` also holds the finance-legitimate nonlinear
alternative, **[[gu-kelly-xiu-2021]]**, the conditional autoencoder. If QCML is to earn its
place over a nonlinear latent-factor model, that is the benchmark it has to beat.
