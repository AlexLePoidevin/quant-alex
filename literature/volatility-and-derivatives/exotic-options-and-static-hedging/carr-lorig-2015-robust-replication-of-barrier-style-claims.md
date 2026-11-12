# Robust Replication of Barrier-Style Claims on Price and Volatility

| | |
|---|---|
| **Authors** | Peter Carr (NYU Courant), Matthew Lorig (University of Washington) |
| **Year** | 2015 (this version dated 3 August 2015) |
| **Type** | Working paper, 36pp; arXiv [1508.00632](https://arxiv.org/abs/1508.00632) (later versions to 2022) |
| **PDF** | Not hosted in this repository (this copy is the SSRN download, SSRN 2639454); the arXiv version is free at the link above |
| **Find it** | [arXiv:1508.00632](https://arxiv.org/abs/1508.00632) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Robust+Replication+of+Barrier-Style+Claims+on+Price+and+Volatility%22+Carr) |
| **BibTeX** | `carr2015barrier` |
| **Status** | Reference: §1 (the literature on semi-robust barrier hedges), §3 (European claims on price and realised variance) and §6 (examples) give the ideas; §4–5 are the formulas |

## What it is

A unified method for pricing and hedging claims whose payoff depends on both the final
log price X and the realised variance ⟨X⟩ (quadratic variation), with or without
barrier conditions. The hedges use only the underlying, a bond, and vanilla calls and
puts with the same expiry.

- **Assumptions.** No arbitrage, no frictions, zero rates. The price is positive and
  continuous (no jumps in price). Volatility is a separate process that may jump and
  need not be Markov, but must be **independent of the price's Brownian motion**, so
  there is no correlation between returns and volatility.
- **The key trick (Proposition 3.1).** Under independence, the joint characteristic
  function of (X_T, ⟨X⟩_T) equals the characteristic function of X_T alone, evaluated
  at a transformed frequency. So any claim on log price *and* realised variance can be
  rewritten as a claim on the final price alone, which vanilla options span. The
  pricing formula is model-free in the sense that it needs only today's option prices,
  not a volatility model.
- **Hedges.** A European-style claim on (X_T, ⟨X⟩_T) is hedged by dynamic trading in
  options, extending Carr and Lee's (2008) replication of claims on realised variance.
  Single- and double-barrier knock-in, knock-out and rebate versions are then built
  from these. Depending on the claim, the hedge is static, semi-static (trade once when
  the barrier is hit) or dynamic.
- **Background it builds on.** The classic static hedge of a down-and-out call is a long
  call plus K/H puts struck at H²/K. It works if there are no jumps over the barrier
  and calls and puts have the same implied volatility at the barrier (put–call
  symmetry). The authors call this "semi-robust": it holds across many models, but not
  all.
- **Examples (§6).**
  - Options on the *realised Sharpe ratio* of an asset over a period.
  - Barrier-start variance and volatility swaps that begin accruing when a level is
    first hit.
  - Barrier claims on **leveraged ETFs**. A leveraged ETF's log return is β times the
    index log return minus ½β(1 − β) times realised variance. So an option on a
    leveraged ETF is a claim on (X, ⟨X⟩), and the standard barrier hedges do not apply
    to it.
- **What it doesn't do.** There are no numbers, no hedging simulations and no data. The
  independence assumption is strong for equities. The authors note that FX and bond
  markets, whose smiles are roughly symmetric, fit it better, and they leave
  correlated volatility to future work.

## Why it's in the library

**It shows how far "price from vanillas" can go.** The variance swap (replicated by a
strip of options) is the best-known case. This paper extends the same idea to payoffs
on realised variance and price together, including barriers. The common thread is that
the vanilla smile already contains the market's view of volatility. Many exotic payoffs
can be read off it without choosing a volatility model, as long as the assumptions
hold.

**The leveraged ETF example ties two parts of the library together.** The decay of a
leveraged ETF is a realised-variance term. An option on one is therefore partly an
option on volatility, and hedging it needs the tools here, not standard barrier
hedges.

**The independence assumption is the cost.** Equity index returns and volatility are
strongly negatively correlated (the leverage effect), so in equities the formulas are an
approximation. The paper is most directly useful for FX and rates, or as a benchmark
for how much correlation matters.

## Links

- [[avellaneda-zhang-2010]] — the leveraged-ETF return formula (log return minus a realised-variance term) that §6.3 uses
- [[sun-carr-2018-bond-yield-curve-convexity-trading]] — a simpler static no-arbitrage argument from the same school
- [[carr-lee-2007-realized-volatility-and-variance-options-via-swaps]] — the practical side of the same Carr–Lee programme: pricing and hedging options on realised variance with variance and volatility swaps
