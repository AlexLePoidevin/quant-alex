# IEOR E4602 Quantitative Risk Management: Introduction to Copulas (lecture slides)

| | |
|---|---|
| **Author** | Martin Haugh (Columbia University, IEOR) |
| **Year** | 2016 (compiled 23 February) |
| **Type** | Graduate course lecture, Beamer slides, 64pp |
| **Based on** | McNeil, Frey & Embrechts, *Quantitative Risk Management* (2nd ed.), ch. 7; Ruppert & Matteson, *Statistics and Data Analysis for Financial Engineering*, ch. 8; Schmidt, "Coping with Copulas" |
| **PDF** | `haugh-2016-introduction-to-copulas-slides.pdf` (in this folder) |
| **BibTeX** | `haugh2016copulaslides` |
| **Status** | Explainer — cite [[nelsen-2006-introduction-to-copulas]] (theory) or McNeil, Frey & Embrechts (risk applications) instead |

## What it is

A complete graduate lecture on copulas from the risk-management side. It goes further than
[[nguyen-2020-introduction-to-copulas-slides]], which stops at definitions and bounds, and
it ends with CDO pricing. Seven parts:

1. **Definition and Sklar's theorem** (1959), with its conditions: the copula is unique
   when the marginals are continuous, and the converse holds (any copula combined with any
   marginals gives a valid joint distribution).
2. **Invariance under *strictly increasing* transformations**, with proof. This is the
   precise version of the claim [[finance-tutoring-2024-sklar-theorem]] overstates.
3. **Fréchet–Hoeffding bounds**, comonotonic and countermonotonic variables, and the
   independence, Gaussian, t and Gumbel copulas, with simulated scatter plots.
4. **Three fallacies of correlation**, each false:
   - the marginals plus the correlation matrix determine the joint distribution;
   - any ρ ∈ [−1, 1] can be reached for any given marginals (it can't: the attainable
     range is [ρ_min, ρ_max], set by the comonotonic and countermonotonic cases);
   - the VaR of a sum is largest at maximal correlation.
5. **Spearman's ρ, Kendall's τ and tail dependence** (λ_u, λ_l). The Gaussian copula has
   λ = 0; the t copula has λ_l = λ_u > 0.
6. **Estimation:** full MLE and two-step pseudo-MLE (empirical-CDF ranks, then the copula
   likelihood). Gaussian and t copulas can be fitted from Kendall's τ via
   ρ_τ = (2/π)·arcsin(Ω_ij).
7. **CDO pricing:** a one-factor Gaussian copula X_i = a_i·M + √(1−a_i²)·Z_i, defaults
   independent conditional on M, the loss distribution by numerical integration over M,
   tranche loss functions, premium and default legs, and the fair spread. Then cash
   against synthetic CDOs, implied tranche correlation (sometimes no solution for the
   mezzanine, sometimes several) and base-correlation curves.

## Why it's in the library

**It is the best single path from Sklar's theorem to a priced instrument.** Nelsen is the
theory, and [[mackenzie-spears-2014-formula-that-killed-wall-street]] and
[[donnelly-embrechts-2010-devil-is-in-the-tails]] are the history and the critique. These
slides show the working model the critique is about, equation by equation.

**The fallacies slide is the elliptical-trap argument in three lines.** Correlation plus
marginals don't fix the joint distribution, correlation can't take every value, and
diversification measured by correlation doesn't bound tail risk.

**The one-factor model is PC1 written as a credit model.** X_i = a_i·M + idiosyncratic is
a single-factor covariance structure, so calibrating one implied ρ is the same as assuming
the market mode carries all the dependence.

**Pseudo-MLE on ranks is the practical method.** It is how
[[munnix-schafer-2011-copula-dependencies]] and any empirical copula study separate the
marginals from the dependence before fitting.

## Links

- [[nelsen-2006-introduction-to-copulas]] — the theory behind sections 1–5
- [[nguyen-2020-introduction-to-copulas-slides]] — shorter deck covering only the
  definitions, to read first
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — the critique of the CDO model built
  in section 7
- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — how that model came to be
  the industry standard
- [[munnix-schafer-2011-copula-dependencies]] — rank-transformed empirical copulas for
  S&P 500 stocks
- [[wikipedia-copula-statistics]] — formula sheet for the copula families
