# Kipnis Defensive Adaptive Asset Allocation (KDA)

| | |
|---|---|
| **Author** | Ilya Kipnis (QuantStrat TradeR) |
| **Published** | January 2019, [mirrored at R-bloggers](https://www.r-bloggers.com/2019/01/right-now-its-kdaasset-allocation/); [robustness follow-up](https://www.r-bloggers.com/2019/02/kda-robustness-results/) |
| **Also** | [Allocate Smartly](https://allocatesmartly.com/ilya-kipnis-defensive-adaptive-asset-allocation/) |
| **BibTeX** | `kipnis2019kda`, `allocatesmartly_kda` |
| **Status** | Rules verified, backtested |

⚠️ The original `quantstrattrader.com` domain no longer resolves to the author's blog —
it now 301-redirects to an unrelated commercial site. Use the R-bloggers mirrors above.

## The rules

A hybrid of Keller & Keuning's canary idea ([[keller-keuning-2018-daa]]) and ReSolve's
Adaptive Asset Allocation.

**Momentum** is a weighted *sum*, not an average:

```
12·r(1m) + 4·r(3m) + 2·r(6m) + 1·r(12m)
```

Each term covers twelve months of exposure (12×1, 4×3, 2×6, 1×12), which loads the score
on the most recent month. The weights total 19, so the score scales with 19 and is not
itself a return.

| | |
|---|---|
| **Investment universe** | SPY, VGK, EWJ, EEM, VNQ, RWX, IEF, TLT, DBC, GLD |
| **Canary** | EEM and AGG |
| **Crash protection** | IEF or BIL, whichever has higher momentum |
| **Selection** | top five of ten by momentum, discarding any that are negative |
| **Weighting** | **long-only minimum variance** on a blended covariance matrix |
| **Risk fraction** | `pctAggressive = mean(canary momentum > 0)` → 1, 0.5 or 0 |

The covariance matrix is the part that gets dropped in reconstructions:

```
cors = [12·corr(21d) + 4·corr(63d) + 2·corr(126d) + corr(252d)] / 19
vols = 21-day standard deviation
cov  = volsᵀ vols ∘ cors
w    = argmin wᵀ cov w    s.t.  Σw = 1,  w ≥ 0
```

## ⚠️ The weighting step is the strategy

It is tempting to equal-weight the five selected assets, since the selection is unchanged
either way. That is not a simplification — it removes the *adaptive* half of Adaptive Asset
Allocation. Measured 2009–2026:

| | Ann. return | Volatility | Sharpe | Sortino | Max DD | Calmar |
|---|---:|---:|---:|---:|---:|---:|
| **Minimum variance (the spec)** | **8.05%** | **8.97%** | **0.908** | 1.079 | −13.4% | 0.60 |
| Equal weight across the same five | 7.07% | 10.30% | 0.715 | 0.845 | −12.6% | 0.56 |

Same assets, same canary, same momentum. 0.19 of Sharpe sits entirely in the sizing.

## What minimum variance does here

It concentrates. With no return input the solution piles into whichever asset has the
lowest estimated variance and the least correlation to the rest, and five assets is not
enough breadth to restrain it: the largest single holding is a median **66%** of the risk
book against 20% under equal weighting, and regularly reaches 100%.

This is a benign corner of the estimation problem that wrecks mean-variance at scale —
n = 5 against T = 252 gives q ≈ 0.02, so the covariance matrix is well conditioned and the
inverse is stable. The pathologies in [[varadi-et-al-2012]]'s motivation, and in the
broader minimum-variance literature, bite as q grows.

## Measured 2009–2026

Against 60/40 SPY/IEF: return 8.05% against 10.22%, volatility 8.97% against 10.28%,
Sharpe 0.91 against 1.00. Drawdown −13.4% against −21.0%, giving Calmar 0.60 against 0.49.

Canary states: fully invested 52.1% of rebalances, half invested 32.4%, fully defensive
15.5%. Gross exposure is 1.00× throughout.

## Links

- [[keller-keuning-2018-daa]] — the canary universe KDA borrows
- [[keller-keuning-2023-haa]] — the other canary-gated strategy here, binary rather than
  three-state
- [[varadi-et-al-2012]] — the alternative to optimisation: rank-weighted correlation
  heuristics chosen for estimator stability
