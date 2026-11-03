# Shallow-circuit Supervised Learning on a Quantum Processor

| | |
|---|---|
| **Authors** | Luca Candelori, Kharen Musaelian, Santhanam Nagarajan, Sunil Pinnamaneni, Dario Villani (Qognitive, Inc.); Swarnadeep Majumder, Antonio Mezzacapo, Javier Robledo Moreno, Kunal Sharma (IBM Quantum, T.J. Watson Research Center). Majumder and Pinnamaneni are joint primary authors |
| **Year** | 2026 |
| **Type** | Preprint — arXiv:2601.03235v1 [quant-ph], January 2026, 13pp |
| **PDF** | `candelori-et-al-2026-shallow-circuit-supervised-learning-on-a-quantum-processor.pdf` (in this folder) |
| **BibTeX** | `candelori2026shallow` |
| **Status** | Reference — §2.1 (the model) and §3 (hardware runs and results) carry it; §2.2 is the gradient and SKQD machinery |

## What it is

The QCML model run on real quantum hardware for the first time: a classifier whose
ground states are computed partly on a 156-qubit IBM Heron processor, trained on a small
synthetic dataset with up to 50 qubits. It is a proof that training works on current
hardware, not a claim of beating classical methods.

- **The model.** Each data point x gets its own Hamiltonian H(x) = B − Σ_f a_f X_f, where
  a_f are the feature values and B and the X_f are learned operators. The point is
  represented by the ground state of H(x); class scores (logits) are expectations of
  learned output operators on that state, fed through a softmax and cross-entropy loss.
  This is the same structure as classical QCML, but here the operators are sums of Pauli
  strings on n qubits, restricted to one- and two-qubit terms on neighbouring qubits so the
  circuits stay shallow. Training learns the Pauli coefficients.
- **Why this encoding.** Most quantum machine learning loads data through deep
  state-preparation circuits and suffers from vanishing gradients ("barren plateaus").
  Here the data only enter as coefficients in the Hamiltonian, i.e. as rotation angles in
  one- and two-qubit gates.
- **What runs where.** Ground states come from sample-based Krylov quantum diagonalisation
  (SKQD). The quantum processor runs short time-evolution circuits e^(−iHkΔt) and returns
  sampled bitstrings. A classical computer then projects H onto the span of those
  bitstrings, diagonalises it, and computes the ground state, a few excited states, the
  gradients (from perturbation theory, truncated to a small number of excited-state terms)
  and the parameter updates. The quantum chip only supplies the samples.
- **Hardware setup.** IBM's ibm_fez (156-qubit Heron). A chain of 50 qubits was chosen
  using a layer-fidelity benchmark, with dynamical decoupling against decoherence. The
  50-qubit circuits used over 1,000 two-qubit (CZ) gates. Runs at 18 qubits or fewer were
  simulated classically and used to pick hyperparameters; runs at 20 qubits or more used
  the hardware.
- **Data and results.** One synthetic scikit-learn binary classification problem: 500
  points, 10 features, 80/20 train/test split. Over about eight epochs at 30 and 50 qubits,
  test loss falls from about 0.69 to 0.42 and test accuracy rises from 50% to 91%. In
  simulation at 10–16 qubits, two excited-state terms in the gradient were already enough
  for high accuracy after one epoch.
- **What is not reported.** No classical baseline on the same data, one dataset, and no
  repeated runs. The authors list a systematic comparison with classical methods as the
  key next step.

## Why it's in the library

**It shows what "quantum" means in QCML.** The other QCML papers run entirely on classical
hardware with small dense matrices (Hilbert spaces of 8–32 dimensions). This paper maps the
same idea onto qubits, where the Hilbert space is 2^50-dimensional but the operators are
restricted to local Pauli terms. It makes clear that the finance and geometry results in
this folder do not depend on quantum hardware.

**The encoding idea is the transferable part.** Loading data as coefficients of a
Hamiltonian, rather than into a quantum state directly, avoids the two problems that have
stalled near-term quantum machine learning: expensive data loading and untrainable
circuits. Training worked here with non-vanishing gradients at 50 qubits.

**The evidence is a feasibility check.** A binary problem with 10 features and 500 points
is easy for logistic regression or a small tree ensemble, and none was run. 91% test
accuracy shows the hybrid loop trains; it says nothing yet about quantum advantage, which
the paper itself does not claim.

## Links

- [[musaelian-et-al-2024-quantum-cognition-machine-learning-ai-needs-quantum]] — the QCML
  framework and the case for a quantum representation, here put on a quantum processor
- [[abanov-et-al-2025-quantum-geometry-of-data]] — the full classical exposition of the
  model whose Hamiltonian H(x) = B − Σ a_f X_f is used here
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — the same
  ground-state model on classical hardware, applied to intrinsic dimension
- [[candelori-santhanam-2025-breaking-the-curse-of-dimensionality-qcml-vs-tree-based-models]]
  — another synthetic-data QCML benchmark, where a linear baseline turned out to matter
- [[busemeyer-bruza-2012]] — the quantum-cognition models QCML is named after
