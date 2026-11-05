# Hedging Effectiveness of VIX Futures

| | |
|---|---|
| **Authors** | Yueh-Neng Lin, Anchor Y. Lin (National Chung Hsing University) |
| **Year** | c. 2009 (undated working paper; presented at 2008 conferences, volume data to February 2009) |
| **Type** | Working paper, 35pp |
| **PDF** | Local copy only (working paper, no open licence) |
| **BibTeX** | `lin2009hedging` |
| **Status** | Reference: §2 (the two hedging schemes), §5 (Tables 3–4) and §6 carry the results |

## What it is

A test of whether VIX futures hedge volatility risk better than ordinary options. The
position hedged is a short call on S&P 500 futures.

- **Why that target.** A call on an S&P 500 futures contract that expires before the
  futures contract carries *forward* volatility risk: the volatility between the option's
  expiry and the futures' expiry. VIX futures settle on 30-day volatility starting at
  their expiry, so in principle they are the natural hedge for that piece.
- **Two hedges, both delta- and vega-neutral.**
  - Scheme 1 uses S&P 500 futures plus a forward-start strangle: short a near-dated
    strangle and long a later-dated one. This is a standard way to trade forward
    volatility with vanilla options.
  - Scheme 2 uses S&P 500 futures plus VIX futures.
  - Each is run with Greeks from three models: constant volatility (Black), Heston
    stochastic volatility, and stochastic volatility with jumps (Bates). American exercise
    is handled by a quadratic approximation.
- **Data.**
  - Hedging period: 20 October 2004 to 30 June 2005, with parameters re-estimated monthly
    on the previous month's prices (from April 2004).
  - 2,482 futures-option observations remain after filtering.
  - Rebalancing happens whenever the target option has a quote, on average every 4.4
    days.
- **Results.** Average absolute hedging errors (one point is $250):
  - **VIX-futures hedge:** about 0.01 to 4.6 points, rising with maturity and moneyness.
  - **Strangle hedge:** about 0.6 to 11.6 points.
  - The VIX hedge wins in almost every moneyness–maturity bucket, under all three models.
  - Of the three models, stochastic volatility with jumps hedges best, then Heston, then
    constant volatility. This differs from Bakshi, Cao and Chen (1997), who found jumps
    added nothing for hedging; the authors attribute the difference to American-style
    options and a higher estimated jump frequency.
  - VIX futures most reduce the error caused by using the wrong (constant-volatility)
    model, and the gain is largest for short-dated options.
  - This is the opposite of Psychoyios and Skiadopoulos (2006), who found volatility
    options no better than vanilla options as hedges.

## Why it's in the library

**It shows what VIX futures are actually for.** They are a direct instrument for
forward volatility, the exposure that is otherwise awkward to hedge with vanilla options
because it has to be built from two maturities. The paper is an early, concrete
comparison of the two routes.

**Model choice matters for the hedge, not just the price.** The same instruments hedge
noticeably better with Greeks from a model that has stochastic volatility and jumps. A
constant-volatility hedge leaves exposures that the VIX futures then partly cover.

**The evidence is thin.** It covers eight calm months (late 2004 to mid 2005), with VIX
futures in their first year of trading and illiquid. Rebalancing is irregular, and the
forward-start strangle is built from the most extreme listed strikes, which makes for a
weak benchmark. Treat the ranking as suggestive, not settled.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] —
  VIX futures as a portfolio hedge over 2006–2017, and what holding them costs
- [[merton-1976]] — the jump component that improves the hedge here
- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]] — the cost side of hedging
  with SPX options: spreads widen when dealers are short gamma
