# Optimal Trend Following Trading Rules

| | |
|---|---|
| **Authors** | Min Dai (NUS), Zhou Yang (South China Normal University), Qing Zhang (University of Georgia), Qiji Jim Zhu (Western Michigan University) |
| **Year** | 2016 (the copy is the SSRN 1630903 preprint; published in *Mathematics of Operations Research* 41(2), 626–642, 2016) |
| **Type** | Paper, 20pp. Stochastic control theory, with a simulation and an S&P 500 test over 1972–2011 |
| **PDF** | Not hosted in this repository (SSRN preprint of an INFORMS journal article) |
| **Find it** | [doi.org/10.1287/moor.2015.0743](https://doi.org/10.1287/moor.2015.0743) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Optimal+Trend+Following+Trading+Rules%22+Dai) |
| **BibTeX** | `dai2016trend` |
| **Status** | Reference: §2 (set-up), Theorem 1 (the two-threshold rule) and §4 (simulations and market test) carry the result |

## What it is

A proof that, in a market that switches unobservably between bull and bear, the best
long/flat strategy is a trend-following rule.

- **The model.** The stock's drift switches between μ₁ > 0 (bull) and μ₂ < 0 (bear)
  following a hidden two-state Markov chain, with constant volatility. The investor sees
  only prices and is either all in the stock or all in cash.
  - **Costs:** each purchase and sale pays a proportional cost.
  - **Objective:** maximise expected log growth of wealth over a finite horizon.
  - **Difference from earlier work:** this extends the authors' earlier single-share
    version, whose wealth process was not self-financing.
- **The optimal rule.** Track p, the filtered probability that the market is in the bull
  state; it updates from each day's return. Buy when p rises above an upper boundary p_b*.
  Sell when it falls below a lower boundary p_s*. Do nothing in between.
  - **Boundaries:** they come from a system of HJB variational inequalities, and they rise
    as the horizon nears (never buy right before the end).
  - **Practice:** constant limits work well. The structure is the same as a moving-average
    crossover with a band, but derived rather than assumed.
- **Simulation.** The parameters are the ones used in the authors' earlier paper: bull drift
  18%, bear drift −77%, volatility 18.4%, mean bull spell about 2.8 years, mean bear spell
  about 5 months. The thresholds come out at about 0.80 (sell) and 0.95 (buy).
  - **Results:** over 40 years the trend rule turns $1 into 75.8 on average (11.4% a
    year), against 5.6 (4.4%) for buy and hold, with about 41 trades.
  - **Single paths:** these vary enormously.
- **Market test (S&P 500, 1972–2011).** Parameters are first estimated on 1962–1972. Up and
  down trends are defined as moves of at least 20%, and the parameters are updated once a
  year as new trends complete.
  - **Return:** the rule earns 11.0% a year against 9.8% for buy and hold with dividends,
    with a smoother equity curve.
  - **Sharpe ratio:** 0.217 against 0.128, frequency not stated. The simulation section
    calls a similar number "monthly".
  - **Correction:** the paper also corrects the earlier paper's backtest, which had left
    out reinvested dividends.

## Why it's in the library

**It gives trend following a derivation.** Moving-average rules are usually justified by
backtests. Here a buy/sell band on the filtered bull probability comes out as the optimal
policy when trends are regimes you can't see. It explains why such a rule is long/flat
with hysteresis rather than a single cut-off.

**It sits between regime models and trend rules.** The same hidden-Markov bull/bear set-up
appears in the regime-dating papers in `bear-markets/`. This paper turns it into a trading
decision.

**Limits.** The market test is one index on one historical path. There is no significance
test, and the cost assumed in the market test is not stated. The result depends on
estimating drift and switching rates, which the authors themselves find unstable across
decades. A bear drift of −77% a year is an extreme calibration. The rule is long/flat
only, with no leverage or shorting.

## Links

- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — the same bull/bear switching set-up, solved for the optimal moving-average window instead
- [[yang-wagner-2014-optimal-probabilistic-market-timing-using-bull-bear-cycle-statistics]] — a practitioner version: Wonham-filter bull probability with closed-form buy and sell thresholds
- [[maheu-mccurdy-2000-identifying-bull-and-bear-markets-in-stock-returns]] — estimating the bull and bear regimes this rule assumes
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the empirical case for trend following across futures markets
