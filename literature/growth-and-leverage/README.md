# Growth and leverage

**What an edge is worth, and how much of it you can actually harvest.**

The other folders are about the **cross-section** — what a return decomposes into, how many
independent forces there are, how much of your position count is real diversification. This
one is about **time**: how a return compounds, why the compounded figure sits below the
average one, and how much leverage converts an information ratio into growth before the
arithmetic turns on you.

The hinge is a single asymmetry. Under leverage `f`, drift scales linearly and variance
scales quadratically:

```
g(f) = r + f(mu - r) - 0.5 * f^2 * sigma^2
```

which peaks at `f* = (mu - r)/sigma^2 = SR/sigma`, where growth equals `r + SR^2/2`. That
is the exchange rate between a Sharpe (or information) ratio and compound growth — and via
`IR = IC * sqrt(BR)`, it means **growth is linear in breadth**, not square-root.

| Section | Question |
|---|---|
| `01-compounding` | Why the compounded return sits below the average one, and what that does *not* mean |
| `02-growth-optimal` | Kelly, Breiman, Merton's CRRA generalisation — and Samuelson's objection |
| `03-estimation-error` | Why `f*` is unusable as stated: it is linear in the hardest parameter to estimate |
| `04-tails-and-jumps` | Where continuous-path math stops: fat tails, CVaR, jump diffusion, the ruin bound |
| `05-applied-leverage` | Leveraged ETFs, the diversification return, practitioner writing |

> ⚠️ **Standing caveat.** Notes marked *To read* were written from general knowledge of what
> each source is known for, not from the source itself. Volumes, issues and page numbers are
> from recall. **Verify before citing in print.** Notes marked *Read* were written from the
> source.

## The correction this folder exists to make

Variance drag is routinely described as a "tax" that "erodes" capital. For an unlevered
holding that is **false**, and the error is load-bearing. Under GBM,
`E[S_T] = S_0 * exp(mu*T)` exactly — nothing leaks. The `-sigma^2/2` term is the gap between
the **mean and the median** of a lognormal: the rate at which the typical path falls behind
the average one, because the average is carried by a thinning set of lucky paths.

The cost becomes real under **leverage**, where the quadratic term bites. The sharpest
statement in the folder: for `f > 2f*`, the expected value of the portfolio compounds
exponentially while the portfolio itself goes to zero almost surely. That is not a paradox;
it is what a right-skewed distribution does.

Cross-topic: `../market-structure/03-effective-number-of-bets/` sets the `BR` that this
folder converts into growth. Booth & Fama (`05-applied-leverage`) is the bridge — the
diversification return is variance drag run backwards, and the structural entanglement
measured over there is therefore a direct tax on compound growth over here.
