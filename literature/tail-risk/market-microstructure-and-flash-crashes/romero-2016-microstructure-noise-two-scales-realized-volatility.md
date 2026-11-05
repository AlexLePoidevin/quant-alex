# Microstructure Noise: The Use of Two Scales Realized Volatility for Noisy High-Frequency Data and its Implications for Market Efficiency and Financial Forecasting

| | |
|---|---|
| **Authors** | Aristides A. Romero Moreno (Utah State University) |
| **Year** | 2016 (May 2016) |
| **Type** | Master's thesis (Plan B report, Economics), Utah State University, 36pp. Posted on DigitalCommons@USU, Graduate Reports 826 |
| **PDF** | Local copy only ("All Rights Reserved"; no open licence) |
| **BibTeX** | `romero2016microstructure` |
| **Status** | Reference: §II–III (the five estimators) and §V (the Monte Carlo) carry the content; §VI is a small, inconclusive empirical test |

## What it is

A student thesis that explains and re-runs the two-scales realized volatility estimator
(TSRV) of Zhang, Mykland and Aït-Sahalia (2005). The problem it addresses is simple to
state. Summing squared returns estimates volatility well when prices are clean, but at
tick frequency every trade price also carries noise from the bid-ask bounce and the
trading process. That noise does not shrink as you sample faster, so the naive sum blows
up.

- **The model.** Observed log price = efficient log price + independent noise,
  `Y = X + ε`.
- **The five estimators**, worst to best, following the original paper:
  - *Fifth best*: sum squared returns over every tick. With `n` observations it estimates
    `2n·E[ε²]`, the noise variance, not the volatility.
  - *Fourth best*: sample sparsely, e.g. every 5 minutes. Less noise, but a 6.5-hour day of
    one-second data has 23,400 observations and 5-minute sampling uses 78 of them.
  - *Third best*: sparse sampling at the optimal frequency, which depends on the noise
    variance and the integrated quarticity.
  - *Second best*: average the sparse estimator over K offset sub-grids (start at the
    first tick, the second tick, …), so all the data are used. Still biased by the noise.
  - *First best (TSRV)*: the second-best estimator (slow time scale) minus `n̄/n` times the
    all-ticks estimator (fast time scale), which removes the noise bias. A further
    small-sample factor `(1 − n̄/n)⁻¹` reduces the remaining bias.
- **A by-product.** Because the all-ticks sum is dominated by noise, dividing it by `2n`
  gives a consistent estimate of the noise variance itself, a direct measure of how far
  trade prices sit from the efficient price.
- **Monte Carlo.** 25,000 simulated days from a Heston model with Gaussian noise (standard
  deviation 0.05% of price), using the original paper's parameters. The results reproduce
  the original ordering. The relative bias falls from about 295 for the all-ticks estimator
  to about 1 for 5-minute sampling, 0.2 for the averaged estimator, and essentially zero
  for the adjusted TSRV.
- **The empirical test.** Do Dow stocks with wider bid-ask spreads carry more noise? One
  month of TAQ data (October 2013) for the 30 stocks in the Dow as of January 2016, split
  into 25 below-average-spread and 5 above-average-spread names. The answer was no: the
  noise estimates were about 5.1 × 10⁻⁷ and 5.0 × 10⁻⁷, essentially zero for both groups
  and slightly the wrong way round. The author attributes this to one month of data, very
  liquid stocks and a membership list that postdates the sample (Apple joined the Dow in
  2015).

## Why it's in the library

**It is a clear walk-through of why naive high-frequency volatility is wrong.** Anyone
computing realised volatility from intraday bars has to choose a sampling frequency.
The five-estimator ladder shows the trade-off directly: sample too fast and you measure the
bid-ask bounce, sample too slowly and you throw away almost all the data. TSRV removes the
bounce statistically instead of by sampling sparsely.

**The noise-variance estimate is a useful diagnostic in its own right.** `[Y,Y]/(2n)` gives
a number for how noisy a price series is at tick level. That number says how far apart a
signal price and a fill price can be, and it differs across instruments.

**It is a thesis, not the primary source.** The method, theory and simulation design are
all Zhang, Mykland and Aït-Sahalia (2005, *JASA*). Its own empirical section is one month
of data on 30 very liquid stocks and does not find the effect it tests for. Use it as a
readable route into the original paper.

## Links

- [[merton-1976]] — jumps, the other reason a sum of squared returns misstates diffusive
  volatility
- [[carr-et-al-2005-pricing-options-on-realized-variance]] — pricing options on realized variance, the quantity this thesis estimates from noisy data
- [[carr-et-al-2017-pricing-variance-swaps-on-time-changed-markov-processes]] — what a variance swap on that realised variance is worth, and which option strip replicates it when there are jumps
- [[itkin-carr-2010-pricing-swaps-and-options-on-quadratic-variation]] — how discrete sampling and jumps change the fair strike of a variance swap
