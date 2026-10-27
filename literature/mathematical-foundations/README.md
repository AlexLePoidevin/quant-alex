# Mathematical foundations

The mathematics the rest of the library assumes. Read these selectively: each note says
which chapters matter and why.

| Folder | Question | Start with |
|---|---|---|
| `probability-and-statistics` | Random variables, sampling distributions, convergence, inference, measure-theoretic probability | [[hopfensperger-1999-probability-models]] (gentle) → [[wackerly-2008-mathematical-statistics]] and [[evans-rosenthal-2009-probability-and-statistics]] → [[le-gall-2022-measure-theory-probability]] (rigorous) |
| `stochastic-calculus` | Brownian motion and Itô's formula, the language of continuous-time finance | [[shreve-2004]] |
| `linear-algebra-and-eigenvectors` | Eigendecomposition of a symmetric positive semi-definite matrix: principal axes, which is what PCA does to a covariance matrix; projection, the spectral theorem and the SVD proved in general | [[peraire-widnall-2008-inertia-tensor]] (intuition) → [[axler-2024-linear-algebra-done-right]] (theory) |
| `optimization` | Linear programming and duality, behind portfolio optimisation and CVaR minimisation | [[nemirovski-2023-linear-optimization]] |

Copulas are mathematics too, but they are filed with the finance they serve, in
`../correlation-and-dependence/copulas-and-tail-dependence/`.
