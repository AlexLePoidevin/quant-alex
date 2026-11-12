# Short-term Momentum

| | |
|---|---|
| **Authors** | Mamdouh Medhat (Cass Business School, City, University of London), Maik Schmeling (Goethe University Frankfurt, CEPR) |
| **Year** | 2022 (Review of Financial Studies 35(3), 1480–1526; online June 2021). This copy is the accepted manuscript posted on SSRN |
| **Type** | Journal article (accepted manuscript), 68pp. US common non-financial stocks July 1963–December 2018; 22 developed markets January 1993–December 2018 |
| **PDF** | Not hosted in this repository (SSRN accepted manuscript of an Oxford University Press article, no open licence) |
| **Find it** | [doi.org/10.1093/rfs/hhab055](https://doi.org/10.1093/rfs/hhab055) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Short-term+Momentum%22+Medhat) |
| **BibTeX** | `medhat2022shortterm` |
| **Status** | Reference: §1 (double sorts, persistence, size and international evidence) and §2 (costs, other momentum strategies, crash risk) carry the results |

## What it is

A study showing that last month's stock return predicts this month's in opposite
directions depending on how heavily the stock was traded: reversal for thinly traded
stocks, continuation for heavily traded ones.

- **The textbook fact it splits.** Stock returns reverse at the one-month horizon
  (Jegadeesh 1990) and continue at 2–12 months (Jegadeesh and Titman 1993). A
  conventional one-month reversal strategy (buy last month's losers, short the winners)
  earns about 3.4% a year in this sample.
- **The double sort.** Stocks are sorted into deciles on last month's return and,
  independently, last month's share turnover (NYSE breakpoints, value-weighted,
  rebalanced monthly).
  - Among the lowest-turnover stocks, buying winners and shorting losers loses 16.9% a
    year: strong reversal.
  - Among the highest-turnover stocks, the same trade earns +16.4% a year. The authors
    call this short-term momentum.
- **Its properties.** It persists for 12 months after formation, is strongest among the
  largest, most liquid and most covered stocks, and is stronger (about 22% a year) if the
  last few days of the month are skipped, which removes end-of-month liquidity trading.
  It is not explained by industry momentum, factor momentum, or the correlation of
  turnover with size, liquidity or volatility, and conventional momentum and earnings
  momentum do not span it.
- **Costs.** Estimated from turnover and half-spreads, the strategy turns over about 90%
  of each side a month but mostly in large stocks, so costs are about 0.37% a month and
  the net return is 1.00% a month (t = 3.47). The low-turnover reversal strategy's costs
  (about 1.94% a month) wipe out its gross return. A large-cap or megacap version earns
  about 0.60% a month after costs.
- **International evidence.** Across 22 developed markets from 1993, the high-turnover
  momentum strategy earns 1.39% a month (t = 3.65) and the low-turnover reversal is even
  larger (3.25% a month).
- **Crash risk.** Unlike conventional 12-month momentum, it has only a mild negative skew
  and does not develop a large negative market beta in rebounds after bear markets (beta
  about +0.05 in up months after a bear market, against about −1.06 for conventional
  momentum in the Daniel–Moskowitz regression).
- **Interpretation.** Rational models of volume and returns predict that high-volume
  moves reverse, or continue only where information asymmetry is high (small, illiquid,
  little-covered stocks). The effect is strongest in exactly the opposite stocks, so the
  authors favour an explanation in which some traders under-infer information from
  prices. Supporting this, last month's return times turnover predicts next year's growth
  in gross profits and earnings.

## Why it's in the library

**It shows that one-month reversal and momentum are the same signal split by volume.**
Treating last month's return as a single reversal factor averages two opposite effects.
Conditioning on turnover recovers a momentum effect as large as conventional 12-month
momentum, in the most liquid stocks.

**It is a momentum strategy that is cheap to trade and does not crash the usual way.**
Most of its weight sits in large and mega caps, and its net return survives conservative
half-spread costs. It lacks the rebound crashes that make conventional momentum
dangerous after bear markets.

**It connects to the reversal literature.** Short-horizon reversals are usually read as
compensation for providing liquidity; this paper shows where that reading stops holding:
when volume is high, prices continue instead.

**Limits.** These are corner portfolios of a ten-by-ten double sort, with costs
estimated rather than measured and no price impact. Turnover deciles are relative, and
the strongest return figure (skipping the end of the month) is a refinement chosen in the
same sample.

## Links

- [[collin-dufresne-daniel-2015-liquidity-and-return-reversals]] — short-horizon reversals in large stocks as liquidity provision, the effect this paper splits by volume
- [[kelly-moskowitz-pruitt-2021-understanding-momentum-and-reversal]] — conventional momentum and long-term reversal explained by time-varying betas
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — momentum in an asset's own returns, the futures counterpart
- [[arnott-et-al-2019-alices-adventures-in-factorland]] — why published factor returns tend to shrink after publication
