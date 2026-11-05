# Fire and Ice: Confronting the Twin Perils of Inflation and Deflation

| | |
|---|---|
| **Authors** | AQR Portfolio Solutions Group (work credited to Alfie Brixton, Jordan Brooks, Thomas Maloney and Ashwin Thapar) |
| **Year** | 2020 (*Alternative Thinking*, Q4 2020) |
| **Type** | Manager research note, 18pp. US data January 1972 – June 2020 |
| **PDF** | Local copy only (AQR publication, no open licence) |
| **BibTeX** | `aqr2020fireice` |
| **Status** | Reference: the inflation sensitivity metric (Exhibit 5), the upside/downside surprise betas (Exhibit 6) and the growth/inflation regime table (Exhibit 9) carry the results |

## What it is

Written at the end of 2020, when the pandemic had produced both deflationary shocks
(collapsing demand, a large output gap) and potentially inflationary responses (money
supply growth larger than in 2008, offset by a fall in money velocity). AQR notes that
survey forecasts and CPI cap/floor prices still showed inflation expectations anchored
near 2%, and that the inflation risk premium (breakevens minus survey forecasts) was
negative, meaning investors were paying to hold nominal bonds as deflation insurance.

The core of the paper measures how investments respond to inflation, controlling for
growth:

- **An inflation sensitivity metric** combining three measures: Sharpe ratios in
  positive versus negative 12-month inflation surprises, Sharpe ratios in rising versus
  falling inflation regimes, and correlation with subsequent inflation, each controlling
  for growth.
- **Results 1972–2020:** stocks, bonds and real estate all have negative sensitivity
  (Treasuries −0.77, real estate −0.54, US 60/40 −0.45); credit and TIPS are near zero;
  breakevens, commodities and gold are strongly positive. A simple risk parity portfolio
  is noticeably less negative than 60/40. Since 1997 equities are slightly positive, which
  the authors attribute to demand-driven inflation and the absence of any severe
  inflation episode in that window.
- **Asymmetry.** Equities and bonds suffer about equally from upside inflation surprises,
  but bonds gain much more from downside surprises. Trend following and macro momentum
  gain from surprises in both directions.
- **Stock–bond correlation.** It has been higher when inflation surprises are larger
  than growth surprises; commodities have diversified both in those periods.
- **Regimes.** Across growth up/down and inflation up/down quarters since 1972, a global
  60/40 earned 0.3× its long-run Sharpe ratio in "inflation up" periods. Adding 20% risk
  parity, 10% trend and 10% macro momentum raised that to 0.6×.

The recommendation is resilience rather than a forecast: a risk-balanced allocation that
keeps nominal bonds for deflation and holds commodities for inflation, plus dynamic
trend and macro strategies that can go either way.

## Why it's in the library

It gives a usable answer to "what hedges inflation" with the growth confound removed,
and it states the asymmetry that matters for crisis protection: nominal bonds help in a
deflationary bust but not in an inflationary one. That frames why the stock–bond
correlation can turn positive, the failure mode for 60/40 that other notes in this
section study.

The strategies are AQR's hypothetical backtests (trend and macro momentum are discounted
in the backtest to allow for data mining), the metric's weights are chosen by the
authors, and the recommended allocations are AQR products. The sensitivities are
evidence; the portfolio advice is the manager's argument.

## Links

- [[aqr-2017-exploring-rates-sensitivity]] — the earlier study of hiking cycles, real
  yields and expected inflation across the same assets
- [[aqr-2021-inflation-outlook-the-macro-the-micro-the-transitory]] — the follow-up a
  year later, when US CPI had reached 5%
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — another manager's view that a
  regime change in inflation would break strategies built on a stable stock–bond
  correlation
- [[chen-roll-ross-1986]] — inflation as a priced macro factor in stocks
- [[barnes-et-al-2009-a-tips-scorecard]] — what TIPS do and do not hedge: a locked-in real yield to maturity, but mostly real-rate risk over a one-year holding
