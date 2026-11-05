# What Happened May 6, 2010? Anatomy of the Flash Crash

| | |
|---|---|
| **Authors** | Geoffrey Poitras (Simon Fraser University) |
| **Year** | 2012 (chapter 11 of Poitras (ed.), *Handbook of Research on Stock Market Globalization*, Edward Elgar) |
| **Type** | Book chapter; this copy is the author's manuscript, 36pp |
| **PDF** | Local copy only (book chapter, publisher copyright) |
| **BibTeX** | `poitras2012flash` |
| **Status** | Reference: §1 (the events), §3 (HFT on the day) and §4 (the short-selling argument) |

## What it is

A historian of financial markets reads the SEC–CFTC reports on the 6 May 2010 flash crash
alongside the 1987 crash, and argues that the real problem is short selling through
futures that escapes the collateral limits on short selling stocks.

- **The events, from the joint SEC–CFTC report.** Indices already down more than 4% fell
  another 5–6% within minutes after 2:32 p.m., then recovered to close about 3% down. The
  trigger was a mutual fund complex selling 75,000 E-mini S&P 500 contracts (about
  $4.1bn) as a hedge. The CME's Stop Logic paused the E-mini for five seconds at 2:45:28,
  after which the E-mini and SPY recovered. Individual stocks and ETFs kept falling until
  about 3:00 p.m.: over 20,000 trades in more than 300 securities printed 60% or more away
  from their 2:40 prices and were cancelled. More than two thirds of them were in ETFs.
- **What high-frequency traders did.** In the E-mini, HFTs traded about 140,000 contracts
  (over a third of volume) while never holding more than 3–4 thousand, so the chapter
  rejects blaming their market making. In equities, 17 HFT-associated broker-dealers
  averaged 43.8% of dollar volume, rose to 50.3% up to 2:45 and fell to 36.6% after,
  sold $9.3bn aggressively during the decline, and "removed significant buy liquidity".
  Some HFTs stopped trading altogether for minutes. The SEC's audit trail covered less
  than half of volume.
- **1987 as the precedent.** The chapter retells the 1987 crash: portfolio insurance
  implemented by selling index futures, the NYSE order-routing system (DOT) overwhelmed,
  the ticker 130 minutes late, the Dow down 508 points (23%). Its point is that both
  crashes came from futures-market selling transmitted to the stock market by index
  arbitrage, without a matching flow of bad news.
- **The argument.** Short selling stocks is limited by the need to borrow the stock;
  selling index futures is not. Cross-market arbitrage turns futures selling into stock
  selling, and exemptions for arbitrage in the post-2008 short-sale rules leave that
  channel open. The SEC's answer (single-stock circuit breakers, the Rule 201 price test)
  complicates this without restricting it. Poitras proposes requiring every short sale,
  including through arbitrage, to locate borrowable stock by the next morning or before
  the trade.

## Why it's in the library

**It documents a liquidity crash with no fundamental cause.** Prices of large, liquid
securities fell by 5–60% and came back within twenty minutes. The mechanism was
liquidity providers stepping back while a large sell programme kept going. That is the
crash that tail-risk measures fitted to daily returns cannot see.

**It connects 1987 and 2010 through the same plumbing.** Portfolio insurance in 1987 and
the E-mini hedge in 2010 were both large, mechanical futures sales passed to the stock
market by arbitrage. The 1987 story is also the template for the volatility-feedback
argument elsewhere in this section.

**It is an argument, not an empirical study.** The facts come from the SEC–CFTC reports;
the conclusions about "predatory" HFT selling and about short-sale collateral are the
author's interpretation, and the policy proposal is not tested. Later empirical work on
the same day (order-flow toxicity, the CFTC's own HFT study) reaches more specific
conclusions.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — 1987 portfolio insurance as the
  template for a market-wide short-volatility feedback loop
- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — another case of a hedging
  model becoming a source of the risk it hedged
- [[soros-2013]] — reflexivity: trading flows that change the prices they respond to
- [[easley-et-al-2011-microstructure-of-the-flash-crash]] — the order-flow-toxicity account of the same day
