# Analyzing Dependent Data with Vine Copulas: A Practical Guide With R

| | |
|---|---|
| **Author** | Claudia Czado (Technical University of Munich) |
| **Year** | 2019 |
| **Type** | Textbook — Springer Lecture Notes in Statistics 222. ISBN 978-3-030-13784-7, doi:10.1007/978-3-030-13785-4 |
| **Prerequisite** | Bivariate copulas and Sklar's theorem ([[nelsen-2006-introduction-to-copulas]] ch. 2, 5); basic maximum likelihood; R |
| **Link** | https://doi.org/10.1007/978-3-030-13785-4 (no PDF in this repo) |
| **BibTeX** | `czado2019vine` |
| **Status** | Reference |

## What it is

The standard practical text on **vine copulas**, by one of the people who developed them.
It covers the step from two variables to many. A single parametric copula family (Gaussian,
t, one Archimedean family) forces one kind of dependence on every pair of variables. A
vine instead builds a d-dimensional copula out of d(d−1)/2 *bivariate* copulas. Each pair
copula can come from a different family, so it can have its own strength and its own tail
behaviour (lower tail, upper tail, both or neither).

The construction is the **pair-copula decomposition**: any joint density factors into its
marginals times a product of bivariate copula densities. Some of these are unconditional
(e.g. assets 1–2) and some conditional (e.g. 1–3 given 2). A **regular vine** is the tree
sequence that says which pairs and conditioning sets are used. C-vines (star-shaped trees,
one central variable per level) and D-vines (path-shaped trees) are the two special cases.

Contents, in order:
1. Multivariate distributions and copulas; Sklar's theorem
2. Dependence measures: Pearson, Kendall's τ, Spearman's ρ, tail dependence, partial and
   conditional correlation
3. Bivariate copula families, how to visualise them (normalised contour plots) and how to
   estimate them; rotations to move tail dependence into other quadrants
4. Pair-copula decompositions and constructions
5. Regular vines: the tree structure and how to represent it as a matrix
6. Simulating from regular vine copulas
7. Parameter estimation: sequential (tree by tree) and joint maximum likelihood
8. Model selection: Dißmann's algorithm, which builds each tree as a maximum spanning tree
   on |Kendall's τ| and picks each pair's family by AIC/BIC
9. Comparing vine models: Vuong and Clarke tests, information criteria
10. Case study: dependence among German DAX stocks
11. Recent developments

Every method comes with R code using the `VineCopula` package, which is also available
for Python as `pyvinecopulib`.

## Why it's in the library

**It is the practical answer to the elliptical trap.** A correlation matrix, and any
Gaussian or t copula built on it, gives every pair of assets the same symmetric
dependence. Vines allow equity–equity pairs to have lower-tail dependence (they crash
together) while equity–bond pairs have a different structure, all in one model. This is
the multivariate step beyond what [[munnix-schafer-2011-copula-dependencies]] measures pair
by pair.

**The model-selection algorithm is a dependence tree.** Dißmann's first tree is a maximum
spanning tree on |Kendall's τ|. That is the rank-based relative of the correlation
minimum-spanning trees in [[mantegna-1999]], with a copula family fitted to each edge.

**It makes stress testing possible.** Vines can be simulated from directly, so scenario
sets with realistic joint tails can be generated for CVaR optimisation
([[rockafellar-uryasev-2000]]). [[donnelly-embrechts-2010-devil-is-in-the-tails]] argue
exactly this kind of stress test was missing in 2008.

**Its caveats are the ones that matter in a backtest.** Most applications use the
*simplified* vine, where the conditional copulas don't depend on the conditioning values.
That's an assumption, not a fact. A d-dimensional vine has O(d²) pair copulas and
parameters to choose and fit, so fit statistics have to be read with the number of
choices in mind (ch. 8–9).

## Links

- [[nelsen-2006-introduction-to-copulas]] — the bivariate theory this book builds on
- [[haugh-2016-introduction-to-copulas-slides]] — Gaussian and t copulas, fitting from
  Kendall's τ, the single-family case vines generalise
- [[munnix-schafer-2011-copula-dependencies]] — empirical equity tail dependence, the
  structure vines are built to capture
- [[ang-chen-2002]] — asymmetric correlation in down markets, a lower-tail effect a
  vine can model pair by pair
- [[mantegna-1999]] — correlation spanning trees, the linear relative of Dißmann's tree
  selection
- [[wikipedia-tree-graph-theory]] — trees, paths, stars and spanning trees: the vocabulary
  for R-, D- and C-vines
- [[donnelly-embrechts-2010-devil-is-in-the-tails]],
  [[mackenzie-spears-2014-formula-that-killed-wall-street]] — what a single one-factor
  Gaussian copula got wrong
- [[rockafellar-uryasev-2000]] — CVaR optimisation, which needs realistic joint-tail
  scenarios
