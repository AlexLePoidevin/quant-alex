# Stock–Bond Correlation and Duration Risk Allocation

| | |
|---|---|
| **Authors** | Liu Xinyi, Fan Hua (China Investment Corporation) |
| **Year** | 2016 (the copy is the authors' updated version, SSRN 2941948, with data appended to March 2017) |
| **Type** | Journal article, *Journal of Portfolio Management* 42(2), 56–63. doi:10.3905/jpm.2016.42.2.056. 15pp |
| **PDF** | Local copy only (authors' SSRN version of a JPM article, no licence) |
| **BibTeX** | `liu2016stockbond` |
| **Status** | Reference: Exhibit 3 (the decile results), equation (5) (factor-adjusted alpha) and the "Possible explanations" section carry the paper |

## What it is

A short practitioner paper claiming that the recent stock–bond correlation, measured
precisely from intraday futures data, forecasts Treasury returns: when the correlation is
unusually negative, yields tend to fall over the following weeks.

- **The measure.** One stock–bond correlation per week, from 10-minute S&P 500 futures and
  10-year Treasury note futures prices, January 1985 to September 2013 (1,496 weekly
  observations). The intraday estimate reacts much faster than the usual one-year rolling
  daily correlation.
- **The signal.** Each week, the correlation is placed in a decile relative to its own
  history over the last 20, 40, 80 and 160 weeks, and the deciles are averaged. The 10-year
  bond position is scaled linearly from long (decile 1, the most negative correlation) to
  short (decile 10).
- **Results, 1997–2013.** In the week after the lowest-correlation decile, the 10-year bond
  returned 19% annualised; after the highest, −13%. The gap persists at about 13% a year
  over weeks 2–8, then disappears. The simple strategy earned 3.9% a year over cash at 5.9%
  volatility (Sharpe 0.66, bootstrap-significant).
- **After controlling for other factors.** The authors regress the strategy on bond and
  equity returns and on portfolios built the same way from yield momentum, the curve spread
  and the VIX. The weekly alpha is 0.066% (t = 3.5), about 3.4% a year. The strategy loads
  negatively on equities and on the curve spread. For the 1-year bond, the effect is
  explained by those factors.
- **The pre-1997 period is weaker.** The effect at the long end is less significant before
  1997, which the authors treat as a structural break (as in Ilmanen and Campbell et al.).
- **Explanations offered.**
  - **1-year bond:** a low correlation signals that growth worries dominate inflation
    worries, so the Fed is likely to ease, and markets under-react to that.
  - **10-year bond:** markets are slow to reprice the bond's growing value as a
    safe-haven hedge.

  A worked mean–variance example for April–June 2013 suggests that a move in correlation
  from −0.6 to 0 implied about 1.7 percentage points more required yield, against an actual
  rise of 0.8 points that took several more weeks to follow.

## Why it's in the library

**It turns the stock–bond correlation into a duration signal.** The other papers in this
topic explain why the correlation changes sign over decades; this one says its week-to-week
level is informative for the next two months of bond returns. It also makes the
liability-holder's point clearly. A negative correlation is good for an asset-only
investor, but bad for a pension fund with bond-like liabilities, whose liabilities rise
in value just when equities fall.

**Treat it as a promising in-sample result.** The sample runs to 2013, with a short update.
The window choices (20–160 weeks), the post-1997 split and the factor portfolios were all
set by the authors on the same data. The strategy trades 10-year futures weekly, and costs
aren't modelled. The effect is concentrated in the post-1997 negative-correlation regime;
the 2022 inflation shock is exactly the kind of change it assumes away.

## Links

- [[brixton-thapar-maloney-2021-when-stock-bond-diversification-fails]] — when and why the stock–bond correlation turns positive
- [[campbell-pflueger-viceira-2020-macroeconomic-drivers-of-bond-and-equity-risks]] — a macro model of the post-2000 sign flip
- [[baele-van-holle-2017-stock-bond-correlations-macroeconomic-regimes-and-monetary-policy]] — accommodating policy and low inflation as the regime for negative correlations
- [[li-et-al-2022-does-fiscal-policy-matter-for-stock-bond-return-correlation]] — fiscal versus monetary leadership as the driver of the sign
- [[soper-2015-vix-and-us-treasuries-during-quantitative-easing]] — flight to quality from stocks into Treasuries, measured with the VIX
