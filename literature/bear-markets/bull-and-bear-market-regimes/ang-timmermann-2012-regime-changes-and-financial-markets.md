# Regime Changes and Financial Markets

| | |
|---|---|
| **Authors** | Andrew Ang (Columbia) and Allan Timmermann (UC San Diego) |
| **Year** | 2012 |
| **Type** | Survey. *Annual Review of Financial Economics* 4, 313–337 (doi 10.1146/annurev-financial-110311-101808); the copy is NBER Working Paper 17182 (June 2011), 34pp |
| **PDF** | Local copy only (NBER working paper, "All rights reserved"; the journal version is Annual Reviews copyright) |
| **BibTeX** | `ang2012regime` |
| **Status** | Reference: §2 (what a regime-switching model is and what it implies for moments and equilibrium prices), §3.1 and Table 1 (a typical estimation on equities, T-bills and FX), §3.5 (asset allocation) |

## What it is

A short survey of Markov regime-switching models in finance by two of the main contributors to
the literature. It covers four things:

- **The model.** Returns are drawn from a different normal distribution in each regime, and an
  unobserved Markov chain moves between regimes. A mixture of normals this way produces fat
  tails, skewness, volatility clustering and correlations that change over time, from a model
  with only a few parameters.
- **Equilibrium.** Regimes in consumption or dividend growth carry through to asset prices, and
  can make the risk-return trade-off negative in some regimes. Investors learning which regime
  they are in add further non-linearity.
- **A worked estimation.** Two-regime models on monthly data: S&P 500 excess returns and
  three-month T-bill yields (1953–2010), and USD/DEM-EUR carry returns (1975–2010). Results:
  - **Regimes are identified by volatility, not by mean.** Equal means across regimes cannot be
    rejected for any of the three series, but equal volatilities are rejected in all of them.
    For equities, the high-volatility regime (4.9% a month against 2.4%) has the lower mean
    return. That is the bear market regime, though the paper stresses these are not real-time
    expected returns.
  - **Regimes don't line up with the narrative.** The equity high-volatility regime covers
    1997–2003, which includes the late-1990s bull market as well as the crash after it.
  - **Rates are near-random-walk in calm times.** The T-bill yield behaves like a random walk in
    the low-volatility regime, which the authors attribute to Fed smoothing.
  - **Carry goes up by the stairs and down by the elevator.** The high-volatility FX regime
    marks sudden dollar depreciations.
- **Asset allocation.** Regimes still leave large gains from international diversification
  (Ang and Bekaert). Ignoring them costs an investor 2–3 cents per dollar of initial wealth.
  Persistent regimes also create horizon effects and home bias.

## Why it's in the library

It is the standard short reference for what a "regime" means statistically. That matters for
reading the other bull/bear papers in this folder, which use the word in different senses.

The most useful single finding for practice is that two-state models on returns mostly separate
**calm from turbulent** periods, not **up from down** markets. Calling the states "bull" and
"bear" therefore needs care.

The survey is also candid that what causes regimes is unresolved: policy shifts, one-off events
or investor expectations.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — a four-state extension that
  separates bear rallies and bull corrections from the main regimes
- [[ang-chen-2002]] — asymmetric correlations in down markets, one of the time-varying
  correlation patterns regimes reproduce
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — a regime-switching model fitted
  directly to volatility
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — what a two-state
  model implies for the optimal trend-following rule
- [[ang-bekaert-2002-regime-switches-in-interest-rates]] — the interest-rate regime model this
  survey summarises
- [[haase-neuenkirch-2023-predictability-of-bull-and-bear-markets]] — forecasting the regimes in
  real time with time-varying transition probabilities
