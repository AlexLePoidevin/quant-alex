# Option Profit and Loss Attribution and Pricing: A New Framework

| | |
|---|---|
| **Authors** | Peter Carr, Liuren Wu |
| **Year** | 2020 (*Journal of Finance* 75(4), 2271–2316). The copy here is the accepted ("forthcoming") version from SSRN 3148796 |
| **Type** | Paper, 63pp. Empirical part on S&P 500 index options from OptionMetrics, January 1996 to April 2016 |
| **PDF** | Local copy only (SSRN copy of a *Journal of Finance* article; no open licence) |
| **BibTeX** | `carr2020option` |
| **Status** | Reference: §II (Theorems 1–2 and equation 9) is the whole idea; §IV.G (out-of-sample trading) and §V (limits) are the parts to reread |

## What it is

A way to price an option from its daily P&L rather than from its payoff at expiry. A
trader marks an option to market every day and explains the day's P&L with Black–Scholes
Greeks. The paper asks: if that daily attribution is done with the option's own implied
volatility, what does "no arbitrage" require of that implied volatility?

- **The P&L attribution.** Expand the Black–Merton–Scholes (BMS) price to first order in
  time and second order in spot and implied vol. The day's P&L is theta, plus delta and
  gamma on the spot move, plus vega on the implied-vol move, plus volga (vol of vol) and
  vanna (spot–vol covariance).
- **The pricing relation (Theorem 1).** Take risk-neutral expectations and require zero
  expected excess return. The option's theta loss must then exactly balance four
  expected gains:
  - gamma × spot variance;
  - vega × the expected drift of implied vol;
  - volga × the variance of implied vol;
  - vanna × the covariance of spot and implied vol.
- **The algebraic form (Theorem 2).** In BMS all the Greeks are multiples of cash gamma,
  so cash gamma cancels. What remains is one equation: the fair implied variance equals
  the spot variance, plus a term for the expected drift of implied vol, plus a
  covariance term and a vol-of-vol term. Both of those scale with the option's
  standardised moneyness.
- **Top-down, not bottom-up.** Classical models (Heston, Lévy, local vol) specify the full
  dynamics of the underlying and price every option off that one reference. That keeps
  options consistent with each other, but it is wrong if the dynamics are wrong. Here each
  option is priced only against forecasts of its own first and second moments. Consistency
  across strikes comes only from extra assumptions about common movement.
- **The cross-section under commonality assumptions.**
  - At the money, defined by standardised moneyness zero, vanna and volga vanish. The ATM
    term structure then reflects only the expected drift of implied vol.
  - Away from the money, after vega-hedging with the ATM option, the skew reflects the
    spot–vol covariance and the curvature reflects vol of vol.
- **Evidence on SPX options, 1996–2016.**
  - Implied-vol drifts extracted from the ATM term structure forecast future
    implied-vol changes with slopes close to 1 for maturities up to six months.
  - The skew implied by historical spot–vol covariance is on average flatter than the
    market's: the market skew is steeper than the time series warrants.
- **A stylised trading test.** Spreads go long the ATM option and short the OTM option,
  sized by the gap between the market smile and the smile implied by forecast
  covariances. They are vega-neutral, delta-hedged daily and held 21 days.
  - On average the strategy is short OTM puts and long OTM calls.
  - Out of sample from 2000, the annualised information ratio rises from 0.52 for the
    one-month spreads to 3.81 for the twelve-month spreads.
  - There are no transaction costs, and the weights are not optimised.

## Why it's in the library

**It is how options desks actually think.** The relation is the daily theta-versus-gamma
trade-off, extended to vanna and volga. That is the same set of exposures behind the
vanna–volga smile method used in FX. Reading the smile this way turns it into three
forecastable quantities:
- skew as expected spot–vol covariance;
- curvature as expected vol of vol;
- term-structure slope as expected implied-vol drift.

**It separates forecasting from pricing.** Whether an option is cheap becomes a question of
whether your forecast of realised variance and covariance differs from what the smile
implies. That is a mean–variance problem on implied-vol returns. The paper says it could
be handled with factor-model covariance machinery, much as equity risk models handle stock
returns.

**It names its own limits.**
- The relation assumes continuous paths, so jumps, which matter most for short-dated and
  far-OTM options, are left out. The authors suggest handling them separately with
  scenarios and stress tests.
- The trading test is stylised: no costs, and a single sample that includes 2008.
- Nothing guarantees static no-arbitrage across the whole surface.

**It explains long-dated smiles.** A stationary stochastic-volatility model says smiles
should flatten at long maturities, by the central limit theorem. SPX and FX smiles do not
flatten. Here a long-dated option's smile is set by its own large implied-vol variation,
so a steep long-dated skew is not a puzzle.

## Links

- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]] — the market-maker side of
  the same gamma exposures: who holds them and what it does to spreads
- [[baldacci-et-al-2020-options-market-making-in-high-dimension]] — managing an inventory of
  many options through their vega exposures, the bottom-up use the paper contrasts with its
  own
- [[merton-1976]] — the jump risk the framework deliberately leaves out
- [[shreve-2004]] — Itô's lemma and risk-neutral expectation, the two steps the derivation
  rests on
- [[carr-wu-2016-analyzing-volatility-risk-and-risk-premium-in-option-contracts]] — the implied-volatility dynamics this attribution rests on
