# The Effect of Uncertainty on Volatility and Correlation

| | |
|---|---|
| **Authors** | Hossein Asgharian (Lund), Charlotte Christiansen (Aarhus), Ai Jun Hou (Stockholm) |
| **Year** | 2023 (Journal of Banking & Finance 154, 106929, as "The effect of uncertainty on stock market volatility and correlation") |
| **Type** | Journal article; copy is the March 2022 SSRN working paper (3146924), 40pp. January 1990 – July 2020 |
| **PDF** | Local copy only (SSRN working paper of an Elsevier article) |
| **BibTeX** | `asgharian2023uncertainty` |
| **Status** | Reference: the in-sample HAR-RV-X tables, the out-of-sample forecasts and Table 9 (portfolio tests) carry the results |

## What it is

A horse race between measures of economic uncertainty and investor risk aversion as
predictors of stock-market volatility and cross-country correlation.

- **The model.** Corsi's HAR model forecasts realised volatility from its own daily,
  weekly and monthly averages. Here it is extended with outside predictors (HAR-RV-X), and
  a parallel version does the same for realised correlation (HAR-RC-X). Daily realised
  volatility comes from 5-minute S&P 500 returns; monthly volatility and correlations come
  from daily index returns for the US, Canada, France, Germany, Switzerland, Japan, Hong
  Kong, the UK and MSCI World ex-US.
- **The candidates.** Bekaert et al.'s risk aversion (RA) and economic uncertainty (EU)
  indices, which are built from financial and macro data, are the benchmark. Against them:
  Ludvigson et al.'s macro (MAC) and financial (FIN) uncertainty, the Baker–Bloom–Davis
  newspaper economic-policy uncertainty index (EPU), the VIX, the TED spread, industrial
  production and the OECD leading indicator.
- **What predicts US volatility.** Risk aversion is the strongest and most robust
  predictor in sample, ahead of economic uncertainty. Adding the VIX or financial
  uncertainty helps further. Policy uncertainty, the TED spread, industrial production and
  the leading indicator add nothing once RA and EU are in. The extra predictors matter
  much more for monthly than for daily volatility.
- **Out of sample the gains shrink.** At the daily horizon the plain HAR model is hard to
  beat. At the monthly horizon the benchmark plus financial uncertainty gives the lowest
  forecast error. The authors attribute the weaker out-of-sample showing to parameter
  instability as more predictors are added.
- **Portfolio test.** Volatility and correlation forecasts feed minimum-variance and
  market-neutral portfolios across the nine markets for a US investor. Models with RA or EU
  give the lowest portfolio risk and the highest utility. The economic value of switching
  from the worst models is up to 3.17% a year (random walk) and 1.93% (the full model with
  every predictor), and 0.5% a year relative to the plain HAR model. Most of the benefit
  comes through better volatility forecasts, not better correlation forecasts.

## Why it's in the library

**It tests the usual "fear" and "uncertainty" indicators by what they add to a standard
volatility forecast.** The answer is that measures built from market prices (risk
aversion, financial uncertainty, the VIX) carry the information. Macro and policy
uncertainty mostly don't once those are included.

**It is a clean extension of the HAR model.** It shows where outside predictors help (a
month ahead) and where they don't (a day ahead), and it warns that adding many predictors
overfits.

**Limits.** The benchmark RA and EU indices are themselves estimated from financial data,
so part of their success may be that they contain lagged market information. Everything
is from US-sourced uncertainty measures, and the portfolio test is a nine-index exercise.
There are small slips in the text: the TED spread and VIX are described as credit- and
stock-market measures in the wrong order, and "EU and RV" appears where "EU and RA" is
meant.

## Links

- [[corsi-2009-a-simple-approximate-long-memory-model-of-realized-volatility]] — the HAR model this extends
- [[audrino-huang-okhrin-2019-flexible-har-model-for-realized-volatility]] — another way to improve on fixed HAR lags
- [[caporale-et-al-2018-is-market-fear-persistent]] — persistence in the VIX itself
- [[smales-2016-risk-on-risk-off-financial-market-response-to-investor-fear]] — how markets respond on the day fear rises
