# How Does the Daily Volatility of Foreign Exchange Rates Depend on the Time of Day at Which the Daily Returns Are Calculated?

| | |
|---|---|
| **Authors** | Małgorzata Doman (Poznań University of Economics and Business), Ryszard Doman (Adam Mickiewicz University, Poznań) |
| **Year** | 2020 (SSRN posting, July 2020) |
| **Type** | Working paper, 19pp (SSRN 3651344) |
| **PDF** | Local copy only (SSRN working paper with no open licence) |
| **Link** | <https://ssrn.com/abstract=3651344> |
| **BibTeX** | `doman2020timeofday` |
| **Status** | Reference: §3 (data and the intraday pattern) and §4 (results per pair) carry it; the conclusions are one page |

## What it is

An empirical check of something usually taken for granted: that "daily volatility" of an
exchange rate is one number. FX trades around the clock, so a daily return can be measured
from any hour to the same hour the next day, and the paper asks whether the choice of hour
changes the volatility estimate.

- **Data.** EUR/USD, GBP/USD, AUD/USD and NZD/USD from Dukascopy, March 2003 to October
  2019 (4,216 daily returns for each hour). Bid and ask prices are analysed separately,
  for every hour 0:00–23:00 London time: 192 daily return series in all.
- **The intraday pattern.** Average absolute one-hour returns peak at the Asian open
  (1:00 London), the European open (7:00–9:00), the US open (13:00–15:00) and the US close
  (22:00).
- **Models.** An ARMA–GARCH model is fitted to each series, choosing among GARCH,
  GJR-GARCH and APARCH with normal, Student-t or skewed-t errors. Most chosen models are
  asymmetric (GJR or APARCH), with the base currency's depreciation against the dollar
  raising volatility more than its appreciation. The authors add a dummy for the weeks
  when US daylight saving time is in force but European time is not, because it shifts
  the market opens.
- **Results.** The volatility estimates differ visibly by hour, and most clearly for hours
  near market opens and closes. The day-by-day range of the 24 hourly estimates goes from
  about 0.03 to 0.47 (percentage points of daily volatility) for EUR/USD, up to 1.93 for
  GBP/USD ask prices around the Brexit referendum, and up to about 2.2 for AUD/USD.
  Bid and ask volatility also differ at some hours (for example EUR/USD at 19:00–20:00
  London, NZD/USD around the New Zealand open). For AUD/USD and NZD/USD every fitted model
  has strongly significant negative skewness.
- **Why it matters for risk.** A rough calculation: a 0.2 difference in the daily
  volatility estimate changes the 10-day 99% VaR of a $100,000 position by about $4,650.
  So a risk manager in Sydney and one in New York, each using local-hour closes, can see
  the same position as more or less risky, and a manager could in principle choose the
  hour that flatters the number.

## Why it's in the library

It is a concrete demonstration that the sampling time of "daily" data is a modelling
choice, not a given, in a market with no single close. The same issue arises for any
daily FX feature, label or risk number: the estimate depends on when the day is cut, and
the differences are largest around the opens and closes. The paper documents the effect
descriptively; it does not test which hour gives better forecasts or better-calibrated
VaR.

## Links

- [[lv-wang-yuan-2026-garch-evt-rvine-scad-portfolio]] — GARCH-filtered marginals feeding
  a tail-risk portfolio, where the volatility estimate is an input like the one studied
  here
- [[rockafellar-uryasev-2000]] — VaR and CVaR, the risk measures whose value shifts with
  the hour chosen
