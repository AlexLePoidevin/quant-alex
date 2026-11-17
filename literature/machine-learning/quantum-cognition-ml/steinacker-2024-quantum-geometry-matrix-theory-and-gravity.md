# Quantum Geometry, Matrix Theory and Gravity

| | |
|---|---|
| **Author** | Harold C. Steinacker (University of Vienna) |
| **Year** | 2024 |
| **Type** | Book — Cambridge University Press, 2024. The author's open version of the notes (414pp, April 2024) is free to view and download for private research and study |
| **PDF** | Not hosted in this repository (the open version is licensed for private study only, not for redistribution) |
| **Find it** | [doi.org/10.1017/9781009440776](https://doi.org/10.1017/9781009440776) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Quantum+Geometry%2C+Matrix+Theory+and+Gravity%22+Steinacker) |
| **BibTeX** | `steinacker2024quantum` |
| **Status** | Reference — chapter 4 (§4.1–4.3, §4.7) is the part QCML uses; chapters 1–3 are the background it needs; parts III–IV are physics |

## What it is

A graduate text on **matrix geometry**: how a set of D Hermitian matrices X¹…X^D can be
read as a quantised space, a "fuzzy" manifold embedded in R^D, and how that idea becomes
a framework for gravity in the IKKT/BFSS matrix models of string theory.

- **Part I (ch. 1–2)** — differentiable and symplectic manifolds, Poisson structures, Lie
  groups and coadjoint orbits.
- **Part II (ch. 3–5)** — quantising symplectic manifolds: the Moyal–Weyl plane, coherent
  states, the fuzzy sphere, fuzzy CPⁿ and the fuzzy torus; then the general theory of
  **quantum spaces from matrices** (ch. 4) and covariant quantum spaces such as the fuzzy
  4-sphere and hyperboloid (ch. 5).
- **Part III (ch. 6–10)** — noncommutative field theory, Yang–Mills matrix models,
  fuzzy extra dimensions, higher-spin gauge theory.
- **Part IV (ch. 11–13)** — the maximally supersymmetric matrix models (IKKT, BFSS) and
  gravity emerging as a quantum effect on quantum spacetime.

**Chapter 4 is the core.** Given the matrices X^a and a point x in R^D, define the
*displacement Hamiltonian*

  H_x = ½ Σ_a (X^a − x^a)²

(Eq. 4.1.1). Its ground state |x⟩ is the **quasi-coherent state** at x: the state that is
as close as possible to a common eigenvector of all the X^a, with expectation values
⟨x|X^a|x⟩ ≈ x^a. The ground-state energy splits exactly into two parts,
2λ(x) = Δ²(x) + d²(x) (Eq. 4.1.7): the *dispersion* Δ² (how far the matrices are from
commuting at that point) and the *displacement* d² (how far x lies from the underlying
space). The set of all these states is a manifold M inside CP^{N−1} (§4.2), which carries
a **quantum metric** and a **Berry-connection field strength** (a would-be symplectic form)
inherited from the Hilbert space. Its intrinsic dimension follows from the rank of that
structure, and the **matrix Laplacian** □ = Σ_a [X^a, [X^a, ·]] (§4.7) has a spectrum that
approximates the Laplacian of M. If the matrices are random there is no geometry ("quantum
foam"); if they almost commute, the geometry is a good classical approximation.

## Why it's in the library

This is the mathematics QCML is built on. QCML learns the matrices X^a from data and
represents each data point x by the ground state of exactly this displacement Hamiltonian;
it calls the energy the error Hamiltonian, and the 2λ = Δ² + d² split is its trade-off
between fitting a point and keeping the operators near-commuting. Steinacker is a co-author
of [[abanov-et-al-2025-quantum-geometry-of-data]], which takes §4.2's quantum metric,
Berry curvature and matrix Laplacian and applies them to data. The intrinsic-dimension
estimator in [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]]
is the rank of the quantum metric of §4.2.

The Qognitive papers state these results briefly and cite this line of work; the book
derives them, with worked examples (fuzzy sphere, Moyal plane) where every quantity can be
checked by hand. Physics beyond chapter 5 is not needed for QCML.

## Links

- [[abanov-et-al-2025-quantum-geometry-of-data]] — chapter 4's quantum metric, Berry
  curvature and matrix Laplacian applied to data, with Steinacker as co-author
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — intrinsic
  dimension from the quantum metric of the quasi-coherent states
- [[musaelian-et-al-2024-quantum-cognition-machine-learning-ai-needs-quantum]] — the QCML
  position paper that this mathematics makes precise
- [[axler-2024-linear-algebra-done-right]] — the Hermitian operators, spectral theorem and
  inner-product spaces the book takes for granted
- [[coifman-lafon-2006]] — diffusion maps, the graph-based counterpart of the matrix
  Laplacian
