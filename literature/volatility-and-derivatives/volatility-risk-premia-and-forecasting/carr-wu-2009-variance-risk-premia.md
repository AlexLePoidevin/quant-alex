# Variance Risk Premia

| | |
|---|---|
| **Authors** | Peter Carr (Bloomberg LP; Courant Institute, NYU); Liuren Wu (Baruch College) |
| **Year** | 2009 (*Review of Financial Studies* 22(3), 1311–1341; first draft July 2003, this copy dated 24 October 2007) |
| **Type** | Journal paper (author's final working-paper version, 44pp). Options data January 1996 to February 2003 on five stock indexes and 35 stocks |
| **PDF** | Local copy only (journal article, no open licence) |
| **BibTeX** | `carr2009variance` |
| **Status** | Reference: Proposition 1 (synthesising the variance swap rate from options), §3.1 (sign and size of the premium) and §3.2 (factor regressions) carry the paper |

## What it is

The paper that turned "options are expensive" into a measurable quantity. It defines the
variance risk premium as realized variance minus the variance swap rate, and shows how to
read the swap rate straight off option prices without assuming a model.

- **The measurement.** A variance swap pays realized variance minus a fixed rate agreed
  today. The fixed rate is the risk-neutral expectation of realized variance. Proposition 1
  shows it equals, up to a small error, a weighted strip of out-of-the-money puts and calls
  across all strikes, each weighted by one over strike squared. The error is zero if
  prices move continuously and of third order in the size of jumps otherwise. This is the
  same replication that sits under the VIX.
- **The premium.** The variance risk premium is realized variance minus the synthetic swap
  rate over the next 30 days. It is also the profit or loss of holding a long variance
  swap to maturity. The log version, ln(realized / swap rate), is the excess return on
  that position.
- **The size.** For the S&P 500 a long 30-day variance swap lost on average $2.74 per $100
  of notional over 1996–2003. In log-return terms that is an average excess return of
  about −66% per contract. The premium is strongly negative and significant for the
  S&P 500, S&P 100 and Dow, and significant but weaker for the Nasdaq-100.
- **Shorting variance.** Selling 30-day variance swaps on the S&P 500, S&P 100 and Dow had
  annualised Sharpe ratios of 0.98, 0.85 and 0.87 in this sample. The paper warns these
  use synthetic swap rates, ignore what real quotes and spreads would have cost, and
  that Sharpe ratios mislead for non-linear payoffs.
- **Single stocks.** Only 7 of 35 stocks had a significantly negative premium in dollar
  terms, 23 of 35 in log terms. Stocks whose variance moves more with index variance (a
  higher "variance beta") have more negative premia. The authors read this as a single
  priced, market-wide variance factor.
- **Not explained by known factors.** Index returns move against index variance, so a long
  variance swap has a strongly negative CAPM beta. But that beta explains only a small part
  of the premium. Fama–French size and value, a squared-market term, momentum, and the
  term and default spreads explain little more. The paper concludes that either the index
  variance market is very inefficient or variance is a separate risk that investors pay
  heavily to hedge.
- **Time variation.** Regressing realized variance on the swap rate gives slopes well below
  one (0.455 for the S&P 500; 0.618 after correcting for measurement error), so the dollar
  premium grows when the swap rate is high. In logs the slope is close to one, so the
  premium in return terms is roughly constant.
- **Robustness.** Model simulations put the replication error at under 2% of the variance
  level (Merton jumps) and under 1% with stochastic volatility. The premium stays
  significantly negative for the S&P and Dow using bid rather than mid prices, and in both
  the 1996–2000 bull market and the 2000–2003 bear market.

## Why it's in the library

**It is the price of crash protection, measured.** The tail-hedging notes describe what
holding long volatility costs a portfolio. This paper is the other side of the same trade:
on average buyers of index variance paid about two-thirds of their premium away each
month, because they wanted insurance against volatility rising. That drag is what
[[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] finds
in long-VIX positions.

**It explains why short-volatility strategies look so good for so long.** A positive
average return on selling variance, with Sharpe ratios near one before costs, is the
reward for bearing a risk that pays out rarely and badly. That is the trade
[[cole-2017-volatility-and-the-alchemy-of-risk]] argues has grown too large.

**The replication formula is the workhorse of the section.** The options strip that prices
a variance swap is the basis of the VIX, of variance swap pricing, and of the model-free
results elsewhere in this section.

**The evidence is from one period and from synthetic prices.** The sample is seven years
around the dot-com bubble, and the swap rates are built from interpolated option quotes,
not traded. The single-stock results are mostly insignificant in dollar terms. The index
result is the robust part.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — what
  paying the variance risk premium does to a 60/40 portfolio in calm years and in 2008
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the case that strategies collecting
  this premium have become one crowded short-volatility trade
- [[merton-1976]] — jump-diffusion, the source of the replication error in Proposition 1
- [[carr-wu-2017-leverage-effect-volatility-feedback-and-self-exciting-market-disruptions]] — what drives the variance risk premium: leverage, feedback and jumps
