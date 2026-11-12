# Singular Exotic Perturbation

| | |
|---|---|
| **Authors** | Florian Monciaud; Adil Reghai |
| **Year** | 2021 (January 2021; this version December 2021; SSRN 3860721) |
| **Type** | Working paper, 17pp |
| **PDF** | Not hosted in this repository (SSRN download with no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3860721](https://doi.org/10.2139/ssrn.3860721) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Singular+Exotic+Perturbation%22+Monciaud) |
| **BibTeX** | `monciaud2021singular` |
| **Status** | Reference: §2 (P&L explain), §4 (the expansion) and §5 (the scenario recipe) carry the method; the autocall tests in §6 are shown only as charts |

## What it is

A fast approximation for how much a local-stochastic-volatility (LSV) model changes the
price of an exotic option compared with plain local volatility (LV), without running the
LSV model.

- **The problem.** Local volatility fits every vanilla option but implies the wrong smile
  dynamics: how the smile moves when spot moves. For exotics such as autocalls that matters.
  The paper's P&L explain shows a seller who hedges an autocall with LV loses steadily on
  the vanna term (spot and volatility moving together). LSV fixes this by adding a
  stochastic volatility factor while keeping the vanilla fit. To match observed equity
  smile dynamics it needs extreme parameters (fast mean reversion, high vol-of-vol,
  spot–vol correlation near −1), and calibration is slow.
- **Exotic greeks.** Hedge an exotic's vega with vanillas first (at every strike and
  maturity), then measure what risk is left. The leftover gamma, vanna and volga are the
  "exotic greeks". They are exactly zero for anything that can be replicated with vanillas.
- **The method.** Because the stochastic-volatility parameters are large, a singular
  perturbation expansion applies. Expand without calibrating to vanillas, then correct
  with a first-order Newton step ("price adjustment") so the vanilla fit is restored. The
  result: the LSV price is about the LV price, plus a vol-of-vol term times the exotic
  volga, plus a correlation term times the exotic vanna. The coefficients depend only on
  the stochastic-volatility parameters; the exotic greeks depend only on the product and
  the volatility surface.
- **Computing it cheaply.** The exotic greeks come from three local-volatility prices
  under specially built volatility scenarios. Each scenario is constructed so that the
  vanilla prices do not change, which guarantees the correction is zero on vanillas.
- **Tests.** On 28 autocall structures (seven barrier levels, maturities of one to eight
  years) and hundreds of random stochastic-volatility parameter sets, the formula is
  compared with a full LSV Monte Carlo. The paper shows the agreement only as charts, with
  no error statistics.

## Why it's in the library

**It explains why matching today's smile is not enough.** Two models fitted to the same
vanillas can price an exotic differently, because they disagree about how the smile moves.
The exotic vanna and volga name that difference and measure it.

**It turns smile dynamics into a small number of sensitivities.** The LSV correction splits
into "how exposed is this product" (exotic greeks) and "how strong are the smile dynamics"
(model parameters). That split is useful for risk management, and for backing out the
stochastic-volatility parameters from observed exotic prices.

**Caveat.** It is a short practitioner paper. The accuracy claim rests on charts for one
product family.

## Links

- [[derman-et-al-1995-static-options-replication]] — a static barrier hedge is matched to
  today's model; what it leaves exposed is exactly this smile-dynamics risk
- [[kirkby-deng-2019-static-hedging-and-pricing-of-exotic-options-with-payoff-frames]] — the
  vanilla-replication side of the same split: everything a vanilla portfolio can hedge has
  zero exotic greeks
