# Arbitrage, Factor Structure, and Mean-Variance Analysis on Large Asset Markets

| | |
|---|---|
| **Authors** | Gary Chamberlain; Michael Rothschild |
| **Year** | 1983 |
| **Type** | Paper — *Econometrica* 51(5), 1281–1304 |
| **BibTeX** | `chamberlain1983arbitrage` |
| **Status** | To read |

## Known for

**Approximate factor structure.** Ross's APT assumed residuals were mutually uncorrelated —
an *exact* factor structure, which no real market satisfies. Chamberlain and Rothschild
weaken this to allow residuals to be **mildly correlated**, requiring only that the
eigenvalues of the residual covariance matrix stay bounded as the number of assets grows.

The definition that follows is the key one: **factors are the directions whose eigenvalues
diverge with N**, while everything else stays bounded.

## Why it's here

⭐ **The pivot of the entire series.** It defines a factor *by the behaviour of the
covariance matrix's eigenvalues*, which means the formal model (post 2) and the eigenvalue
methods (post 3) are **the same object described two ways**. Post 2 can end pointing at
post 3 without hand-waving, because this paper is the bridge.

It is also the honest answer to the objection that real residuals are correlated: the theory
already accommodates that, and says precisely how much correlation is tolerable.
