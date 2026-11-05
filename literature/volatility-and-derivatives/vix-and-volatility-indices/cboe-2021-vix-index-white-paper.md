# Cboe Volatility Index (VIX) White Paper

| | |
|---|---|
| **Authors** | Cboe Exchange, Inc. |
| **Year** | 2021 (copyright date of this edition; the methodology dates from 2003, with SPX Weeklys added in 2014) |
| **Type** | Exchange methodology document, 20pp, with a worked example and the full option data in two appendices |
| **PDF** | Local copy only (Cboe proprietary, all rights reserved; the current version is on cboe.com) |
| **BibTeX** | `cboe2021vix` |
| **Status** | Reference: the step-by-step calculation (pp. 4–9), the filtering algorithm and the settlement (SOQ) section (pp. 10–11) |

## What it is

The exchange's own description of how the VIX is calculated.

- **History.** The 1993 VIX used at-the-money S&P 100 options (now VXO). In 2003 Cboe and
  Goldman Sachs moved it to S&P 500 options across a wide range of strikes, citing the
  Demeterfi et al. variance-swap note for the formula. Weekly SPX options were added in 2014,
  so the two expiries used always bracket 30 days (more than 23 and fewer than 37 days).
- **The formula, in words.** For each of the two expiries, take the out-of-the-money puts
  and calls around the forward, weight each option's mid price by the strike spacing divided
  by the strike squared, sum, and subtract a small correction for the forward not sitting
  exactly on a strike. That gives a variance per expiry; interpolate the two to 30 days
  (time measured in minutes), take the square root and multiply by 100.
- **Which options count.** Only options with a non-zero bid. Moving away from the money,
  once two consecutive strikes have zero bids, nothing further out is used, even if it has
  a bid. The forward comes from the strike where call and put mids are closest. The worked
  example gives VIX = 13.69.
- **Filtering.** Since 2016 the published value is smoothed: within two minutes of a baseline,
  drops of 0.50 points or more are held back and the baseline republished; rises are never
  filtered.
- **Settlement is a different number.** VIX futures and options settle on a Special Opening
  Quotation: a single expiry 30 days out (no interpolation), a strike range Cboe sets in
  advance that can include zero-bid options, and opening trade prices from an auction
  rather than mid quotes.
- **Related indexes.** VIX9D, VIX3M, VIX6M, VIX1Y, VXN, VXD and RVX, and the bid- and ask-based
  VWB/VWA and near/far components VIN/VIF.

## Why it's in the library

It is the primary source for the formula that much of this section's work starts from. The
details matter for anyone using VIX data: the zero-bid cut-off makes the strike range, and so
the index, move with liquidity; the filter means the published series is asymmetric at
short horizons; and the settlement value is built differently from the index, which is the
gap that the settlement-manipulation debate is about. The document describes methods only and
makes no claims about trading results.

## Links

- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — the
  variance-swap replication the formula comes from
- [[carr-wu-2006-a-tale-of-two-indices]] — the old VXO against the new VIX, and why VIX² is a
  variance-swap rate
- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — a replication of
  this calculation from raw quotes and the biases in it
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — what the VIX does
  and does not measure in an orderly decline
- [[brenner-et-al-2007-the-market-for-volatility-trading-vix-futures]] — the futures written
  on this index
