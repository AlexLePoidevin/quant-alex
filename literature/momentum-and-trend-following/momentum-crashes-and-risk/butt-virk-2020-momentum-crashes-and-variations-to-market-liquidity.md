# Momentum Crashes and Variations to Market Liquidity

| | |
|---|---|
| **Authors** | Hilal Anwar Butt (IBA Karachi) and Nader Shahzad Virk (Plymouth Business School) |
| **Year** | 2020 (SSRN 3314095 working paper; published online 2020 in *International Journal of Finance & Economics* 27(2), 1899–1911, 2022) |
| **Type** | Working paper, 41pp. US monthly data, June 1965–December 2012, using Ken French's momentum deciles |
| **PDF** | Not hosted in this repository (SSRN working paper; journal version © Wiley) |
| **Find it** | [doi.org/10.1002/ijfe.2249](https://doi.org/10.1002/ijfe.2249) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Momentum+Crashes+and+Variations+to+Market+Liquidity%22+Butt) |
| **BibTeX** | `butt2020crashes` |
| **Status** | Reference: the regressions on down-market states interacted with liquidity changes, and §5 (conclusion) carry the result |

## What it is

Momentum (winners minus losers, sorted on months t−12 to t−2) occasionally crashes, mostly
after market declines when the market rebounds (Daniel and Moskowitz 2016). This paper adds
market liquidity, measured by the Amihud (2002) price-impact measure.

- **The asymmetry.** After a down market, a month in which market liquidity improves
  produces a large momentum loss (coefficient −9.665, t = −8.92); a month in which it
  worsens produces only a small gain (1.233, t = 2.19).
- **Mechanism.** Past losers are less liquid than past winners, so they rally harder when
  liquidity returns, and the short leg drives the crash.
- **What it subsumes.** Once contemporaneous liquidity changes are included, the market
  rebound, lagged market variance, momentum volatility and the momentum gap are subsumed or
  weakened as explanations of crashes. The result also holds for a
  momentum strategy built to remove the option-like market exposure (Grobys 2018).
- **Robustness.** The effect is weaker with the Pástor–Stambaugh liquidity measure than with
  Amihud's.

## Why it's in the library

It gives a liquidity reading of momentum crashes: the dangerous moment is a relief rally
after a selloff, when illiquid losers snap back. That links momentum risk to the bear-market
rally and reversal material elsewhere in the library.

The key variable is the same-month change in liquidity, so this explains crashes after the
fact rather than predicting them, and it does not give a trading rule. The sample ends in 2012.

## Links

- [[swedroe-2020-left-tail-risk-and-left-tail-momentum]] — tail risk in momentum from the
  single-stock side
- [[kelly-moskowitz-pruitt-2021-understanding-momentum-and-reversal]] — momentum's
  time-varying factor exposures
- [[collin-dufresne-daniel-2015-liquidity-and-return-reversals]] — liquidity and reversal at
  short horizons
- [[goetzmann-kim-2018-negative-bubbles-what-happens-after-a-crash]] — rebounds after large
  market falls, the conditions in which momentum crashes
- [[fan-et-al-2022-momentum-and-the-cross-section-of-stock-volatility]] — cutting crash risk at selection by scaling past returns by volatility
