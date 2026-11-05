# Gold's Value as an Investment

| | |
|---|---|
| **Authors** | Urban J. Jermann (Wharton School; NBER) |
| **Year** | 2022 (draft of 26 April 2022, SSRN 3934052; later NBER Working Paper 31386, 2023) |
| **Type** | Working paper, 35pp. Theory plus calibration to US real yields, 1975–2020 |
| **PDF** | Local copy only (SSRN working paper, no open licence) |
| **BibTeX** | `jermann2022gold` |
| **Status** | Reference: §2 (gold and real rates, Table 1), §4 (two-state example), §6 (calibration, Table 3) |

## What it is

A no-arbitrage model of what gold is worth to investors, given that it pays no yield.

- **The stylised fact.** The real gold price and real Treasury yields are negatively
  related, as earlier studies found, but over 1975–2020 the link is weak unconditionally.
  It comes from low-rate periods. Regressing gold price changes on 10-year real yield
  changes in the third of months with the lowest yields gives an R² of 0.35 monthly and
  0.65 annually; in high-rate periods the relation all but disappears.
- **The idea.** Two kinds of holder. Users (jewellery, industry) value gold for its use.
  Investors hold it only as a store of value, like a zero-coupon real bond, so they buy
  when real rates are low and sell when rates rise. When they sell, users absorb the gold
  at a floor price. That floor gives investors an embedded put option, and the chance that
  investors come back raises the price even while they are out of the market.
- **The model.** Prices come from an exogenous stochastic discount factor (a Vasicek
  model of real rates) without specifying investor preferences, and are solved like a
  fixed-income derivative. A two-state version has closed-form solutions; the general
  version is a fixed point the paper proves exists.
- **Results.** In the benchmark calibration investors are out of the market 71% of the
  time, yet the average gold price is 3.8 times what it would be if only users ever held
  it: more than two-thirds of gold's value comes from its investment role. That number is
  sensitive to one parameter: across the plausible range investors add between 30% and
  more than 500% to gold's value. Real-rate moves explain a little over a quarter of gold
  price volatility (4.3% against 14.8% a year). Fitted to 10-year real yields, the model
  tracks the main swings in gold since about 2007; adding the real dollar exchange rate
  improves the fit before 2007.

## Why it's in the library

**It explains why gold and real yields are linked only some of the time.** The option
structure makes the relation non-linear: when real rates are high, investors are absent
and gold behaves like a commodity; when rates fall, investors enter and gold trades like a
long-duration real bond. That fits the post-2007 period, when gold and TIPS yields moved
closely together.

**It is a pricing model, not a timing rule.** Its headline numbers depend on a calibrated
parameter with a wide plausible range, and the fit before 2007 needs an extra
exchange-rate factor.

## Links

- [[capie-mills-wood-2005-gold-as-a-hedge-against-the-dollar]] — the dollar side of gold, which this model needs before 2007
- [[baur-smales-2018-gold-and-geopolitical-risk]] — a non-rate driver of gold demand
- [[keller-keuning-2023-haa]] — a tactical allocation rule that uses TIPS as its signal for rising real yields
- [[brooks-2021-what-drives-bond-yields]] — what drives the real yields that drive gold here
