# Stochastic Risk Premiums, Stochastic Skewness in Currency Options, and Stochastic Discount Factors in International Economies

| | |
|---|---|
| **Authors** | Gurdip Bakshi, Peter Carr, Liuren Wu |
| **Year** | 2008 (*Journal of Financial Economics* 87(1), 132–156). The copy here is the SSRN working paper, version of 20 December 2006 |
| **Type** | Paper. Data: weekly OTC quotes on dollar–yen, dollar–pound and pound–yen options, November 2001 to January 2004 |
| **PDF** | Local copy only (SSRN working paper of a journal article; no open licence) |
| **BibTeX** | `bakshi2008stochastic` |
| **Status** | Reference: §3 (the model), §4.1 (how FX options are quoted) and §5 (the six findings) carry the paper |

## What it is

An exchange rate is the ratio of two countries' stochastic discount factors (the random
discount rate that prices every asset in that economy). So currency returns and currency
options carry information about how investors in both countries price risk. The paper
uses three currencies that form a triangle (USD, JPY, GBP) to pull apart the risk
premiums that are global from those that are country-specific.

- **Why currencies, not stocks or bonds.** A risk that does not move a country's bond
  yields or stock cash flows is invisible in bond and stock prices. It still moves the
  exchange rate, unless the two economies are perfectly symmetric. Currency options can
  therefore reveal risks that domestic markets do not span.
- **The model.** Each country's discount factor has three parts:
  - a deterministic interest rate;
  - a global Brownian shock whose risk premium varies over time;
  - a country-specific shock with jumps, whose risk premium varies separately.

  The time variation is modelled as a stochastic clock: the risk premium rate is the
  speed at which each shock's clock runs.
- **The jump specification.** Jumps follow an exponentially dampened power law, the
  CGMY-type family. One parameter (α) moves the jumps from rare compound-Poisson jumps,
  as in Merton (1976), to infinitely many small jumps.
- **How FX options are quoted.** The data are delta-neutral straddle volatility, 10- and
  25-delta risk reversals (call vol minus put vol, the skew) and butterflies (the
  wings' average vol minus the straddle vol, the curvature). There are seven maturities
  from one week to a year, 12,285 quotes in all. The model is estimated by maximum
  likelihood, with an unscented Kalman filter tracking the risk premium rates.
- **Finding 1: the economies differ.** Japan's average risk premium is about 50% higher
  than the US or UK. The scaling coefficient is about 1.5, with the US normalised to 1.
  Asymmetric versions fit far better than symmetric ones: pricing-error variance
  roughly halves.
- **Finding 2: global premiums are slower and bigger.** The global risk premium rate is
  close to non-stationary: mean reversion is not distinguishable from zero. Its
  volatility coefficient is about 0.8, against 0.14–0.18 for the country-specific
  premiums, which have half-lives of two to three months.
- **Finding 3: premiums react to relative wealth.** A negative country-specific shock
  raises that country's risk premium; the correlation is −0.70 to −0.999. A negative
  global shock lowers it; the correlation is +0.52 to +0.65. The paper's reading:
  investors demand more only when their economy falls *relative to* the world.
- **Finding 4: frequent jumps, priced only on the downside.** The best fit has
  high-frequency jumps (α = 1), not rare ones. Positive jumps in the pricing kernel can
  be set to zero with no loss of fit, so only downside jumps carry a premium.
- **Findings 5 and 6: fundamentals.**
  - The implied international risk-sharing index is 0.96–0.99.
  - Country premiums rise when short rates fall, when the curve steepens, and with local
    interest-rate cap and equity-option volatility.
  - In levels, regressions on fundamentals explain 16–47%. In weekly changes they
    explain 1–7%.

## Why it's in the library

**It explains what the FX smile is made of.** Risk reversals and butterflies are not
just quoting conventions. In this model they are the market's price of skewness and tail
risk, and they move because the risk premiums move. Stochastic skew, meaning the risk
reversal changing sign and size over time, falls out of having two premium processes with
different dynamics.

**It shows that only downside jumps are priced.** Both up and down jumps occur, but the
pricing kernel only charges for down jumps. This is the same asymmetry that makes index
puts expensive in equities. It is also why tail hedges cost more than their historical
payoff frequency would justify.

**It separates global from local risk.** A study of one economy's index options sees only
a one-dimensional projection of the pricing kernel. The triangle shows that global and
country shocks move premiums in opposite directions. If you regress currency returns on
fundamentals without separating the two, the effects can cancel.

**Limits.** The sample is about two years of weekly data from 2001 to 2004, one
particular regime. The free jump parameter α is poorly identified, so the authors
compare fixed values. Rates are deterministic.

## Links

- [[merton-1976]] — the compound-Poisson jump model that the dampened power law contains
  as a special case
- [[shreve-2004]] — change of measure and stochastic discount factors, the machinery
  behind equations (1)–(3)
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — how far the
  equity volatility index's own tails are from normal, the equity-side counterpart of
  butterfly prices
