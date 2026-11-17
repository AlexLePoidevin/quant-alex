# Quantum (Matrix) Geometry and Quasi-Coherent States

| | |
|---|---|
| **Author** | Harold C. Steinacker (University of Vienna) |
| **Year** | 2021 |
| **Type** | Paper — *Journal of Physics A: Mathematical and Theoretical* 54(5), 055401 (2021). arXiv:2009.03400v3 [hep-th], February 2023, 38pp |
| **Link** | [doi.org/10.1088/1751-8121/abd735](https://doi.org/10.1088/1751-8121/abd735); [arxiv.org/abs/2009.03400](https://arxiv.org/abs/2009.03400) |
| **PDF** | `steinacker-2021-quantum-matrix-geometry-and-quasi-coherent-states.pdf` (in this folder; arXiv version) |
| **BibTeX** | `steinacker2021quasicoherent` |
| **Status** | Reference — §2 and §2.1 are what QCML uses; §3 adds the abstract space M and the Kähler case; §6 has worked examples |

## What it is

The paper that turns "a set of Hermitian matrices is a fuzzy space" into a general
construction that works for **any** D matrices X¹…X^D of finite size N, with no large-N
limit and no representation theory.

- **Quasi-coherent states (§2).** For a point x in R^D, the *displacement Hamiltonian*
  H_x = ½ Σ_a (X^a − x^a)² (Eq. 1) is positive definite when the matrices are irreducible.
  Its ground state |x⟩ is the quasi-coherent state: the state in which all X^a are as
  nearly diagonal as possible together. The ground-state energy splits into the dispersion
  δ²(x) (joint uncertainty of the X^a) and the displacement d²(x) (how far ⟨x|X^a|x⟩ lies
  from x) (Eq. 9).
- **Geometry from the states (§2.1).** The map x ↦ |x⟩ carries a Berry-type U(1)
  connection, whose field strength ω is a would-be symplectic form, and a **quantum
  metric** g, the Fubini–Study metric of CP^{N−1} pulled back to R^D. Both come from one
  Hermitian D×D tensor h_ab = ½(g_ab + iω_ab) (Eq. 18). The overlap ⟨x|y⟩ = e^{iφ−D} gives
  a distance between points, quadratic in g at short range (Eqs. 13, 23).
- **The abstract quantum space M (§3).** The set of all quasi-coherent states is a variety
  inside CP^{N−1}, the "quantum space" the matrices describe. Its tangent space and the
  rank of g give its dimension, and operators that are almost local on M are the ones with
  a good classical description.
- **Quantum Kähler spaces (§3.2, §4).** When the states depend holomorphically on x, M is
  a quantum Kähler manifold, as for the fuzzy sphere and fuzzy CPⁿ, and a quantisation
  map onto all operators follows. Examples in §6 include cases that are not Kähler, such as
  the minimal fuzzy torus.

## Why it's in the library

This is the paper the QCML programme draws on directly. QCML's error Hamiltonian is
exactly Eq. 1, with the matrices learned from data instead of given by physics, and each
data point is represented by its quasi-coherent state. The intrinsic-dimension estimator in
[[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] cites this
paper and reads the dimension off the quantum metric g of §2.1, and
[[abanov-et-al-2025-quantum-geometry-of-data]] builds its metric and curvature tools on it.

It is the short version of chapter 4 of [[steinacker-2024-quantum-geometry-matrix-theory-and-gravity]]:
the same definitions in 38 pages, without the physics that follows in the book. Read this
first; go to the book for the background and longer worked examples.

## Links

- [[steinacker-2024-quantum-geometry-matrix-theory-and-gravity]] — the textbook version,
  with chapters 1–3 as background
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — intrinsic
  dimension from the quantum metric defined here
- [[abanov-et-al-2025-quantum-geometry-of-data]] — the quantum metric, Berry curvature and
  matrix Laplacian applied to data, with Steinacker as co-author
- [[musaelian-et-al-2024-quantum-cognition-machine-learning-ai-needs-quantum]] — the QCML
  position paper
