# Robust Leveraged ETF Portfolios: Extending Classic 40/60 Portfolios and Portfolio Insurance

| | |
|---|---|
| **Authors** | Mikhail Smirnov (Columbia University), Alexander Smirnov (Stuyvesant High School) |
| **Year** | 2020 (data to 28 February 2020, with a table to 5 March 2020) |
| **Type** | Slide deck posted as SSRN 3549581, 65 slides. Backtests of fixed-weight leveraged-ETF portfolios, plus slides on portfolio insurance and a "dynamic leverage" barrier model |
| **PDF** | Not hosted in this repository (SSRN posting, no licence) |
| **Find it** | [doi.org/10.2139/ssrn.3549581](https://doi.org/10.2139/ssrn.3549581) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Robust+Leveraged+ETF+Portfolios%3A+Extending+Classic+40%2F60+Portfolios+and+Portfolio+Insurance%22+Smirnov) |
| **BibTeX** | `smirnov2020leveraged` |
| **Status** | Reference: the performance slides for the 40-20-40 and 20-0-80 portfolios carry the claims; the second half is background on ETFs and a barrier-probability model of leverage |

## What it is

A practitioner deck arguing that a stock/bond portfolio built from leveraged ETFs, with
monthly rebalancing, beats both a stock index and a classic balanced portfolio on a
risk-adjusted basis, without borrowing at the portfolio level.

- **The baselines (1986 to February 2020, mutual funds, monthly rebalancing).**

  | Portfolio | Return | Volatility | Sharpe |
  |---|---|---|---|
  | 60% long Treasuries / 40% S&P 500 | 9.4% | 8.5% | 0.64 |
  | 72% / 48%, levered 120% with 20% borrowed at 1-month LIBOR + 25bp | 10.4% | 10.2% | 0.63 |
  | S&P 500 alone | 10.1% | 17.8% | 0.35 |

- **The "aggressive" 40-20-40 portfolio.** 40% TQQQ (3× Nasdaq-100), 20% TMF (3× long
  Treasuries), 40% TLT (1× long Treasuries), rebalanced monthly. The authors proposed it in
  2017. Reported results:
  - **2013–2017**, the window it was proposed on: 27.2% a year at 17.5% volatility.
  - **January 2018 to February 2020**, out of sample: 29.2% a year, Sharpe 1.31.
  - **August 2005 to February 2020**, extended with simulated leveraged series before the
    ETFs existed: 22.3% a year at 21.5% volatility, Sharpe 0.95. Over the same period QQQ
    returned 13.0% (Sharpe 0.56) and SPY 8.4% (Sharpe 0.37).
- **The "conservative" 20-0-80 portfolio.** 20% TQQQ, 80% TLT. The authors describe it as a
  form of constant-proportion portfolio insurance with multiplier 3. From August 2005 to
  February 2020 it returned 14.0% at 12.4% volatility (Sharpe 1.00), and 16.9% from 2009.
- **First weeks of COVID.** Daily tables from the 19 February 2020 peak to 5 March show
  the worst drawdowns at 11.9% for 40-20-40 and 4.9% for 20-0-80, against 13.2% for QQQ;
  the bond legs rallied as stocks fell. The authors say plainly that how the portfolio fares
  as the crisis continues "is still to be seen".
- **Portfolio insurance and dynamic leverage.** The second half recasts leverage as the
  probability that a fund's NAV hits a barrier (for example −15% to −30%) within a year,
  using reflection-principle formulas for Brownian motion. In a simple normal model,
  "dynamic leverage" is 2N(−z), with z the distance to the barrier in standard deviations.
  It proposes "constant dynamic leverage portfolio insurance": cut risk so that the
  probability of hitting the barrier stays fixed (for example at 5%). That is a
  volatility-aware alternative to CPPI.

## Why it's in the library

**It shows why a leveraged stock/bond mix looked so good, and why that depended on the
period.** Both portfolios are long duration twice over: TMF and TLT are long Treasuries,
and the equity leg is 3× Nasdaq. The backtests run through a 2005–2020 window when long
bonds rallied, rates fell, the stock–bond correlation was negative and the Nasdaq led.
That is the regime in which this construction works. Daily-reset leveraged ETFs also
lose to volatility drag in choppy markets, and the deck does not stress-test against
rising rates or a positive stock–bond correlation. 2022, when stocks and long bonds fell
together, is exactly that case.

**The barrier view of leverage is the useful idea.** Measuring leverage as the probability
of hitting a loss limit makes leverage non-linear in risk and short-gamma near the
barrier. As the NAV falls towards the limit, the effective leverage rises unless risk is
cut. That links to drawdown control and to the CPPI-style rules elsewhere in the library.

**Treat the numbers as in-sample.** The 40-20-40 weights were chosen on 2013–2017 data. The
"out-of-sample" window is two years. The pre-2010 history uses simulated leveraged series.
Costs, ETF expense ratios and tracking error are not discussed.

## Links

- [[avellaneda-zhang-2010]] — why daily-reset leveraged ETFs drift away from their multiple over time
- [[insiderfinance-volatility-drag]] — volatility drag, the cost of holding leveraged products through choppy markets
- [[return-stacked-2025]] — another route to stacking stock and bond exposure with leverage
- [[peters-2011]] — time-average growth, the frame in which leverage and volatility drag interact
- [[brixton-thapar-maloney-2021-when-stock-bond-diversification-fails]] — when stocks and bonds fall together, the regime this portfolio is not built for
- [[harvey-et-al-2018-the-impact-of-volatility-targeting]] — scaling exposure by volatility, the alternative way to manage leverage
