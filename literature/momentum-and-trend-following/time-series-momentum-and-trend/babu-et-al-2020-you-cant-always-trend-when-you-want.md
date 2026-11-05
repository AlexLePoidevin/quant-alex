# You Can't Always Trend When You Want

| | |
|---|---|
| **Authors** | Abhilash Babu, Brendan Hoffman, Ari Levine, Yao Hua Ooi, Sarah Schroeder, Erik Stamelos (AQR Capital Management) |
| **Year** | 2020 (working paper 2019) |
| **Type** | Paper. SSRN 3487134, 27pp; published in *Journal of Portfolio Management* 46(4), 52–68 (2020). Hypothetical trend strategy on 67 futures markets, 1880–2018 |
| **PDF** | Local copy only (SSRN download of an AQR paper; no open licence) |
| **BibTeX** | `babu2020trend` |
| **Status** | Reference: read in full. The decomposition (Equations 1–2), Exhibits 3–8 and Appendix C carry the argument |

## What it is

AQR's explanation of why trend following did poorly in 2010–2018, using a decomposition of a
trend strategy's Sharpe ratio into three parts.

- **The strategy.** The Hurst–Ooi–Pedersen backtest: equal-weighted 1-, 3- and 12-month
  time-series momentum signals on 67 markets (29 commodities, 11 equity indices, 15 bond
  markets, 12 currency pairs), each position sized to equal risk, the portfolio scaled to 10%
  ex-ante volatility and rebalanced monthly. Data go back to 1880, partly from hand-transcribed
  Chicago Board of Trade reports. Returns are net of estimated transaction costs, gross of fees.
- **The decomposition.** For each market and year they regress the trend strategy's Sharpe
  ratio on the absolute Sharpe ratio of the market itself (the size of the move). This gives:
  - **market moves**: the average absolute Sharpe ratio of the underlying markets;
  - **trend efficacy**: the intercept and slope that turn a given move into trend profit
    (negative intercept because trendless markets lose money, slope below 1);
  - **diversification**: a multiplier from the average per-market trend Sharpe ratio to the
    portfolio Sharpe ratio, which depends on correlations between the trend returns.
- **The finding.** The weak 2010–2018 decade is explained almost entirely by smaller market
  moves. Efficacy was about the same as in the full sample: in years with large moves, such
  as 2014, trend profited as expected. Diversification was not worse either: the multiplier
  was about 4.1× in 2010–2018 against about 3.5× on average across rolling decades (read
  from Exhibit 6). For context, the SG Trend Index had a Sharpe ratio of 0.05 over 2010–2018
  against 0.28 since 2000.
- **Decades.** In the strongest decade, the 1970s, all three factors were favourable. The
  authors find no persistent pattern in any factor over time.

## Why it's in the library

**It gives a way to tell a broken strategy from a quiet market.** A trend program that loses
money can be failing to convert moves into profit (efficacy), losing diversification, or
simply facing small moves. Only the first two would mean the strategy has changed.

**It quantifies the intuition that trend needs big moves.** That is the same mechanism the
Amundi model derives analytically: trend profit rises with the absolute Sharpe ratio of the
underlying market.

**Limits.** This is an AQR paper defending a strategy AQR runs. The backtest is
hypothetical, transaction costs before recent decades are inflated estimates, and the
"current decade" sample is nine years. The decomposition attributes past performance but
does not predict when large moves return.

## Links

- [[jusselin-et-al-2017-understanding-the-momentum-risk-premium]] — a model in which trend performance rises with the absolute Sharpe ratio of the market
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — another long-history trend backtest, focused on crisis periods
- [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]] — AQR on trend as a crisis hedge
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — trend following as optimal when markets persist in bull or bear states
