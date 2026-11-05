# The Sklar's Theorem in Simple Terms

| | |
|---|---|
| **Author** | Not named on the page (site: Finance Tutoring, contact Florian Campuzan) |
| **Year** | 2024 (9 February) |
| **Type** | Practitioner blog post — Finance Tutoring, "Mathematical Principles and Quantitative Finance" |
| **Link** | https://www.finance-tutoring.fr/understanding-sklar%27s-theorem-in-layman%E2%80%99s-terms%E2%80%A6/ |
| **BibTeX** | `financetutoring2024sklar` |
| **Status** | Explainer — cite [[nelsen-2006-introduction-to-copulas]] §2.3 / §2.10 instead |

## Key takeaway

A plain-language statement of Sklar's theorem: a joint distribution splits into its
marginals and a copula, F(x₁,…,x_N) = C(F₁(x₁),…,F_N(x_N)), so each can be modelled
separately. Dependence is described through ranks. The example is a Clayton copula,
C(u,v) = (u^−θ + v^−θ − 1)^−1/θ, joining a normal X to an exponential Y. When X is
re-specified as log-normal, only its marginal changes. The post closes by listing
multi-asset pricing, risk management and portfolio optimisation as uses, without detail.

## Why it's here

It is the shortest intuition for Sklar's theorem in the library. Read it before
[[nguyen-2020-introduction-to-copulas-slides]] and the book. Nothing here is load-bearing.

## Links

- [[wikipedia-copula-statistics]] — formula sheet: Archimedean generator table,
  Gaussian copula density, bounds
- [[nelsen-2006-introduction-to-copulas]] — the theorem with its conditions; chapter 5 for
  rank correlations and tail dependence
- [[nguyen-2020-introduction-to-copulas-slides]] — the next step: definitions and the
  Fréchet–Hoeffding bounds
- [[munnix-schafer-2011-copula-dependencies]] — what the dependence structure actually
  looks like in S&P 500 returns
- [[chen-et-al-2008-static-super-replicating-strategies-for-exotic-options]] — the comonotonic (upper Fréchet) case turned into a model-free price bound and a static hedge for basket options
