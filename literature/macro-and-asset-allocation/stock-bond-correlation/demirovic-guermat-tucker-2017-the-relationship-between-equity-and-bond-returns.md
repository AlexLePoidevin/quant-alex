# The Relationship Between Equity and Bond Returns: An Empirical Investigation

| | |
|---|---|
| **Authors** | Amer Demirovic (Sarajevo School of Science and Technology), Cherif Guermat, Jon Tucker (University of the West of England) |
| **Year** | 2017 |
| **Type** | Journal article, *Journal of Financial Markets* 35, 47–64 (accepted manuscript). 351 US non-financial firms, 33,870 firm-months, August 1996 to February 2011 |
| **PDF** | Local copy only (Elsevier accepted manuscript, no open licence) |
| **BibTeX** | `demirovic2017equitybond` |
| **Status** | Reference: §2 (hypotheses from Merton's model), §4.2–4.5 and Table 5 carry the results |

## What it is

The stock–bond correlation at the level of a single firm: how a company's share returns
co-move with returns on its own corporate bond, and what the Merton (1974) structural model
says that co-movement should depend on.

- **The two forces.** In Merton's model equity is a call on the firm's assets and debt is a
  risk-free bond minus a put. News about asset value moves both in the same direction
  (positive correlation). A rise in asset volatility transfers value from bondholders to
  shareholders (negative correlation). Which dominates is an empirical question.
- **Method.** Monthly conditional correlations for each firm from a bivariate diagonal VECH
  GARCH model, then a panel regression of those correlations on the Merton distance to
  default (DD), GARCH equity volatility, their interaction, discrete DD bands, and either
  period fixed effects or the VIX.
- **Average correlation is small and positive**, about 0.089. Asset-value news dominates
  wealth-transfer events on average.
- **Credit risk drives it.** The correlation falls monotonically as distance to default
  rises: about 0.71 for firms near default, falling to about −0.05 to −0.08 for the
  safest. Example firms in the paper: a risky issuer (average DD 1.4) averages 0.73, a safe
  one (DD 15.6) averages 0.01.
- **Volatility, holding credit risk fixed, lowers it**, as the model predicts: raising
  equity volatility from 1% to 70% cuts the correlation by about 47 points for the safest
  firms but barely moves it for the riskiest, the opposite of the paper's own fourth
  hypothesis.
- **In stress the firm-level pattern disappears.** At the sample's maximum VIX (62.6) the
  predicted correlation is flat across DD and volatility: common market factors swamp
  firm-specific risk. In late 2008 the safe firm's correlation rose towards 0.20 while the
  risky firm's fell to about 0.25.

## Why it's in the library

- Most stock–bond work in this section is about the S&P 500 against Treasuries. This is the
  credit version: a company's own bonds behave more like its equity the closer it is to
  default, which matters for anyone holding both, or using corporate bonds as a diversifier.
- It is a clean empirical test of Merton's structural model on matched equity–bond pairs,
  with distance to default rather than credit ratings as the risk measure.
- The crisis result, that firm-level structure collapses when the VIX is extreme, is the
  same "correlations go to one" message as the risk-on/risk-off papers, seen from the
  credit side.
- Caveats: the four DD thresholds were chosen by searching 4,753 specifications for the
  lowest AIC; the predicted-correlation tables hold DD fixed while volatility changes,
  which the authors note is not how firms actually move; early years have few firms (33
  before 2001).

## Links

- [[carr-wu-2010-stock-options-and-credit-default-swaps]] — the same equity–credit link priced jointly from options and CDS
- [[campbell-pflueger-viceira-2020-macroeconomic-drivers-of-bond-and-equity-risks]] — the aggregate (Treasury) stock–bond correlation and why it changed sign
- [[papenbrock-schwendner-2015-risk-on-risk-off-correlation-regimes-and-networks]] — cross-asset correlation regimes where common factors take over in crises
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — dependence in credit portfolios and what breaks in stress
