# Stochastic Calculus for Finance II: Continuous-Time Models

| | |
|---|---|
| **Authors** | Steven E. Shreve |
| **Year** | 2004 |
| **Type** | Book — Springer. Ch. 4 (Itô's Formula) is the relevant chapter |
| **BibTeX** | `shreve2004stochastic` |
| **Status** | To read |

## Key takeaway

The rigorous derivation the whole folder rests on. Itô's formula for `f(S_t)` keeps a
second-order term that ordinary calculus discards, because `(dW)² = dt` rather than
vanishing at order `dt`. Apply it to `f(S) = ln S` under GBM and the `½f''(S)(dS)²` term
contributes exactly `−σ²/2`:

```
d(ln S_t) = (mu - sigma^2/2) dt + sigma dW_t
```

Chapter 4 also gives the lognormal solution `S_T = S_0 exp((mu - sigma^2/2)T + sigma W_T)`,
from which both `E[S_T] = S_0 e^{mu T}` and `median[S_T] = S_0 e^{(mu - sigma^2/2)T}` fall out.

## Why it's here

**The `−σ²/2` has to be derived, not asserted, and this is where.** Most write-ups state
it and move on, which is how it acquires the folklore reading of a "tax". Having the Taylor
argument in hand is what lets you say precisely what it is: the gap between two different
summaries of the same distribution, both of which are in the same two lines of algebra.
