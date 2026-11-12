# Momentum Strategies for the ETF-Based Portfolios

| | |
|---|---|
| **Authors** | Daniel Nadler and Anatoly B. Schmidt (Kensho Technologies; NYU) |
| **Year** | 2019 (dated April 2019; SSRN 3269475) |
| **Type** | Working paper, 20pp. Daily data 2007–2017 and 2011–2017 |
| **PDF** | Not hosted in this repository (SSRN download, "© 2019 Kensho Technologies, all rights reserved") |
| **Find it** | [doi.org/10.2139/ssrn.3269475](https://doi.org/10.2139/ssrn.3269475) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Momentum+Strategies+for+the+ETF-Based+Portfolios%22+Nadler) |
| **BibTeX** | `nadler2019etfmomentum` |
| **Status** | Reference: Exhibits 1–4 (ETF portfolios) and the sector-proxy exhibits carry the results |

## What it is

A test of the textbook momentum pattern on ETF universes: short lookbacks (about a month)
should show reversal, with past losers beating past winners, and long lookbacks (about a
year) should show continuation. The authors form equal-weighted baskets of the top and
bottom deciles over lookbacks of 21, 63, 126 and 252 trading days, enter on every day of
the sample, and compare the next 21 days' returns with each other and with an
equal-weighted benchmark, using paired t-tests at p ≤ 0.10.

- **Universes.** 28 US equity ETFs; the same plus gold, five international equity and five
  bond ETFs (a multi-asset set); and the holdings of SPY, QQQ and nine Select Sector SPDRs
  as of January 2018.
- **Results.** The full pattern (one-month reversal, one-year continuation) is significant
  only for the multi-asset ETF set, in both periods, and for the S&P 500 and Industrials
  proxies in 2011–2017. Elsewhere results depend on the universe and on whether 2008 is in
  the sample. Skipping the last month of the one-year lookback rarely changes conclusions.
- **Sector patterns.** Several sectors show their own winner–loser gaps, which the authors
  suggest could be traded against each other or against the benchmark.

## Why it's in the library

It is a small, direct check of whether stock-style momentum carries over to ETFs, and the
answer is "only in a diversified multi-asset set": inside one equity sleeve the pattern is
weak or reversed. That fits the view that momentum across asset classes and momentum
within a homogeneous group behave differently.

The statistics are weaker than they look. Daily entry with one-month holding periods
means about 2,700 heavily overlapping returns treated as independent, which inflates
t-statistics. The sector proxies use January 2018 holdings, so firms that left the indices
are missing despite the authors' filter. Many universes, lookbacks and benchmarks are
tested at a 10% threshold, and there are no trading costs.

## Links

- [[resolve-2019-global-equity-momentum-a-craftsmans-perspective]] — how much results move
  with the choice of lookback in a related ETF-level momentum rule
- [[collin-dufresne-daniel-2015-liquidity-and-return-reversals]] — short-horizon reversal,
  the one-month effect tested here
- [[keller-keuning-2016-paa]] — momentum asset allocation across a multi-asset ETF universe
- [[harvey-liu-zhu-2016]] — the multiple-testing problem behind many lookbacks, universes and
  benchmarks
