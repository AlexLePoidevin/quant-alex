# Left Tail Risk and Left Tail Momentum

| | |
|---|---|
| **Authors** | Larry Swedroe (Alpha Architect blog) |
| **Year** | 2020 (posted 14 July 2020) |
| **Type** | Article: a 3-page blog summary of Atilgan, Bali, Demirtas and Gunaydin, "Left-Tail Momentum: Underreaction to Bad News, Costly Arbitrage and Equity Returns", *Journal of Financial Economics* 135(3), 725–753, 2020 |
| **PDF** | Not hosted in this repository (web-page printout, no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Left+Tail+Risk+and+Left+Tail+Momentum%22+Swedroe) for the title and authors |
| **BibTeX** | `swedroe2020lefttail` |
| **Status** | Reference for the summary; the numbers are the underlying JFE paper's |

## What it is

A summary of a study that tests whether stocks with more left-tail risk earn more, as a
risk-averse investor would demand. Left-tail risk is measured by recent value-at-risk and
expected shortfall from daily returns, on US stocks over 1962–2014.

- **The result is the opposite of a risk premium.** Stocks with high left-tail risk earn
  lower future returns. The highest-minus-lowest decile spread is −0.94% a month (t = −4.42)
  after risk adjustment, driven by the high-risk decile underperforming.
- **Persistence.** Left-tail risk is persistent, and the effect is strongest for stocks with
  large daily losses in both the formation month and the month before. Large losses tend to
  continue: "left-tail momentum".
- **Explanation.** The authors read it as underreaction: investors underestimate how
  persistent large losses are, partly through the disposition effect. The effect is stronger
  where individual investors dominate, institutional ownership is low and arbitrage is costly.
- **Robustness.** It survives controls for size, beta, idiosyncratic volatility, lottery
  demand and known factors, holds in international markets, and appears in mutual funds.

## Why it's in the library

It adds a downside version of momentum to the momentum topic: recent crash-like losses in a
stock predict more underperformance, not a rebound. That cuts against both the idea of a
tail-risk premium in single stocks and the intuition of buying what has just fallen hard.

This note is of the blog summary, not the paper; it gives no out-of-sample test, cost
estimate or capacity figure, and the stocks involved skew small and costly to trade, which
is where the effect is strongest.

## Links

- [[butt-virk-2020-momentum-crashes-and-variations-to-market-liquidity]] — the other side of
  momentum's tail: crashes of the winner-minus-loser portfolio
- [[goetzmann-kim-2018-negative-bubbles-what-happens-after-a-crash]] — at the market level,
  very large falls tend to be followed by recoveries, unlike these single-stock losses
- [[kelly-moskowitz-pruitt-2021-understanding-momentum-and-reversal]] — a risk-based account
  of momentum and reversal in stocks
