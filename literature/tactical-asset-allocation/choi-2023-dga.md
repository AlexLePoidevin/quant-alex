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
2. S&P 500 trailing dividend yield ≥ **1.6%**, lagged one month
3. no 10y–3m inversion below **−0.5%** at any point **7 to 15 months** prior

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

Measured November 2012 – September 2026, the gates pass individually at 70% (TIP), 79%
(dividend yield) and 75% (curve), but all three together only **42.3%** of months.

The dividend-yield gate last passed in **May 2024** at 1.64% and has failed for **28
consecutive months** since. The S&P's trailing yield was 2.18% at the start of this window,
peaked at 2.76% in February 2016, and is **1.23%** now — the index has outrun its dividends
for a decade.

A fixed 1.6% threshold calibrated on fifty years of history does not survive that drift.
Absent roughly a 25% fall in the index or a sharp acceleration in dividend growth, gate two
does not reopen. The book has been risk-off for **40 consecutive months**, the longest run
in the sample, and it is ongoing.

This is a live design problem rather than a historical note: the paper was published in
November 2023, when the yield was still around 1.8%.

## Measured 2012–2026

| | DGA | 60/40 SPY–IEF |
|---|---:|---:|
| Ann. return | 12.84% | 9.57% |
| Ann. volatility | 15.19% | 9.97% |
| Sharpe | 0.87 | 0.97 |
| Sortino | 0.99 | 1.22 |
| Calmar | 0.45 | 0.46 |
| Max drawdown | −28.6% | −21.0% |
| Skew | −0.76 | −0.21 |

Holdings: QQQ 28.6% of months, SCHD 13.7%, defensive 57.7%.

**Reproduction notes.** SCHD begins October 2011, which sets the start date. DBC stands in
for PDBC (inception November 2014). The dividend yield is SPY's trailing twelve-month
distributions over price rather than the index's own; Shiller's canonical series ends mid
-2023 and is no longer usable for a current test. Yield curve from FRED `DGS10` − `DGS3MO`.

## Links

- [[keller-keuning-2023-haa]] — the single-asset TIP canary DGA reuses
- [[keller-keuning-2018-daa]] — the canary-universe idea behind both
