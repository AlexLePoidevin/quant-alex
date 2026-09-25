# A Century of Generalized Momentum: From Flexible Asset Allocation (FAA) to Elastic Asset Allocation (EAA)

| | |
|---|---|
| **Authors** | Wouter J. Keller; Adam Butler (ReSolve) |
| **Year** | 2014 (30 December) |
| **Type** | Working paper — SSRN 2543979 |
| **Link** | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2543979 |
| **Also** | [TrendXplorer primer](https://indexswingtrader.blogspot.com/2015/01/a-primer-on-elastic-asset-allocation.html) · [ReSolve](https://investresolve.com/published-century-generalized-momentum/) |
| **BibTeX** | `keller2014eaa` |
| **Status** | Rules verified, backtested |

## Generalized momentum

The paper's contribution is to treat momentum as a *family* rather than a rule. Return,
volatility and correlation each enter one score through their own elasticity, and a fourth
exponent controls concentration:

```
z_i = ( r_i^wR · (1 − c_i)^wC / v_i^wV )^wS
```

with `r` the average of the 1-, 3-, 6- and 12-month return, `v` the 12-month volatility and
`c` the 12-month correlation to the equal-weighted universe. Named parameterisations:

| Variant | wR | wC | wV | wS | Reduces to |
|---|---|---|---|---|---|
| **Golden Defensive** | 1 | 1 | 0 | 0.5 | `√(r(1−c))` |
| Golden Offensive | 1 | 0.5 | 0 | 2 | `r²(1−c)` |
| Equal Weighted Hedged | 1 | 1 | 0 | ≈0 | rank only, near-equal weights |
| Equal Weighted Return | 1 | 0 | 0 | ≈0 | equal weight on positive returns |

Allocation: `CPF = #{r_i ≤ 0}/N` to the cash proxy, `TopN = min(1 + ⌈√N⌉, ⌊N/2⌋)` assets
selected, weights proportional to `z` and scaled to `1 − CPF`.

## Which term is load-bearing

Measured 2009–2026 on a twelve-asset universe (TopN = 5), removing one piece at a time:

| | Ann. return | Volatility | Sharpe | Max DD | Calmar |
|---|---:|---:|---:|---:|---:|
| **Golden Defensive, as specified** | 8.25% | 8.94% | **0.932** | **−11.4%** | **0.72** |
| without the CPF cash fraction | 9.54% | 12.71% | 0.781 | −24.0% | 0.40 |
| without the TopN cut | 7.87% | 8.44% | 0.940 | −12.2% | 0.64 |
| wS = 2 (Golden Offensive) | 8.35% | 10.96% | 0.786 | −21.8% | 0.38 |

**The cash fraction is the strategy.** Drop it and the drawdown doubles. The TopN cut is
worth almost nothing on Sharpe. The concentration exponent matters about as much as the
crash protection.

⚠️ A reconstruction that keeps `z = r(1−c)` — i.e. wS = 1, no named variant — and omits
both TopN and the CPF returns 9.39% at 12.15% volatility, Sharpe 0.800, drawdown −21.4%.
Higher return, and none of the defensive character the paper is about.

## Relation to the rest of the folder

The CPF is the same breadth arithmetic as [[keller-keuning-2016-paa]]'s bond fraction,
with `n₁ = 0`: cash rises linearly with the count of assets that have stopped working. The
correlation discount `(1 − c)` reappears as the whole signal in [[gpm]]. EAA is the more
general object both of those specialise.

## Links

- [[keller-keuning-2016-paa]] — the breadth-driven cash fraction
- [[gpm]] — `r(1−c)` with breadth-scaled cash and a fixed top-three
- [[varadi-et-al-2012]] — the other correlation-aware sizing rule here
