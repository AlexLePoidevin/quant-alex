# Dispelling False Narratives About 0DTE Options

| | |
|---|---|
| **Authors** | The Ambrus Group (Ambrus Capital); no individual author named |
| **Year** | 2023 (undated; OPRA data run from January 2022 to March 2023, backtests to about May 2023) |
| **Type** | Manager white paper, 10pp |
| **PDF** | Local copy only (manager material marked confidential, no licence) |
| **BibTeX** | `ambrus2023zerodte` |
| **Status** | Reference: the flow analysis and the October 13, 2022 example carry the argument; the classification method is not disclosed |

## What it is

A response to the 2023 worry, voiced in a J.P. Morgan note, that zero-days-to-expiry (0DTE)
SPX options could cause a 20% one-day crash, a "Volmageddon 2.0". Ambrus argues that the
common story about who trades 0DTE options, and in which direction, is wrong. It then
argues that the risk is real anyway, but only in a crisis.

- **Who trades them.** A survey of ten market makers in the SPX complex found that
  institutions, not retail, are most of the volume. The institutions include wealth
  managers and RIAs running yield programmes, market makers, volatility hedge funds and
  event hedgers. The paper dates the jump in volume to Q2 2022, when yield programmes
  moved into short-dated options.
- **Which way they trade.** Classifying trades as buys or sells by whether they print at
  the bid or the offer is misleading, because many fill at mid. Ambrus instead tags each
  order by how the local implied volatility at that strike moves just afterwards; the
  full method is proprietary.
  - Most volume is in the first part of the day, in strikes 98–102% of the open.
  - The opening flow is mostly institutions *selling* volatility, mainly about 1%
    out-of-the-money calls and 2% out-of-the-money puts.
  - Later in the day those positions are closed and a second wave of directional buyers
    arrives.
- **Backtests, 2020 to about May 2023, no costs stated.**
  - Buying either of those two contracts at the open and holding to expiry lost steadily.
    The 2% OTM put lost about 400 SPX points cumulatively.
  - Selling them made money: the 2% OTM put had a Sharpe of 1.67 and a 4.1% CAGR at
    one-times notional; the 1% OTM call had a Sharpe of 0.40.
  - The paper's argument: volume keeps growing, so end users must mostly be profitable
    sellers.
- **Effect on the rest of the options market.** Measured as shares of rolling 50-day
  volume by tenor, 0DTE took most of the gamma (about 80%) and a rising share of contract,
  delta and theta volume. Its share of vega stayed small. VIX call volume stayed high, and
  in the March 2023 banking stress VIX call buying was among the heaviest in three years.
  The conclusion is that 0DTE is replacing 1-day to 6-month SPX options, not 30-day
  volatility hedges.
- **Where the risk is.**
  - Normally, opening volatility sales leave dealers long gamma, which damps moves.
  - On 13 October 2022, its model shows end users net *buying* 0DTE puts heavily at the
    year's intraday low. Had the market reversed into the close, dealers would have had
    to sell over $10bn of delta from positioning at 2 pm alone.
  - The conclusion: 0DTE options do not add systemic risk day to day, but in a shock
    one-sided put buying could amplify a crash.

## Why it's in the library

**It is a useful corrective on a widely repeated claim.** The direction of option flow, not
its volume, decides whether dealer hedging stabilises or destabilises the market. Volume
that is mostly sold at the open leaves dealers long gamma and dampens moves. That is the
opposite of the "retail buying 0DTE calls pushes the market around" story, and it is
consistent with the absence of a 0DTE-driven crash so far.

**Its own evidence cannot be checked.** The direction classification, which everything
depends on, is proprietary. The survey of ten market makers is unpublished. The
"volume is growing, so sellers must be winning" argument is weak: growing volume is also
consistent with buyers who keep paying for lottery-ticket payoffs. The October 2022
figure is a counterfactual from the firm's own model.

**Read it with its companion papers.** Its conclusion, that 0DTE is calm day to day and
dangerous in a shock, is the same "reflexive in a crisis" thesis as the 2022 Ambrus
papers, now applied to one product, from a firm that sells protection against that shock.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the general case that strategies
  which damp volatility in calm markets amplify it in a shock
- [[merton-1976]] — jumps in the underlying, the risk a short 0DTE seller is paid to carry
- [[peters-2011]] — why a strategy that wins most days can still be ruinous over time, the
  question the short-0DTE backtests do not answer
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]]
  — the same firm on why fixed-rule option strategies, bought or sold, have no edge
- [[squeezemetrics-2020-the-implied-order-book]] — the dealer-hedging framework behind the 0DTE feedback argument
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — why the VIX may understate stress when hedging moves to short-dated options
