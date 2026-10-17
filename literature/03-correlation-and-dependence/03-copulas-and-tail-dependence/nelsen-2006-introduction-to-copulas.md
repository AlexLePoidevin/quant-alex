# An Introduction to Copulas

| | |
|---|---|
| **Author** | Roger B. Nelsen (Lewis & Clark College) |
| **Year** | 2006 |
| **Type** | Graduate monograph — Springer Series in Statistics, 2nd edition, 276pp |
| **Prerequisite** | Upper-level undergraduate probability and mathematical statistics; no measure theory |
| **PDF** | `nelsen-2006-introduction-to-copulas.pdf` (in this folder) |
| **BibTeX** | `nelsen2006copulas` |
| **Status** | Reference |

## What it is

The standard introduction to copulas: functions that join a multivariate distribution to
its one-dimensional margins, or equivalently, multivariate distributions on the unit cube
with uniform margins. The book is mostly bivariate, and most chapters end by extending
their results to the multivariate case.

1. Introduction — the history from Hoeffding and Fréchet to Sklar (1959)
2. **Definitions and basic properties** — Sklar's theorem (§2.3), the Fréchet–Hoeffding
   bounds (§2.5), survival copulas, symmetry, order, random variate generation (§2.9),
   multivariate copulas (§2.10)
3. **Methods of constructing copulas** — inversion, geometric, algebraic (Plackett,
   Ali–Mikhail–Haq), extreme value copulas (§3.3.4)
4. **Archimedean copulas** — one- and two-parameter families such as Clayton, Gumbel and
   Frank, their properties and multivariate forms
5. **Dependence** — Kendall's tau and Spearman's rho (§5.1), quadrant and tail
   monotonicity, **tail dependence (§5.4)**, **empirical copulas (§5.6)**
6. Additional topics — fixed margins, quasi-copulas, Markov processes

There are about 150 exercises. Many of them carry the counterexamples that later sections
refer back to.

## Why it's in the library

**Sklar's theorem is what lets dependence be asked about apart from the margins.** Any
joint distribution factors into its marginals and a copula. When the margins are continuous
that copula is unique. Heavy tails in each return series and heavy *joint* tails across
series are therefore separate objects. They need separate estimators and separate fixes.

**Chapter 5 says what a correlation coefficient does not measure.** Kendall's tau and
Spearman's rho depend on the copula alone, so they are unchanged by any strictly
increasing transformation of the margins. Pearson's ρ does not have that property. §5.4
defines tail dependence as a property of the copula. A Gaussian copula has none for
|ρ| < 1, which is exactly the assumption [[munnix-schafer-2011-copula-dependencies]]
measures as wrong on S&P 500 data. This book is the source for the definitions that paper
uses.

**It sets the limit on anything computed from a covariance matrix.** PCA, effective
dimension, eigenvalue cleaning and effective-bet counts all summarise *linear* dependence.
The copula is the full object those summaries are drawn from. Chapter 5 is the reference
for when the summary is enough and when it is not.

**§2.9 and the Archimedean families are the practical toolkit** for simulating dependent
returns with a chosen tail behaviour, as an alternative to a multivariate normal.

## Links

- [[czado-2019-analyzing-dependent-data-with-vine-copulas]] — the next step: building
  many-asset copulas from bivariate ones (vines)
- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — how the Gaussian copula
  reached credit markets (Vasicek → Li → base correlation)
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — Gaussian against Gumbel at equal
  correlation: the tail-dependence result applied to the 2008 crisis
- [[wikipedia-copula-statistics]] — formula sheet: Archimedean generator table,
  Gaussian copula density, bounds
- [[finance-tutoring-2024-sklar-theorem]] — plain-language Sklar's theorem blog post;
  overstates invariance, see its caveats
- [[nguyen-2020-introduction-to-copulas-slides]] — 37-slide walk through chapter 2, a
  quick way in before the book
- [[haugh-2016-introduction-to-copulas-slides]] — 64-slide Columbia lecture: fallacies of
  correlation, pseudo-MLE, Gaussian-copula CDO pricing
- [[munnix-schafer-2011-copula-dependencies]] — the empirical counterpart: average
  pairwise copula and tail dependence across S&P 500 constituents
- [[evans-rosenthal-2009-probability-and-statistics]],
  [[wackerly-2008-mathematical-statistics]] — the probability and statistics this book
  assumes
- [[ledoit-wolf-2004]], [[laloux-et-al-1999]] — improving the estimate of linear
  dependence, which leaves a non-Gaussian copula untouched
- [[meucci-2009]] — the diversification measure that inherits the Gaussian copula
- [[hyvarinen-oja-2000]] — the other route to non-Gaussian dependence, through independence
  rather than through the copula
