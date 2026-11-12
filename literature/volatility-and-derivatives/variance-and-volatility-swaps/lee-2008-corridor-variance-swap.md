# Corridor Variance Swap

| | |
|---|---|
| **Authors** | Roger Lee (University of Chicago) |
| **Year** | 2008 (dated 29 December 2008) |
| **Type** | Reference article, 3pp; written as an encyclopedia-style entry that cites a companion "weighted variance swap article" |
| **PDF** | Not hosted in this repository (author's copy, no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Corridor+Variance+Swap%22+Lee) for the title and authors |
| **BibTeX** | `lee2008corridor` |
| **Status** | Reference: short enough to read whole; equations 3–5 carry the replication and pricing |

## What it is

A three-page definition-and-pricing entry for the corridor variance swap, a variance swap
that only counts the variance realised while the price is inside a chosen range.

- **The contract.** On an underlying Y, the payoff sums the squared daily log returns
  only on days when Y ends inside the corridor C, annualised (for example by 252/N) and
  multiplied by notional. Up-variance uses C = (H, ∞); down-variance uses C = (0, H).
- **Why buy it.** It costs less than a full variance swap. Reasons given: a directional
  view on Y; a view that the skew is too steep or too flat, making down-variance
  expensive or cheap relative to up-variance; or hedging a short volatility position that
  gets worse as Y rises (or falls).
- **Model-free replication.** In continuous time, for any positive continuous price
  process with deterministic rates and proportional dividends, the corridor swap is
  replicated by statically holding 2/K² dK out-of-the-money options at each strike K
  inside the corridor, plus a "zero-vol" delta hedge in the underlying. For a one-sided
  corridor at H the replicating payoff is λ(y) = (−2 log(y/H) + 2y/H − 2) on the
  corridor.
- **Further properties.**
  - A very narrow corridor approximates a contract on local time at that level.
  - A variance swap replicated with only a limited range of strikes is really a corridor
    variance swap, so missing strikes turn a variance hedge into a corridor one.
  - For C = (H, ∞) the replication is long calls on Y and short calls on log Y, which
    gives a semi-explicit Fourier pricing formula from the characteristic function of
    log Y.
  - With daily monitoring, a move that crosses H raises the question of how much of its
    variance to count; one contract convention counts a fraction chosen so that the
    discrete hedging error is only third order.

## Why it's in the library

**It is the shortest complete statement of corridor variance.** Contract definition,
motivation, replication, Fourier pricing and the discrete-monitoring problem fit on three
pages, with references to the Carr–Madan and Carr–Lewis papers for the details.

**Up- and down-variance turn the skew into something tradable.** Splitting variance at a
level H separates the variance realised in sell-offs from that realised in rallies. That
is the instrument for expressing a view on the skew, rather than on the overall level of
volatility.

**The truncated-strike point matters in practice.** Index variance-swap replication uses
listed strikes, which run out in the wings; this entry shows the result is a corridor
claim, so the replicating portfolio misses variance realised outside the traded strike
range. That is one reason variance swaps were hard to hedge in large sell-offs.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the case that selling variance in
  calm markets builds a hidden short-volatility position; down-variance is the leg that
  carries it
- [[merton-1976]] — jumps, where the continuous-time replication of variance no longer
  holds exactly
