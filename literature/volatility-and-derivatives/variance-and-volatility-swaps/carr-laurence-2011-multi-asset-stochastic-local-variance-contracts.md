# Multi-asset Stochastic Local Variance Contracts

| | |
|---|---|
| **Authors** | Peter Carr (NYU Courant Institute), Peter Laurence (Università di Roma 1) |
| **Year** | 2011 (*Mathematical Finance* 21(1)); the local copy is the 2 March 2009 working version |
| **Type** | Paper, 43pp |
| **PDF** | Local copy only (journal paper, no open licence) |
| **BibTeX** | `carr2011multiasset` |
| **Status** | Reference: §1 (motivation and summary of results), §2 (basket calls to joint density) and §4.2 (why the multi-asset case is harder) carry the ideas; the appendices are the proofs |

## What it is

A generalisation of two classic single-asset results to baskets of several assets.

- **The single-asset starting points.**
  - **Breeden–Litzenberger (1978):** the second derivative of a call price with respect to
    strike is the risk-neutral density of the terminal price. So any payoff on the final
    price can be built from a static position in options.
  - **Dupire (1996):** if the price moves continuously, the market's expected
    instantaneous variance at a given price and date (the "local variance") can be read
    from option prices: twice the ratio of a calendar spread to a butterfly spread. It
    holds without ever specifying how volatility itself moves. Variance swaps, forward
    variance swaps and corridor variance swaps (which pay variance only while the price is
    in a range) are special cases, and all can be hedged with options plus trading in the
    underlying.
- **Result 1: basket calls give the joint density.** For a basket call on n assets, the
  second strike derivative is the Radon transform of the joint risk-neutral density, as
  Lipton (2001) noticed for two assets. Inverting the Radon transform recovers the full
  joint density from basket-call prices of all weights and strikes. The same static
  position replicates any payoff on the final prices of the n assets. This part needs no
  continuity, so prices may jump.
- **Result 2: local variance on a portfolio.** A "multi-asset local variance contract"
  pays the realised variance of a fixed portfolio only while the asset prices are inside a
  chosen region, for example only while every stock is down more than some percentage.
  Assuming all assets run on one common, unspecified stochastic clock (so their
  volatilities rise and fall together but stay at different levels), the authors show how
  to price and hedge such contracts from basket option prices. The volatility process is
  never specified.
- **Why it is harder than one asset.** In one dimension the key step uses the fact that
  the Laplacian of |S − K|/2 is a point mass at K. In two or more dimensions the
  corresponding fundamental solution blows up at the point, so local time does not
  generalise. The fix is to smooth the payoff near the pole; the cost is that the payout
  region cannot shrink to a single point.
- **Dynamics covered.** Worked out for a time-changed Bachelier model (normal volatility)
  and a time-changed Black–Scholes model (lognormal), with a two-asset stochastic
  volatility illustration.

The contracts were hypothetical when the paper was written; the authors say they are not
yet traded. The method also assumes over-the-counter quotes on customised baskets for
many weights and strikes, which is a strong liquidity assumption.

## Why it's in the library

- It is the theory behind the idea that variance can be bought conditionally: only in a
  region of prices, and for a portfolio rather than a single asset. A "pay me the
  portfolio's variance if everything falls together" contract is a crash hedge expressed
  as a variance product.
- It shows exactly which part of option replication survives jumps (static positions in
  options) and which needs continuous prices (variance-type payoffs).
- The basket-to-joint-density result is a model-free route to the market-implied
  dependence between assets, the same object copula models try to specify.

## Links

- [[ang-chen-2002]] — correlations rise in down markets, the situation a "pay variance if
  all assets fall" contract is designed for
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — what goes wrong when the joint
  distribution of several assets is specified by a model instead of read from prices
- [[shreve-2004]] — Itô's formula, local time and changes of measure used throughout
