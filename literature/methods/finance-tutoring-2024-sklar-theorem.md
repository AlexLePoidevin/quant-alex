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

## Read with care

- **Invariance is overstated.** The copula is unchanged only under *strictly increasing*
  transformations of each variable (Nelsen Thm 2.4.3). Normal → log-normal through exp is
  one of those. Swapping in an arbitrary new marginal and keeping C is a modelling choice
  that the theorem does not guarantee.
- **It contradicts itself on ranks.** Under strictly increasing transformations the ranks,
  Kendall's τ and Spearman's ρ are all preserved, because they depend on the copula alone.
  The post also warns that marginal changes can alter rank correlation, which cannot happen
  in the case it just described.
- **The theorem is stated without its conditions.** The copula is unique only for
  continuous marginals. The converse, that any copula combined with any marginals gives a
  valid joint distribution, is not mentioned.
- **Clayton's tail asymmetry is not specified.** With θ > 0 it has *lower*-tail dependence
  and no upper-tail dependence (Nelsen §5.4). That is the direction that matters for joint
  crashes.

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
