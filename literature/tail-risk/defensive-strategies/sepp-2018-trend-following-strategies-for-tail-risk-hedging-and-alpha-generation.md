# Trend-Following Strategies for Tail-Risk Hedging and Alpha Generation

| | |
|---|---|
| **Authors** | Artur Sepp |
| **Year** | 2018 (23 April 2018) |
| **Type** | Practitioner research note, SSRN 3167787, 36pp |
| **PDF** | Not hosted in this repository (SSRN download, no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Trend-Following+Strategies+for+Tail-Risk+Hedging+and+Alpha+Generation%22+Sepp) for the title and authors |
| **BibTeX** | `sepp2018trend` |
| **Status** | Reference: the convexity-by-measurement-frequency results and the S&P 500 trend model (half-life sweep) carry the argument; the risk-parity allocation is a short illustration |

## What it is

A quant's study of when trend following actually works as a crash hedge. The central claim is
that a trend strategy's protective shape, its **convexity** (gaining in big down and big up
markets), only appears when returns are measured over a period longer than the strategy
takes to change its position.

- **Two risk statistics.** Skewness of returns, and a convexity beta: the coefficient on the
  squared benchmark return in a regression of strategy returns on the benchmark return and
  its square.
- **Hedge fund indices, 2003–2018, monthly.** Short-volatility funds are negatively skewed
  (−2.5) and concave. Long-volatility funds are positively skewed (1.6) but not convex: their
  gains don't arrive in the tail. Tail-risk funds are both (skew 4.5, convexity 1.17) but with
  negative alpha. The SG Trend CTA index is convex (1.03) with a positive return. The
  regressions explain only about 10% of the variance.
- **Measurement frequency decides the answer.** For the SG Trend index, 2000–2018, skewness
  goes from −0.4 for daily returns to 1.1 for quarterly and 0.6 for annual. The convexity
  beta is negative for daily and weekly returns and about 1.0 for monthly and annual. Trend
  is no protection against shocks that play out within a month.
- **Conditional on the S&P 500's quarter.** In the worst quarter of S&P outcomes (−35% to
  −1%), CTAs averaged +4.6%; in the best quarter (+6% to +35%) +3.8%. In the middle buckets
  (choppy or slowly rising markets) they lost −1.8% and −0.6%.
- **Autocorrelation explains the 2011–18 slump.** CTAs had a Sharpe ratio of 0.49 over
  2000–2011 against 0.06 for the S&P 500; over 2011–2018 it was 0.06 against 1.13. The lag-1
  autocorrelation of quarterly S&P returns moved from +0.13 to −0.43 (significant), i.e. a
  mean-reverting market. He proposes an "autocorrelation vol ratio" (quarterly move against
  average daily move) to measure this within a single quarter, and finds trending quarters
  are only about a quarter of the sample.
- **A one-asset trend model.** An exponential moving average of volatility-normalised S&P 500
  returns, following the CFM construction, with position capped at ±100%, 1951–2018 and no
  costs. With a 4-month half-life it correlates 0.42 with the SG Trend index and has a Sharpe
  ratio of 0.54 against 0.58 for the index. Sweeping the half-life from 1 to 16 months:
  positive convexity on quarterly returns needs monthly rebalancing and a half-life of about
  4 months or less; on annual returns, a half-life under about 8 months. Slower systems carry
  more market beta; faster ones trade more and earn less in a rising market.
- **Trend versus stock momentum, 2000–2018.** Market-hedged stock momentum is concave
  (convexity −1.41) while CTAs are convex. In a PCA of the strategies, both load on a shared
  "autocorrelation" eigen-portfolio, but CTAs load on it more.
- **Allocation example.** HFR Risk Parity funds and the SG Trend index each had a maximum
  drawdown of about −22% over 2003–2018 (quarterly returns); a 50/50 mix had −11% with
  almost the same Sharpe ratio (0.83 against 0.87), because their drawdowns didn't overlap in
  this sample.

## Why it's in the library

It gives a precise reason why trend following hedges some crashes and not others: the
hedge is only as fast as the signal's half-life, so a fast crash (1987, February 2018) is
outside its reach and a slow bear market is inside it. That frames the crisis-alpha evidence
in [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] and the put-versus-trend
comparison in [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]].
The convexity-beta regression is a simple check to run on any strategy that claims to
protect a portfolio.

It is a practitioner note, not a refereed paper. The convexity regressions have low R²
(often 2–12%) and few observations, the model ignores costs and uses the S&P 500 index as a
proxy for futures, the 4-month half-life is chosen to match the CTA indices in the same
data, and the risk-parity drawdown halving rests on one 15-year sample.

## Links

- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — the long-history
  evidence that trend pays in equity and bond crises
- [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]] — puts against
  trend as crash hedges, and why the worst month is rarely the first month of a drawdown
- [[harvey-et-al-2019-the-best-of-strategies-for-the-worst-of-times]] — trend scored
  against other crisis hedges over 1985–2018
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — the optimal
  moving-average window derived from a bull/bear model
- [[carr-lee-2003-trading-autocorrelation]] — autocorrelation as something that can be traded
  directly
- [[hood-et-al-2019-risk-parity-is-not-short-volatility]] — the risk-parity side of the
  allocation example
- [[harvey-et-al-2018-the-impact-of-volatility-targeting]] — volatility targeting, the
  de-levering that makes risk parity concave here
- [[fung-hsieh-2001-the-risk-in-hedge-fund-strategies-trend-followers]] — the lookback-straddle model of trend-follower returns
