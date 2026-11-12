# What Drives Bond Yields?

| | |
|---|---|
| **Authors** | Jordan Brooks (AQR Capital Management) |
| **Year** | 2021 (July) |
| **Type** | Manager white paper, 27pp. Non-technical framework, with G6 regressions for 1990–2020 |
| **PDF** | Not hosted in this repository (AQR white paper, no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22What+Drives+Bond+Yields%3F%22+Brooks) for the title and authors |
| **BibTeX** | `brooks2021yields` |
| **Status** | Reference: §2 (the decomposition), §5–6 (policy and non-policy drivers), Exhibit 5 (the regression) |

## What it is

A framework for thinking about government bond yields, written when yields were near
record lows and many argued that central banks had made bond risk one-sided.

- **The decomposition.** A long bond's yield equals the average expected short rate over
  its life plus a term premium, the extra return demanded for holding a long bond instead
  of rolling short bills. So yields depend on three things: today's short rate, expected
  future short rates, and the term premium.
- **What central banks control.** Today's short rate and, through forward guidance, its
  near-term path. Rate policy, forward guidance, quantitative easing (QE), yield-curve
  control and average inflation targeting are presented as versions of one thing: each
  works by moving long yields. QE does it by removing duration from the market and
  compressing the term premium.
- **What they don't.** Long-horizon rate expectations converge to the natural real rate
  (r\*, tied to trend growth) plus long-term inflation expectations. Term premia depend on
  inflation uncertainty, counter-cyclical risk aversion, and demand for safe assets,
  including reserve managers and flight to safety in a crisis.
- **The evidence.** Across G6 markets, quarterly from 1990 to 2020, ten-year yields move
  roughly one-for-one with consensus forecasts of long-term inflation and real growth,
  whatever central banks are doing (Exhibit 5). At shorter maturities the current policy
  rate matters more. Yields also still react to news about unemployment and inflation in
  a similar way to earlier periods, even with policy rates near zero (Exhibit 4).
- **The secular decline.** From 2000 to 2021, the New York Fed's estimate of the US
  natural rate fell from 3.4% to about zero and long-term inflation expectations from
  3.2% to 1.6%, so r\* plus expected inflation fell from 6.6% to 1.6%. Ten-year Treasury
  yields fell from 6.5% to 1.5% over the same period. On this reading, fundamentals
  account for the whole decline.
- **The conclusion.** Bond risk is two-sided even at low yields. Yields can fall further
  with the policy rate fixed, and a fundamentals-driven approach to bonds still works.

## Why it's in the library

**It is the cleanest statement of the yield decomposition.** Short rate, expected path and
term premium is the identity every bond view has to fit into, and the paper uses it to
dismiss a common error: that a policy rate at its lower bound caps how far long yields can
fall.

**It separates policy from fundamentals.** The one-for-one link between long yields and
long-run growth and inflation expectations is the key fact. It explains why yields fell
for two decades and what would have to change for them to rise.

**It is a manager's framework, not a test.** The empirical support is a handful of
regressions and charts, and the r\* estimates it relies on are model outputs with wide
uncertainty. It was written in July 2021, just before the inflation surge, which tested
the "two-sided risk" point from the other direction.

## Links

- [[sun-carr-2018-bond-yield-curve-convexity-trading]] — a no-arbitrage argument about the shape of the yield curve
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — how a long period of falling yields and low volatility fed leverage across asset classes
- [[keller-keuning-2023-haa]] — a tactical rule that uses TIPS prices as its signal for rising real yields
