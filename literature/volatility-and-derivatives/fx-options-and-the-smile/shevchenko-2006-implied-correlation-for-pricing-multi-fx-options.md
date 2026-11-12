# Implied Correlation for Pricing Multi-FX Options

| | |
|---|---|
| **Authors** | Pavel V. Shevchenko (CSIRO Mathematical and Information Sciences, Sydney) |
| **Year** | 2006 (*Derivatives Week*, 13 and 20 March 2006; first submitted April 2004) |
| **Type** | Short trade-press article, 4pp |
| **PDF** | Not hosted in this repository (no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Implied+Correlation+for+Pricing+Multi-FX+Options%22+Shevchenko) for the title and authors |
| **BibTeX** | `shevchenko2006implied` |
| **Status** | Reference: the whole note is the result |

## What it is

A four-page derivation of the correlation between two exchange rates implied by FX option
prices, including the less familiar case where the two rates have different quote
currencies.

- **The currency triangle.** For three currencies, the cross rate is the ratio of two rates
  against the same currency. So the variance of the cross equals the two variances minus
  twice their covariance. Rearranged, the implied correlation between, say, USD/EUR and
  USD/JPY is (σ₁² + σ₂² − σ_cross²) / (2σ₁σ₂), using the three implied volatilities. This
  is the standard way FX desks price baskets on a common currency.
- **Different quote currencies.** For an option on two rates with four distinct currencies
  (for example, a payoff on one pair with a barrier on another), applying the triangle twice
  gives the correlation from six implied volatilities: the two rates themselves and four
  crosses. With a shared currency it reduces to the triangle formula.
- **Term structure.** The same formulas apply to forward implied volatilities between option
  expiries, giving piecewise-constant correlations over time for Monte Carlo pricing of
  barrier options.
- **Correlation risk becomes volatility risk.** With correlation implied from volatilities,
  a multi-currency option's price depends only on FX volatilities, so its correlation
  exposure can be hedged with vanilla options on the crosses.
- **Limits.** Everything assumes lognormal FX rates. With a smile, these correlations are
  consistent only with one set of volatilities, typically at the money. A smile-consistent
  version needs local-volatility-style models, which the note leaves aside.

## Why it's in the library

**FX is the one market where correlation is quoted.** Because crosses trade, the correlation
between two dollar rates can be read off option prices rather than estimated from history.
That makes FX the natural laboratory for implied correlation.

**It is the same algebra as the cross-rate geometry of FX correlation regimes.** The variance
identity behind the triangle is how the regime paper translates dollar-based correlations
into numeraire-free cross-rate volatilities.

## Links

- [[beber-et-al-2013-switching-risk-off-fx-correlations-and-risk-premia]] — uses the same
  triangle identity to read FX correlation regimes as cross-rate volatilities
- [[ang-chen-2002]] — correlations that change with market conditions, the reason a single
  historical correlation is a poor input for multi-asset options
