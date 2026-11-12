# When Stock-Bond Diversification Fails: Managing Inflation Risk in Investor Portfolios

| | |
|---|---|
| **Authors** | Alfie Brixton, Ashwin Thapar, Thomas Maloney (AQR Capital Management) |
| **Year** | 2021 (October) |
| **Type** | Manager white paper, 17pp. US data, quarterly, 1972 to mid-2021 |
| **PDF** | Not hosted in this repository (AQR white paper, no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22When+Stock-Bond+Diversification+Fails%3A+Managing+Inflation+Risk+in+Investor+Portfolios%22+Brixton) for the title and authors |
| **BibTeX** | `brixton2021stockbond` |
| **Status** | Reference: §II (stocks and bonds), §III (real assets), §IV–V (trend, macro momentum, the "real return" basket) |

## What it is

A study of how stocks, bonds and other assets behave when inflation surprises, and of
why the stock–bond diversification that held from the 1990s to 2020 may not survive an
inflationary period.

- **Measuring inflation news.** Asset prices react to inflation surprises, not the level.
  The paper averages two standardised measures: year-on-year CPI inflation minus the
  previous year's (a random-walk forecast), and inflation minus the survey forecast made
  a year earlier. A matching measure of growth news is the control.
- **Stocks and bonds both lose to inflation.** Over 1972–2021 the S&P 500, ten-year
  Treasuries and a 60/40 mix all have negative correlations with inflation news. A 1-point
  inflation surprise over 12 months goes with about −2.2% on equities and −1.3% on bonds
  (against full-sample excess returns of 5.6% and 1.7% a year).
- **Why the correlation flips.** Stocks and bonds diversify each other on growth news
  (stocks up, bonds down) but not on inflation news, which hurts both. In quarters when
  growth news dominates, the stock–bond correlation has been near zero; when inflation
  news dominates, it has been positive. Growth news dominated most of the time after 1990.
- **Real assets.** Commodities (S&P GSCI) and inflation breakevens (long TIPS, short
  duration-matched nominals) have clearly positive inflation sensitivity, energy most of
  all. Real estate behaves much like equities. Unhedged TIPS are near zero, because their
  short-term returns are driven by real yields. Equities also lagged in disinflationary
  surprises, which coincided with growth shocks in this sample.
- **Strategies with convexity.** Trend following (1-, 3- and 12-month trends across
  global macro markets) and macro momentum have done well in both upside and downside
  inflation surprises and lagged in stable periods.
- **Putting it together.** A hypothetical "simple real return" basket gives a 25% risk
  allocation each to breakevens, commodities, trend and macro momentum. A 20% allocation
  to it moves the 60/40 portfolio's correlation with inflation news from −0.27 to −0.05.
  All of this is hypothetical, backfilled performance.

## Why it's in the library

**It explains the stock–bond correlation through the type of macro shock.** Growth shocks
push stocks and bonds in opposite directions; inflation shocks push them the same way.
Which kind of news dominates sets the sign of the correlation, and the post-1990
negative correlation was a growth-dominated regime, not a law.

**It was written just before the test.** In 2022 inflation surprised sharply upward and
stocks and bonds fell together, which is the scenario this paper describes.

**It is a manager's case for its own products.** Trend following and macro momentum are
strategies AQR runs, the hypothetical basket is backfilled, and the evidence is
dominated by the 1970s and early 1980s. The diagnosis (which shocks break diversification)
is more robust than the suggested fix.

## Links

- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — diversification assumptions failing when correlations change in a crisis
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — risk parity as a levered bet on a stable, negative stock–bond correlation
- [[keller-keuning-2023-haa]] — a tactical allocation rule designed for rising yields and inflation
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — why trend following can work: persistent regimes
- [[brooks-2021-what-drives-bond-yields]] — what drives the bond side: rate expectations, inflation expectations and term premia
- [[bekaert-engstrom-2010-inflation-and-the-stock-market-the-fed-model]] — stagflation as the reason equity and bond yields move together
- [[czasonis-kritzman-turkington-2021-the-stock-bond-correlation]] — forecasting the five-year stock–bond correlation from growth, inflation and relative yields
- [[durham-2019-us-treasury-bond-betas-1961-2019]] — quantile evidence that long Treasury returns are wider and more left-skewed on the worst equity days
- [[liu-fan-2016-stock-bond-correlation-and-duration-risk-allocation]] — the recent stock–bond correlation used as a short-horizon signal for duration
