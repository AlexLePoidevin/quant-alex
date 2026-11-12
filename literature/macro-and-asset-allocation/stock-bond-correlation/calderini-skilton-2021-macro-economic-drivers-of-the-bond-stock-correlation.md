# Macro-Economic Drivers of the Bond-Stock Correlation

| | |
|---|---|
| **Authors** | Pablo Calderini, Brent Skilton (Graham Capital Management) |
| **Year** | 2021 (August 2021) |
| **Type** | Manager research note, 6pp |
| **PDF** | Not hosted in this repository (Graham Capital; "may not be reproduced … without Graham's express written consent") |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Macro-Economic+Drivers+of+the+Bond-Stock+Correlation%22+Calderini) for the title and authors |
| **BibTeX** | `calderini2021stockbond` |
| **Status** | Read in full |

## What it is

A short practitioner model that splits stock and bond moves into four macro shocks and uses
them to explain why the US stock–bond correlation was positive from 1972 to 1999 and
negative from 2000 to 2020.

- **The pattern.** The rolling five-year correlation of the S&P 500 with the 10-year
  Treasury has averaged about zero (+0.04 since the 1930s), but it sits in long positive or
  negative regimes rather than near zero.
- **Four latent factors**, following Cieslak and Pang (2020): *growth* (stocks up, yields
  up, so a negative correlation); *monetary policy/inflation* (hawkish moves push stocks
  down and yields up, so a positive correlation); a *hedging premium* (fear of future
  growth shocks: stocks down, yields down, the classic risk-off move); and a *common
  premium* (fear of future tightening: both fall).
- **How they are identified.** Daily changes in 2-, 5- and 10-year zero-coupon yields and
  the log S&P 500 dividend yield. A matrix of loadings is fitted to their covariance under
  sign and size restrictions, for example that policy shocks hit short maturities hardest.
- **The decomposition.** The growth factor tracks industrial production and the policy
  factor tracks CPI. The difference between the two eras comes mainly from the premia: the
  common premium was more than twice as large before 2000, and the hedging premium
  subtracted about 20% more from the correlation after 2000.
- **Shock scenarios** (two standard deviations over a year, for a 60/40 portfolio): growth
  −1.1%; hedging premium −5.8% (bonds +8.5% offset stocks −15.3%); monetary policy −7.1%;
  common premium −12.0% (stocks −16.4% and bonds −5.4% together).

## Why it's in the library

**It is a compact version of the stock–bond regime argument.** Bonds hedge equity losses
caused by growth fears. They do not hedge losses caused by inflation or tightening fears.
After a 600bp fall in the one-year yield from 2000 to 2020, the authors argue, the
negative correlation of the last two decades may help less over the next two.

**It is a manager's note, not a tested model.** The factors are latent and identified only
through the authors' sign restrictions, there are no standard errors, and the scenario
numbers depend on those identifying choices. Use it for the framework. The academic
treatments linked below carry the evidence.

## Links

- [[campbell-pflueger-viceira-2020-macroeconomic-drivers-of-bond-and-equity-risks]] — the academic model of the same regime change, driven by monetary-policy rules
- [[brixton-thapar-maloney-2021-when-stock-bond-diversification-fails]] — a century of evidence that bonds stop hedging stocks when inflation is high
- [[li-et-al-2022-does-fiscal-policy-matter-for-stock-bond-return-correlation]] — fiscal policy as another driver of the correlation's sign
- [[bekaert-engstrom-2010-inflation-and-the-stock-market-the-fed-model]] — stagflation as the reason stock and bond yields move together
- [[fang-liu-roussanov-2022-getting-to-the-core-inflation-risks-across-asset-classes]] — core versus energy inflation as the switch between positive and negative correlation
- [[kinlaw-turkington-2014-correlation-surprise]] — measuring when correlations break from their usual pattern
