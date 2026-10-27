# Generalized Protective Momentum (GPM)

| | |
|---|---|
| **Authors** | Jan Willem Keuning; Wouter J. Keller |
| **Published** | Documented by [Allocate Smartly](https://allocatesmartly.com/keuning-kellers-generalized-protective-momentum/); metric derived at [TrendXplorer](https://indexswingtrader.blogspot.com/2016/06/deciphering-correlation-hedged-momentum.html) |
| **Type** | Practitioner strategy, rules public |
| **BibTeX** | `allocatesmartly_gpm`, `trendxplorer2016corrhedged` |
| **Status** | Reconstructed and backtested |

## The rules

**Universe:** 12 risk assets — SPY, QQQ, IWM, EEM, VGK, EWJ, IYR, GSG, GLD, TLT, HYG,
LQD — plus 2 crash-protection assets (IEF, BIL).

**Signal:** `z_i = r_i · (1 − c_i)`, where `r` is the average of the 1-, 3-, 6- and
12-month returns and `c` is the 12-month correlation of the asset to the equal-weighted
return of the 12 risk assets. The multiplier discounts momentum for co-movement: an asset
correlated 0.9 with the universe keeps a tenth of its score, a negatively correlated one
has its score amplified, up to 2× at `c = −1`.

**Allocation:** `n = #{z_i > 0}`. If `n ≤ 6`, hold 100% of the crash-protection asset.
Otherwise hold `(12 − n)/6` in it and split the remainder equally across the top three
by `z`.

The allocation rule is [[keller-keuning-2016-paa]]'s bond fraction at `N = 12`, `a = 2`.
GPM's contribution is the correlation hedge on the momentum score.

## ⚠️ A reconstruction trap worth recording

`BF = (12 − n)/6` is bounded in [0, 1] **only because `n` is counted over the same 12
assets the constants were derived from**. An implementation that keeps the constants while
counting `n` over a larger list breaks the bound.

Counting `n` over 14 names — which happens if IEF and BIL, the crash-protection assets, are
left in the risk list — makes the numerator negative whenever `n > 12`. The result is a
short safe-asset leg: **133% long, 33% short, 167% gross**, on roughly a quarter of
rebalances. PAA never levers and never shorts, so this is a defect, not a variant.

Measured on 2009–2026, the effect is leverage rather than edge:

| | Ann. return | Volatility | Sharpe | Max DD | Max gross |
|---|---:|---:|---:|---:|---:|
| 14 names, constants N=12, n₁=6 | 6.78% | 9.49% | 0.739 | −17.7% | **1.67×** |
| 12 names, N=12, n₁=6 (the spec) | 4.98% | 7.09% | 0.721 | −13.0% | 1.00× |
| 14 names, N=14, n₁=7 (generalised) | 5.42% | 7.14% | 0.775 | −13.4% | 1.00× |

Sharpe is indistinguishable across all three; only the scale changes. Either
self-consistent reading caps gross at 1.00×.

## Links

- [[keller-keuning-2016-paa]] — the breadth rule and the BF formula
- [[keller-keuning-2017-vaa]], [[keller-keuning-2018-daa]] — the later breadth strategies
- [[varadi-et-al-2012]] — the other correlation-aware construction in this folder, applied
  to weights rather than to the momentum score
- [[optimum3]] — correlation used to select assets rather than to discount their momentum
