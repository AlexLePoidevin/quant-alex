# On the Pricing of Corporate Debt: The Risk Structure of Interest Rates

| | |
|---|---|
| **Authors** | Robert C. Merton (MIT) |
| **Year** | 1974 |
| **Type** | Journal article, *Journal of Finance* 29(2), 449–470 (AFA Papers and Proceedings), 22pp. Theory |
| **PDF** | Not hosted in this repository (JSTOR copy of the Wiley/AFA article) |
| **Find it** | [doi.org/10.1111/j.1540-6261.1974.tb03058.x](https://doi.org/10.1111/j.1540-6261.1974.tb03058.x) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22On+the+Pricing+of+Corporate+Debt%3A+The+Risk+Structure+of+Interest+Rates%22+Merton) |
| **BibTeX** | `merton1974pricing` |
| **Status** | Reference: §II (the pricing equation), §III (the discount bond and equity-as-a-call), §V (debt risk relative to firm risk) |

## What it is

The paper that turned option pricing into a theory of credit. It prices a company's debt
from three inputs: the value of the firm's assets, how volatile they are, and how much
the firm has promised to repay.

- **Setup.** The firm's total value follows a geometric Brownian motion; the firm has one
  zero-coupon bond promising B at time T and equity as the residual claim; the riskless
  rate is constant; markets are frictionless and trade continuously. Any claim on the
  firm satisfies the same Black–Scholes-type partial differential equation, and only the
  boundary conditions distinguish debt from equity.
- **Equity is a call option on the firm.** At maturity shareholders pay B if the firm is
  worth more than B, and otherwise hand the firm to the bondholders. So equity is a
  European call on firm value with strike B, and debt equals riskless debt minus a put
  on the firm.
- **The risk structure of interest rates.** For a given maturity, the yield spread over
  the riskless rate depends on just two things: the firm's volatility and the "quasi"
  leverage ratio d (the promised payment discounted at the riskless rate, divided by firm
  value). The spread rises with both. With maturity it can go either way: for highly
  levered firms (d ≥ 1) longer maturity *lowers* the spread.
- **How risky is the debt?** The bond's volatility is a fraction g of the firm's, with
  0 ≤ g ≤ 1: debt is never riskier than the firm, equity never less risky. At d = 1 the
  debt has exactly half the firm's volatility, whatever the maturity or business risk.
  A bond is equivalent to holding a fraction g in the unlevered firm and 1 − g in riskless
  bonds.
- **Modigliani–Miller with bankruptcy.** Because risky debt and levered equity can both be
  replicated from the unlevered firm and riskless bonds, the value of the firm does not
  depend on its debt–equity mix even when default is possible, without needing an
  equilibrium model.
- **Extensions.** Coupon bonds (only the perpetual case has a closed form), and callable
  bonds, where the firm picks the call boundary to maximise equity value.

## Why it's in the library

**It is where "structural" credit models start.** Treating a firm's debt as a short put
on its assets ties credit spreads to equity volatility and leverage, the basis of
distance-to-default measures, KMV-style default probabilities and joint models of equity
options and credit default swaps.

**It explains why credit gets riskier in a selloff.** As firm value falls, d rises and
the debt behaves more and more like equity, so credit spreads widen and credit becomes
more correlated with stocks exactly when diversification is most needed.

**Its known weakness is a lesson in itself.** Calibrated to realistic leverage and
volatility, the model produces short-maturity spreads close to zero, far below observed
spreads. The gap is usually attributed to jumps (firms can default without warning) and
to liquidity premia, both outside the diffusion setup.

## Links

- [[merton-1976]] — Merton's jump-diffusion paper, the usual fix for the model's
  too-small short-term spreads
- [[carr-wu-2010-stock-options-and-credit-default-swaps]] — a joint model of equity
  options and credit default swaps in the same structural spirit
- [[chernenko-sunderam-2020-measuring-the-perceived-liquidity-of-the-corporate-bond-market]]
  — the liquidity part of corporate bond pricing that a default-only model leaves out
