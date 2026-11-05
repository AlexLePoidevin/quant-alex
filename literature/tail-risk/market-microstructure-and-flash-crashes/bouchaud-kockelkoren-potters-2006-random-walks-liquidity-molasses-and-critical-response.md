# Random Walks, Liquidity Molasses and Critical Response in Financial Markets

| | |
|---|---|
| **Authors** | Jean-Philippe Bouchaud, Julien Kockelkoren, Marc Potters (Science & Finance, Capital Fund Management) |
| **Year** | 2006 (arXiv preprint cond-mat/0406224v2, June 2004) |
| **Type** | Journal article, *Quantitative Finance* 6(2), 115–123. doi:10.1080/14697680500397623. 19pp preprint |
| **PDF** | `bouchaud-kockelkoren-potters-2006-random-walks-liquidity-molasses-and-critical-response.pdf` (the arXiv version) |
| **BibTeX** | `bouchaud2006molasses` |
| **Status** | Reference: §2.2 (response functions, the test of the Lillo–Farmer model), §2.3 (the critical line β ≈ (1−γ)/2) and §2.4 (the economic story) carry the argument |

## What it is

A short econophysics paper on why stock prices look like a random walk even though the
order flow that moves them is strongly predictable. It is a reply to Lillo and Farmer, who
offered a different explanation, and it uses trade-by-trade data on 11 Paris Bourse stocks
for 2002 (plus Carrefour in 2001).

- **The puzzle.** The signs of market orders (buy or sell) are correlated over very long
  horizons, because large traders split orders into many small trades over hours or days.
  The correlation decays as a power law, C(ℓ) ~ ℓ^(−γ), with γ between about 0.1 and 0.7
  across the stocks. If every trade moved the price permanently, that persistence would
  make prices trend (superdiffusive). They don't: the variance of price changes grows
  almost exactly linearly with the horizon, so returns are close to uncorrelated.
- **The authors' answer: impact is transient.** The impact of a single trade (the "bare
  impact function" G0) is flat at first and then decays as a power law, ℓ^(−β). Prices are
  diffusive when β sits close to a critical value, β ≈ (1−γ)/2. The fitted (β, γ) pairs for
  the 11 stocks all scatter around that line. Small deviations explain why the measured
  response function sometimes rises monotonically and sometimes peaks and turns negative.
- **The competing answer, rejected.** Lillo and Farmer argued that impact is permanent but
  liquidity (volume at the best quote) fluctuates in step with order flow and cancels the
  persistence. The paper reports three objections:
  - Their rescaled variable explains price moves about three times less well than signed
    log volume.
  - A permanent-impact model implies a response function that grows roughly 30-fold with
    the lag, which the data don't show.
  - The apparent lack of correlation in their variable is an artefact: volume at the best
    quote is extremely skewed, so the ratio is dominated by moments when the queue is tiny.

  Lillo and Farmer agreed, per a footnote, that their London results are compatible with
  this reading.
- **The mechanism: a "liquidity molasses".** Liquidity providers who see a run of buy
  orders, and who are now short, push the price back. They stack sell limit orders at the ask
  (a wall the price bounces off) and keep bids low. The data show both effects:
  - sell orders that follow buys move the price more than buys that follow buys;
  - the mid-quote moves between trades are anti-correlated with the preceding market
    orders.
- **A self-organised balance.** If providers revert too slowly, prices trend and they lose
  money, so they revert harder; if they revert too hard, takers wait and spread their
  orders more thinly, which lowers γ. The market settles near the critical line. The paper
  argues that patches of persistence and anti-persistence around it show up as swings in
  local volatility. When the molasses disappears, liquidity crises and crashes follow.

## Why it's in the library

**It gives a microstructure account of how calm turns into a crash.** In this picture,
ordinary low volatility is something liquidity providers manufacture by mean-reverting
the price against a persistent order flow. A crash is the moment they step back, consistent
with the liquidity-withdrawal stories of 6 May 2010 in this folder. The crash claim is
stated, not tested: the data are one year of normal trading in 11 French stocks.

**It explains why execution cost depends on how fast you trade.** Because impact decays,
an order spread over time costs less than its summed instantaneous impact suggests. The
same transient-impact idea underlies later propagator models of market impact.

**Limits worth keeping in mind.** The evidence is one market, one year, and fits of power
laws over two to three decades of lag. The equilibrium story (providers and takers pushing
β and γ onto the critical line) is an interpretation, not something the paper tests.

## Links

- [[bouchaud-potters-2009]] — the same authors on random matrix theory for correlation matrices
- [[easley-et-al-2011-microstructure-of-the-flash-crash]] — 6 May 2010 as liquidity providers withdrawing, measured with order-flow toxicity
- [[sarkissian-2019-statistical-mechanics-of-price-stabilization-and-destabilization]] — another physics-style model in which small imbalances are absorbed and large ones tip into a crash
- [[romero-2016-microstructure-noise-two-scales-realized-volatility]] — bid-ask bounce and microstructure noise in measured volatility
- [[shi-et-al-2020-modeling-flash-crash-behavior-with-multivariate-hawkes-processes]] — self-exciting order flow during a crash
- [[kirilenko-et-al-2018-automation-intermediation-and-the-flash-crash]] — what intermediaries actually did with their inventory on the flash-crash day
