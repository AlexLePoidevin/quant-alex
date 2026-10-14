# Correlation and dependence

How assets move together, how to measure it, and where the usual measure fails.

A correlation matrix is the starting object for almost everything in portfolio
construction. This section covers four questions about it: how much of it is signal, how to
estimate it well, what it misses, and where the structure comes from.

| Folder | Question |
|---|---|
| `01-random-matrix-theory` | How much of a sample correlation matrix is noise? Marčenko–Pastur, eigenvalue cleaning, the market and sector modes |
| `02-covariance-estimation` | How to estimate a large covariance matrix that is usable in an optimiser (shrinkage) |
| `03-copulas-and-tail-dependence` | What a correlation coefficient leaves out: copulas, Sklar's theorem, tail dependence, correlations that rise in crashes, and the Gaussian copula in 2008 |
| `04-why-assets-move-together` | Where comovement comes from: networks, granular firms, style investing, excess comovement, hierarchical clustering |

**Suggested path:** [[laloux-et-al-1999]] → [[bouchaud-potters-2009]] → [[ledoit-wolf-2004]]
→ [[ang-chen-2002]] → [[nelsen-2006-introduction-to-copulas]] (chapters 2 and 5) →
[[munnix-schafer-2011-copula-dependencies]] → [[mackenzie-spears-2014-formula-that-killed-wall-street]]
→ [[donnelly-embrechts-2010-devil-is-in-the-tails]].

For the copulas folder, the explainers go from easiest to hardest:
[[finance-tutoring-2024-sklar-theorem]] → [[nguyen-2020-introduction-to-copulas-slides]] →
[[wikipedia-copula-statistics]] → Nelsen.

Related: the factor-model view of the same matrix is in `../02-factor-models-and-asset-pricing/`
(**model there, measurement here**). What the matrix implies for diversification is in
`../05-portfolio-construction-and-risk/02-diversification-and-effective-bets/`.
