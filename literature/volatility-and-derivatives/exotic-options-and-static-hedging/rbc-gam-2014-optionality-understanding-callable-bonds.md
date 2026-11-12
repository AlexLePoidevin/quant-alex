# Optionality: Understanding Callable Bonds

| | |
|---|---|
| **Authors** | RBC Global Asset Management (no individual authors; "RBC GAM Fundamental Series") |
| **Year** | 2014 (data to July 2014) |
| **Type** | Asset manager's educational piece, 8pp |
| **PDF** | Not hosted in this repository (manager marketing material, no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Optionality%3A+Understanding+Callable+Bonds%22+Management) for the title and authors |
| **BibTeX** | `rbcgam2014callable` |
| **Status** | Reference: short and introductory; the total-return comparison on p.5 is the only data |

## What it is

A plain-language guide for institutional investors to bonds the issuer can redeem early,
using callable US agency notes as the example.

- **What is being sold.** A callable bond is an ordinary bond plus a call option the
  investor has sold to the issuer. The issuer calls when rates fall, so it can refinance
  more cheaply, and does not call when rates rise. Agencies use callables partly to match
  their mortgage assets, which borrowers can prepay in the same circumstances.
- **Call styles.** European (one date), Bermudan (a schedule of dates), American (any time
  after the first call date) and Canary (callable on a schedule for a set period, then not).
  The call price may be fixed, follow a schedule, or be set by a make-whole formula.
- **The risks.** Call risk (uncertain cash flows), interest-rate risk (the bond stays
  outstanding when rates rise, so its price falls like a longer bond), and reinvestment
  risk (principal comes back when rates are low).
- **Measuring it.** Yield to maturity overstates the return. Yield to call and yield to
  worst (the lowest across all call dates) are better, and option-adjusted spread (OAS)
  strips out the value of the option so callables and bullets can be compared.
  OAS = spread − spread attributable to the option.
- **The one piece of evidence.** A 3-year callable agency bought in January 2007 and rolled
  into identical callables when called, against a 1–3 year government index, January 2007
  to December 2011: the callable returned 0.89% over one year, 1.27% a year over three and
  2.34% a year over five, against 1.55%, 1.56% and 3.69% for the bullets. Rates were falling
  over the period, which is exactly when the call costs the investor most.

## Why it's in the library

**It is the most common short-volatility position investors hold without thinking of it
as one.** The extra yield on a callable is the premium for a written option on interest
rates. The investor gives up the gains when rates fall and keeps the losses when they rise:
negative convexity. Reaching for yield with callables, mortgages or structured notes is
selling volatility, the same trade [[cole-2017-volatility-and-the-alchemy-of-risk]] argues
is hidden across many strategies.

**It is introductory marketing.** The single backtest uses one structure over a period of
falling rates, which favours the conclusion. The piece names OAS but does not show how to
compute it (that needs a model of interest-rate volatility).

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — reaching for yield by selling
  optionality, as part of a market-wide short-volatility trade
- [[bossu-strasser-guichard-2005-just-what-you-need-to-know-about-variance-swaps]] — the
  equity version of being paid to carry convexity risk
