# Static Hedging of Standard Options

| | |
|---|---|
| **Authors** | Peter Carr (Bloomberg L.P. and NYU Courant), Liuren Wu (Baruch College, CUNY) |
| **Year** | 2014 (first draft July 2002; local copy dated 21 May 2004) |
| **Type** | Paper, *Journal of Financial Econometrics* 12(1), 3–46. The local copy is the 61-page 2004 working paper |
| **PDF** | Local copy only (working paper of a journal article, no open licence) |
| **BibTeX** | `carr2014statichedge` |
| **Status** | Reference: §1 Theorem 1 (the spanning relation), §2 the simulations (Black–Scholes vs Merton), §3 the S&P 500 test |

## What it is

A way to hedge a long-dated option with a fixed portfolio of shorter-dated options. The
portfolio needs no rebalancing until those shorter options expire, and it works even when
the underlying can jump by a random amount.

- **The spanning result.** Assume a one-factor Markov model in which the price can diffuse
  and also jump to any non-negative level. Then a European option maturing at T equals a
  static portfolio of a continuum of options maturing at an earlier date u.
  - The weight on the strike-K option is proportional to the gamma the target option will
    have at u if the price is then at K.
  - That future gamma does not depend on today's price or the date, so the weights never
    change.
  - Only the dynamics between u and T need to be modelled correctly. Delta hedging needs
    the model to be right over the whole life of the option.
- **Where it sits.** Breeden–Litzenberger static replication is model-free but can only
  span payoffs at the same maturity. Delta hedging spans almost anything but fails with
  jumps. This hedge sits in between: mild model structure in exchange for robustness to
  jumps.
- **Making it practical.** The continuum is replaced by a few strikes chosen by
  Gauss–Hermite quadrature. A 21-node rule prices the Black–Scholes target ($12.35) to
  about a cent.
- **Simulations.**
  - Under Black–Scholes, daily delta hedging and a 21-option static hedge are comparable,
    with a slight edge to delta hedging. Since the underlying is more liquid than options,
    delta hedging wins in that world.
  - Under Merton jump-diffusion, delta hedging's error standard deviation rises about
    tenfold and its mean absolute error about fourfold. A static hedge with only three
    options beats it.
  - The kurtosis of delta-hedge errors goes from 4.68 to 59.79, while static-hedge errors
    stay below 6. The worst delta-hedged loss is $12.12, more than the option's price.
  - Rebalancing more often does not rescue delta hedging under jumps. More strikes, or a
    hedge maturity closer to the target, improve the static hedge.
  - The results survive ad hoc implementations in which the hedger does not know the true
    process.
- **S&P 500 test.** CBOE SPX options from OptionMetrics, January 1996–July 2002: 79
  non-overlapping month-long hedges for four maturity groups (one month to 12–17 months).
  - In every case a static hedge of at most five options beats daily delta hedging with
    futures. The authors read this as evidence of random-size jumps in the index.
  - The static hedge deteriorates moderately as the gap between hedge and target maturity
    widens, which points to further risk factors such as stochastic volatility.
- **Extension.** The method extends to path-dependent claims, illustrated with a globally
  floored, locally capped compounding cliquet hedged semi-statically with European options.

## Why it's in the library

- **Delta hedging fails in crashes.** Rebalancing in the underlying cannot hedge a jump of
  random size, and the failure shows up as fat-tailed hedge errors exactly when markets gap
  or liquidity disappears. A static option hedge holds through the gap because nothing has
  to be traded.
- **Hedge with what is liquid.** Long-dated and exotic options are often hedged with
  short-dated listed options. This paper gives the weights and shows that three to five
  strikes are enough.
- **A practical check on model risk.** Because only the dynamics between the two
  maturities matter, the hedge relies on a much shorter stretch of the model than a
  dynamic hedge does.

## Links

- [[merton-1976]] — the jump-diffusion world in which delta hedging breaks down and the
  static hedge does not
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — buying
  crash protection directly, the portfolio-level counterpart of hedging an option book
  against jumps
