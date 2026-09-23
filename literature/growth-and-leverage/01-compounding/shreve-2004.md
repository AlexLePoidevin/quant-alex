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

## Where it's weak

Not weak as a book — weak as a *fit*, in two specific ways worth knowing before you open it.

**It is measure-theoretic, and you need about two pages of it.** Chapter 4 earns its rigour
by building on filtrations, martingales and quadratic variation developed over three prior
chapters. If the only thing wanted is why `½f''(S)(dS)²` survives, that is a short Taylor
argument plus `(dW)² = dt`; Shreve is the place to *check* it, not necessarily the place to
learn it.

**Its frame is risk-neutral pricing, and variance drag is not a risk-neutral phenomenon.**
The book's purpose is derivative valuation under `Q`, where the drift is replaced by `r`
almost immediately and `μ` stops mattering. Variance drag lives entirely under `P`, in the
real-world drift, and the whole question here is what `μ` is and how badly it is estimated.
A reader arriving from Shreve can carry the habit of treating drift as a nuisance parameter
into a problem where drift is the only thing that decides whether the book compounds. Take
the Itô machinery; leave the measure.
