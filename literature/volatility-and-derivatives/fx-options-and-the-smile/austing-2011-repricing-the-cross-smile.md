# Repricing the Cross Smile: An Analytic Joint Density

| | |
|---|---|
| **Authors** | Peter Austing (Barclays Capital) |
| **Year** | 2011 (first draft March 2009; this draft 17 May 2011; published in *Risk*, July 2011) |
| **Type** | Working paper, 13pp (SSRN 1882343); the published version is a *Risk* "Cutting Edge" article |
| **PDF** | Not hosted in this repository (SSRN working paper with no open licence; the *Risk* version is publisher copyright) |
| **Find it** | Use the link above, or [search Google Scholar](https://scholar.google.com/scholar?q=%22Repricing+the+Cross+Smile%3A+An+Analytic+Joint+Density%22+Austing) for the title and authors |
| **Link** | <https://ssrn.com/abstract=1882343> |
| **BibTeX** | `austing2011cross` |
| **Status** | Reference: §2–3 (best-of options and the density) carry the result; §5 is the worked basket example; §6 gives the no-arbitrage conditions |

## What it is

A short paper on a problem specific to foreign exchange: an option on two currency pairs
must also be consistent with the options on the third pair they imply.

- **The problem.** Take EUR/USD and GBP/USD as the two "driving" pairs. EUR/GBP is then
  fixed as their ratio, and its options are liquid too. In Black–Scholes the three
  volatilities pin down the correlation through the *triangle rule*,
  σ₃² = σ₁² − 2ρσ₁σ₂ + σ₂². Dealers back the correlation out of at-the-money vols this
  way. But putting two smiles together with that single correlation (two correlated
  local-vol processes, or a Gaussian copula) gives a cross smile that is typically too
  flat and does not even reprice the at-the-money cross option. Any multi-currency
  product priced that way can be arbitraged against EUR/GBP vanillas, or bleeds money as
  the cross vega is hedged.
- **The key observation: best-of options.** A best-of option pays the better of a call on
  pair 1 and a call on pair 2 (each scaled by its strike). Depending on where spot goes,
  it turns into a vanilla on pair 1, a vanilla on pair 2, or a call on the cross plus a
  forward. And the prices of best-ofs for all strike pairs determine the whole joint
  distribution: differentiating the payoff gives a dual digital, whose value is the joint
  cumulative distribution, and one more differentiation gives the joint density. This is
  the two-dimensional version of Breeden–Litzenberger.
- **The construction.** Black–Scholes has a closed form for best-of options in terms of
  the three volatilities. Austing plugs into it each pair's *smile* volatility at the
  relevant strike (σ₁ at K₁, σ₂ at K₂, σ₃ at K₁/K₂). Because each limit of the formula is
  a Black–Scholes vanilla price at the market's own volatility, the resulting function
  reprices all three smiles by construction. Differentiating it gives an analytic joint
  density, with no numerical calibration.
- **N dimensions.** The same argument works for N driving pairs and all their crosses.
- **The basket test.** A one-year at-the-money call on an equal basket of EUR and JPY
  against USD (14 April 2008, notional $100m), back-tested by hedging daily with vanillas
  at 10- and 25-delta and at-the-money plus forwards. The final hedging P&L, which should
  be zero for a perfect model, was about 87bp of notional using Black–Scholes without a
  smile, 37bp with a Gaussian copula calibrated to the at-the-money cross, and 12bp with
  this density.
- **What it does not guarantee.** The density always integrates to 1, but it is only
  real and non-negative if the implied correlation stays between −1 and 1 for every strike
  pair. That gives a necessary no-arbitrage condition on a triangle of smiles: at every
  strike combination, each volatility must be less than the sum of the other two. The
  density is also not unique; it is one consistent choice among many.

## Why it's in the library

It is the clearest example of a theme that runs through the FX smile material: in FX the
"correlation" between two pairs is not a free parameter but is implied by a third liquid
market, so multi-asset pricing becomes a smile-consistency problem.

The paper is also a compact lesson in dependence modelling. A copula joins two marginals
with a few parameters; this construction instead fits an entire extra marginal (the cross
smile). The comparison is instructive next to the copula notes, where the dependence
structure usually has to be assumed. The one-trade back-test is an illustration, not
evidence of general performance.

## Links

- [[nelsen-2006-introduction-to-copulas]] — the general theory of joining marginals into a
  joint distribution, which this paper does analytically with an extra marginal as the
  constraint
- [[finance-tutoring-2024-sklar-theorem]] — why marginals alone do not fix the joint
  distribution, the non-uniqueness the paper notes
- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — a single Gaussian-copula
  correlation used as the market's price of dependence, the shortcut the paper shows
  fails for FX crosses
- [[bossens-et-al-2010-vanna-volga-methods-applied-to-fx-derivatives]] — the FX quote
  conventions (ATM, risk reversals, butterflies) from which each of the three smiles is
  built
