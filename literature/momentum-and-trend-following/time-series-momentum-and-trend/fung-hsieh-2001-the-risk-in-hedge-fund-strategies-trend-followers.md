# The Risk in Hedge Fund Strategies: Theory and Evidence from Trend Followers

| | |
|---|---|
| **Authors** | William Fung (PI Asset Management), David A. Hsieh (Duke University) |
| **Year** | 2001 (Review of Financial Studies 14(2), 313–341) |
| **Type** | Journal article, 29pp. Lookback-straddle returns on 26 futures markets from the mid-1980s to 1997; trend-following fund returns 1989–1997 from the TASS CTA database |
| **PDF** | Local copy only (published RFS article, © The Society for Financial Studies) |
| **BibTeX** | `fung2001trend` |
| **Status** | Reference: §1 (lookback straddle as the "primitive trend-following strategy"), §3 (what explains trend-fund returns) and §4 (individual funds) carry the results |

## What it is

The paper that gave trend following an option-based description: a trend follower's
returns look like those of a portfolio of lookback straddles on the markets it trades.

- **The problem.** Trend-following funds (CTAs) have returns that are almost
  uncorrelated with stocks, bonds, currencies and commodities, so a linear factor
  model says they carry no systematic risk. But their returns are large and positive in
  both the best and worst months for world equities, an option-like pattern.
- **The model.** A "primitive trend-following strategy" (PTFS) is defined as the best
  possible single trade over a period: buy at the period's low and sell at its high. Its
  payout, the maximum minus the minimum price, is exactly that of a lookback straddle.
  A market timer in Merton's (1981) sense, by contrast, earns the payout of a standard
  straddle (the move from start to end). The lookback straddle's delta behaves like a
  trend follower's: long when price is near its high, short near its low, buying
  breakouts and selling breakdowns.
- **The data.** Lookback straddles are not traded, so they are replicated by rolling two
  ordinary three-month straddles to new highs and lows, using daily settlement prices on
  26 markets (stock indices, government bonds, short-rate futures, currencies,
  commodities). These are grouped into five PTFS portfolios.
- **What explains trend-fund returns.** The benchmark is an equal-weighted portfolio of
  407 CTA funds (live and dead) that load on the first principal component of 1,304 CTA
  funds. Regressed on eight major asset-class indices its adjusted R² is about 1%; on the
  26 underlying markets in groups, from −3% to 7.5%; on commodity indices, about zero.
  On the five PTFS portfolios the adjusted R² is 47.9%, driven mainly by currencies and
  commodities.
- **In equity crises.** In the two worst periods for world equities in the sample
  (Sept–Nov 1987, −20.4%; Aug–Sept 1990, −18.9%) trend funds returned +13.0% and +10.2%.
  Sorting months into five states by world equity returns, the bond, short-rate and
  currency PTFSs earn the most in the extreme states at both ends; commodity PTFSs do not
  show the pattern. In the extreme equity months, PTFSs on US bonds, the Deutschemark,
  wheat and silver explain 60.7% of trend-fund returns, with no role for stock-index
  PTFSs (the authors note this regression was selected after the fact).
- **Individual funds.** Across 163 funds with at least 24 months of returns, the PTFS
  portfolios give an average adjusted R² of 24% against 11% for buy-and-hold portfolios
  of the same markets. No fund loads significantly on the stock PTFS. Of 21 funds named
  as currency traders, 18 load only on the currency PTFS.
- **Standard versus lookback straddles.** With quarterly options and monthly returns the
  two are hard to tell apart (monthly correlation 0.86 on the yen, 0.83 on the Swiss
  franc); the authors use lookback straddles for their theoretical fit, not because the
  data prefer them.

## Why it's in the library

**It is the bridge between trend following and options.** Saying that trend following
is "long volatility" or "convex" usually means this paper's result: a trend follower
behaves like an owner of lookback straddles, paid when prices move far in either
direction within a period. That is why trend returns are positively skewed and do well
in sustained crashes.

**It shows why linear factor models miss trend-follower risk.** A fund can have zero
beta to every asset class and still carry systematic risk, because the exposure is
non-linear. The PTFS factors became standard hedge-fund benchmarks (the Fung–Hsieh
trend-following factors) for this reason.

**It also marks what trend following does not hedge.** Equity-index trend explains
nothing in this sample; the crisis payoff came from bonds, currencies and commodities.
The straddle analogy is also a statement about cost: the option premium is the price
of the payoff, and the PTFS portfolios themselves mostly have insignificant average
returns, while trend funds earned a positive mean the model does not explain.

**The evidence is from one decade.** Fund data cover 1989–1997, survivorship is handled
by including dead funds, and the straddle replication is approximate: rolls happen once a
day at settlement rather than continuously, near-the-money strikes stand in for at-the-money
ones, and most US options are American-style, which the authors say biases PTFS returns
downward. The selection of significant regressors in the crisis
regressions is ex post.

## Links

- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the time-series momentum strategy whose straddle-like smile this paper explains
- [[cfm-2018-the-convexity-of-trend-following]] — a direct derivation of trend convexity, and how diversification weakens it
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — trend following's returns in equity and bond crises over a longer sample
- [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]] — trend set against the explicit option hedge, index puts
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — buying the convexity directly with VIX options, and what it costs
