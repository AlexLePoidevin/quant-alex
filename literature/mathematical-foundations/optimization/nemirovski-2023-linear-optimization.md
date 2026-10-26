# Introduction to Linear Optimization

| | |
|---|---|
| **Author** | Arkadi Nemirovski (Georgia Institute of Technology, ISyE) |
| **Year** | 2023 |
| **Type** | Graduate textbook — World Scientific, 610pp |
| **Origin** | Lecture notes from 15+ years teaching ISyE 6661 at Georgia Tech |
| **PDF** | `nemirovski-2023-linear-optimization.pdf` (in this folder) |
| **BibTeX** | `nemirovski2023lo` |
| **Status** | Reference |

## What it is

A rigorous, self-contained treatment of linear optimization in eight chapters:

1. LO modelling — what can be posed as an LO program
2. Polyhedral sets and their geometry
3. Systems of linear inequalities and LP duality
4. Simplex method
5. Network simplex
6. Polynomial-time solvability of LO
7. **Conic programming**
8. **Interior point methods for LO and semidefinite optimization**

The author is explicit that the classical pivoting material (4–5) is treated more sketchily
than the descriptive theory, on the grounds that most readers will *apply* LO rather than
develop its algorithms. The weight is on chapters 1–3 and 7–8.

## Why it's in the library

**Chapters 7 and 8 are the theory under the solver.** Conic programming and interior-point
methods are what a modern portfolio optimiser actually runs — second-order cone programs
for anything with a volatility or tracking-error constraint, semidefinite programs for
covariance-structured problems. This is the reference for what those solvers are doing and
when they are guaranteed to work.

**It is the foundation for the robust-optimization line.** Nemirovski, with Ben-Tal, is the
origin of Robust Optimization as a field; the book covers the robust counterpart of an
uncertain LO and ellipsoidal uncertainty sets as an application of duality. That matters
here because robust and distributionally-robust formulations are the direct answer to
mean-variance optimization's instability under estimation error — instead of plugging point
estimates into `w ∝ Σ⁻¹μ`, you optimise against a set of plausible parameters. The chain
runs: [[markowitz-1952]] states the problem, [[michaud-1989]] and [[chopra-ziemba-1993]]
show the point-estimate version is unstable, and this book supplies the machinery for
writing down the problem so the instability is priced rather than ignored.

**Chapter 1 is about recognising the form.** The genuinely reusable skill is the "calculus
of polyhedrally representable sets and functions" — knowing which constraints keep a problem
tractable. Turnover limits, position bounds, sector caps, long-only, gross and net exposure
are all polyhedral; that is why they can be layered onto a portfolio problem freely, while
a cardinality constraint cannot.

## Links

- [[rockafellar-uryasev-2000]] — CVaR minimisation reduces to an LP, the cleanest example
  in finance of chapter 1's "recognise the LO form" skill
- [[artzner-delbaen-eber-heath-1999]] — why the coherent risk measures that are tractable
  this way are the ones worth optimising
- [[ledoit-wolf-2004]] — the other response to estimation error: fix the input rather than
  the formulation
- [[meucci-2009]] — diversification measured in the eigenbasis, an objective that needs
  more than an LP
