# Quantum Cognition Machine Learning: Financial Forecasting

| | |
|---|---|
| **Authors** | Ryan Samson, Jeffrey Berger, Luca Candelori, Vahagn Kirakosyan, Kharen Musaelian, Dario Villani (Qognitive, Inc.; Wayne State; Duality Group) |
| **Year** | 2024 |
| **Type** | White paper — Qognitive, September 2024, 11pp. Not peer-reviewed |
| **Link** | [qognitiveai.com/papers/Qognitive_Financial_Forecasting.pdf](https://www.qognitiveai.com/papers/Qognitive_Financial_Forecasting.pdf) |
| **BibTeX** | `samson2024qcml` |
| **Status** | Reference — §3 (the model and training loop) and §4.3–4.7 (setup and results) |

## What it is

The first worked finance example of QCML: forecasting US stock returns with a QCML model
and a small neural network side by side, and testing whether either adds anything beyond
the linear effect of its inputs.

- **The model.** Each feature k gets a learned Hermitian matrix A_k. For a data vector x,
  the *error Hamiltonian* is H(x) = Σ_k (A_k − x_k·I)², and the data point is represented
  by its ground state |ψ⟩ (the eigenvector with the lowest eigenvalue). Training alternates:
  fix the matrices and find each ground state, then fix the states and take a gradient step
  on the matrices. To forecast, build H from whichever features are available, find its
  ground state, and read any other feature off as ⟨ψ|B|ψ⟩. Missing inputs are simply left
  out of H instead of being filled in. The Hilbert space here has dimension 32; the exact
  operator parameterisation is proprietary.
- **The motivating argument.** A joint distribution over many features needs exponentially
  many cells (10 features in quintiles is 5^10 ≈ 9.8 million bins, more than ten years of
  daily data on 3,000 stocks). The authors claim the Hilbert-space representation needs
  only logarithmically many parameters by comparison.
- **Data and target.** About 1,500 large, liquid US stocks; daily data from Bloomberg, S&P
  Capital IQ and S&P securities-lending data. Features: momentum, value (sales/price),
  accruals, EBITDA/TEV, operating efficiency, profit margin, short utilisation and size,
  with beta and industry dummies as controls. The target is the 15-day forward log return
  with the linear effect of every input and control projected out, so only the nonlinear
  part is left to learn.
- **Training and testing.** Trained once on January 2008 – August 2013, then frozen. Stocks
  are split at random into groups of about 50, a model is trained per group, and forecasts
  are averaged over 100 such splits. Out of sample from September 2013 to June 2024,
  forecasts are turned into mean-variance portfolios (weights V⁻¹f, with a proprietary
  covariance estimate) with zero exposure to the inputs and controls, smoothed over 15
  days, with no transaction costs.
- **Two-feature model (momentum, value).** Sharpe 0.69 for QCML, 0.58 for the network,
  0.75 combined; their returns correlate 0.41. Both models learn a similar interaction:
  value works better among past losers, momentum works better among expensive stocks,
  matching Asness (1997). By sub-period the network goes from 1.91 to −0.30 to 0.11; QCML
  stays between 0.53 and 0.80.
- **Eight-feature model.** Both reach Sharpe 1.25, with return correlation 0.32; combined
  1.39. Adding either nonlinear forecast to the equal-risk mix of linear factor forecasts
  raises its Sharpe from 1.17 to 1.38 (network) or 1.43 (QCML), and 1.58 with both.
- **Stated limits.** The authors make no claim of superiority, and the results exclude
  costs and are not meant as a standalone strategy.

## Why it's in the library

**The method is the useful part.** The test design is a good template for any nonlinear
model on factor data: project the target and the final forecast away from the inputs and
controls, so a Sharpe ratio measures only what the model learned beyond the linear
factors. Then judge it by what it adds to a linear blend, not by its standalone number.

**Two different nonlinear models found different signals.** At the same Sharpe (1.25),
QCML and the network correlate only 0.32, and the combination beats either one. That is
an argument for running dissimilar model families side by side and combining them.

**The interaction surface is a sanity check.** With two inputs the learned forecast can be
plotted. Both models recover the value–momentum interaction documented independently by
Asness, which is evidence they are learning structure rather than noise.

**It is the finance anchor for the QCML programme.** Together with the intrinsic-dimension
paper and the data-cleaning white paper, it shows the same ground-state model used for
forecasting, missing data and geometry. The evidence is one universe, one fixed training
window and gross returns, so it needs replication before it counts as a result.

## Links

- [[rosaler-et-al-2025-supervised-similarity-for-high-yield-bonds]] — the same supervised model used to define a distance between bonds
- [[musaelian-et-al-2024-quantum-cognition-machine-learning-ai-needs-quantum]] — the position paper whose argument this one opens with
- [[samson-et-al-2025-supervised-similarity-for-firm-linkages]] — the same universe and
  portfolio test, with QCML used to learn which firms are linked instead of to forecast
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — the same
  ground-state model extended to intrinsic dimension, the follow-up named in the conclusion
- [[candelori-santhanam-2026-the-shape-of-your-data]] — the same model used for imputation;
  the forecasting rule here (leave missing inputs out of H) is its starting point
- [[busemeyer-bruza-2012]] — the quantum-cognition models QCML is named after
- [[gu-kelly-xiu-2021]] — a nonlinear latent-factor model of returns, the benchmark QCML
  has to beat in finance; the network here follows the same authors' 2020 design
- [[markowitz-1952]] — the mean-variance weights (V⁻¹f) used to turn forecasts into
  portfolios
- [[fama-french-2015]] — the linear factor set the residualised target controls for
- [[harvey-liu-zhu-2016]] — the multiple-testing bar for any new return predictor
