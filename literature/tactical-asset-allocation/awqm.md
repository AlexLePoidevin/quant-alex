# All-Weather Quad Momentum (AWQM)

| | |
|---|---|
| **Author** | Todd Tresidder, FinancialMentor.com |
| **Documented by** | [Allocate Smartly](https://allocatesmartly.com/financial-mentors-all-weather-quad-momentum/) |
| **Type** | Proprietary practitioner strategy — **rules not disclosed** |
| **BibTeX** | `allocatesmartly_awqm` |
| **Status** | Reconstructed and backtested |

## ⚠️ The rules are not public

Allocate Smartly state: *"Unlike most strategies that we track, we will not be disclosing
the specific rules traded by AWQM."* The same author's [[optimum3]] is in the same
position. Anything built from the public description is a reconstruction and should be
reported as one.

## What is publicly stated

- **A four-quadrant universe**, chosen so something in it works in each economic regime:
  prosperity (equities), recession (cash and short Treasuries), inflation (gold, TIPS),
  deflation (long Treasuries)
- **The book split evenly between two momentum horizons** — long-term at roughly 10–12
  months and short-term at roughly 1–6 months
- Conceptually, *Traditional Dual Momentum* (the long leg) blended with *Accelerating Dual
  Momentum* (the short leg), over a broader universe than either
- Monthly rebalance
- Allocate Smartly's caution: *"this strategy takes aggressive positions. It will at times
  be entirely allocated to risk, and does not enforce a meaningful degree of
  diversification."*

One design note they record is worth keeping: the authors deliberately did **not** maximise
the historical allocation to short-term momentum, choosing instead on *"intuition about how
the future will differ from the past."* Philosophy over backtest optimisation — unusual to
see stated.

## Reconstruction used here

Not from the source: 12-month and mean(1, 3, 6)-month lookbacks; top three per sleeve;
equal weight within a sleeve; an absolute-momentum hurdle against BIL that sends a failed
slot to cash. Universe SPY, QQQ, EFA, EEM · VNQ, RWX · DBC, GLD, TIP · IEF, TLT, with BIL
as the safe asset.

## The finding that survives the uncertainty

Whatever the exact lookbacks, the interesting question is whether two horizons are worth
running separately. On this reconstruction they are: the two lists are **identical in only
20% of months** and share on average **1.81 of three** picks, with nothing in common in 4%.

But they agree on *regime*. The share of slots by quadrant is near-identical on both
horizons — prosperity 49%, inflation 22–24%, real assets 14–18%, deflation 11–13%. The
horizons disagree about which asset expresses a regime, not about which regime is running.

## Measured 2009–2026

| | AWQM | 60/40 SPY–IEF |
|---|---:|---:|
| Ann. return | 10.28% | 10.22% |
| Ann. volatility | 12.79% | 10.28% |
| Sharpe | 0.83 | 1.00 |
| Sortino | 1.07 | 1.28 |
| Calmar | 0.52 | 0.49 |
| Max drawdown | −19.8% | −21.0% |
| Skew | −0.41 | −0.13 |

Return is a dead heat at 2.5 points more volatility. The absolute-momentum hurdle passes
95% of the time, so the book is almost always fully in risk — consistent with Allocate
Smartly's warning about aggressiveness.

## Links

- [[optimum3]] — the same author, also undisclosed, also correlation/momentum based
- [[keller-butler-2014-eaa]] — the other strategy here that blends horizons, via
  elasticities on one score rather than two separate sleeves
