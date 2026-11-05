# Risk Parity Is Not Short Volatility (Not That There's Anything Wrong with Short Volatility)

| | |
|---|---|
| **Authors** | Benjamin Hood, John Huss, Roni Israelov, Matthew Klein (AQR Capital Management) |
| **Year** | 2019 (August 2019 working paper) |
| **Type** | Working paper, SSRN 3432438, 55pp |
| **PDF** | Local copy only (SSRN working paper, no open licence) |
| **BibTeX** | `hood2019riskparity` |
| **Status** | Reference: Section 4 (trades, Exhibits 7–8) and Section 5 (returns, Exhibit 13) carry the result; the appendix repeats it for fixed income |

## What it is

A direct test of the claim, made by Cole (2017) and Bhansali and Harris (2018), that risk
parity is a hidden short-volatility trade and that the two together amplify sell-offs.
Daily simulations, January 1996 to April 2018:

- **Risk parity:** S&P 500, US 10-year and GSCI futures, each targeted to 5% volatility
  using a 35-day half-life volatility estimate, trading instantly at the close (a choice
  meant to *exaggerate* the overlap with short volatility).
- **Short volatility:** monthly sales of a 50-delta straddle and a 25-delta strangle on the
  S&P 500 (100% of NAV in notional), delta-hedged daily; the same on 10-year bond futures.

Findings:

- **Trades.** The one-day correlation between risk parity's equity trades and the short-
  volatility delta hedge is close to zero, and stays flat or slightly negative at horizons
  up to 65 days. The trades are *related* in magnitude rather than direction: a big
  short-volatility trade signals a big market move, after which risk parity is likely to
  sell. The largest 20% of risk-parity sells were twice as likely to coincide with
  short-volatility *buys* as with sells.
- **Returns.** Raw correlations are modest (0.3 between the equity sleeves; 0.2 and 0.1 for
  the whole portfolio against equity and bond short volatility), and they come from shared
  long exposure. After removing static market exposure, short volatility explains less than
  1% of risk parity's variance; average exposures to equities, bonds and commodities explain
  28%, 24% and 34%, with 14% left in residuals.
- **Size.** The authors put risk-parity assets at about $150 billion, against roughly $500
  billion a day of global equity index futures volume.
- **Caveat they flag.** A risk parity that sized positions on the VIX instead of realised
  volatility would trade much more like short volatility's hedges.

## Why it's in the library

It is the explicit rebuttal of a central claim in [[cole-2017-volatility-and-the-alchemy-of-risk]],
so the two should be read together. The distinction it draws is precise: risk parity's
*positions* depend on the level of volatility, while short volatility's *returns* depend on
changes in it.

The authors work for a large risk-parity manager. The test uses one stylised version of
each strategy rather than real fund flows, and "uncorrelated on average" does not rule out
the specific conditional scenario Cole describes (a sharp fall from low volatility, near
option expiry), which the paper concedes can happen but argues is not self-reinforcing.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the essay this paper answers: volatility-sized strategies as one hidden short-volatility trade
- [[cole-2018-what-is-water-in-markets]] — Cole's follow-up after February 2018
- [[ambrus-capital-2022-volatility-and-the-changing-market-structure]] — another practitioner case that volatility-targeting and dealer hedging make markets fragile
- [[barbon-buraschi-2021-gamma-fragility]] — evidence that option dealers' hedging, rather than risk parity, deepens intraday crashes
- [[carr-wu-2009-variance-risk-premia]] — the volatility risk premium that short-volatility strategies harvest
- [[mcquinn-thapar-villalon-2021-portfolio-protection-its-a-long-term-story]] — risk parity as a diversifier in long bad periods for 60/40
