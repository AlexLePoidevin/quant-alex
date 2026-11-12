# Does Volatility Harvesting Really Work?

| | |
|---|---|
| **Authors** | Magnus Erik Hvass Pedersen |
| **Year** | 2021 (first published 17 May 2021) |
| **Type** | Working paper. SSRN 3847692, 91pp (mostly charts). Daily, weekly, monthly and annual returns for about 920 US stocks, 2007–2021, plus 1- and 5-minute data for 70 stocks over 9 days in April 2021. Code released as a Python notebook |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3847692](https://doi.org/10.2139/ssrn.3847692) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Does+Volatility+Harvesting+Really+Work%3F%22+Pedersen) |
| **BibTeX** | `pedersen2021harvesting` |
| **Status** | Reference: §1–3 (definitions and toy examples), §4 (daily returns), §5 (weekly), §8–10 (intraday and correlations) and §11 (conclusion) |

## What it is

An empirical test of "volatility harvesting": the claim, going back to Booth and Fama (1992),
that rebalancing a portfolio of volatile assets to fixed weights earns a return above buy and
hold. The author deliberately avoids the algebra used on both sides of the debate and
simulates thousands of random equal-weight portfolios from real stock data.

- **Design.** For portfolio sizes from 2 to 100 stocks, draw 1,000 random portfolios with
  random start and end dates, and compare an equal-weight portfolio rebalanced every period
  with a buy-and-hold portfolio of the same stocks. Compare arithmetic and geometric means,
  standard deviation, Sharpe ratio, maximum drawdown and the largest one-year rise ("max
  pull-up").
- **Daily rebalancing, 2007–2021.** The rebalanced portfolios have a slightly higher mean
  daily return, worth roughly 0.15–0.45% a year depending on portfolio size. On geometric
  means the differences change sign across portfolio sizes and are mostly borderline or
  insignificant (about 0.2% a year for 10-stock portfolios). Rebalanced portfolios also have
  higher daily volatility. Over 2010–2021 alone the arithmetic differences are not
  statistically significant. Over 2007–2010 they are, at about 2.75–4.25% a year.
- **Crash and recovery.** Rebalanced portfolios tend to do somewhat worse while the market
  falls (their maximum drawdowns are about 1 percentage point deeper with weekly rebalancing)
  and clearly better in the recovery. With weekly rebalancing the one-year max pull-up is
  7.5–14 points higher on average, 19–24 points in 2007–2010 and only 3.3–5.1 points in
  2010–2021. Weekly rebalancing looks better than daily or monthly.
- **Intraday.** With 1- and 5-minute data, rebalancing usually beats buy and hold; for
  5-minute rebalancing the estimate is 0.6–1.3% a year. Average pairwise correlations are
  0.12 for 1-minute returns, 0.17 for 5-minute and 0.41 for daily, which may be why. The
  author stresses that 9 days of data for 70 stocks cannot support a general conclusion, and
  that data errors or rounding could be responsible.

## Why it's in the library

**It is a sober check on a popular claim.** Outside the 2008–09 crash and recovery the
rebalancing premium in this data is close to zero and small next to trading costs and taxes,
which the paper does not deduct. The gain that does exist is concentrated in rebounds after
crashes.

**It fits the defensive-strategy papers.** Rebalancing buys what has fallen. That hurts during
a prolonged decline and pays in the recovery, which is the same short-volatility profile the
Man Group rebalancing papers describe.

**Limits.**

- One 14-year sample dominated by a single crash.
- The stock list has survivorship bias: few stocks that went to near zero.
- The random portfolios overlap heavily, so the many significant p-values are not
  independent tests.
- No costs, and the intraday evidence is tiny.
- The Sharpe ratio is computed from raw per-period returns without a risk-free rate, which is
  fine for comparing the two strategies but not as an absolute figure.

## Links

- [[booth-fama-1992]] — the diversification-return argument this paper tests
- [[granger-et-al-2014-rebalancing-risk]] — rebalancing as buy-and-hold plus a short straddle, and its drawdown cost
- [[rattray-et-al-2020-strategic-rebalancing]] — making rebalancing less harmful in prolonged selloffs with a trend overlay
