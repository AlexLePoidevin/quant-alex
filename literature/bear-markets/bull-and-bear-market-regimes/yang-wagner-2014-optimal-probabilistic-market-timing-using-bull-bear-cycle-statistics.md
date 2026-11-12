# Optimal Probabilistic Market Timing Using Bull Bear Cycle Statistics

| | |
|---|---|
| **Authors** | Z. George Yang and Jerry C. Wagner (Flexible Plan Investments) |
| **Year** | 2014 |
| **Type** | Working paper, SSRN 2453507 (doi 10.2139/ssrn.2453507), 46pp |
| **PDF** | Not hosted in this repository (SSRN download; no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.2453507](https://doi.org/10.2139/ssrn.2453507) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Optimal+Probabilistic+Market+Timing+Using+Bull+Bear+Cycle+Statistics%22+Yang) |
| **BibTeX** | `yang2014probabilistic` |
| **Status** | Reference: the cycle-dating procedure (Exhibit 1–2), the threshold formulas (Eq. 3–4), Tables 3–8 (in-sample tests), Tables 11–12 (long/flat/short) and Table 14 (out-of-sample, 1940–2014) carry the results |

## What it is

A market-timing rule built on a two-state bull/bear view of the stock market, written by the
research director and founder of a US tactical asset manager.

- **Dating the cycles.** Bull and bear markets are separated with three thresholds: a minimum
  gain G, a minimum loss L and a minimum duration D. The baseline is G = 20%, L = 19% and
  D = 25 trading days on the daily S&P 500 price index from 1928. L is set to 19% rather than
  20% so that 1990, 1998 and 2011 count as bear markets. For each cycle the paper records
  return, volatility and a "risk-adjusted average return" λ = μ/σ, which it finds more stable
  across bull markets than the Sharpe ratio.
- **The signal.** A Wonham filter turns daily returns into the probability that the market is in
  a bull regime, with time-varying volatility. Following the optimal-stopping work of Dai et al.
  (2010, 2011), the paper derives closed-form buy and sell thresholds for that probability, with
  a gap between them (hysteresis) to cut whipsaws. The rule is fully invested above the buy
  threshold and in T-bills below the sell threshold. A long/flat/short version adds two more
  thresholds.
- **In-sample results (daily S&P 500, 1928–2014, price index).**

  | Rule | Annual return | Max drawdown | Time in market | Trades |
  |---|---|---|---|---|
  | Probabilistic timing | 8.44% | 38.9% | 62% | 140 |
  | Golden Cross (50/200-day) | 7.02% | 71.6% | 66% | 102 |
  | Buy and hold | 5.55% | 86.2% | 100% | 0 |

  On the Shanghai Composite (1995–2014) the gap is wider: 14.5% a year against 7.2% for buy and
  hold. On monthly data the rule loses to a 2-month/10-month moving-average cross.
- **Out-of-sample.** From 1940 the parameters are re-estimated from the last ten completed
  cycles. Timing returns 8.95% a year with a 35.3% drawdown, against 8.49% and 33.2% for the
  Golden Cross and 7.24% and 56.8% for buy and hold.
- **Shorting.** On the S&P 500 the short leg loses value: long/flat/short returns 6.64% a year
  against 8.44% for long/flat, with a deeper drawdown. It helps only on the Shanghai index.

## Why it's in the library

It turns the bull/bear dating rules practitioners use (20% up, 20% down) into a trading rule,
and states plainly what that buys: mostly a shallower drawdown, not a higher return.

The edge is smaller than the headline numbers suggest:
- **The comparison flatters the rule.** Its returns are on the price index, so buy-and-hold
  loses its dividends while the rule earns T-bill interest when out of the market. The paper
  estimates this costs the rule at most about 1% a year, and it doesn't deduct trading costs.
- **The out-of-sample edge is small.** Over 1940–2014 the rule beats the Golden Cross by only
  0.46% a year, with a slightly deeper drawdown.
- **Results are sensitive to the cycle definition.** Moving L from 20% to 19% changes the
  in-sample annual return from 7.40% to 8.44% (Table 3 against Table 4).
- **Ex-post dating.** The cycles that set the parameters are dated with hindsight. The
  out-of-sample test uses only completed cycles, but a cycle is only known to be complete after
  the fact.

The rule also failed visibly in late 2008: it re-entered on 31 December 2008, during a bear
rally, three months before the March 2009 low.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — why a two-state bull/bear
  model mistakes bear rallies for new bull markets, the failure this rule shows in late 2008
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — another optimal
  trend rule derived from a two-state model, with the moving average as the answer
- [[schultz-2002-bear-market-investing-strategies]] — the Dow Theory rules of thumb for bull and
  bear phases that this formalises
- [[keller-keuning-2016-paa]] — a rule-based tactical allocation that also moves to cash in bad
  markets
- [[harvey-liu-zhu-2016]] — why an in-sample parameter choice (here the cycle thresholds)
  overstates a strategy's performance
- [[haase-neuenkirch-2023-predictability-of-bull-and-bear-markets]] — forecasting the same regimes
  in real time from macro and financial data rather than price alone
- [[hoepfner-2018-retrospective-identification-of-bull-and-bear-markets]] — a dating rule with a
  single parameter, an alternative to the gain, loss and duration thresholds used here
- [[dai-et-al-2016-optimal-trend-following-trading-rules]] — the rigorous version: two-threshold rule on the bull probability derived from HJB equations
