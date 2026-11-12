# Stock Market Bubbles and Anti-Bubbles

| | |
|---|---|
| **Authors** | Martin B. Tarlie, Georgios Sakoulis, Roy Henriksson (QMA; Tarlie later at GMO) |
| **Year** | 2022 (International Review of Financial Analysis 81, 101235); the copy here is the working paper dated 11 July 2018 (SSRN 2859795) |
| **Type** | Working paper (empirical asset pricing, state-space model), 42pp |
| **PDF** | Not hosted in this repository (SSRN working paper; the journal version is Elsevier) |
| **Find it** | [doi.org/10.1016/j.irfa.2018.07.012](https://doi.org/10.1016/j.irfa.2018.07.012) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Stock+Market+Bubbles+and+Anti-Bubbles%22+Tarlie) |
| **BibTeX** | `tarlie2022antibubbles` |
| **Status** | Reference: §3 (the valuation model), §4.2 (time-varying mean reversion), Table 4 and §6.3 (the mechanism) carry the results |

## What it is

A definition of stock market bubbles, and their mirror image *anti-bubbles*, as periods
when valuation stops mean-reverting and briefly runs away from fair value, estimated on
US data back to 1871.

- **Valuation.** Fair value is a fixed multiple (15.5) of trailing ten-year real
  earnings, as in the Shiller CAPE. Valuation is the log of price over fair value, so a
  market twice as expensive and one half as cheap sit symmetrically either side of zero.
  Returns split into the change in valuation, growth in fair value, and income.
- **The innovation.** Valuation mean-reverts, but the *speed* of mean reversion is itself
  a random, mean-reverting quantity, estimated with a Kalman filter (and GARCH errors).
  When the speed turns negative, expensive markets get more expensive and cheap ones get
  cheaper: valuation is temporarily explosive.
- **Five episodes in 1881–2017.** Anti-bubbles in the late 1910s/early 1920s and the
  early 1980s; bubbles in 1929, the late 1990s, and 2017, the time of writing. Large
  crashes with roughly neutral valuations, such as 1974, 1987 and 2008, are not flagged:
  in those, valuation became *more* important for returns, not less.
- **What drives the speed.** Regressing the estimated speed on powers of valuation and on
  valuation times the expected change in profitability (profitability is modelled as an
  AR(2) process with a roughly nine-year cycle) gives an R² of 0.33. With a four-quarter
  lag of squared valuation added, the R² rises to 0.49.
- **The mechanism.** Bubbles form when an expensive market meets rising expected
  profitability, and anti-bubbles when a cheap market meets falling profitability. They
  burst, or reflate, when the expected change in profitability flips sign. The economic
  story is capital supply: high profits bring heavy investment, which eventually drives
  profits back down.
- **Return implications.** In a bubble the valuation effect is reversed: expensive
  markets are expected to get more expensive in the short run, but the term structure of
  expected returns falls steeply over the next two years, so the market is unstable.
  Changes in valuation contribute nothing to long-run returns; on average, returns come
  from growth plus dividends.

## Why it's in the library

**It treats cheap markets and expensive markets with one model.** Most bubble tests only
look for explosive *rises*. Working with the log of price over fair value makes the
early-1980s cheapness the mirror image of the late-1990s expense, which is relevant to
bear markets as much as to booms.

**It explains why value signals sometimes stop working.** If the mean-reversion speed can
turn negative, a valuation-based forecast can be wrong-signed for years at the extremes,
exactly when it looks most compelling. That is a concrete warning for anyone timing the
market on CAPE.

**Read the evidence carefully.** Several things limit how far the results go:

- **Fair value is assumed**, not estimated: a constant multiple of ten-year earnings,
  with pre-1926 earnings scaled down by 0.89 to match average returns.
- **The bilinear term is fragile.** It is the paper's key mechanism (valuation times
  expected change in profitability). It is significant on its own (−10.3, standard error
  2.6), but not once the lagged valuation term is added (−2.8, standard error 3.3).
- **The fourth-power term**, which keeps valuation bounded, is never significant.
- **Five episodes in 137 years** is very little to estimate a mechanism from.

The 2017 "bubble" call came with no timing, and the model makes no claim to predict when
a bubble bursts.

## Links

- [[gurkaynak-2008-econometric-tests-of-asset-price-bubbles]] — the standard bubble tests this paper contrasts with (unit-root and regime-switching approaches)
- [[phillips-shi-2018-real-time-monitoring-of-asset-markets-bubbles-and-crises]] — the explosive-root test that this paper reframes as a negative mean-reversion speed
- [[goetzmann-kim-2018-negative-bubbles-what-happens-after-a-crash]] — the empirical evidence on what happens after very cheap, post-crash markets
- [[west-1988-bubbles-fads-and-stock-price-volatility-tests]] — the excess-volatility evidence that motivates time-varying discount rates
- [[campbell-1991]] — the return decomposition into expected-return news and cash-flow news
