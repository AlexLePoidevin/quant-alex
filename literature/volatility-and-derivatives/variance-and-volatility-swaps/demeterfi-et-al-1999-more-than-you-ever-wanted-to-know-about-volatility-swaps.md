# More Than You Ever Wanted To Know About Volatility Swaps

| | |
|---|---|
| **Authors** | Kresimir Demeterfi, Emanuel Derman, Michael Kamal, Joseph Zou (Goldman Sachs Quantitative Strategies) |
| **Year** | 1999 (March) |
| **Type** | Bank research note, Goldman Sachs Quantitative Strategies Research Notes, 56pp. A shorter version appeared as "A Guide to Volatility and Variance Swaps", *Journal of Derivatives* 6(4), 1999 |
| **PDF** | Not hosted in this repository (Goldman Sachs research, "All rights reserved") |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22More+Than+You+Ever+Wanted+To+Know+About+Volatility+Swaps%22+Demeterfi) for the title and authors |
| **BibTeX** | `demeterfi1999volswaps` |
| **Status** | Reference: §I–II (replication by a log contract), §IV (skew formulas), §V (strike range and jumps) and §VI (volatility vs variance) are the core |

## What it is

The standard practitioner derivation of how to price and hedge a variance swap, and why a
volatility swap is harder. It is the theory the 2003 VIX formula was built on.

- **The contracts.** A variance swap pays the notional times (realized variance − strike);
  a volatility swap pays (realized volatility − strike). Both give exposure to volatility
  alone. A stock option's volatility exposure is mixed up with its dependence on the
  stock price, which is why these swaps exist.
- **The key idea: a log contract captures variance.** An option's vega is concentrated
  near its strike. A portfolio of options weighted by 1/K² (one over strike squared) has
  a vega that does not depend on the stock price. That portfolio replicates a log payoff,
  and holding it, delta-hedged with the stock, earns exactly the realized variance. The
  fair variance strike is the cost of that option strip, which needs only continuous
  prices and no model for how volatility moves.
- **A worked example.** Section III builds the replicating strip from a discrete set of
  puts and calls on a 20%-volatility index with a skew, and shows the estimate converge to
  the fair variance as strike spacing narrows.
- **Skew raises the fair variance.** With implied volatility linear in strike (slope b),
  fair variance ≈ (ATM vol)² × (1 + 3Tb² + …): the correction grows with maturity and
  with the square of the skew. With volatility linear in delta, the first correction is
  of order b√T, so it is larger. These closed forms let traders requote swaps as the
  skew moves.
- **Practical failures.** A finite strike range underprices variance: with a flat 25%
  volatility, strikes from 75% to 125% of spot give a one-year fair variance of 23.0²
  instead of 25.0², and the hedge stops accruing variance once the index leaves the
  range. Jumps also break the replication. The quadratic part of a jump is captured, but
  a cubic mismatch remains, and its sign depends on the jump's direction. A short
  three-month variance swap hedged this way loses 101.5 variance points on a single 15%
  down jump.
- **Volatility swaps need a model.** Volatility is the square root of variance, so a
  volatility swap cannot be replicated statically. Its fair strike sits below the square
  root of the variance strike by a convexity bias that depends on the volatility of
  volatility. Pricing it properly needs a stochastic-volatility model.

## Why it's in the library

**It explains what the VIX actually is.** The VIX formula is the discretised version of
the 1/K²-weighted option strip derived here. The notes on the VIX (construction,
settlement, manipulation risk) all start from this replication.

**It shows where implied variance and the at-the-money volatility differ.** Fair variance
is the whole smile integrated with heavy weight on low strikes. In a skewed market it sits
well above at-the-money volatility squared, so the two should not be compared directly.

**The failure cases are the tail-risk cases.** The replication fails in exactly two ways:
the market leaves the strike range, or it jumps. Both describe a crash. A short variance
position is a short tail position, and the losses in the jump table are large.

**Volatility of volatility is a separate risk.** The convexity gap between variance and
volatility swaps is the price of uncertainty about volatility itself, the same quantity
that VIX options and VVIX trade.

## Links

- [[merton-1976]] — jump-diffusion, the price behaviour that breaks variance replication
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — the VIX formula in
  practice, and why it can stay low in an orderly decline
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — what
  long-volatility positions cost and pay in a portfolio
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the short-variance trade at market scale
