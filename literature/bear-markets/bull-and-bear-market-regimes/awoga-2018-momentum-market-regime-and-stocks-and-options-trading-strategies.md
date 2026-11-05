# Momentum, Market Regime and Stocks & Options Trading Strategies

| | |
|---|---|
| **Authors** | Oluwaseyi Awoga (MSc Financial Engineering capstone, WorldQuant University; supervisor Ritabrata Bhattacharyya) |
| **Year** | 2018 (dated December 2018; SSRN 3306329) |
| **Type** | Student capstone project, 19pp. S&P 500, January 2007 – November 2018 |
| **PDF** | Local copy only (SSRN upload, no open licence) |
| **BibTeX** | `awoga2018momentum` |
| **Status** | Reference: the four portfolio sections and Tables 1–4; useful mainly as a worked example of what not to conclude |

## What it is

A capstone project that adds a two-state hidden Markov model (HMM) "volatility regime"
filter to simple moving-average strategies on the S&P 500, and to option strategies
priced with Black–Scholes. It follows the 2018 IAQF student competition problem.

- **Portfolio 1, the index.** Long when the 10-day moving average is above the 50-day,
  short when below. Skipping new trades when the HMM says "high volatility" lifted the
  annualised return from 6.6% to 7.2% and the Sharpe ratio from 0.33 to 0.37, against
  5.5% and 0.28 for buy-and-hold (Table 1). The text calls the plain crossover's 52.3%
  cumulative return an outperformance of buy-and-hold's 73.2%, which contradicts itself.
- **Portfolio 2, short options.** Sell a 90-day at-the-money call (or put) each day
  depending on the crossover, buy it back the next day. Option prices come from
  Black–Scholes, not market data, and returns are defined as (premium − payoff)/payoff.
  The result is an "annualised return" of about 403,500% with a 100% win rate, which the
  author attributes to the data and the return formula.
- **Portfolio 3, long straddles.** Buying straddles only in the high-volatility regime
  does best (annualised Sharpe 4.4 against 3.6 unfiltered and 2.8 in the low-volatility
  regime).
- **Portfolio 4, a delta-hedged short straddle.** About 15% a year at 42% volatility,
  against 5.1% for buy-and-hold.

## Why it's in the library

**As a catalogue of backtest errors.** The HMM is fitted on the whole 2007–2018 sample
(and the author notes its state labels flip between runs and are set by hand), so the
regime filter uses future information. There are no transaction costs. Option prices are
synthetic, so the strategies trade at Black–Scholes values with constant volatility,
which removes the volatility risk premium they are meant to earn. The return definition
divides by a payoff that is often near zero. Each of these alone could produce the
headline numbers.

**The underlying idea is sound and well studied elsewhere.** Trend rules do worse in
high-volatility, choppy regimes, and long-volatility positions pay in volatile ones. The
regime notes linked below test that idea properly.

## Links

- [[srivastava-bhattacharyya-2018-dynamically-adaptive-systematic-trading-strategy]] — a
  companion capstone from the same programme and supervisor, with the same full-sample
  regime-labelling problem
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — the
  optimal trend rule derived inside a bull/bear Markov switching model
- [[ang-timmermann-2012-regime-changes-and-financial-markets]] — what two-state regime
  models on returns actually pick up (volatility more than direction)
- [[maheu-mccurdy-2000-identifying-bull-and-bear-markets-in-stock-returns]] — a
  properly estimated Markov-switching model of bull and bear markets
