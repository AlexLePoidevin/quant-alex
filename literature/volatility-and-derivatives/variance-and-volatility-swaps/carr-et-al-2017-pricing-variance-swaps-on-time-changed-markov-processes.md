# Pricing Variance Swaps on Time-Changed Markov Processes

| | |
|---|---|
| **Authors** | Peter Carr, Roger Lee, Matthew Lorig |
| **Year** | 2017 (arXiv 1705.01069; this is v3, 15 November 2019) |
| **Type** | Paper, 19pp, mathematical finance (theorem and worked examples, no data) |
| **PDF** | `carr-et-al-2017-pricing-variance-swaps-on-time-changed-markov-processes.pdf` (arXiv copy) |
| **BibTeX** | `carr2017variance` |
| **Status** | Reference: §1 (where it sits), Theorem 3.5 with equation 3.11 (the result), §4.1 (the constant-ratio case) and §4.3.1 (why the ratio moves) |

## What it is

A variance swap pays realised variance minus a fixed strike set so the swap costs nothing
to enter. The paper asks when that fair strike can be read off today's option smile for
the same maturity, and with which portfolio of options.

- **The classical answer.** If the forward price moves continuously, with no jumps,
  Neuberger (1990) and Dupire (1993) show the variance swap is worth exactly two log
  contracts. A log contract pays −log(F_T/F_0). It can be replicated with a strip of
  out-of-the-money puts and calls weighted by 1/K², which is how the VIX is built. This
  holds whatever the volatility does.
- **With jumps, the log contract is wrong.** Carr, Lee and Wu (2012) showed that if the
  log price is a Lévy process run on any continuous stochastic clock (stochastic
  volatility as a time change), the swap is still worth a fixed multiple Q of log
  contracts. Q depends only on the jump law. Q = 2 with no jumps; with pure jumps, Q is
  the second moment of the jump measure divided by a convexity term. Q does not depend
  on the clock.
- **This paper: Markov instead of Lévy.** The driving process may now be any
  time-homogeneous Markov process run on a continuous clock that can be correlated with
  it in any way. Two things become possible:
  - local volatility and jump intensity can depend on the price level in different ways;
  - the relative frequency of different jump sizes can change with the level.
- **The main result (Theorem 3.5).** The variance swap strike equals the price of a
  European claim paying G(log F_T) − G(log F_0). G solves an ordinary
  integro-differential equation that depends only on the Markov dynamics, not on the
  clock. With G known, the Carr–Madan spanning formula prices the claim from the
  co-terminal calls and puts.
- **Examples with explicit G.**
  - Constant relative jump intensity: local variance and the jump kernel scale together.
    G is linear, which reproduces the constant-ratio result above.
  - "Fractional linear" relative jump intensity: G is new, and not a multiple of the log.
- **The ratio moves.** In a worked example with downward jumps, the paper approximates
  the ratio of the variance swap value to the log-contract value. The ratio now depends on
  the current price level and maturity. That matches Carr, Lee and Wu's (2012) S&P 500
  evidence that the ratio is not constant, which the Lévy setting could not explain.

## Why it's in the library

**It shows exactly when "variance = options strip" breaks.** The 1/K² strip is exact only
without jumps. With jumps, the right replicating payoff depends on the jump structure, so
a VIX-style index measures something slightly different from the variance a swap pays.
This paper gives the corrected payoff in a much wider class of models.

**It keeps stochastic volatility out of the problem.** The clock, which carries all the
stochastic volatility and can be correlated with the price, drops out entirely. Only the
level-dependence of volatility and jumps matters. That makes the result robust to the
part of the model that is hardest to pin down.

**It is pure theory.** There is no data and no calibration. Turning G into a trade means
estimating the local variance and jump kernel, which brings back the model risk the
clock-independence avoided. Continuous monitoring is assumed: real swaps are monitored
daily, and the discrete-sampling gap is not addressed.

## Links

- [[merton-1976]] — the jump-diffusion setting in which two log contracts no longer
  price the variance swap
- [[shreve-2004]] — semimartingales, Itô's formula and time changes, the tools the proof
  uses
- [[romero-2016-microstructure-noise-two-scales-realized-volatility]] — measuring the
  realised variance a swap actually pays, when high-frequency prices are noisy
