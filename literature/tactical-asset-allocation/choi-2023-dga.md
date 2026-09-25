# Balance Between Growth and Dividend: Dividend & Growth Allocation (DGA)

| | |
|---|---|
| **Author** | Paul Choi |
| **Year** | 2023 (20 November) |
| **Type** | Working paper — SSRN 4633601 |
| **Link** | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4633601 |
| **Also** | [Allocate Smartly](https://allocatesmartly.com/chois-dividend-growth-allocation/) |
| **BibTeX** | `choi2023dga` |
| **Status** | Rules verified, backtested |

## The rules

| | |
|---|---|
| **Offence** | QQQ (Nasdaq 100) or SCHD (Dow Jones US Dividend 100) — 100% in whichever has higher momentum, never both |
| **Defence** | BIL, TLT, PDBC — highest positive momentum, else cash |
| **Momentum, risk-on** | average of the 1-, 3-, 6-, 9- and 12-month return |
| **Momentum, risk-off** | close / 6-month average month-end close − 1 |
| **Rebalance** | monthly, last trading day |

Risk-on requires **all three** of:

1. TIP above its 12-month average — the single-asset canary from [[keller-keuning-2023-haa]]
2. S&P 500 trailing dividend yield ≥ **1.6%** — current price, previous month's dividend
3. no 10y–3m inversion below **−0.5%** at any point **7 to 15 months** prior

## Two details that are easy to get wrong

**The one-month lag applies to the dividend, not the yield.** Quarterly S&P dividend data
is not released in real time, so the rule uses *"the most recent S&P 500 cash price, but
the dividend value from the previous month"* — `D(t−1) / P(t)`, not `D(t−1) / P(t−1)`.
Lagging the whole ratio flips the gate in 7 of 168 months and moves the last passing month.

**The inversion is evaluated on monthly data.** Allocate Smartly use FRED `T10Y3MM`, the
monthly 10-year-less-3-month series. Checking the daily spread for *any* inverted day in
the 7–15 month window is materially stricter — it drops the gate's pass rate from 81.5% to
74.9% and flips 11 of 167 months.

## What is new here

Every other strategy in this folder reads prices. DGA's second and third gates read
**macro and valuation data that is not in the traded universe at all** — an index-level
dividend yield and a Treasury yield spread. The lag on the curve condition is the
interesting design choice: an inversion is a forward signal, so the strategy de-risks on
the *anniversary* of one rather than on the day, which is why the window is 7–15 months
rather than contemporaneous.

The canary lineage runs through [[keller-keuning-2018-daa]] and
[[keller-keuning-2023-haa]]; Choi cites both.

## ⚠️ The valuation gate has become structurally binding

Measured November 2012 – September 2026, the gates pass individually at 69.6% (TIP), 79.8%
(dividend yield) and 81.5% (curve), but all three together only **48.2%** of months.

The dividend-yield gate last passed in **April 2024** and has failed for **29 consecutive
months** since. The S&P's trailing yield was 2.02% at the start of this window, peaked at
2.76% in February 2016, and is **1.21%** now — the index has outrun its dividends for a
decade.

A fixed 1.6% threshold calibrated on fifty years of history does not survive that drift.
Absent roughly a 25% fall in the index or a sharp acceleration in dividend growth, gate two
does not reopen. The book has been risk-off for **40 consecutive months**, the longest run
in the sample, and it is ongoing.

This is a live design problem rather than a historical note: the paper was published in
November 2023, when the yield was still around 1.8%.

## Measured 2012–2026

| | DGA | 60/40 SPY–IEF |
|---|---:|---:|
| Ann. return | 14.04% | 9.57% |
| Ann. volatility | 16.26% | 9.97% |
| Sharpe | 0.89 | 0.97 |
| Sortino | 1.01 | 1.22 |
| Calmar | 0.49 | 0.46 |
| Max drawdown | −28.6% | −21.0% |
| Skew | −0.66 | −0.21 |

Holdings: QQQ 33.9% of months, SCHD 14.3%, defensive 51.8%.

**Reproduction notes.** SCHD begins October 2011, which sets the start date. DBC stands in
for PDBC (inception November 2014). The dividend yield is SPY's trailing twelve-month
distributions over price rather than the index's own; Shiller's canonical series ends mid
-2023 and is no longer usable for a current test. Yield curve from FRED `T10Y3MM`.

## Links

- [[keller-keuning-2023-haa]] — the single-asset TIP canary DGA reuses
- [[keller-keuning-2018-daa]] — the canary-universe idea behind both
