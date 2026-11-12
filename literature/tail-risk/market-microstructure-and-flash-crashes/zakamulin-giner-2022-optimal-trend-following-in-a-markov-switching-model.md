# Optimal Trend-Following in a Markov Switching Model

| | |
|---|---|
| **Authors** | Valeriy Zakamulin (University of Agder); Javier Giner (University of La Laguna) |
| **Year** | 2022 (version dated 25 April 2022) |
| **Type** | Working paper, SSRN 4092437, 12pp |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Optimal+Trend-Following+in+a+Markov+Switching+Model%22+Zakamulin) for the title and authors |
| **BibTeX** | `zakamulin2022trend` |
| **Status** | Reference: §4 (the derivation), §5 (the S&P 500 estimate) and §6 (comparative statics) are the whole paper |

## What it is

A short theory paper that asks which moving-average rule is best for timing a market whose
returns switch between a bull state and a bear state, and how long its window should be.

- **The model.** Returns follow a two-state Markov switching model: a bull state A and a
  bear state B, each with its own mean and volatility, and fixed probabilities α (bull to
  bear) and β (bear to bull) of switching each period. Even with normal shocks inside each
  state, the mixture has fat tails, negative skew, volatility clustering and positive
  autocorrelation that decays geometrically, ρ_k = c(1 − α − β)^k.
- **The main result.** A two-state Markov switching process can be written as an
  ARMA(1,1). The best linear predictor of the *sign* of next period's return in an
  ARMA(1,1) is an exponentially weighted sum of past returns. That is exactly the
  exponential moving average (EMA) rule: buy when price is above its EMA, sell when below.
  So the EMA is the optimal trend-following rule in this model.
- **The optimal window in closed form.** Matching autocorrelations gives the AR parameter
  φ = 1 − α − β and the decay constant λ = θ = d − √(d² − 1), where
  d = (1 + φ²(1 − 2c)) / (2φ(1 − c)) and c depends on the state means, volatilities and
  probabilities. The window size is n = (1 + λ)/(1 − λ).
- **The S&P 500 estimate.** Monthly S&P 500 price returns, January 1926 to December 2020,
  with bull and bear markets dated by the Pagan–Sossounov method: 26 bull and 25 bear
  states, average durations 28.5 and 13.5 months, annualised mean returns +23.8% and
  −28.7%, volatilities 16.2% and 19.7%. The optimal decay constant is λ = 0.797, a window
  of n = 8.85, so a 9-month EMA. The authors note its signal is almost identical to the
  popular 10-month simple moving average.
- **Comparative statics.** The optimal window is longer when the signal-to-noise ratio
  |µ_A − µ_B|/σ is lower, and shorter when regimes switch more often. A trend rule has to
  trade off accuracy in reading the trend (longer windows) against delay in spotting a
  turn (shorter windows).

## Why it's in the library

**It gives a reason for a rule that is usually justified by backtest alone.** The 10-month
moving average that runs through tactical asset allocation is normally chosen because it
worked historically. Here a 9–10 month window falls out of a model of bull and bear
markets fitted to 95 years of data, and the paper says which market features would move
it.

**It ties trend-following to the fat-tailed, regime-switching view of returns.** The
same two-state mixture that produces crashes and volatility clustering is what makes
trend rules work. Trend-following is, in this model, a way of getting out of the bear
state after it has started, which is the crash-avoidance role it plays in practice.

**The limits are plain.** It is a discrete-time model with no transaction costs, only two
states, and parameters estimated in-sample on one index. The bull and bear dating is
itself done with hindsight. The result says the EMA is the best *linear* predictor of the
sign, not that trend-following earns a premium after costs.

## Links

- [[prior-sanz-et-al-2026]] — 86 systematic tactical allocation strategies over 30 years,
  most of them trend or momentum rules of the kind this paper derives
- [[keller-keuning-2016-paa]] — a defensive allocation rule driven by how many assets are
  in an uptrend, the cross-asset counterpart of a single-index trend filter
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — trend-following named as one of the
  volatility-sensitive strategies that can amplify a sell-off
- [[antoons-2018-market-timing-opportunities-and-risks]] — the case against all-in, all-out market timing, from best- and worst-day statistics
- [[baur-et-al-2020-investing-in-gold-market-timing-or-buy-and-hold]] — moving-average and momentum rules on gold, tested against data snooping
- [[brooks-2017-a-half-century-of-macro-momentum]] — trend following on macroeconomic fundamentals instead of prices, and how the two diversify
- [[bruder-et-al-2011-trend-filtering-methods-for-momentum-strategies]] — a survey of trend filters, including the Kalman filter as an exponential moving average
- [[dai-et-al-2016-optimal-trend-following-trading-rules]] — the same hidden bull/bear model solved as an optimal-stopping problem: buy and sell thresholds on the filtered bull probability
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — 56 years of futures trend following and its performance in equity and bond crises
- [[hoffstein-sibears-2018-diversifying-the-what-how-and-when-of-trend-following]] — the practical spread between moving-average rules and lookbacks over time
- [[jusselin-et-al-2017-understanding-the-momentum-risk-premium]] — another model deriving the moving-average trend filter, with the strategy's skew, hit ratio and diversification properties
- [[li-zakamulin-2020-stock-volatility-predictability-in-bull-and-bear-markets]] — the same bull/bear dating applied to volatility forecasting
- [[maheu-mccurdy-2000-identifying-bull-and-bear-markets-in-stock-returns]] — evidence that bull and bear states get more persistent the longer they last
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — four states instead of two: bear rallies and bull corrections inside each regime, which is why two-state models switch too often on weekly data
- [[molyboga-swedroe-qian-2020-short-term-trend-a-jewel-hidden-in-daily-returns]] — faster trend signals as a diversifier for slow trend following, after costs
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the empirical evidence for trend: time-series momentum in all 58 futures markets tested
- [[rattray-et-al-2020-strategic-rebalancing]] — trend signals used to time a 60/40 portfolio's rebalancing trades
- [[schultz-2002-bear-market-investing-strategies]] — the practitioner (Dow Theory) view of bear market rallies and legs that trend rules have to sit through
- [[sethi-2016-applied-machine-learning-for-systematic-equities-trading]] — a neural-network approach that decides per stock whether to follow or fade a short-term trend, using Kaufman's efficiency ratio
- [[yang-wagner-2014-optimal-probabilistic-market-timing-using-bull-bear-cycle-statistics]] — another optimal timing rule from a two-state bull/bear model, tested on the S&P 500 since 1928
