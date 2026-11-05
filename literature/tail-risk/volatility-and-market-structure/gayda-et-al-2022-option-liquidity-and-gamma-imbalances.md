# Option Liquidity and Gamma Imbalances

| | |
|---|---|
| **Authors** | Leander Gayda, Thomas Grünthaler, Jan Harren (University of Münster) |
| **Year** | 2022 (version of 18 June 2022) |
| **Type** | Working paper, SSRN 4138512. S&P 500 index options, 2004–2020 |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `gayda2022gamma` |
| **Status** | Reference: §IV (building the gamma inventory), §V (spreads) and §VI (balanced inventory in turbulent times) carry the results |

## What it is

An empirical paper on how SPX option market makers' aggregate gamma position affects the
price of liquidity in index options.

- **Measuring the dealers' book.** Cboe's Open-Close data split every SPX option trade by
  who traded (customer, professional customer, broker-dealer, market maker) and whether it
  opened or closed a position. Accumulating these from 1996 gives each day's net open
  interest held by market makers, assumed to be the other side of everyone else.
  - Weighting each contract by its Black–Scholes gamma, scaled by the squared index level,
    gives the dealers' net dollar gamma.
  - Dividing by the 30-day average number of contracts held gives the **aggregate gamma
    inventory (AGI)**, in dollars of gamma per contract.
- **What the series looks like.**
  - Before 2011 net gamma averaged about $1bn in absolute size and was almost always
    negative. It fell below −$10bn around the financial crisis.
  - From 2011 to 2021 it averaged about $5bn in absolute size and was more often positive,
    with the largest positive reading in 2018.
  - In 2009–2012 AGI sat near zero for long stretches. Dealers were not willing to build
    gamma inventory in either direction.
- **Spreads widen when dealers are short gamma.**
  - Regressing daily volume-weighted effective spreads (from intraday Cboe trades) on AGI
    gives a negative coefficient in every moneyness bucket, for calls and puts.
  - A one-standard-deviation fall in AGI goes with a relative spread about 1.5% higher
    for out-of-the-money options (1.53% for OTM calls).
  - AGI explains up to 34% of the daily variation in at-the-money call spreads, where gamma
    is largest.
  - The result survives controlling for the VIX and for yesterday's spread, and using
    quoted spreads or implied-volatility spreads instead. AGI also predicts the next day's
    spreads.
- **Why the sign matters.**
  - A dealer short gamma has to sell into falls and buy into rallies to stay delta-neutral,
    so they trade with the crowd and find counterparties harder to get.
  - Stock-market illiquidity (Amihud) and funding illiquidity (Hu–Pan–Wang) are both higher
    when AGI is negative, but controlling for them leaves the AGI effect unchanged. The
    authors conclude it is not just illiquidity spilling over from the underlying.
- **In turmoil, dealers flatten their gamma.**
  - The most illiquid days almost all have AGI close to zero.
  - A probit links "balanced" AGI (bottom fifth of absolute AGI) to high Amihud illiquidity,
    high realised volatility and weak intermediary capital (the He–Kelly–Manela factor). The
    intermediary measure is the strongest.
  - Balanced-AGI days coincide with extreme variance risk premia, both high and negative.
    The authors read this as dealers repricing options to steer their inventory.
  - Balanced AGI also predicts higher next-day returns to short-term reversal strategies,
    a standard proxy for what liquidity provision earns. This holds in 2004–2010 and is not
    significant in 2011–2020.

## Why it's in the library

**It gives a measured version of the dealer-gamma story.** Manager letters often argue
that dealers' option hedging amplifies moves. This paper builds the dealers' gamma
position from exchange data rather than inferring it. It shows dealers charge more for
liquidity when they are short gamma and try to get flat when markets are stressed. That
is the mechanism that makes option-based protection expensive and scarce exactly when it
is wanted.

**The inventory construction is reusable.** The daily accumulation of open-close volumes,
gamma-weighted and normalised by contracts held, is the standard way to estimate dealer
positioning. It is also the template behind commercial "gamma exposure" indicators.

**Its limits are the usual ones for this literature.**
- It assumes dealers are the counterparty to all public and broker-dealer flow.
- It uses Black–Scholes gamma.
- It assumes hedging happens once a day at the close.
- It covers SPX options on Cboe only, not SPY options or futures options.
- It is a working paper.
- The reversal-return result holds only in the sample that includes the financial crisis.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — short-volatility positioning as a
  source of crash risk
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — what
  index puts and VIX calls cost a hedger, the other side of the dealers' book
- [[merton-1976]] — the jump risk that dealers short options cannot hedge away
- [[barbon-buraschi-2021-gamma-fragility]] — the same dealer-gamma mechanism measured on single stocks: short gamma deepens crashes
- [[squeezemetrics-2020-the-implied-order-book]] — the GEX estimate of dealer gamma that this paper rebuilds more carefully
- [[carr-wu-2020-option-profit-and-loss-attribution-and-pricing]] — what the gamma, vanna and volga exposures are worth: an option priced from its daily P&L attribution
- [[boyarchenko-larsen-whelan-2023-the-overnight-drift]] — dealers' risk-bearing capacity in S&P futures: selling at the close is reversed overnight, more so when volatility is high
