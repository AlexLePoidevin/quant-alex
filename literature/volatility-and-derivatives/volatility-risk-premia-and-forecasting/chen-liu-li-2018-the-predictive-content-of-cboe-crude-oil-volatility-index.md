# The Predictive Content of CBOE Crude Oil Volatility Index

| | |
|---|---|
| **Authors** | Hongtao Chen (Southeast University), Li Liu (Nanjing Audit University), Xiaolei Li (UNSW) |
| **Year** | 2018 |
| **Type** | Journal article, *Physica A* 492, 837–850 (doi 10.1016/j.physa.2017.11.014). The copy is the accepted manuscript, 40pp. Daily data, May 2007 to November 2016 |
| **PDF** | Local copy only (accepted manuscript under Elsevier's user licence, which is not an open redistribution licence) |
| **BibTeX** | `chen2018ovx` |
| **Status** | Reference: §4 (in-sample, out-of-sample, longer horizons, success ratios, robustness) carries the results |

## What it is

A test of whether the CBOE crude oil volatility index (OVX), the VIX method applied to
options on the United States Oil Fund (USO), helps forecast the volatility of spot oil prices,
both WTI and Brent.

- **Set-up.** Six GARCH-type models (GARCH(1,1), GJR, EGARCH, FIGARCH, HYGARCH and FIEGARCH)
  are fitted to daily spot returns, each with and without yesterday's OVX (squared and
  divided by 252, to make it a daily variance) as an extra term in the variance equation.
  Forecasts come from a rolling 1,000-day window. Because spot oil prices exist only daily,
  the target is the squared daily return, a very noisy stand-in for true volatility.
- **Findings.**
  - In-sample, the OVX coefficient is significantly positive in every model for both oils.
  - Out of sample, adding OVX improves one-day forecasts under most of the six loss functions
    (Diebold–Mariano tests), and the models without OVX are always excluded from the model
    confidence set. GARCH(1,1) and FIGARCH with OVX do best.
  - The improvement holds at 5- and 20-day horizons.
  - The OVX model is the more accurate of the pair on about 60% of days at best (FIGARCH),
    and its "success ratio" is significantly above 50% for all models.
  - Adding the short-term interest rate to both models does not remove OVX's contribution.

## Why it's in the library

It shows the usual implied-volatility result, that options carry forward-looking information
that past returns do not, outside equities: oil option prices on a futures-based ETF help
forecast the volatility of spot oil, including Brent, which the options do not reference.

The limits are standard for this kind of study. One 9½-year sample with one big oil crash in
2008 and another in 2014–16; a noisy volatility target (squared daily returns); and a gain
that is statistically clear but modest, with the OVX model winning about six days in ten.

## Links

- [[carr-wu-2006-a-tale-of-two-indices]] — the VIX methodology that the OVX copies
- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — how the VIX
  calculation behaves in practice, and its biases
- [[doman-doman-2020-daily-fx-volatility-and-the-time-of-day]] — another GARCH volatility
  study, where the choice of daily close changes the answer
- [[carr-wu-zhang-2019-using-machine-learning-to-predict-realized-variance]] — forecasting
  realised variance from option prices with machine learning
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — regime switching in an implied
  volatility index
