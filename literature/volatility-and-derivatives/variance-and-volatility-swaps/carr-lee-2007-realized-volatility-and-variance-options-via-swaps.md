# Realized Volatility and Variance: Options via Swaps

| | |
|---|---|
| **Authors** | Peter Carr (Bloomberg; NYU Courant), Roger Lee (University of Chicago) |
| **Year** | 2007 (this version dated 26 October 2007) |
| **Type** | Journal article, *Risk* 20(5), May 2007, 76–83; 22pp author version with appendices ("OVSwithAppendices") |
| **PDF** | Local copy only (author version of a *Risk* article) |
| **BibTeX** | `carr2007options` |
| **Status** | Reference: §2 (synthetic variance and volatility swaps), §3 (the option formulas and the hedging test) and §4 (VIX options); Appendix B is a worked example on discrete strikes |

## What it is

A practical method for pricing and hedging options on realised variance and realised
volatility. The inputs are only the prices of variance swaps and volatility swaps, or
vanilla options from which those swaps can be built.

- **Variance from two swaps.**
  - A variance swap pays realised variance and a volatility swap pays realised
    volatility.
  - Because the square root is concave, the volatility-swap rate is below the square
    root of the variance-swap rate.
  - The gap measures the volatility of volatility exactly: variance-swap rate minus
    (volatility-swap rate)² = the risk-neutral variance of realised volatility. So the
    two swap prices give both the mean and the spread of future realised volatility.
- **Synthetic variance swap.** The standard replication: a static strip of
  out-of-the-money options weighted 1/K², plus a dynamic position in the underlying.
  It needs only positive, continuous prices.
- **Synthetic volatility swap.** Volatility swaps are usually thought to be
  model-dependent. Carr and Lee's earlier result replicates them from vanilla options
  with weights given by modified Bessel functions, mostly at-the-money straddles. The
  out-of-the-money calls and puts in the position cancel the first-order effect of
  correlation between price and volatility.
  - In a Heston test (T = 0.5, correlation −0.64), the synthetic volatility swap was
    off by 6 bp, against 30 bp for the usual shortcut of reading the volatility-swap
    rate off at-the-money implied volatility.
- **The option formulas.** The method assumes that remaining realised volatility is
  (displaced) lognormal at each date, and calibrates its mean and variance to the two
  swap prices. Closed-form, Black–Scholes-like formulas follow for variance and
  volatility calls, valid at any time during the averaging period. Hedge ratios in the
  two swaps follow from the same formulas.
- **Hedging test.**
  - Setup: Heston dynamics, correlation −0.64, a one-year at-the-money variance call,
    daily rebalancing and daily-sampled variance, 400 simulated paths.
  - Mean absolute hedging error, as a share of the option price, was 4.7% with real
    swaps, 6.7% with hybrid swaps and 8.1% with fully synthetic swaps.
  - Rolling the hedge into newly started volatility swaps each day lowered these to
    3.5%, 5.5% and 6.2%.
- **VIX options.** The same formulas price and hedge options on the VIX, using variance
  swaps (or their futures) and VIX futures as the two inputs. A displacement parameter
  produces the upward skew seen in VIX options. The authors leave its accuracy to
  future work.

## Why it's in the library

**It turns two swap prices into a volatility-of-volatility estimate.** The concavity
gap between variance and volatility swaps is the market's price for uncertainty about
volatility itself. That is the quantity options on variance and on the VIX depend on.
The same identity explains why the VIX (a variance-swap rate) sits above at-the-money
implied volatility (roughly a volatility-swap rate).

**It is the bridge from the VIX index to VIX options.** The VIX squared is a
variance-swap rate, and VIX futures are volatility-like. With those two, this method
prices and hedges VIX calls.

**The test is in one model.** The hedging errors come from Heston simulations only. The
authors flag that real equity dynamics, with jumps and a richer skew, need further
testing.

## Links

- [[carr-wu-2006-a-tale-of-two-indices]] — VIX² as a variance-swap rate, and the bounds on VIX futures that use the same Jensen gap
- [[carr-lorig-2015-robust-replication-of-barrier-style-claims]] — the same replication ideas extended to barrier claims on price and realised variance
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — what VIX calls and futures did in a portfolio, the products this paper prices
- [[carr-et-al-2005-pricing-options-on-realized-variance]] — options on realized variance under Lévy models
