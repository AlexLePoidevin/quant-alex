# Volatility and the Changing Market Structure Driving U.S. Equities

| | |
|---|---|
| **Authors** | The Ambrus Group (Ambrus Capital); no individual author named |
| **Year** | 2022 (undated; data run to January 2022 and the references were accessed in May 2022) |
| **Type** | Manager white paper, 16pp |
| **PDF** | Not hosted in this repository (manager marketing material with no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Volatility+and+the+Changing+Market+Structure+Driving+U.S.+Equities%22+Group) for the title and authors |
| **BibTeX** | `ambrus2022structure` |
| **Status** | Reference: §III (the ten causes) carries the argument; §IV–V are the case for holding volatility |

## What it is

A tail-risk manager's account of why US equities have become **fragile**: calm most of the
time, but liable to fall very fast. The paper calls the mechanism "reflexivity", after
Soros, and says it means any feedback loop that pushes prices further in the direction
they are already moving.

The causes it lists:

- **Speculative frenzy.** Valuations near records (market cap / GDP), a generation of
  investors who have never seen a long bear market, phone-based trading, meme stocks and
  Dogecoin. Call skew in one-month SPX options rose from 2019 to 2022, which the paper
  reads as more appetite for upside leverage.
- **Gamma reflexivity.** End users mostly buy options and dealers sell them. A dealer
  hedging a short option position has to sell as the price falls and buy as it rises,
  which can push the price further. Small moves get reversed, which looks like stability,
  but a large shock can cascade. As evidence it shows a backtest of buying the S&P 500 at
  the close the day before monthly option expiry and selling at the expiry close: about a
  15% loss over three years (2020–2022).
- **Few market makers.** The OCC's Q3 2021 report says four banks held 89.3% of banking
  industry derivative notional. The paper adds that 80% of retail option contracts are
  routed to four wholesalers.
- **Regulation (Dodd–Frank).** Banks have hard risk limits, so a position that breaches
  them has to be hedged immediately whatever the price. That makes hedging
  price-insensitive.
- **Structured products.** Yield products such as worst-of autocallables leave dealers
  long puts and exposed to short-dated volatility, which they hedge in listed options.
- **Passive investing.** $7.3tn in US passive open-ended funds by 2021, overtaking active
  funds. Leveraged and inverse ETFs must rebalance in the direction of the day's move: a
  3× fund with $100m that sees its index rise 1% must buy $6m more. The paper links this
  to the February 2018 "Volmageddon".
- **Common risk triggers.** Banks and funds use similar VaR and VIX-based limits, so they
  deleverage together.

It then argues that large losses are hard to recover from (−50% needs +100%), that the
S&P 500 had five 30-day drawdowns of 20% or more since 2000, and that bonds and gold were
not reliable hedges in recent crashes. It concludes that investors should hold a small,
actively managed allocation to volatility.

## Why it's in the library

**It is a practitioner's list of the mechanisms behind the "calm, then crash" pattern.**
Several of them are real and documented elsewhere:
- leveraged-ETF rebalancing;
- dealer hedging of option inventory;
- concentration among option dealers;
- forced, price-insensitive hedging under risk limits.
The note is useful as a map of where to look.

**The evidence is thin, and much of it is assertion.** The expiry-day backtest is one
three-year window with no costs and no test of significance. "Market makers are short
gamma" is assumed rather than measured; the 2023 Ambrus paper on 0DTE options finds the
opposite flow pattern in normal conditions. Correlation of Bitcoin with Nasdaq and the
Dogecoin anecdote are colour, not evidence. The paper also contains a date error: the
intraday reversal it describes happened on 24 January 2022, not 2021.

**It is written to sell a product.** It ends by recommending a volatility allocation run
by professionals and declines to describe its own approach ("proprietary"). Read it as
the argument for long volatility, not as a neutral survey.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the earlier, more detailed version
  of the same thesis: volatility-sized strategies as one hidden short-volatility trade
- [[soros-2013]] — the reflexivity idea the paper borrows, and loosens to mean any
  feedback loop
- [[avellaneda-zhang-2010]] — the mathematics of daily-rebalanced leveraged ETFs, the
  rebalancing flow the paper describes
- [[huang-rise-of-passive]] — the rise of passive investing, one of the paper's causes
- [[peters-2011]] — the ergodicity argument behind "never take a big loss"
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]]
  — the same firm's case for trading hedges on price rather than by a fixed rule
- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]] — evidence on the dealer-gamma claim this paper leans on
- [[cole-2018-what-is-water-in-markets]] — an earlier version of the same calm-then-crash structural argument
