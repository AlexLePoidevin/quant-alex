# Quantum Cognition Machine Learning: AI Needs Quantum

| | |
|---|---|
| **Authors** | Kharen Musaelian (lead), Alexander Abanov, Jeffrey Berger, Luca Candelori, Vahagn Kirakosyan, Ryan Samson, James Smith, Dario Villani (Qognitive, Inc.) |
| **Year** | 2024 |
| **Type** | White paper — Qognitive, 1 March 2024, 7pp. Not peer-reviewed |
| **Link** | [qognitiveai.com/papers/QCML - Qognitive, Inc.pdf](https://www.qognitiveai.com/papers/QCML%20-%20Qognitive,%20Inc.pdf) |
| **BibTeX** | `musaelian2024qcml` |
| **Status** | Reference — short position paper; §2–3 carry the argument |

## What it is

The founding position paper of the QCML programme. It argues that machine learning built
on classical probability cannot do abstraction, relevance or concept formation, and that
representing data the way quantum-cognition models represent a state of mind can. It
contains no equations for the model and no results; it is the argument, not the method.

- **The case against classical probability.** A joint distribution over N binary features
  has 2^N − 1 free numbers, so learning it from data needs exponentially many samples.
  Statistics works in practice only because people choose the variables first. Concepts
  as classical sets run into the same count: a set of N elements has 2^N − 1 non-empty
  subsets.
- **Categories that are both at once.** The worked example is Iron Mountain (IRM),
  reclassified under GICS in 2020 from Commercial and Professional Services to Equity
  REIT. The authors argue it is fully both, depending on context, so neither a hard
  category nor a Bayesian 50/50 mix (which treats the label as noisy) describes it. A
  quantum state can be a superposition of the two.
- **Quantum cognition.** Following Aerts, Khrennikov and Busemeyer, a state of mind is a
  vector in a Hilbert space and each question is an operator on it. The authors take no
  position on whether brains are physically quantum. Operators that do not commute obey
  an uncertainty principle: no state matches every feature exactly, so encoding many
  features costs precision.
- **Uncertainty without entropy as abstraction.** In a two-spin Bell state the joint state
  is pure (zero entropy) while each spin alone is maximally uncertain. The authors present
  this as the formal picture of abstraction. The representation becomes classical as the
  Hilbert space grows large, because all operators can then be made to commute.
- **What QCML does.** Training learns the operators and encodes each data point as a
  quantum state, so correlations live in the operators and their commutation relations.
  The paper says it was benchmarked on MNIST, COIL-20, PenDigits and time-series tasks,
  but reports no numbers.
- **Claims stated without evidence here.** A "logarithmic reduction" in representation
  complexity, an explanation of why evolution would favour quantum cognition, that
  attention, abstraction and concept generation "arise naturally", and that QCML on
  quantum hardware would be "the first example of a non-Turing machine". The paper also
  says its forecasts are already used in asset management. None of these is supported
  with data in the paper; the later papers in this folder are where the evidence is.
- **Where it points.** Data with far more features than samples (the example is about 28
  million DNA methylation sites), finance, and quantum hardware, where the ground state of
  a data-dependent Hamiltonian is a natural way to load data, unlike amplitude or angle
  encoding.

## Why it's in the library

**It is the source of the programme's vocabulary.** Hamiltonian, ground state, observables
per feature, uncertainty as a feature rather than a bug: the later QCML papers assume
these ideas, and this is where they are argued in plain language.

**The IRM example is a real modelling problem.** Industry labels are hard assignments
applied to firms with several business lines. Whether a firm should be described by one
category, a fixed mix, or a context-dependent mix matters for any model that uses sector
membership as a feature or for grouping. The firm-linkages and bond-similarity papers
attack the same problem by learning similarity from data instead of from labels.

**It is useful to read the claims against what was later shown.** The 2024–2026 papers
supply the model equations, the financial-forecasting test, the intrinsic-dimension
estimator and the quantum-hardware run. Reading this first makes it clear which of the
original claims those papers back up and which remain assertions.

## Links

- [[busemeyer-bruza-2012]] — the Hilbert-space models of cognition this paper builds on
- [[abanov-et-al-2025-quantum-geometry-of-data]] — the full mathematical exposition of the
  model this paper only describes in words
- [[samson-et-al-2024-quantum-cognition-machine-learning-financial-forecasting]] — the
  first published test, on US stock returns, and the model equations
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — the
  peer-reviewed estimator built on the same representation
- [[rosaler-et-al-2025-supervised-similarity-for-high-yield-bonds]],
  [[samson-et-al-2025-supervised-similarity-for-firm-linkages]] — learned similarity
  between firms and bonds, the data-driven answer to the IRM classification problem
- [[di-caro-et-al-2025-quantum-cognition-machine-learning-for-forecasting-chromosomal-instability]]
  — the biomedical application this paper anticipates
- [[candelori-et-al-2026-shallow-circuit-supervised-learning-on-a-quantum-processor]] —
  the move to quantum hardware proposed in §5
- [[dawid-lecun-2023-introduction-to-latent-variable-energy-based-models]],
  [[choi-2022-the-curious-case-of-commonsense-intelligence]] — the two "something is
  missing in current AI" references the paper opens with
