# Option Pricing When Underlying Stock Returns Are Discontinuous

| | |
|---|---|
| **Authors** | Robert C. Merton |
| **Year** | 1976 |
| **Type** | Paper — *Journal of Financial Economics* 3(1–2) |
| **BibTeX** | `merton1976option` |
| **Status** | To read |

## Key takeaway

Adds a compound Poisson jump component to GBM:

```
dS/S = mu dt + sigma dW + (J - 1) dq
```

where `dq` counts jumps at intensity `lambda` and `J` is the multiplicative jump size. The
continuous part models the ordinary two-sided flow of quotes; the jump part models the
events that do not pass through intermediate prices — gaps, announcements, defaults.

## Why it's here

**Where the continuous-path mathematics stops, and the reason leverage fails
discontinuously rather than gradually.** Under jumps the growth rate acquires a term
`lambda * E[ln(1 + f(J-1)) - f(J-1)]`, whose logarithm diverges to `−∞` as `f(1-J) → 1`.
So there is a hard bound `f < 1/J_max` that exists independently of any expected-growth
calculation: at `f = 4`, a 25% overnight gap is not drag, it is termination. That is a
different kind of constraint from everything else in this folder and deserves to be drawn
as one.
