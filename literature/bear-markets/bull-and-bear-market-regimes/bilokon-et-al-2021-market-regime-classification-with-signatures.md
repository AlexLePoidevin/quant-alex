# Market Regime Classification with Signatures

| | |
|---|---|
| **Authors** | Paul Bilokon (Thalesians; Imperial College London), Antoine Jacquier (Imperial; Alan Turing Institute), Conor McIndoe (Imperial) |
| **Year** | 2021 (dated 30 June 2021) |
| **Type** | Working paper, arXiv 2107.00066 (q-fin.RM), also SSRN 3877650, 14pp. Code at github.com/mcindoe/regimedetection |
| **PDF** | `bilokon-et-al-2021-market-regime-classification-with-signatures.pdf` (arXiv version) |
| **BibTeX** | `bilokon2021signatures` |
| **Status** | Reference: §2 (the clustering algorithm), §3 (signatures) and §4 (the distance between sets of paths and the synthetic test) carry the method |

## What it is

A method for finding market regimes without deciding in advance how many there are or what
they look like. Hidden Markov and Markov-switching models fix the number of states first;
this approach lets the data suggest it.

- **Paths to vectors: the signature.** Each price path (with time added as a second
  coordinate) is summarised by its *signature*, the sequence of its iterated integrals.
  The first level is the net move; higher levels capture the order in which things happened
  (for example, the signed areas between coordinates). The signature is truncated at level
  3, and level-k terms are multiplied by k! so the levels are on a comparable scale.
- **A regime is a cloud of paths.** One "point" to be clustered is a set of paths observed
  under the same conditions (here 40 paths). The distance between two points is the maximum
  mean discrepancy, a kernel two-sample statistic that is zero only when the two sets come
  from the same distribution.
- **Clustering without choosing k.** The Azran–Ghahramani algorithm turns distances into a
  random walk between points. Points in the same cluster keep their random walks inside it,
  so the number of clusters shows up as a large gap between eigenvalues of the transition
  matrix. Each local peak in that gap suggests a clustering, scored by its size (at most 1).
- **The test.** Synthetic Black–Scholes paths in four regimes: drift 5% or 2% crossed with
  volatility 10% or 20%, ten points per regime, 100 steps each. The best-scored partition
  recovers the four regimes exactly (separation 1.000). The 3-cluster (0.994) and 2-cluster
  (0.812) suggestions merge regimes rather than mixing them.

## Why it's in the library

It is a different way to answer "what regime are we in?" from the Markov-switching models
elsewhere in this section. Rather than fitting a model with a fixed number of bull and bear
states, it compares the shape of recent price paths and lets the clusters emerge. Path
signatures are also a general way to turn a time series into features.

The evidence is thin. The only test is on simulated Brownian paths whose regimes differ by
construction, there is no real market data, and the paper does not show how to label a
live window or how stable the clusters would be in practice. Treat it as a method sketch.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — the parametric
  alternative: a four-state Markov-switching model of bull and bear markets
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a two-state
  bull/bear model used to derive a trading rule
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — volatility regimes found with a
  two-state Markov-switching model
- [[kim-et-al-2021-investigation-of-flash-crash-via-topological-data-analysis]] — another
  shape-based, model-free summary of price paths used to flag unusual market states
