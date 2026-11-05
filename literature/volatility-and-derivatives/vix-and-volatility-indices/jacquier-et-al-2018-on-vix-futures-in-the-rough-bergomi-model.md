# On VIX Futures in the Rough Bergomi Model

| | |
|---|---|
| **Authors** | Antoine Jacquier (Imperial), Claude Martini (Zeliade), Aitor Muguruza (Imperial) |
| **Year** | 2018 (*Quantitative Finance* 18(1), 45–61); the copy is arXiv 1701.04260v1, January 2017 |
| **Type** | Model and calibration paper, 21pp. Calibrated to SPX options and VIX futures on 4 Dec 2015, 4 Jan 2016 and 22 Feb 2016 |
| **PDF** | `jacquier-et-al-2018-on-vix-futures-in-the-rough-bergomi-model.pdf` (arXiv version) |
| **BibTeX** | `jacquier2018roughvix` |
| **Status** | Reference: §3.1–3.2 (VIX dynamics and bounds), §3.5 (VIX futures calibration) and §4.3 (joint SPX check) carry the results |

## What it is

Rough volatility models drive instantaneous variance with a fractional Brownian motion whose
Hurst exponent H is small (about 0.1), which reproduces the steep short-dated SPX smile that
ordinary stochastic-volatility models miss. The rough Bergomi model (Bayer, Friz and Gatheral
2016) is the standard pricing version. This paper works out what the model implies for the
VIX and VIX futures.

- **VIX dynamics.** It gives an exact link between the forward variance curve at a future
  date and today's curve ξ₀, which allows the VIX to be simulated inside the model.
- **Bounds on VIX futures.** A model-specific lower bound (from Jensen's inequality and the
  model's lognormal structure) and the model-free upper bound (the square root of the
  average forward variance, the convexity gap).
- **Simulation.** Two schemes for the VIX: the hybrid scheme of Bennedsen, Lunde and
  Pakkanen plus forward Euler, and a truncated Cholesky method used as a benchmark. Both
  need large Monte Carlo samples; errors grow with maturity.
- **Lognormal approximation.** A refinement of Bayer–Friz–Gatheral's lognormal approximation
  for the VIX that matches the first two moments exactly. In tests the two approximations
  agree over a four-year horizon, and the original is about 40 times cheaper, so the authors
  use it for calibration.
- **Calibration.** ξ₀ is read off the SPX surface (via an eSSVI fit and the variance-swap term
  structure), then H and vol-of-vol ν are fitted to the VIX futures curve. The fitted H is
  0.09, 0.10 and 0.05 on the three dates, and the model reproduces the shape of the futures
  term structure, with the largest errors at short maturities, where the eSSVI fit is weakest.
- **Joint consistency.** Fixing H from VIX futures and fitting ν and correlation to SPX options
  gives a decent SPX fit except at short maturities, but ν comes out about 20% higher from SPX
  than from VIX. The authors flag this as a possible inconsistency between the two markets.

## Why it's in the library

Joint VIX–SPX consistency is the standing hard problem of volatility modelling: one model
should price S&P options and VIX derivatives together. This paper shows how far the
leading rough model gets, using few parameters, and where it falls short (short maturities,
and a gap in vol-of-vol between the two markets).

Read with the other joint models in the folder: Carr and Madan's double-gamma model fits both
markets at one maturity with a pure-jump approach. The convexity gap between VIX futures and
forward variance links back to the variance-swap notes.

## Links

- [[carr-madan-2014-joint-modeling-of-vix-and-spx-options]] — a pure-jump alternative fitted
  to SPX and VIX options at a single maturity
- [[dupire-2006-model-free-results-on-volatility-derivatives]] — the model-free upper bound on
  VIX futures used here
- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — the
  variance-swap replication behind ξ₀ and the VIX formula
- [[avellaneda-papanicolaou-2018-statistics-of-vix-futures-and-applications-to-trading]] — a
  statistical (physical-measure) model of the same futures curve
- [[carr-et-al-2003-stochastic-volatility-for-levy-processes]] — another route to stochastic
  volatility, by running a Lévy process on a random clock
