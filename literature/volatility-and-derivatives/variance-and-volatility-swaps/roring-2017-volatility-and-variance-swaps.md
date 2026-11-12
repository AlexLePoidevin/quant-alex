# Volatility and Variance Swaps: A Comparison of Quantitative Models to Calculate the Fair Volatility and Variance Strike

| | |
|---|---|
| **Authors** | Johan Röring (supervisor Åke Brännström) |
| **Year** | 2017 (dated 8 June 2017) |
| **Type** | Master's thesis, Department of Mathematics and Mathematical Statistics, Umeå University, 49pp |
| **PDF** | Not hosted in this repository (thesis with no open licence stated) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Volatility+and+Variance+Swaps%3A+A+Comparison+of+Quantitative+Models+to+Calculate+the+Fair+Volatility+and+Variance+Strike%22+R%C3%B6ring) for the title and authors |
| **BibTeX** | `roring2017volatility` |
| **Status** | Reference: §2 (contracts), §3.1–3.2 (variance replication and the volatility strike), §3.4 (vanna-vomma model) and §6–7 (results) carry the content |

## What it is

A student thesis that explains variance and volatility swaps from first principles and
then compares four ways of setting their fair strike against realised S&P 500 volatility.

- **The contracts.** A variance swap pays notional × (realised variance − strike); a
  volatility swap pays on realised volatility instead. Because volatility is the square
  root of variance, the two strikes differ by a convexity correction.
- **Replicating variance.** The fair variance strike can be built from a strip of
  out-of-the-money puts and calls weighted by 1/K², the standard log-contract
  replication; the thesis works through a discrete-strike approximation with a numerical
  example. Getting a volatility strike from it needs a further step (a Laplace-transform
  technique) because of the convexity gap.
- **Four estimators of the strike.**
  - *Black-Scholes / implied volatility*: the volatility indices VIX, VXV and VXMT as the
    1-, 3- and 6-month forecasts.
  - *Vanna-vomma*: use the implied volatility at the strike where the option's vanna (or
    vomma) is zero, following Rolloos and Arslan (2017), as an estimate of the volatility
    strike that sidesteps the smile.
  - *EWMA* and *GARCH(1,1)*: forecast volatility over the swap's life by Monte Carlo
    (10,000 paths), with GARCH re-estimated daily on 10 years of returns.
- **Tests.** A 2015 comparison of all four at 1-, 2- and 3-month maturities, using S&P 500
  options from Cboe LiveVol; a 2008–2016 backtest at 6 months for Black-Scholes, EWMA and
  GARCH; and a 1995–2016 backtest of EWMA and GARCH at 1, 3 and 12 months.
- **Results.** GARCH has the smallest mean error at 1 and 2 months and the best upper tail
  at most maturities; EWMA is close behind at about half the run time. Implied
  volatility sits almost constantly above realised volatility after 2009, so it
  overestimates the strike (its worst 3-month undershoot is only −0.0007). The
  vanna-vomma estimator has a good mean error, the best at 3 months, but the largest
  dispersion and one extreme 1-month outlier, and only one year of option data.

## Why it's in the library

**It is a clear, worked introduction to the variance-swap replication argument.** The
1/K² strip, its discrete approximation, and the convexity gap between variance and
volatility strikes are laid out step by step, at a level below the original dealer and
academic papers.

**Its main empirical finding is the variance risk premium, seen from the other side.**
Implied volatility exceeding subsequent realised volatility almost all the time after
2009 is the gap a variance-swap seller collects. The thesis reads it as a forecasting
error by implied volatility; in the pricing literature it is a premium for bearing
volatility risk, which is why a time-series forecast can beat implied volatility as a
predictor of realised volatility and still be the wrong strike for a traded swap.

**Treat the comparison as illustrative.** It is a master's thesis: one index, one year of
option data for the vanna-vomma test, no transaction costs or significance tests, and
forecast accuracy measured against realised volatility rather than against traded swap
quotes.

## Links

- [[lv-wang-yuan-2026-garch-evt-rvine-scad-portfolio]] — GARCH as the volatility filter
  in a full portfolio model
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  cost of being long implied volatility through VIX futures and calls, the mirror image of
  implied volatility sitting above realised
- [[merton-1976]] — jumps, the extension the thesis names for models of the swap strike
- [[rolloos-arslan-2015-taylor-made-volatility-swaps]] — the vanna-volga volatility-swap estimator compared here
