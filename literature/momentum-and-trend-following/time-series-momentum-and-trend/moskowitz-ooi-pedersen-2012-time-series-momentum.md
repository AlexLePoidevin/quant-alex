# Time Series Momentum

| | |
|---|---|
| **Authors** | Tobias J. Moskowitz (Chicago Booth), Yao Hua Ooi (AQR), Lasse Heje Pedersen (NYU, CBS, AQR) |
| **Year** | 2012 (Journal of Financial Economics 104(2), 228–250); this copy is the September 2011 working-paper version, Chicago Booth / IGM Working Paper No. 79 |
| **Type** | Journal article (working-paper version), 62pp. 58 futures and forwards (24 commodities, 12 currency pairs, 9 equity indices, 13 government bonds), data from 1965, strategy results from 1985 to 2009 |
| **PDF** | Not hosted in this repository (SSRN working paper of an Elsevier article, no open licence) |
| **Find it** | [doi.org/10.1016/j.jfineco.2011.11.003](https://doi.org/10.1016/j.jfineco.2011.11.003) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Time+Series+Momentum%22+Moskowitz) |
| **BibTeX** | `moskowitz2012tsmom` |
| **Status** | Reference: §3 (predictability regressions and the 12-month strategy), §4 (alpha, extreme markets, correlations) and §5–6 (decomposition, speculator and hedger positions) carry the results |

## What it is

The paper that named and documented time-series momentum: an asset's own past return
predicts its own future return, across every major futures market.

- **The regression evidence.** Each instrument's monthly return, scaled by its ex ante
  volatility, is regressed on its own lagged scaled return at lags of 1 to 60 months, in a
  pooled panel. The t-statistics are positive for the first 12 lags (continuation) and
  turn negative after that (a smaller, partial reversal over the next four years). Using
  only the sign of past returns gives the same pattern.
- **The strategy.** Each month, go long an instrument if its past 12-month excess return is
  positive and short if negative, hold for one month, and size each position to 40%
  annualised ex ante volatility (volatility from an exponentially weighted average of
  squared daily returns). The diversified portfolio (TSMOM) averages across all
  instruments and runs at about 12% volatility.
- **It works everywhere.** All 58 contracts have a positive 12-month time-series
  momentum return over 1985–2009. Results are robust to other look-back and holding
  periods, and strongest with a 12-month look-back held for a month.
- **Size of the effect.** The diversified portfolio has a Sharpe ratio above 1, about
  2.5 times that of the equity market over the same period. Over 1966–1985, with fewer
  instruments, it still has a Sharpe ratio of about 1.1.
- **Alpha and exposures.** Against the MSCI World index and the Fama–French factors the
  alpha is about 1.58% a month. Market, size and value loadings are insignificant, but the
  loading on cross-sectional momentum (UMD) is positive and significant. Against the
  multi-asset value and momentum factors of Asness, Moskowitz and Pedersen the alpha is
  still 1.09% a month (t = 5.40).
- **A "smile" against the market.** TSMOM returns are highest in the most extreme
  market months, up and down: the coefficient on the squared market return is positive
  while the linear beta is insignificant. In 2008 it lost in the third quarter, then made
  large profits in October–December as markets kept falling, and lost sharply when the
  trends reversed in March–May 2009. The authors read the smile as the opposite of
  crash-risk compensation.
- **Correlation structure.** Time-series momentum strategies are more correlated with
  each other across asset classes than the underlying assets are, which the authors
  say no existing behavioural model predicts.
- **Where the returns come from.** A Lo–MacKinlay/Lewellen decomposition attributes
  nearly all of both time-series and cross-sectional momentum profits to positive
  autocovariance of each asset's own returns; lead-lag effects across assets are small
  and of the wrong sign.
- **Who wins and who loses.** CFTC Commitments of Traders data show speculators
  positioned with the trend for about a year and cutting positions as it reverses, while
  hedgers take the other side. Both spot price changes and roll yield contribute to the
  momentum, but only the spot part reverses later.

## Why it's in the library

**It is the reference definition of trend following as a strategy.** The 12-month sign
signal with volatility scaling is the baseline most later trend papers compare against,
and it is close to what managed-futures funds trade. Later variants (different look-backs,
moving averages, filters) are best read as changes to this one rule.

**It separates time-series from cross-sectional momentum.** Time-series momentum asks
whether an asset's own past return predicts its future return; cross-sectional momentum
compares assets with each other. The paper shows both are driven mostly by the same
autocovariance, and that the futures-based TSMOM factor partly captures stock momentum
(UMD) even though it holds no individual stocks.

**It explains why trend is used as crisis protection.** The smile against the market,
with late 2008 as the clearest case, is the empirical basis for the crisis-alpha claims made for
trend following elsewhere in the library.

**Read it with its limits in view.** The headline Sharpe ratio is gross of trading costs
and fees, with the 40% volatility sizing chosen for comparison rather than
implementation. The sample ends in 2009, the best period for the strategy; the years
after publication (2010s) were much weaker for trend followers, which is consistent with
the paper's own caution that a rational explanation is not ruled out and returns may not
persist at this size.

## Links

- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a model in which a moving-average trend rule is optimal
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — the same kind of futures trend strategy extended back to 1960 and tested in equity and bond crises
- [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]] — trend against index puts as a crisis hedge
- [[kelly-moskowitz-pruitt-2021-understanding-momentum-and-reversal]] — cross-sectional stock momentum explained by time-varying betas
- [[brooks-2017-a-half-century-of-macro-momentum]] — trend applied to macroeconomic data instead of prices
- [[fung-hsieh-2001-the-risk-in-hedge-fund-strategies-trend-followers]] — trend-follower returns modelled as lookback straddles, the option view of the same smile
- [[cfm-2018-the-convexity-of-trend-following]] — why a trend rule is mechanically convex in the asset it trades
- [[babu-et-al-2020-trends-everywhere]] — the same strategy tested on 82 assets and 16 equity factors the original study never used
- [[garg-et-al-2021-momentum-turning-points]] — why time-series momentum fails around turning points, and blending fast and slow signals
- [[hutchinson-obrien-2014-is-this-time-different-trend-following-and-financial-crises]] — the autocorrelation behind time-series momentum weakens for years after financial crises
