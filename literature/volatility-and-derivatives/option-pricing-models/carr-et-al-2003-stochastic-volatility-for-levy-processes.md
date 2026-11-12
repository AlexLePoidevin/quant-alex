# Stochastic Volatility for Lévy Processes

| | |
|---|---|
| **Authors** | Peter Carr, Hélyette Geman, Dilip B. Madan, Marc Yor |
| **Year** | 2003 (working paper dated 16 April 2001; published in *Mathematical Finance* 13(3), 2003) |
| **Type** | Paper, 35pp (working-paper version) |
| **PDF** | Not hosted in this repository (pre-publication draft, no open licence) |
| **Find it** | [doi.org/10.1111/1467-9965.00020](https://doi.org/10.1111/1467-9965.00020) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Stochastic+Volatility+for+L%C3%A9vy+Processes%22+Carr) |
| **BibTeX** | `carr2003svlevy` |
| **Status** | Reference: §1 (motivation), §3–4 (the time change and characteristic functions), §7 (estimation results) and §8 (comparison with jump-diffusions); §5 on martingale marginals is theory |

## What it is

A family of option-pricing models that combine pure-jump Lévy processes, which fit the
smile across strikes, with a random clock, which adds stochastic volatility and makes them
fit across maturities too.

- **The problem with plain Lévy models.** NIG, variance gamma and CGMY fit the smile at a
  single maturity well, with no diffusion needed. But because their increments are
  independent and identically distributed, they force a rigid term structure: constant
  variance rate, skewness falling like 1/√T and kurtosis like 1/T. Option markets show
  these moments flat or rising with maturity, and volatility clusters in time.
- **The fix: a CIR clock.** Run each Lévy process on a clock equal to the time integral of
  a Cox–Ingersoll–Ross (square-root) process. The randomness of the clock gives stochastic
  volatility, and its mean reversion gives clustering. The characteristic function stays
  in closed form, so options are priced by FFT (Carr and Madan, 1998).
- **Two ways to make a stock price.** "SA" models exponentiate the process and rescale it to
  match today's forward curve. They rule out arbitrage using only the stock price.
  "SAM" models take the stochastic exponential, which is a true martingale in the larger
  filtration that includes the Lévy process and the clock. That gives six models: NIGSA,
  VGSA, CGMYSA and their SAM versions.
- **Results, S&P 500, 2000.** All six were fitted to out-of-the-money S&P 500 options on
  the second Wednesday of each month of 2000, with maturities of one month to one year.
  - **SA beats SAM in every case.** The average pricing error was lower by 3.62, 2.87 and
    2.70 percentage points for NIG, VG and CGMY.
  - **Mean absolute percentage errors** were 4.13% (NIGSA), 4.43% (VGSA) and 3.37%
    (CGMYSA). CGMYSA was the best and had the most stable parameters.
  - **Errors are largest** for short maturities and for options further out of the money.
  - **Fitted dynamics.** Volatility mean reversion averaged 3.3 to 6.8 a year depending on
    the model. Long-run activity was about half the starting level, consistent with high
    volatility in 2000. The skew was strongly negative throughout.
- **Single stocks and other indexes.** About 20 other underliers were tested (e.g. MSFT,
  INTC, GE, RUT, BKX). Lower-dimensional models (NIGSA, VGSA) did well on single names,
  where fewer options are available to fit.
- **Comparison.** Bates and Duffie–Pan–Singleton jump-diffusions with stochastic
  volatility were estimated on the same data and were competitive. The appeal of the new
  models is that infinite-activity jumps replace the diffusion, so they need fewer
  parameters.

## Why it's in the library

**It is the standard reference for "Lévy plus stochastic clock".** The idea of separating
the shape of returns (the Lévy process) from their speed (the clock) is the template for a
large later literature, including the stochastic-skew currency models in
[[carr-wu-2007-stochastic-skew-in-currency-options]].

**It reports a result that runs against theory.** The models that are true martingales in
the richer filtration fit markedly worse than the ones that only respect the forward
curve. The authors read this as a sign that the market only enforces no-arbitrage on what
it can observe.

**The fits are static.** Each month is calibrated separately, so the paper shows the models
can match a surface on a given day. It does not test hedging, out-of-sample pricing, or
whether the fitted parameters behave consistently over time.

## Links

- [[carr-et-al-2007-time-for-a-change-variance-gamma-model]] — an intuitive introduction to
  variance gamma, one of the three Lévy processes here
- [[carr-et-al-2004-from-local-volatility-to-local-levy-models]] — the deterministic
  alternative: the Lévy process runs at a speed set by price and time, not by a random clock
- [[carr-et-al-2005-pricing-options-on-realized-variance]] — the same model family used to
  price options on realized variance
- [[carr-wu-2007-stochastic-skew-in-currency-options]] — two Lévy processes on two clocks,
  giving a skew that varies and changes sign
- [[merton-1976]] — the finite-activity jump-diffusion that the Bates and DPS benchmarks
  extend
