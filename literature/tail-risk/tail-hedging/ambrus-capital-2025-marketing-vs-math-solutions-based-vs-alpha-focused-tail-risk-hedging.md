# Marketing vs. Math: Solutions-Based Tail Risk Hedging vs. Alpha-Focused Tail Risk Hedging

| | |
|---|---|
| **Author** | Ambrus Capital (no individual byline) |
| **Year** | 2025 (undated; its charts run to 2025) |
| **Type** | Manager white paper — a volatility manager arguing for its own style of tail hedging, not peer reviewed, 11pp |
| **PDF** | `ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging.pdf` (local copy only, not redistributed) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Marketing+vs.+Math%3A+Solutions-Based+Tail+Risk+Hedging+vs.+Alpha-Focused+Tail+Risk+Hedging%22+Capital) for the title and authors |
| **BibTeX** | `ambrus2025marketing` |
| **Status** | Read |

## What it is

A short argument that most tail risk hedging programmes lose money because they are run
as fixed products rather than traded. The paper splits the field in two:

- **Solutions-based hedging.** A fixed rule run whatever the market looks like, for
  example "buy a 1-month, 20% out-of-the-money S&P put on the first of each month and sell
  it if it goes up 10×". The paper says this is typical of large asset managers, bank QIS
  (quantitative investment strategy) programmes, pensions and some hedge funds.
- **Alpha-focused hedging.** The same instruments, but bought only when they look cheap
  (implied volatility low relative to expected realised volatility, thin market depth,
  dealer positioning pointing to a sharp move) and sold into the panic. The paper
  associates this with derivatives proprietary trading firms and volatility hedge funds.

It then lists why a fixed rule bleeds:

- **Three headwinds.** The equity risk premium (a hedge is short an asset that rises over
  time), the volatility risk premium (index options are usually priced above the
  volatility that follows: their chart shows VIX minus the next 20 days' realised
  volatility mostly positive since 1990), and what they call the "No Alpha Dilemma": a
  rule that trades without an edge pays the spread and premium to better-informed
  counterparties.
- **Variance drag cuts both ways.** Their example: a $1M hedge book that bleeds to $100k
  over three years, then returns 500% in a crash, ends at $600k, still 40% down. Bleed
  compounds against you just as the crash payoff compounds for you.
- **Structures are not strategies.** No single strike, tenor or instrument is the best
  hedge in every regime. Their backtests of six fixed structures (VIX calls at three
  deltas, a 10-delta SPX put, a short straddle plus a far put, a put-call risk reversal)
  all show cumulative losses of roughly 40–80% from 2008 to 2025, with jumps only in 2008
  and 2020.
- **Too few crashes to fit.** Tuning when to take profits on a handful of episodes (1987,
  2001, 2008, 2010, 2020, 2022), each with a different shape, is fitting to "an N of
  none".
- **Calendar rules are price-insensitive.** Buying on a schedule means paying the offer
  on wide markets. Their example: a 10-delta VIX call at $0.10 versus $0.05, both going to
  $1.00 in a crash, returns 9× versus 19× the premium. Their chart of a 5-delta VIX call
  bought at the mid versus crossing the spread shows the same gap over time.
- **"There's no such thing as a free hedge" is called a convenient narrative.** The paper
  argues that if alpha exists, a hedge that does not bleed must be possible, and points to
  Chicago derivatives prop firms whose books are flat in calm markets and pay off in
  dislocations.

## Why it's in the library

**The diagnosis is useful and mostly checkable.** The equity and volatility risk premia,
the compounding cost of bleed and the cost of crossing wide spreads on deep out-of-the-money
options are all standard and visible in the paper's own charts. Together they explain why a
calendar-rolled put or VIX-call programme loses money in most years, and why
the Eurekahedge Tail Risk Hedge Fund Index it shows fell about 40% from 2008 to 2025
despite two large spikes.

**The cure is asserted, not shown.** The paper presents no track record, backtest or rule
for its own alpha-focused approach. The case that a carry-neutral, convex book is
achievable rests on the existence of successful prop firms, which says nothing about
whether a given manager can do it. Read the second half as the pitch of a firm that sells
the alpha-focused style.

**Two examples are friendlier than they look.** The variance-drag example sizes the hedge
as the whole $1M rather than a small sleeve of a larger portfolio, which is the usual
setup and makes the bleed far less damaging. The $0.05 versus $0.10 example assumes $500k
of deep out-of-the-money VIX calls can be filled at half the offer, which liquidity in
those strikes may not allow.

**The overfitting point carries over.** Fitting entry and exit rules to six crashes is the
same multiple-testing problem as fitting any strategy to a short history, and the warning
applies to the alpha-focused approach as much as to the fixed rules.

## Links

- [[hughson-stutzer-yung-2006]] — the σ²/2 gap between arithmetic and geometric returns
  behind the variance-drag argument
- [[peters-2011]] — why the time-average growth rate, not the expected return, decides
  whether a bleeding hedge is worth holding
- [[merton-1976]] — jumps in the underlying, the reason deep out-of-the-money puts carry
  value that a continuous model misses
- [[rockafellar-uryasev-2000]] — measuring and optimising the tail directly (CVaR) rather
  than buying insurance against it
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the evidence on what long-VIX hedges did for a 60/40 portfolio, 2006–2017: big help in 2008, a steady drag otherwise
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — why a crash can be bigger than the history suggests: volatility-sized strategies as one hidden short-volatility trade
- [[chang-holdom-bhansali-2021-tail-risk-hedging-performance-measuring-what-counts]] — another manager on how tail-hedge performance should be measured: cash flows and portfolio effect, not compounded NAV
- [[harvey-et-al-2019-the-best-of-strategies-for-the-worst-of-times]] — the measured cost of rolling S&P 500 puts (−7.4% a year) against dynamic hedges
- [[harvey-et-al-2020-strategic-risk-management-out-of-sample-evidence-from-covid-19]] — the non-option alternatives (trend, volatility targeting, rebalancing rules) tested out of sample in 2020
- [[mcquinn-thapar-villalon-2021-portfolio-protection-its-a-long-term-story]] — the opposing view: puts protect only against fast crashes, and diversifiers do better over long bad periods
