# Dual and Canary Momentum with Rising Yields/Inflation: Hybrid Asset Allocation (HAA)

| | |
|---|---|
| **Authors** | Wouter J. Keller; Jan Willem Keuning |
| **Year** | 2023 (3 February) |
| **Type** | Working paper — SSRN 4346906 |
| **Link** | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4346906 |
| **Also** | [Allocate Smartly](https://allocatesmartly.com/hybrid-asset-allocation/) · [TrendXplorer](https://indexswingtrader.blogspot.com/2023/02/introducing-hybrid-asset-allocation-haa.html) |
| **BibTeX** | `keller2023haa` |
| **Status** | Rules verified, backtested |

## The rules

Momentum throughout is **13612U**: the unweighted average of the 1-, 3-, 6- and 12-month
total return.

| | |
|---|---|
| **Canary** | TIP. Never held. If its momentum is non-positive the whole book goes defensive. |
| **Offence** | SPY, IWM, VEA, VWO, VNQ, PDBC, IEF, TLT — top four by momentum, 25% each |
| **Defence** | IEF or BIL, whichever carries the higher momentum |

Two screens run in sequence rather than as one ranking. Relative momentum takes the top
four of the eight; absolute momentum then requires each of those four to be positive, and
any that is not forfeits its 25% to the defensive asset. The book can therefore be three
quarters or half invested without the canary firing at all.

BF-style fractional cash does not appear here — the allocation is always in quarters, and
gross exposure is 1.00× at every rebalance.

## What the canary is for

TIP prices real yields. Inflation-protected Treasuries fall when real yields rise, so a
negative reading marks the regime in which yields and inflation move against every asset
class at once — precisely when spreading across eight of them stops helping. This is the
"rising yields/inflation" of the title, and it is why the signal sits outside the traded
universe rather than inside it.

The canary was negative at 26.8% of rebalances over 2009–2026.

## Relation to the rest of the family

The canary idea comes from [[keller-keuning-2018-daa]], which first separated the
signalling universe from the traded one. HAA simplifies it to a **single** canary asset and
drops the breadth arithmetic of [[keller-keuning-2016-paa]] entirely: where PAA and
[[gpm]] scale cash continuously with the count of positive-momentum assets, HAA is binary
at the portfolio level and quartered at the asset level.

## Measured 2009–2026

Against a 60/40 SPY/IEF benchmark: annualised return 10.92% against 10.22%, volatility
11.21% against 10.28%, Sharpe 0.98 against 1.00. Return and Sharpe are a wash. The
difference is drawdown — **−15.0% against −21.0%** — which carries Calmar from 0.49 to
0.73.

## Links

- [[keller-keuning-2018-daa]] — the canary universe this simplifies
- [[keller-keuning-2016-paa]] — the breadth arithmetic HAA replaces with a binary switch
- [[gpm]] — the other Keller-Keuning strategy in this folder, breadth-scaled rather than
  canary-gated
