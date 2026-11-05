# Analyzing Volatility Risk and Risk Premium in Option Contracts: A New Theory

| | |
|---|---|
| **Authors** | Peter Carr (Courant Institute, NYU), Liuren Wu (Baruch College) |
| **Year** | 2016 (Journal of Financial Economics 120(1); this copy is the SSRN version, abstract 1701685) |
| **Type** | Journal article (SSRN version), 56pp |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `carr2016analyzing` |
| **Status** | Reference: §2 (the quadratic no-arbitrage surface), §3 (option realized and expected volatility) and §6.5 (return prediction, Table 4) carry the results |

## What it is

An option-pricing framework built the way option desks actually work. It models the near-term moves of the
Black–Scholes implied-volatility surface directly, not an unobservable instantaneous
variance, and derives what shape the current surface must have to rule out arbitrage.

- **The starting point.** Each option's implied volatility moves with a drift and a
  volatility-of-volatility ("volvol"), driven by one shock that is correlated with the
  stock. Requiring no dynamic arbitrage between any option, a reference option, the stock
  and cash gives one equation. It is linear in the option's theta, vega, dollar gamma,
  dollar vanna and volga, so the authors call it the Vega-Gamma-Vanna-Volga (VGVV) model.
- **The surface is a quadratic.** With implied volatility moving in proportion to its own
  level (damped for long maturities), the whole implied-variance surface across strike and
  maturity solves a quadratic equation. Its inputs are a handful of current state values:
  - the variance level;
  - the drift and volvol of implied volatility;
  - the return–volatility correlation;
  - a maturity damping rate.
  There are no fixed model parameters. The surface depends only on where these states are
  now, not on how they will evolve, so recalibrating daily is consistent rather than a
  fudge.
- **Option-specific realized and expected volatility.**
  - The *option realized volatility* (ORV) of a contract is the volatility at which buying
    it and delta-hedging daily at Black–Scholes deltas would have broken even. It differs
    across strikes and maturities, because each option weights the price path differently.
  - The *option expected volatility* (OEV) is the forecast at which that trade has zero
    expected profit.
  - Implied volatility minus OEV is the volatility risk premium in that specific option.
    The OEV surface obeys the same quadratic shape constraint, with real-world rather than
    pricing-measure dynamics.
- **Data and fit.**
  - The data are over-the-counter S&P 500 implied volatilities from January 1997 to October
    2014, on a grid of five strikes (80–120% of spot) and eight maturities (one month to
    five years).
  - The states are tracked with an extended Kalman filter, which fits thousands of surfaces
    in seconds.
  - The model explains about 98% of the variation in the implied surface. On the expected
    surface it explains 80% using the full sample, and 67% when the auxiliary parameters
    are estimated on 1997–99 only.
- **What the states show.**
  - The implied return–volatility correlation stays between about −0.47 and −0.98 (a
    persistent negative skew). The correlation implied by realized paths hovers near zero
    and can turn positive.
  - Before both the 1998 and 2008 crises the two diverged: the option-implied correlation
    hit its most negative value while the realized one went positive (volatility rising
    with the index).
  - The implied ATM term structure usually slopes up and the expected one slopes down. The
    gap is the term structure of the risk premium, widest around 1998, 2003 and 2008.
- **Predicting returns.** The variance-risk price (the gap between the real-world and
  pricing drifts) times the return–volatility correlation gives a component of the equity
  risk premium, called RRP. In out-of-sample tests from 2000, against the historical
  average:
  - **VIX²:** R² of about 0–1% at every horizon.
  - **VIX² minus realized variance:** best at three months (4%), then fades.
  - **RRP used in a regression:** negative at short horizons, rising to 8.6% at 12 months.
  - **RRP used directly as the forecast:** with no fitted coefficients, R² is 1.7% at one
    month, 6.1% at three, 15.9% at six and 26.0% at twelve.

## Why it's in the library

**It closes the gap between option theory and option-desk practice.** Desks quote,
risk-manage and delta-hedge in implied volatility. This framework works in those units.
It makes sense of daily recalibration, and it reduces the whole surface to a few
interpretable states.

**It defines the volatility risk premium per contract.** Each strike and maturity gets its own
premium, the ORV/OEV gap, instead of a single number from a variance-swap replication. That is the quantity a
delta-hedged option position actually earns or pays.

**The return-prediction result is striking, but its setup is narrow.** It
rests on one index, one sample (1997–2014) and overlapping long-horizon returns. The
forecasts are also capped to between 0% and 20% a year, following Campbell and Thompson. The 26% twelve-month R² comes from
using the model's structure directly rather than fitting it, which is a strength. But it is
still a single-sample result.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  other side of the volatility risk premium: what a buyer of volatility pays over time
- [[barbon-buraschi-2021-gamma-fragility]] — how dealers' delta-hedging of the same option
  positions feeds back into index volatility
- [[merton-1976]] — the jump risk that this pure-diffusion framework leaves out
- [[carr-wu-2011-a-new-simple-approach-for-constructing-implied-volatility-surfaces]] — the seminar slides that introduced the approach
- [[carr-wu-2020-option-profit-and-loss-attribution-and-pricing]] — the same framework turned into option P&L attribution
