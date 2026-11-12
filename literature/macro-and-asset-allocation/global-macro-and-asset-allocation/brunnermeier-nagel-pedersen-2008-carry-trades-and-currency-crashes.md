# Carry Trades and Currency Crashes

| | |
|---|---|
| **Authors** | Markus K. Brunnermeier, Stefan Nagel, Lasse H. Pedersen |
| **Year** | 2008. Published in *NBER Macroeconomics Annual* 23, 313–348 (doi 10.1086/593088) |
| **Type** | Journal article; this copy is NBER Working Paper 14473 (November 2008), 36pp. Data 1986–2006, eight developed currencies against the US dollar |
| **PDF** | Not hosted in this repository (NBER working paper, "All rights reserved") |
| **Find it** | [doi.org/10.1086/593088](https://doi.org/10.1086/593088) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Carry+Trades+and+Currency+Crashes%22+Brunnermeier) |
| **BibTeX** | `brunnermeier2008carry` |
| **Status** | Reference: Section 2 (skewness and interest differentials), Section 3 (speculator positions and crash risk) and Section 4 (VIX, TED and funding liquidity) |

## What it is

The paper that explains why the currency carry trade, which means borrowing in low-rate
currencies to invest in high-rate ones, "goes up by the stairs and down by the elevator".

- **The puzzle.**
  - **The theory:** uncovered interest parity says high-rate currencies should depreciate by
    the interest differential.
  - **The data:** on average they do not. They even appreciate slightly, with a low R². That
    is why carry earns money.
  - **The anomaly:** large exchange-rate moves sometimes happen with no news. The paper's
    example is the dollar falling sharply against the yen on 7–8 October 1998.
- **The main findings, for eight developed currencies from 1986 to 2006:**
  - **Crash risk:** high-interest currencies have negatively skewed returns and low-interest
    currencies positively skewed ones. Across countries, interest differentials line up with
    skewness, with an R² of 81%. Option risk reversals show the same pattern in risk-neutral
    prices.
  - **Speculator positions:** carry is associated with speculators' net long futures
    positions in the high-rate currency. Larger positions predict more crash risk.
  - **Losses and the price of crashes:** carry-trade losses lower future positions and crash
    probability, but raise the price of crash insurance.
  - **Funding liquidity:** rises in the VIX or the TED spread coincide with unwinding and
    carry losses. High levels of either predict higher later returns to investment currencies,
    and controlling for the VIX weakens the forward-premium puzzle.
  - **Co-movement:** currencies with similar interest rates move together, beyond what
    fundamentals explain.
- **Size of the effect.** An equal-weighted carry portfolio had an annualised Sharpe ratio of
  about 0.65–0.70, with negative skew of roughly the same size as the US stock market's. The
  negative skew did not diversify away across currencies.
- **The model behind it** is funding-liquidity spirals (Brunnermeier and Pedersen). Losses
  force speculators to cut positions, which moves prices further and raises margins and
  volatility. Gains are not amplified the same way, which produces negative skewness.

## Why it's in the library

- **It is the standard account of crash risk as the price of a steady premium.** The same shape
  of small regular gains and occasional sudden losses runs through short volatility, risk
  parity and other crowded trades. The paper ties it to a measurable cause: funding
  constraints that bind for many speculators at once.
- **It links a risk-off variable to returns.** The VIX predicting currency returns, and
  explaining part of a classic anomaly, is a concrete example of risk-on and risk-off
  dynamics working through who holds the positions.
- **Limits.** The sample is 1986–2006, so it ends before the 2008 carry crash. Speculator positions come from CFTC futures data,
  which covers only part of the market.

## Links

- [[bakshi-et-al-2008-stochastic-risk-premiums-and-skewness-in-currency-options]] — currency
  skew and risk premia priced from options on a currency triangle
- [[carr-wu-2007-stochastic-skew-in-currency-options]] — currency risk reversals that swing and
  change sign over time, the option-implied side of crash risk
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the same steady-gains, sudden-loss
  structure argued for volatility-sized strategies
- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]] — another case of intermediaries'
  constraints amplifying price moves
