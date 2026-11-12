# Sticky Varswaps

| | |
|---|---|
| **Authors** | Jingyi Huang, Olaf Torné (Barclays, Hong Kong) |
| **Year** | 2021 |
| **Type** | Article — *Risk*, Cutting Edge: Volatility modelling, December 2021, 5pp |
| **PDF** | Not hosted in this repository (Risk.net article, publisher copyright) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Sticky+Varswaps%22+Huang) for the title and authors |
| **BibTeX** | `huang2021sticky` |
| **Status** | Reference: the introduction (figure 1), "Volatility regime weighting" (equation 8), the closed-form results (equations 3–4) and table A carry the argument |

## What it is

A short quant-desk paper that extends the skew-stickiness ratio (SSR), the standard
measure of how implied volatility moves when spot moves, from at-the-money volatility to
the fair strike of a variance swap.

- **The classical SSR.** Bergomi's SSR is the regression coefficient of changes in
  at-the-money-forward (ATMF) volatility on log-spot changes, normalised by the skew.
  SSR = 1 means "sticky strike" (each strike's implied volatility stays put as spot
  moves); SSR = 0 means "sticky delta" (the smile moves with spot). It is used to
  calibrate stochastic and local-stochastic volatility (LSV) models, since a mismatch
  between realised and model SSR shows up as P&L in an options book.
- **Why ATMF is not enough.** On the Nikkei 225 in the second half of 2019, ATMF
  volatility behaved close to sticky strike, but 60%-strike volatility and the variance
  swap strike had realised SSRs well below 1 at longer tenors. The authors attribute this
  to structured-product hedging flows. The ATMF SSR is also undefined where the skew
  passes through zero, which happens when short-dated skew is positive and long-dated
  skew negative.
- **The varswap SSR.** Replace ATMF volatility by the variance swap's fair strike (the
  standard option-strip value), and normalise by its "skew delta", the change in that
  strike under a sticky-strike move. The result is a weight between sticky-strike (1)
  and sticky-delta (0) dynamics for the whole surface, summarised in one number per
  maturity.
- **Closed-form approximations.** In local volatility, the varswap SSR depends on the
  term structure of the skew and also on the curvature of implied variance, unlike the
  ATMF SSR, which depends on skew alone. In Heston, there is an expression to second
  order in vol-of-variance. Both coincide with the ATMF SSR (equal to 2) at zero tenor.
  Unlike the ATMF SSR, which lies between 1 and 2 in Heston, the varswap SSR can fall
  below 1.
- **Production calculation.** For Heston-LSV they give a numerically exact procedure and
  recommend it over the approximations, whose accuracy depends on the surface. Table A
  calibrates vol-of-variance for Boeing, Uber and Carnival (September 2021) to either SSR
  and shows the choice changes the parameter.

## Why it's in the library

**It shows that the "smile dynamics" question has no single answer.** How the surface
moves with spot differs between the at-the-money point and the wings, and hedging flows
can push them apart. A model calibrated to match ATMF behaviour can still misprice the
wings, and therefore variance swaps and other products that load on them.

**It ties variance swaps to model calibration.** Because the varswap strike packs the
whole strip of strikes into one model-independent number, it is a compact way to measure
how the full smile co-moves with spot, and a natural target when choosing the free
parameters of an LSV model.

**It is a desk-quant note, not an empirical study.** The evidence is one market's
realised SSR term structure over six months and three single-stock calibrations. It is
useful as a definition and a set of formulas, not as a general result about how surfaces
behave.

## Links

- [[ambrus-capital-2022-volatility-and-the-changing-market-structure]] — a manager's view
  of how hedging flows and product supply reshape the volatility surface
- [[bossu-strasser-guichard-2005-just-what-you-need-to-know-about-variance-swaps]] — the variance swap basics this builds on
- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — the replication argument behind the varswap strike
