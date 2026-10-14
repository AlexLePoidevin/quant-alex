# Optimum3

| | |
|---|---|
| **Author** | Todd Tresidder, FinancialMentor.com |
| **Published** | Tested and documented by [Allocate Smartly](https://allocatesmartly.com/financial-mentors-optimum3-strategy/), 17 January 2022 |
| **Type** | Proprietary practitioner strategy — **no paper, rules not fully disclosed** |
| **BibTeX** | `allocatesmartly2022optimum3` |
| **Status** | Reconstructed and backtested |

## ⚠️ The rules are not public

Allocate Smartly state plainly: *"Optimum3 is one of the handful of strategies we track
for which we are unable to disclose the specific rules."* They confirm they know the rules
and replicate them under licence, but the specification has never been published.

Everything below is assembled from the public description. Any implementation built from
it — including the one in `taa_ensemble/strategies.py` — is a **reconstruction, not the
strategy**, and its results should be reported that way.

## What is publicly stated

- **Universe:** 15 global asset classes — SPY, QQQ, VNQ, REM, IEF, TLT, TIP, VGK, EWJ,
  SCZ, EEM, RWX, BWX, DBC, GLD
- **Momentum:** six-month returns
- **Selection:** dual momentum (positive trend *and* relative strength), retaining roughly
  the top half
- **Construction:** of those, the three with the lowest average correlation, equal-weighted
- **Rebalance:** monthly, last trading day
- **Crash protection:** not explicitly stated in the public description

## Known gaps between the description and a reconstruction

| | Published description | Typical reconstruction |
|---|---|---|
| Universe | 15 risk assets | 16, with BIL ranked alongside the rest |
| Momentum filter | dual — absolute *and* relative | relative only (top half) |
| Downside rule | unspecified | all four bond sleeves negative → 100% cash |

None of these is a small difference. The absolute-momentum leg in particular is a
different risk control from a bond-based crash switch and will behave differently in a
drawdown.

## The idea worth keeping

Independent of whether any reconstruction is faithful, the design is unusual and the
design is public. Diversification is normally a **weighting** decision — inverse
volatility, risk parity and minimum variance all take the assets as given and solve for
how much of each to hold. Optimum3 makes it a **selection** decision: the weights are
fixed at one third and all of the work is in choosing which three assets are held.

The objective is the one in [[varadi-et-al-2012]], moved from the weighting stage to the
selection stage.

## Links

- [[varadi-et-al-2012]] — the Minimum Correlation Algorithm, the documented ancestor
- [[ledoit-wolf-2004]] — why correlation estimates are the fragile input here
