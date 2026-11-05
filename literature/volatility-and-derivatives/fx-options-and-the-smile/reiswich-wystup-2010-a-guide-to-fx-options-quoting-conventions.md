# A Guide to FX Options Quoting Conventions

| | |
|---|---|
| **Authors** | Dimitri Reiswich, Uwe Wystup (Frankfurt School of Finance & Management) |
| **Year** | 2010 |
| **Type** | Journal article — *The Journal of Derivatives* 18(2): 58–68, doi:10.3905/jod.2010.18.2.058. Copy from ResearchGate, 12pp |
| **PDF** | Local copy only (journal version, no open licence) |
| **BibTeX** | `reiswich2010guide` |
| **Status** | Reference: the premium conventions, the four deltas, the at-the-money definitions and the delta-to-strike algorithms are the content |

## What it is

A practical guide to how the FX options market quotes prices and volatilities, and to the
conventions that academic papers usually get wrong.

- **FX quotes volatility against delta, not strike.** A smile is given either as implied
  volatility at a grid of deltas (10, 25, ATM, …), or as at-the-money, risk-reversal and
  strangle quotes at 25 and 10 delta. To get strike–volatility pairs you have to know
  which delta and which ATM the numbers refer to.
- **Four premium conventions.** A EUR/USD call's premium can be stated in USD per EUR
  (domestic pips, the Black–Scholes default), in EUR per USD of notional, as a percentage
  of the EUR notional, or as a percentage of the USD notional. In the example
  (spot 1.3900, strike 1.3500) these are 0.1024 USD, 0.054570, 7.3669% and 7.5852%. Which
  is used depends on the pair: the premium is normally paid in the more traded currency
  (USD first, then EUR, GBP, AUD, NZD, CAD, CHF, …). So USD/JPY options are paid in USD,
  the foreign currency.
- **Four deltas.** Spot delta (hedge in the spot market) or forward delta (hedge with a
  forward), each either plain or *premium-adjusted*. Premium adjustment applies when the
  premium is paid in the foreign currency, because the premium received is itself a
  currency position. In the example a 60% delta becomes 52.63%. Only forward deltas make a
  25-delta call and a 75-delta put the same point. The premium-adjusted call delta is not
  monotone in strike, so one delta can match two strikes.
- **Which delta the market uses.** Spot deltas for the main currencies out to one year;
  forward deltas beyond one year and for emerging-market pairs. After 2008 forward deltas
  spread, because forward delta needs no discount factor and banks had stopped agreeing on
  discount curves.
- **Several at-the-moneys.** ATM spot, ATM forward (equivalent to value-neutral) and
  delta-neutral, where a straddle has zero delta. Delta-neutral is the default for short
  FX options, and its strike depends on which delta convention applies.
- **From quotes to strikes.** Plain spot and forward deltas convert to strikes in closed
  form. Premium-adjusted deltas need a root search (Brent's method) on the side of the
  delta maximum. Interpolate the smile in the delta space it was quoted in.

## Why it's in the library

**FX volatility data cannot be used correctly without these conventions.** A "25-delta
volatility" means a different strike depending on premium currency, spot or forward hedge
and maturity. Interpolating it under the wrong convention gives prices the market would
not trade.

**It shows that "delta" is a hedge quantity, not a formula.** The four deltas are four
answers to the question "how much currency do I buy to hedge this?", given where the
premium is paid and what instrument is used. This view carries over to any multi-currency
book.

**It is narrow and technical.** The article describes conventions; it does not test
anything. It is a reference to keep open while reading the smile, vanna-volga and SLV
material.

## Links

The other FX smile notes are in this folder; see the section README.
- [[reiswich-wystup-2012-fx-volatility-smile-construction]] — the follow-up: building the smile from the quotes these conventions define
- [[garrivier-2020-fx-vanilla-pricing-and-smile-calibration]] — the same conventions worked through for a USD/JPY smile calibration
- [[wystup-2017-fx-options-and-structured-products]] — the book-length treatment of FX conventions and products
