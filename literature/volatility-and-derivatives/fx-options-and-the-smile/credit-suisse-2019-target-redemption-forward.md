# Target Redemption Forward (TARF)

| | |
|---|---|
| **Authors** | Credit Suisse, International Trading Solutions (FX Sales, Corporate & Institutional Clients) |
| **Year** | 2019 (dated April 2019) |
| **Type** | Bank product sheet / marketing material, 2pp |
| **PDF** | Local copy only (Credit Suisse marketing material, "All rights reserved", no reproduction without permission) |
| **BibTeX** | `creditsuisse2019tarf` |
| **Status** | Reference: the whole sheet is two pages; page 2 holds the worked examples for a seller |

## What it is

A two-page client sheet describing the target redemption forward (TARF), one of the most
widely sold FX structured products to corporates. It is a sales document, so it explains
the mechanics and lists the benefits, and says little about how the product is priced or
how much the bank earns.

- **The product.** A strip of forward trades in one currency pair, at a fixed strike that
  is better than the prevailing forward rate (and spot) on the trade date. Usually no
  premium is paid ("zero-cost strategy").
- **The profit cap (the "target").** The strip terminates early once the client's
  accumulated gain reaches a preset level. The cap is defined in one of two ways: a
  number of fixings where the strike beat the market rate, or a cumulative profit amount.
- **Leverage on the losing side.** At each expiry, for a seller of the pair (an exporter):
  if the market is below the strike, the client sells the notional at the strike and the
  remaining target shrinks; if the market is above the strike, the client must sell the
  *leveraged* notional (a multiple of the base amount) at the strike; once the target is
  reached, the product ends and no further trades happen.
- **Risks the sheet lists.** Early termination once the cap is hit; a notional that
  depends on the market rate at each expiry (the leverage); costs or gains on closing or
  restructuring early; an OTC trading limit is required.

## Why it's in the library

**It is the plainest statement of the TARF's asymmetry.** The gains are capped by the
target and stop the product early, while the losses continue for every remaining fixing
and are multiplied by the leverage factor. In option terms the client is long a strip of
capped, knock-out-style options and short a larger strip of options on the other side,
which is how the "better than forward" strike is paid for without a premium. The sheet
describes the mechanics without spelling out that decomposition.

**The value of the client's position depends on the smile and on path, not just the
forward.** Because the knock-out depends on accumulated gains and the losing leg is
leveraged, pricing a TARF needs a model of how the exchange rate moves across the whole
schedule. Implied volatility at strikes far from the money, and the correlation between
spot and volatility, matter more than they do for a vanilla forward. That makes it a
practical example of why the FX smile models elsewhere in this topic are needed.

**It is marketing material.** It lists benefits and a short set of risks, gives no
numbers on fair value, margin or worst-case loss, and the examples are stylised charts.
Read it as a description of the contract, not as an assessment of whether it is a good
hedge.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the same shape at portfolio scale:
  small steady gains that are capped, paid for by a large loss when the market moves
  against the position
- [[merton-1976]] — jumps in the underlying, the risk a leveraged, path-dependent short
  option position is most exposed to
