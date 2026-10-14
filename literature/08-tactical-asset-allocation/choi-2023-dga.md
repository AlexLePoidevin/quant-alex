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

## Allocate Smartly's adversarial version

Allocate Smartly, who track DGA, make two changes and we follow the second here:

1. **TIP replaced by IEF before the TIP ETF existed (2003).** A data-quality hedge for
   their long history — TIPS index data does not exist before 1997 and simulations before
   then are an educated guess. Not applicable to a post-2012 test.
2. **The dividend-yield check removed altogether**, *"due to concerns that it's a rule
   overly fit to recent history."*

Their broader critique is about design rather than this rule alone: DGA takes one
straightforward idea — bonds as a predictor of risk-asset performance — and then narrows
time-in-market with further unrelated observations. *"The more we 'stack' historically
successful observations on top of each other, the more we increase the likelihood of
overfitting."* That is a different thing from diversifying across strategies, where the
complexity of each observation is unchanged.

## ⚠️ Why the valuation gate goes

The threshold binds only in recent memory. The S&P's yield first fell below 1.6% in the
late 1990s and, on Shiller's data, was nowhere near it at any point back to the 1870s.

Two facts, pulling opposite ways:

**Historically the gate does nothing.** Over Nov 2012 – Sep 2026 it was the sole blocker in
**6.0%** of months. With it, 14.04% a year at Sharpe 0.89; without it, 13.95% and 0.88 —
the equity curves are indistinguishable.

**Recently it does everything.** The yield fell through 1.6% for good in **April 2024** and
has stayed below. With the gate, the book has been defensive **40 consecutive months**;
without it, **three**. A rule that was redundant for a decade has become the binding
constraint, which is precisely the failure mode Allocate Smartly warned of: *"What if a
dividend yield of 1% becomes the norm in the future? The strategy would remain defensive
indefinitely."* It is already happening — the paper was published in November 2023, when
the yield was still near 1.8%.

## Measured 2012–2026

| | DGA | 60/40 SPY–IEF |
|---|---:|---:|
Two gates, dividend check removed:

| | DGA | 60/40 SPY–IEF |
|---|---:|---:|
| Ann. return | 13.95% | 9.57% |
| Ann. volatility | 16.27% | 9.97% |
| Sharpe | 0.88 | 0.97 |
| Sortino | 1.01 | 1.22 |
| Calmar | 0.49 | 0.46 |
| Max drawdown | −28.6% | −21.0% |
| Skew | −0.61 | −0.21 |

Holdings: QQQ 38.1% of months, SCHD 16.1%, defensive 45.8%. Risk-on 54.2% of months.

**Reproduction notes.** All series are total return, which matters here: SCHD yields 3.6%
a year against QQQ's 1.0%, so on price-only data the dividend sleeve would systematically
lose the momentum race. The dividend-yield denominator is correctly the price index, not a
total-return series. SCHD begins October 2011, which sets the start date. DBC stands in
for PDBC (inception November 2014). The dividend yield is SPY's trailing twelve-month
distributions over price rather than the index's own; Shiller's canonical series ends mid
-2023 and is no longer usable for a current test. Yield curve from FRED `T10Y3MM`.

## Links

- [[keller-keuning-2023-haa]] — the single-asset TIP canary DGA reuses
- [[keller-keuning-2018-daa]] — the canary-universe idea behind both
