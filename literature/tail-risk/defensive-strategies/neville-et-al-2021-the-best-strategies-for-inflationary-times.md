# The Best Strategies for Inflationary Times

| | |
|---|---|
| **Authors** | Henry Neville, Teun Draaisma, Ben Funnell, Campbell R. Harvey, Otto Van Hemert (Man Group; Harvey also Duke) |
| **Year** | 2021 (SSRN version of 25 May 2021); published in *The Journal of Portfolio Management* 47(8), 8–37 |
| **Type** | Research paper, SSRN 3813202, 32pp. US data from 1926, plus the UK and Japan |
| **PDF** | Not hosted in this repository (SSRN download; the published version is JPM copyright) |
| **Find it** | [doi.org/10.3905/jpm.2021.1.274](https://doi.org/10.3905/jpm.2021.1.274) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Best+Strategies+for+Inflationary+Times%22+Neville) |
| **BibTeX** | `neville2021inflation` |
| **Status** | Reference: Exhibit 2 (US summary), the regime definition, Exhibits 4–9 (equities, bonds, TIPS, commodities) and Exhibits 13–14 (equity factors and trend) |

## What it is

A long-history study of which assets and strategies held their value when inflation surged.
It does not try to forecast inflation. It was written in spring 2021, when US M2 had grown by
$4.2tn in a year and the fiscal deficit was 15% of GDP.

- **How an inflation regime is defined.** A regime starts when year-on-year headline CPI
  accelerates and reaches 5% or more. It ends at the inflation peak, provided inflation does
  not then fall below half that peak within a rolling 24-month window. Episodes shorter than
  six months are dropped. The rule gives eight US regimes since 1926, and 34 across the US,
  UK and Japan.
- **Results for traditional assets.** All are real annualised returns during US
  inflationary regimes:
  - **Equities:** about −7%, negative in 75% of regimes. No sector protects; energy is only
    about +1%.
  - **Treasuries:** −3% (2-year), −5% (10-year) and −8% (30-year). Investment-grade and
    high-yield credit are both about −7%.
  - **TIPS:** about +2% over the five regimes with data. That is no better than in normal
    times, and the authors note that their real yield was then −0.7%, against +2.4% at the
    start of past regimes.
- **Hard assets.**
  - **Commodities:** an equal-weighted commodity basket had positive real returns in all
    eight regimes, averaging about +14% a year, against low single digits in normal times.
    Precious metals made about +11% and industrial metals about +19%. Agricultural
    commodities and softs were weakest, though still positive.
  - **Real estate:** residential real estate was about −2%.
  - **Collectibles:** art (+7%), wine (+5%) and stamps (+9%) did well but are illiquid.
- **Dynamic strategies.**
  - **Trend:** a time-series momentum strategy across futures made positive real returns in
    inflationary regimes in every asset class. The bond and commodity trend sleeves were
    positive in every single regime.
  - **Equity factors:** cross-sectional momentum averaged +8% real, but the difference from
    normal times is not significant. Quality made about +3%, value about −1%, size about −4%
    and low beta (BAB) about −3%.
- **The equity–inflation relation depends on the starting level.** Using overlapping 12-month
  windows since 1926, rising inflation helped equities when inflation started below about 1%,
  where deflation is the risk. It hurt them, increasingly, from higher starting levels.

## Why it's in the library

- **It is the reference result for the 60/40 portfolio in an inflation surge.** Both stocks and
  bonds lose in real terms at the same time. The stock–bond diversification that most
  portfolios rely on therefore fails exactly in these regimes.
- **The method is reusable.** It defines regimes in advance by rule, reports a per-episode hit
  rate next to the average, and gives a t-statistic for regime versus non-regime returns. It
  also checks the regime results with a second method based on inflation betas.
- **Read the strategy results with the sample in mind.** There are only eight US episodes,
  several overlap with one another (the 1970s), and the trend and factor series are backtests
  with assumed costs. Gold behaves very differently across episodes; the paper cites Erb and
  Harvey's view that it is too volatile to be a reliable hedge. The trend result is the most
  robust part, because inflation shocks tend to unfold over months, not overnight.

## Links

- [[keller-keuning-2023-haa]] — a tactical allocation rule built to switch out of bonds when
  real yields and inflation are rising
- [[chen-roll-ross-1986]] — unexpected inflation as a priced macroeconomic factor in stock
  returns
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — why trend
  rules work when regimes persist
- [[harvey-et-al-2020-strategic-risk-management-out-of-sample-evidence-from-covid-19]] — the
  same team's test of its crisis-protection rules in the 2020 selloff
