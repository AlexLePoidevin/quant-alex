# Replicating the CBOE VIX Using a Synthetic Volatility Index Trading Algorithm

| | |
|---|---|
| **Authors** | Dayne Cary and Gary van Vuuren (North-West University) |
| **Year** | 2019 (*Cogent Economics & Finance* 7(1), 1641063) |
| **Type** | Empirical paper, 21pp. Daily and monthly price data, 1995–2018; backtests 2004–2014 on IVV and ten large US stocks, plus examples on JSE stocks |
| **PDF** | `cary-van-vuuren-2019-replicating-the-cboe-vix-with-a-synthetic-volatility-index.pdf` (open access, CC BY 4.0) |
| **BibTeX** | `cary2019svix` |
| **Status** | Reference: Figure 1 (correlations), Tables 1–6 (backtests) |

## What it is

A practitioner paper on building a VIX-like indicator from prices alone, so it can be used on
stocks that have no options-based volatility index.

- **Two price-based indicators.** Larry Williams's "VIX fix" (VIXf): how far today's low sits
  below the highest close of the last 20 bars, as a percentage. The authors then rescale it to
  0–100% with a stochastic oscillator (where the latest value sits between the highest and
  lowest of the look-back window) and call the result SVIX.
- **Correlation with the VIX.** On monthly S&P 500 data from 1994, the correlations are 0.76
  (SVIX and VIX), 0.81 (VIXf and VIX) and 0.82 (SVIX and VIXf). Readings above 80% line up with
  market lows in the charts.
- **Trading rule.** Buy when SVIX is above 80% (buying on a stop above the previous day's high,
  or at the next close), exit at the first profitable open, with a fixed dollar stop loss. On
  IVV over November 2004 – October 2014, $1,000 a trade: 176 trades, 98.3% winners, $846 net
  profit, invested 24% of the time. On ten large US stocks (AAPL, C, CMCSA, F, GE, JPM, MA, TSM,
  UL, WFC), $1,000 per stock: 1,474 trades, 74.2% winners, $10,596 net profit on $10,000
  (about 10.6% a year), with $2 commissions.
- **Practical limits.** Stops must be wider for volatile emerging-market stocks, and illiquid
  JSE stocks cannot be traded this way at all.

## Why it's in the library

It is the simplest version of a common question: can you get a fear gauge for something that
has no listed options? The answer here is a price-based proxy that tracks the VIX loosely
(correlation about 0.76 on monthly data), which is useful context for the options-based
indices in this folder.

The trading evidence is weak and should not be taken as a result:

- The proxy is built from past prices only, so it measures how far the price has fallen, not
  expected volatility. That is why it peaks at market lows, and why buying at its peaks is a
  buy-the-dip rule.
- The high win rates come from exiting at the first profitable open with wide stops. The
  backtests have no benchmark (such as buy-and-hold over the same days) and no risk-adjusted
  measures.
- The ten stocks were chosen in 2018 from today's large companies (survivorship bias), the stop
  levels were tuned ("optimised to the general stock market"), and the series the stochastic
  oscillator is applied to is not stated precisely.
- The name collides with Ian Martin's SVIX, an unrelated options-based index (the simple
  variance swap index).

## Links

- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — how the real VIX is
  computed from SPX options, the benchmark this proxy imitates
- [[carr-wu-2006-a-tale-of-two-indices]] — why the VIX is defined from option prices as a
  variance-swap rate
- [[johannsen-2016-dead-cat-bounce]] — a model of why prices bounce after sharp falls, the
  pattern a buy-at-the-peak-of-fear rule tries to catch
