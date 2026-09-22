# Path-Dependence of Leveraged ETF Returns

| | |
|---|---|
| **Authors** | Marco Avellaneda; Stanley Zhang |
| **Year** | 2010 |
| **Type** | Paper — *SIAM Journal on Financial Mathematics* 1 |
| **BibTeX** | `avellaneda2010path` |
| **Status** | To read |

## Key takeaway

Closed form for a daily-reset leveraged fund tracking `L` times an underlying:

```
L_T/L_0 = (S_T/S_0)^L * exp(-0.5 * (L^2 - L) * sigma^2 * T)
```

The tracking term is a deterministic function of realised variance, so the fund's return is
**path-dependent on volatility** but not otherwise. At `L = 3` and `sigma = 20%` the term
costs about 12%/yr. Note it is positive for `L = -1` too — inverse funds decay as well —
and exactly zero at `L = 0` and `L = 1`.

## Why it's here

**The concrete laboratory: a product where the quadratic leverage term is separated out
and directly observable.** Also the cleanest way to show the effect is not about the
rebalancing trade — the formula contains realised variance, not turnover. Read against
`return-stacked-2025`, which makes the same correction for advisors without the derivation.
