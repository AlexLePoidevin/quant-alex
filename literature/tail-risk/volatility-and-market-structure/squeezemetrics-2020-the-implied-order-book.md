# The Implied Order Book

| | |
|---|---|
| **Authors** | SqueezeMetrics ("GEX Ed.") |
| **Year** | 2020 (dated 6 July 2020) |
| **Type** | Vendor white paper, 12pp |
| **PDF** | Local copy only (vendor paper with no open licence) |
| **BibTeX** | `squeezemetrics2020implied` |
| **Status** | Reference — the GEX and VEX definitions, the March 2020 liquidity map and the closing argument about sold puts are the content |

## What it is

An explanation, by the firm that publishes the GEX index, of how S&P 500 option dealers'
hedging acts like a hidden limit order book for the index.

- **The idea.** When a customer trades an SPX option, a dealer usually takes the other
  side and delta-hedges in the index. How that hedge must change as the index and implied
  volatility move is predictable from Black–Scholes. Adding it up over all options gives
  an "implied order book": where dealers will have to buy and where they will have to sell.
- **Dealer directional open interest (DDOI).** Public open interest doesn't say whether
  dealers are long or short. SqueezeMetrics signs each trade from transaction data and
  checks it against the next day's change in open interest. This is their proprietary
  input.
- **GEX (gamma exposure).** Dollars of index dealers must buy per point the index falls
  (and sell per point it rises). Customer-sold options make it positive, which is
  stabilising: dealers buy dips and sell rallies. Customer-bought options push it down.
  The paper says SPX GEX since 2004 is rarely negative and never below about −$200m per
  point, and sometimes above $1bn per point. Higher GEX goes with tighter daily returns,
  and the most extreme volatility has occurred only when GEX was near zero.
- **VEX (vanna exposure).** Dollars dealers must buy or sell when implied volatility
  changes. Its sign depends on moneyness: the same short put makes dealers buy when IV
  rises if it is out of the money, and sell if it is in the money. The paper says VEX
  reached about −$400m per point in late 2008 and again in the 2020 Covid crash, and
  that negative VEX goes with high volatility. GEX+ is GEX plus VEX.
- **Why sold puts are the crash risk.** Out of the money, a customer-sold put makes
  dealers buy both on dips (gamma) and on IV spikes (vanna). Once the index falls through
  the strike, the same put makes dealers sell as IV rises. Falling prices raise IV, which
  forces more selling, which raises IV. The paper argues this loop, not customers buying
  puts, is what produces 20%–30% declines, and that long puts tend to cause only short,
  sharp corrections.
- **The 5 March 2020 map.** A grid of SPX level against VIX showing where GEX+ turns
  negative. Below 3000 on the S&P, dealers became liquidity takers. Below 2800 with VIX
  above 60, there was no historical analogue at all.

## Why it's in the library

**It explains a mechanism by which crashes are bigger than the data before them
suggest.** If most liquidity near the market comes from dealer hedging, it can be
plentiful until a level is crossed and then reverse sign. That is a market-structure
version of the argument in Cole's "Alchemy of Risk".

**It turns option positioning into something you can reason about.** The examples are
simple enough to check by hand with a Black–Scholes delta, and they show why the same
option can add liquidity in one regime and take it in another.

**It is a vendor's argument, and most of the evidence is scatterplots.** The paper asserts
causation ("negative VEX is the cause of sustained S&P 500 volatility") from
co-movement, and its key input, DDOI, can't be checked from the paper. GEX near zero
when IV is high is partly mechanical, since high IV flattens gamma, which the paper
itself points out. The worked examples are loose: dollar amounts ignore the contract
multiplier and some delta changes mix in a day of time decay. Use it for the mechanism,
not the numbers.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the broader case that volatility-
  sensitive positioning creates hidden short-volatility exposure that reverses in a shock
- [[merton-1976]] — option pricing with jumps; the dealer hedges here assume Black–Scholes
  continuity, which is what fails in a gap
- [[flora-reno-2020-v-shapes]] — a statistical test for the overshoot-and-reverse pattern
  that liquidity withdrawal produces
- [[barbon-buraschi-2021-gamma-fragility]] — academic evidence on dealer gamma and crash depth
