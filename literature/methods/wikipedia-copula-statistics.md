# Copula (statistics) — Wikipedia

| | |
|---|---|
| **Author** | Wikipedia contributors |
| **Year** | Living page; read at revision 1380044807 (accessed 2026-10-14) |
| **Type** | Encyclopedia article |
| **Link** | https://en.wikipedia.org/wiki/Copula_(statistics) — pinned: https://en.wikipedia.org/w/index.php?title=Copula_(statistics)&oldid=1380044807 |
| **BibTeX** | `wiki_copula_statistics` |
| **Status** | Reference card — cite [[nelsen-2006-introduction-to-copulas]] for anything load-bearing |

## What it is

A one-page overview of copulas, most useful as a formula sheet:

- **Motivation:** the probability-integral transform gives each variable a uniform marginal.
  The copula is the joint CDF of those uniforms, and running the transform in reverse is
  how you sample from it.
- **Definition and Sklar's theorem, stated with its conditions.** The copula is unique for
  continuous marginals and the converse holds. The density form is
  f(x) = c(F₁(x₁),…,F_d(x_d)) · ∏ f_i(x_i). This is what the
  [[finance-tutoring-2024-sklar-theorem]] post leaves out.
- **Fréchet–Hoeffding bounds W ≤ C ≤ M.** M is a copula in every dimension. W is a copula
  only for d = 2, so perfect countermonotonicity does not extend beyond two variables.
- **Families:** the Gaussian copula and its density. There is also a **table of the main
  Archimedean copulas** (Ali–Mikhail–Haq, Clayton, Frank, Gumbel, independence, Joe) with
  generators and parameter ranges. That table is the main reason to keep the page.
- **Monte Carlo under a copula model:** sample from C, apply the inverse marginals, average.
- **Empirical copula:** pseudo-observations from ranks, and the sample Spearman's ρ.
- **Stationarity:** remove autocorrelation, trend and seasonality first, because
  autocorrelation alone creates spurious dependence. In practice that means fitting a
  copula to the standardised residuals of a GARCH-type model, not to raw returns.
- **Applications.** The finance section covers VaR, stress tests, pairs trading, spread
  options and flight-to-quality. It notes that the Gaussian copula can only represent
  elliptical dependence and handles extremes poorly. It also notes the criticism of its use
  in CDO pricing (David X. Li) as a contributor to 2008. Vine and panic copulas are listed
  as the later fixes. The rest of the section, on engineering, hydrology, medicine and so
  on, is not relevant here.

## Read with care

- It is light on **tail dependence**. The coefficients λ_L and λ_U are mentioned rather than
  derived. Use Nelsen §5.4.
- It barely covers **estimation**: there is no maximum likelihood, IFM or
  canonical-maximum-likelihood fitting.
- The 2008 criticism of the Gaussian copula appears as a link to the Li article rather than
  a sourced argument. The point holds: the Gaussian copula has zero tail dependence for
  |ρ| < 1, so a correlation-only model misses joint crashes. But the source for it is
  [[munnix-schafer-2011-copula-dependencies]] together with Nelsen, not this page.

## Why it's here

It is the quickest lookup for a formula: an Archimedean generator, a Gaussian copula
density, the bounds. The Gaussian-copula criticism also lines up with the elliptical
argument in the spectral-decomposition piece. A covariance matrix describes an elliptical
dependence structure, and an elliptical structure is not where joint crashes come from.

## Links

- [[nelsen-2006-introduction-to-copulas]] — the source for everything here, with proofs
- [[nguyen-2020-introduction-to-copulas-slides]] — definitions and bounds in slide form
- [[finance-tutoring-2024-sklar-theorem]] — the informal version; this page supplies the
  conditions that post omits
- [[munnix-schafer-2011-copula-dependencies]] — empirical evidence that equity tail
  dependence exceeds the Gaussian copula's
