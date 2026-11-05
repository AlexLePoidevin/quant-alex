# An Analysis of the VIX Volatility Index on the US Treasuries, Specifically During the Periods of Quantitative Easing

| | |
|---|---|
| **Authors** | Carolyne Cebrian Soper (Sacred Heart University; supervised by Lucjan Orlowski) |
| **Year** | 2015 (dated 15 April 2015) |
| **Type** | Student research paper, SSRN 2676400, 13pp. Monthly FRED data, February 2005 – February 2015 |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `soper2015vix` |
| **Status** | Reference: the results table in §4.1 and the VAR impulse responses (Model 5) are the whole of the evidence |

## What it is

A short regression study asking whether changes in the VIX move the 10-year Treasury
yield, and whether that link changed during the Fed's three rounds of quantitative easing.

- **Data.** Monthly changes in the VIX and the 10-year yield, 2005–2015 (about 120
  observations). Levels are non-stationary, so everything is in first differences.
- **Five models.**
  1. OLS of the yield change on the same month's VIX change: coefficient −0.009
     (t ≈ −2.0, p = 0.05), R² 3.2%. A one-point VIX rise goes with a yield about 0.9bp lower.
  2. The same with dummies for QE1, QE2 and QE3. None of the dummies is significant; R²
     rises to 5.3%.
  3. An ARMA(1,1) version: VIX coefficient −0.012 (t ≈ −2.8), R² 12.6%. Most of the extra
     fit comes from the MA term, not the VIX.
  4. A GARCH(1,1) on the yield change: VIX significant, R² 0.3%.
  5. A VAR with five lags: the yield's response to a VIX shock is negative and largest at
     about four months.
- **Conclusion.** The author reads all five as showing that the change in VIX "is
  predictive of" the change in the 10-year yield.

## Why it's in the library

The sign is the familiar one: when equity fear rises, Treasury yields fall, which is the
flight-to-quality leg of a negative stock–bond correlation. It is a compact,
readable example of that relationship over the QE years.

The evidence is much weaker than the conclusion. Models 1–4 regress the yield change on the
*same month's* VIX change, so they measure co-movement, not prediction. Only the VAR uses
lags, and it reports no significance bands. The QE dummies, the paper's stated question,
come out insignificant. One monthly sample of about 120 points with R² of 3–13% supports
"yields tend to fall in months when the VIX rises" and not much more. Treat it as an
illustration of flight to quality, not as a forecasting result.

## Links

- [[baur-kuck-2020-the-timing-of-the-flight-to-gold]] — the same flight-to-safety move
  measured intraday, into gold instead of Treasuries
- [[hartmann-straetmans-de-vries-2004-asset-market-linkages-in-crisis-periods]] — how often
  stock and bond markets crash together, and the flight-to-quality cases where they don't
- [[carr-wu-2006-a-tale-of-two-indices]] — what the VIX measures, as used here as a fear gauge
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — VIX
  exposure added to a stock–bond portfolio, the practical side of the same co-movement
