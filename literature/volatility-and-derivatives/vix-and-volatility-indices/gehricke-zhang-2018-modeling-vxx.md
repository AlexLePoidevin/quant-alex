# Modeling VXX

| | |
|---|---|
| **Authors** | Sebastian A. Gehricke, Jin E. Zhang (University of Otago) |
| **Year** | 2018 (published in the *Journal of Futures Markets*). The local copy is the working paper of 13 September 2014 |
| **Type** | Paper, 38pp. VXX and VIX data January 2009 – June 2014; SPVXSTR index replicated from December 2005 |
| **PDF** | Local copy only (working paper with no open licence; the journal version is published by Wiley) |
| **BibTeX** | `gehricke2018vxx` |
| **Status** | Reference: §3 (the VXX model and the roll yield), §4 (estimating the market price of variance risk) and §5 (rebalancing frequency) |

## What it is

A model of the VXX exchange-traded note that starts from the S&P 500 and its stochastic
variance, and shows that VXX's steady losses are the roll yield, driven by the market
price of variance risk.

- **The VXX return puzzle.** VXX tracks the S&P 500 VIX Short-Term Futures index
  (SPVXSTR), which holds the first two VIX futures and rebalances daily to keep a constant
  one-month maturity. From its launch in January 2009 to June 2014 VXX lost 99.6% of its
  value (CAGR −63.5%), while the VIX itself lost 71.7% (CAGR −20.4%).
- **The model.** The S&P 500 follows Heston's stochastic-variance model. Using Zhang, Shu
  and Brenner's approximation, the price of a 30-day VIX future is the square root of a
  weighted average of current variance and its risk-neutral long-run mean (the leading
  term is within about 3% of the exact price for realistic parameters). Differentiating
  this gives the daily log return of the index as the change in a constant 30-day future
  plus a roll-yield term.
- **What drives the roll yield.** With variance held at its long-run (physical) mean, the
  roll yield's sign is set by λ, the market price of variance risk. When λ is negative
  (investors pay to be long variance), the risk-neutral long-run variance exceeds the
  physical one, the curve slopes up, and the roll yield is negative. This matches Eraker
  and Wu's equilibrium explanation via the variance risk premium.
- **Estimating λ from VXX alone.** Given a risk-neutral mean-reversion speed from the
  literature (κ* = 5.46), VXX's total return over the sample pins down λ in closed form:
  the authors get λ = −6.02, in the range of earlier option-based estimates.
- **Rebalancing frequency.** Replicating SPVXSTR from futures prices tracks the real index
  almost exactly. Rebalancing less often than daily lowers the index value (weekly,
  fortnightly and monthly rebalancing end at 1088, 842 and 265 against 1179 for daily).
  Simulations show hourly and daily rebalancing are nearly identical, so the
  continuous-time model is a fair description of the daily product.

## Why it's in the library

**It ties a product's decay to a risk premium.** The negative roll yield of long-VIX
products is not a design flaw: in this model it is the variance risk premium seen through
the futures curve. Holding VXX means paying that premium every day, which is the cost
side of every long-volatility hedge in `tail-risk/`.

**It is a compact, checkable model.** The pieces (Heston dynamics, a closed-form VIX
futures approximation, the index's published rules) are standard, and the λ estimate needs
nothing but two prices and one parameter taken from elsewhere. The weakness is that this
parameter is borrowed from another study and another period, and the single λ is an
average over a sample that starts at the 2009 peak in VIX.

## Links

- [[avellaneda-papanicolaou-2018-statistics-of-vix-futures-and-applications-to-trading]] —
  the same ETN decay from a statistical model of the whole futures curve
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  roll drag measured in a portfolio that holds long VIX futures as a hedge
- [[avellaneda-zhang-2010]] — why daily-rebalanced exchange-traded products drift away from
  their benchmark over long holding periods
