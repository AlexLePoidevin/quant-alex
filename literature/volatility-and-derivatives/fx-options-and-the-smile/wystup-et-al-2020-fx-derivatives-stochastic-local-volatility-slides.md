# FX Derivatives: Stochastic-Local-Volatility Model

| | |
|---|---|
| **Authors** | Uwe Wystup, Frédéric Bossens, Andreas Weber (MathFinance AG) |
| **Year** | 2020 (July 2020) |
| **Type** | Slides, 68pp (37 frames), from a CQF lecture |
| **PDF** | Local copy only (MathFinance slides with no licence) |
| **BibTeX** | `wystup2020slv` |
| **Status** | Reference: the vanna-volga review, the SLV calibration steps and the key take-aways are the content; the charts carry the comparisons and are not reproduced in text |

## What it is

A lecture on how FX desks price first-generation exotics (barriers, one-touch and
double-no-touch options) and why the market moved from vanna-volga to stochastic-local
volatility.

- **Vanna-volga, and its problems.** The traders' rule prices an exotic as its
  Black–Scholes value plus the cost of hedging its vanna (vega's sensitivity to spot) with
  risk reversals and its volga (vega's sensitivity to volatility) with butterflies, scaled
  by a no-touch probability. It is fast and for years fitted barrier and touch prices
  better than pure local or stochastic volatility. Its drawbacks: no guarantee of
  consistent prices across products, rules of thumb per product type, a good fit only
  near 25 delta, wings that are too flat, and arbitrage in extreme markets. The deck's
  example is a reverse knock-out EUR call CHF put in April 2012 that priced above the
  equivalent vanilla. Capping the price fixes that but makes the Greeks jump.
- **Local versus stochastic volatility.** Local volatility fits every vanilla by
  construction but implies unrealistic smile dynamics. Stochastic volatility moves the
  smile with spot the way FX traders expect but cannot fit the whole surface. Forced to
  choose, FX would pick stochastic volatility.
- **Stochastic-local volatility (SLV).** Start from a stochastic-volatility model, scale
  down its vol-of-vol by a mixing factor, then multiply by a *leverage function* so that
  the marginal distributions match the Dupire local-volatility model at every date. The
  leverage function is the local volatility divided by the root of the expected
  stochastic variance given the spot, solved step by step on a forward PDE. The mixing
  factor then moves exotic prices between the pure LV and pure SV answers while every
  vanilla stays fitted. Validate by comparing PDE and Monte Carlo prices.
- **Mixture local volatility (MLV).** Replace the continuous volatility process with a few
  discrete volatility states, fixed at the start, with zero spot–vol correlation and skew
  coming only from the local-volatility part. It is about ten times faster than SLV, and a
  mixing factor per tenor lets it fit a term structure of double-no-touch prices. The
  deck calls it arguably the market standard for FX first-generation exotics.
- **Take-aways.** Vanna-volga is outdated but still used as a quick correction and needs
  consistency wrappers; SLV is the trend for exotic flow, and its calibration is the hard
  part; MLV is the compromise between precision and speed.

## Why it's in the library

**It shows what a fitted smile does not tell you.** Every model in the deck fits the
vanillas, yet the one-touch prices differ. Exotic prices depend on how the smile moves,
which the vanilla market only partly reveals. The mixing factor is a direct control on
that unknown.

**It records how practice changed.** The 2008 vanna-volga deck in this folder presents the
method as the market's own pricing rule; twelve years later the same author calls it
outdated. The change came from its inconsistencies under stress, which the deck shows.

**These are slides from a vendor's team.** The comparisons are charts on single dates
(USD/JPY, January 2018) without tables of numbers, and the product–model matrix is the
vendor's view.

## Links

- [[merton-1976]] — jumps, the part of smile dynamics that none of the diffusion models
  here (LV, SV, SLV, MLV) includes
- [[wystup-2008-vanna-volga-pricing-pros-and-cons]] — the vanna-volga method that SLV models replaced on FX desks
- [[castagna-mercurio-2007-the-vanna-volga-method-for-implied-volatilities]] — the original vanna-volga paper
- [[monciaud-reghai-2021-singular-exotic-perturbation]] — pricing the LSV-minus-local-vol gap with exotic vanna and volga
