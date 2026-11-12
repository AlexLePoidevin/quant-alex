# Momentum and the Cross-Section of Stock Volatility

| | |
|---|---|
| **Authors** | Minyou Fan, Fearghal Kearney, Youwei Li, Jiadong Liu (Queen's University Belfast; University of Hull) |
| **Year** | 2022 (the copy is the November 2021 version, SSRN 3977553; published in *Journal of Economic Dynamics and Control* 144, 104524, 2022) |
| **Type** | Paper, 54pp. All London Stock Exchange stocks 1965–2018, plus 70 futures and indices (27 commodities, 24 equity indices, 19 bond and rate contracts) from 1970–1993 onwards |
| **PDF** | Not hosted in this repository (SSRN working paper; journal version © Elsevier) |
| **Find it** | [doi.org/10.1016/j.jedc.2022.104524](https://doi.org/10.1016/j.jedc.2022.104524) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Momentum+and+the+Cross-Section+of+Stock+Volatility%22+Fan) |
| **BibTeX** | `fan2022momentumvol` |
| **Status** | Reference: §3 (where momentum risk comes from), §4.2 (the volatility exponent N) and §5 (crash periods) carry the argument |

## What it is

An argument that momentum crashes start when the portfolio is formed, not after. Picking
past winners and losers by raw return fills both legs with the most volatile assets. In UK
stocks, the most volatile tenth of stocks are 8.3 times as likely to be picked as the least
volatile tenth, and 11.9 times as likely on the loser side.

- **Volatile stocks have no momentum.** Split by volatility over the formation year, the
  three most volatile deciles show no significant continuation. The low- and
  medium-volatility deciles mostly do. So the riskiest names add risk without adding
  signal.
- **"Excess volatility".** The momentum portfolio is significantly more volatile than a
  random portfolio of the same size, in all four markets tested. The authors call this
  momentum-specific risk.
- **The fix: divide by volatility to a power.** Score each asset by its 12-month return
  divided by its volatility raised to a power N (GRJMOM).
  - **Special cases:** N = 0 is plain momentum and N = 1 is momentum on Sharpe ratios.
  - **Shape:** the Sharpe ratio is hump-shaped in N, peaking in the full sample at N =
    2.8 (UK stocks), 2.3 (commodities), 2.6 (equity indices) and 2.3 (bonds).
  - **Live rule:** the strategy re-picks N each month on an expanding window. The chosen N
    drifts up over time, for UK stocks from about 0.8 before 2008 to above 2 after it.
- **Results (UK stocks, deciles, equal weights, monthly).**

  | | Plain momentum | Sharpe-ratio momentum | GRJMOM |
  |---|---|---|---|
  | Annual return | 17.9% | 17.7% | 22.4% |
  | Sharpe ratio | 0.67 | 0.92 | 1.18 |
  | Maximum drawdown | 90% | 71% | 47% |

  Volatility falls from 27% to 19%. Most of the gain comes from the loser leg, which under
  plain momentum earns positive returns, which the short side then loses.
  - **Other markets:** commodities and equity indices show the same pattern. In bonds none
    of the three versions is significant.
- **Crashes.** In April 2009 plain UK momentum lost 75.9% in one month, against 17.9% for
  GRJMOM. Over the worst six months of 2009 the losses were 86.6% against 11.1%. A
  monthly alpha of about 1% (t ≈ 7) survives controls for the market, size, value and
  plain momentum.

## Why it's in the library

**It locates momentum risk in the selection step.** Barroso–Santa-Clara and
Daniel–Moskowitz scale the whole long/short book after it is built. This paper instead
changes which assets get picked, so the book stays dollar-neutral at a fixed size. The two
fixes can be combined, and the paper shows its version still adds value after
volatility scaling.

**It is a simple, general rule.** Dividing past return by volatility to a power works in
four asset classes. It nests the plain and Sharpe-ratio versions as special cases.

**Limits.** No trading costs are reported. The UK sample equal-weights every listed stock,
so small, illiquid names dominate the extreme portfolios, especially the losers that drive
the gains. The text quotes the 2009 six-month crash as both 84.6% and 86.6% for plain
momentum, and as 19.7% and 11.1% for GRJMOM. The live N is chosen by maximising past
Sharpe ratios, which is a mild form of in-sample tuning.

## Links

- [[butt-virk-2020-momentum-crashes-and-variations-to-market-liquidity]] — when momentum crashes, from market states and liquidity
- [[swedroe-2020-left-tail-risk-and-left-tail-momentum]] — another signal that screens momentum by risk, here by left-tail losses
- [[harvey-et-al-2018-the-impact-of-volatility-targeting]] — volatility scaling of whole portfolios, the time-series counterpart of this cross-sectional adjustment
- [[kelly-moskowitz-pruitt-2021-understanding-momentum-and-reversal]] — momentum explained as time-varying exposure to risk factors
