# VIX Futures and Options: A Case Study of Portfolio Diversification During the 2008 Financial Crisis

| | |
|---|---|
| **Authors** | Edward Szado (CISDM, University of Massachusetts Amherst) |
| **Year** | 2009 (dated August 2009) |
| **Type** | Journal article, *The Journal of Alternative Investments* 12(2), 68–85 (2009); the copy here is the CBOE-supported working paper. Data: March 2006 – December 2008 |
| **PDF** | Not hosted in this repository (no open licence) |
| **Find it** | [doi.org/10.3905/jai.2009.12.2.068](https://doi.org/10.3905/jai.2009.12.2.068) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22VIX+Futures+and+Options%3A+A+Case+Study+of+Portfolio+Diversification+During+the+2008+Financial+Crisis%22+Szado) |
| **BibTeX** | `szado2009vix` |
| **Status** | Reference: Exhibits 9, 12, 15 and 18 (futures, ATM calls, OTM calls, SPX puts) carry the results |

## What it is

The original version of the case study that [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]]
later extended. It asks what a long-VIX position would have done for an investor during
2008, when almost every diversifier failed.

- **Diversification broke down.** Comparing 2004–2006 with 2007–2008, equity correlations
  rose for nearly every asset class: high-yield bonds from 0.51 to 0.87, real estate from
  0.56 to 0.85, commodities from −0.22 to 0.52. Only managed futures (trend followers)
  went the other way, from 0.52 to −0.22.
- **The test.** Three base portfolios (100% equity, 60/40, and an average US institutional
  mix with alternatives), rebalanced monthly, plus 2.5% or 10% in fully collateralised
  front-month VIX futures, or 1% or 3% in one-month VIX calls (at the money or 25% out of
  the money). Calls are bought at the ask and settled at intrinsic value.
- **August–December 2008.** The diversified portfolio lost 19.7%. With 10% VIX futures it
  lost 4.0%; with 1% ATM VIX calls it lost 6.7%; with 1% of 25%-OTM calls it gained about
  18%, and with 3% it gained about 97%, at much higher volatility.
- **March 2006 – December 2008.** VIX futures alone lost 6% a year with an 82% drawdown,
  yet adding them still reduced the portfolios' losses and volatility over this window,
  because the window ends in the crash.
- **VIX calls against S&P 500 puts.** Each month an SPX put is bought costing the same as
  the VIX call. Those puts were on average 13% out of the money and rarely paid off, so
  the put portfolios did worse than the unhedged ones over the full period, while the VIX
  call portfolios did better.

## Why it's in the library

**It is the crisis case for long volatility, measured carefully.** When correlations
among risky assets jump, VIX exposure is one of the few things whose correlation with
equities stays strongly negative, so a small allocation does a lot of work.

**The sample is built to flatter the hedge.** It ends at the bottom of the worst crash in
decades, the allocations are chosen after the fact (the author notes an optimiser would
put 100% in VIX futures), and the put comparison matches cost rather than protection,
which leaves the puts far out of the money. The author says plainly that this is a case
study, not a strategy. The 2020 paper, which adds the calm years, is the fairer test.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  same study extended to 2017: the crisis gains and the long cost of carry
- [[ang-chen-2002]] — correlations rise in down markets, the failure this paper documents
  in 2008
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — 2008 as a failure of assumed
  diversification in the tail
- [[fassas-2017-tracking-the-vix]] — why VIX futures, not spot VIX, are what an investor
  actually holds
