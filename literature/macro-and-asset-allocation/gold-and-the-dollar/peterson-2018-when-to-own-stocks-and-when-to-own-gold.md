# When to Own Stocks and When to Own Gold

| | |
|---|---|
| **Authors** | Timothy F. Peterson (Cane Island Alternative Advisors) |
| **Year** | 2018 (*The Journal of Wealth Management* 21(3), 26–36; doi:10.3905/jwm.2018.21.3.026). The copy is the SSRN 3535152 version dated 13 January 2018 |
| **Type** | Practitioner journal article, 18pp; annual data 1871–2016 |
| **PDF** | Local copy only (SSRN copy of a Pageant Media journal article) |
| **BibTeX** | `peterson2018gold` |
| **Status** | Reference: "A better secular market indicator", the SMI regressions (Exhibits 3–6) and the decision rule (Exhibits 10–12) carry the argument |

## What it is

A manager's proposal for a once-a-decade switch between US stocks and gold, based on
whether the economy is in a *secular* (5–25 year) bull or bear market.

- **The indicator.** The secular market indicator (SMI) is Shiller's CAPE ratio divided by
  the log of the nominal gold price. The idea is to measure equity valuation against a
  real asset instead of against CAPE's own history. That history drifted upward after
  1980, so CAPE stopped giving clean signals.
- **The fit.** Regressed (in first differences) on the next ten years' log S&P 500 return,
  the SMI gives R² of about 0.40 on 125 annual observations, "only a slight improvement" on
  CAPE by the author's own account. Coding only the years where the re-centred SMI is above
  +1 or below −1 as a ±1 dummy raises R² to 0.61 on 49 observations.
- **The rule.** Hold gold once the SMI crosses above +1, until it crosses below −1. Then
  hold stocks until it crosses above +1 again. All in, no blend. The thresholds were
  chosen "by visual inspection" of the full history.
- **Results since 1886 (inflation-adjusted, annual).**

  | | Stocks | Gold | Switching rule |
  |---|---|---|---|
  | Average return | 5% | 1% | 8% |
  | Worst year | −58% | −38% | −28% |
  | Sharpe ratio | 0.26 | 0.05 | 0.56 |

  The rule beats both buy-and-hold portfolios in about 70% of rolling ten-year periods.
- **Bull and bear regimes.** In secular bears (67 years) stocks averaged −2% with a
  Sharpe of −0.13 while gold (post-1971 data) averaged +13%. In secular bulls stocks
  averaged +12% and gold −1%.

## Why it's in the library

It is a clear statement of the long-cycle view of gold: gold is the asset for decades when
financial assets are expensive and the economy stagnates, not a crash-day hedge. It also
links valuation (CAPE) to regime-switching asset allocation.

Treat the backtest with suspicion, though:
- The thresholds were picked by looking at the whole sample, and the author concedes the
  model is "constructed with the benefit of hindsight".
- The rule trades only a handful of times in 130 years, so the result rests on very few
  independent decisions.
- Gold's price was fixed before 1971, so the indicator's denominator barely moved for most
  of the sample, and the gold-side regime statistics use only post-1971 data.
- Ten-year forward returns overlap heavily, which overstates the regression's significance.
- The author runs a global macro strategy.

## Links

- [[baur-kuck-2020-the-timing-of-the-flight-to-gold]] — what gold does on the day of a crash, the short-horizon complement to this long-cycle view
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — a statistical model of bull and bear markets (with bear rallies and bull corrections) on the same long S&P 500 history
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — switching between stocks and cash on a bull/bear regime model, derived rather than eyeballed
- [[keller-keuning-2016-paa]] — a rules-based risk-on/risk-off allocation that moves to safe assets on momentum signals
