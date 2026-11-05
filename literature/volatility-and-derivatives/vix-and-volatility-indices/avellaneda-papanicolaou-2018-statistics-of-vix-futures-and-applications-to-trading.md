# Statistics of VIX Futures and Applications to Trading Volatility Exchange-Traded Products

| | |
|---|---|
| **Authors** | Marco Avellaneda (Courant Institute, NYU), Andrew Papanicolaou (NYU Tandon) |
| **Year** | 2018 (version of 24 February 2018; SSRN 3028910) |
| **Type** | Paper, 39pp. VIX and VIX futures data 2004–2017; model fitted on 2011–2016 and 2007–2016 |
| **PDF** | Local copy only (SSRN download with no open licence) |
| **BibTeX** | `avellaneda2018vixfutures` |
| **Status** | Reference: §2 (stationarity and the equilibrium PCA of the curve), §3 (rolling-futures returns and Proposition 3.1) and §5–6 (the two-factor model and simulated ETNs) carry the results |

## What it is

A statistical model of the whole VIX futures curve, used to answer one question: what do
the exchange-traded notes that roll VIX futures (VXX long, XIV short, VXZ mid-curve)
earn over time, and how risky is that?

- **VIX is not a commodity.** There is no way to store VIX and deliver it against a
  futures contract, so there is no cash-and-carry arbitrage tying futures to spot. VIX
  and its futures therefore swing far more than oil or an equity index, and the futures
  curve can sit well above or below spot.
- **VIX looks stationary, but only just.** Over 1990–2017 an augmented Dickey–Fuller test
  rejects a unit root (p = 0.003), but the result depends on including 2008: over other
  windows, or with 2008 removed, it does not reject. VIX's mean is 19.1, its mode 12.0,
  and the right tail fits a power law with exponent about −3.4. VIX has never closed below 9.
- **The curve is usually in contango.** The authors build constant-maturity futures
  (CMFs) from VIX to 8 months by interpolating the monthly contracts. A principal
  component analysis of the log curve around its long-run average (2011–2016) needs two
  shapes: the first explains 72% of the variation, two explain 90%, three 96%. The most
  likely curve, built from the modes of the two loadings, slopes upward.
- **Why rolling long futures loses.** A fund that holds a constant-maturity futures
  position earns the change in the CMF plus a "roll" term set by the slope of the curve.
  The roll is negative in contango and positive in backwardation. VXX is the 30-day
  version; XIV and SVXY are the short versions; VXZ rolls months 4–7 (average maturity
  5 months).
- **Proposition 3.1.** If the CMFs are stationary and ergodic and the curve is in
  contango on average, then shorting VXX, or buying XIV, makes money with certainty as the
  holding period goes to infinity. The authors stress that this is a long-run statement:
  over any finite window a spike in VIX with backwardation can wipe the position out.
- **A two-factor model.** Log VIX is modelled as the sum of two mean-reverting
  (Ornstein–Uhlenbeck) factors, with a constant risk premium shifting each factor's mean
  and speed under the pricing measure. Fitted by maximum likelihood with a Kalman filter
  to daily VIX and CMFs, it gives a slow factor and a fast, volatile second factor that
  produces the occasional backwardation. The fitted long-run futures level is about 25–29
  against a VIX mode of 12.6–13.8, which is the contango equilibrium.
- **The simulated ETNs match the real ones.** Simulating the model reproduces the
  historical drift, volatility and Sharpe ratio of VXX (2010–2017: drift −0.64, volatility
  0.63, Sharpe −1.02), VXZ (−0.27, 0.31, −0.87) and XIV (+0.52, 0.66, +0.79), all inside
  the bulk of the simulated distributions. The model's equilibrium Sharpe ratio for short
  VXX is between 0.23 and 0.87 depending on the fitting window.
- **The conclusion.** Selling VIX through ETPs has been profitable, but the Sharpe ratios
  are modest (no better than holding the S&P 500) and vary a lot over one-year horizons,
  because VIX spikes with backwardation happen sporadically but inevitably.

## Why it's in the library

**It explains the most consistent loss in listed products.** Long-VIX ETNs bleed because
of the roll down a curve that is usually in contango, not because of fees or bad luck.
The paper writes the roll down as a formula and shows that a stationary model fitted only
to the futures curve reproduces the historical ETN returns.

**It is precise about why the "free money" in short volatility isn't free.** The theorem
says short-VXX wins in the infinite limit; the simulations show a Sharpe ratio around 0.5
with wide dispersion over a year. The paper was dated three weeks after XIV lost about
90% in one day (5 February 2018), which is the risk its model describes.

**It is the cost side of the hedges in `tail-risk/`.** The steady contango drag that
makes long-VIX hedges expensive to carry in Szado's backtests is the same roll term that
pays short-volatility sellers here.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  hedger's side: what the contango drag costs a 60/40 portfolio that holds long VIX
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — short-VIX products as part of a much
  larger short-volatility trade, written months before XIV failed
- [[avellaneda-zhang-2010]] — the same first author on how daily-rebalanced leveraged ETFs
  drift away from their benchmark
- [[peters-2011]] — why a time average can differ from an ensemble average, the issue
  behind the "sure profit in the limit" result
- [[gehricke-zhang-2018-modeling-vxx]] — VXX decay as roll yield priced by variance risk
