# Correlation Surprise

| | |
|---|---|
| **Authors** | Will Kinlaw; David Turkington (State Street Associates) |
| **Year** | 2014 (*Journal of Asset Management* 14(6), 385–399; published online 9 January 2014) |
| **Type** | Paper, 15pp. Daily data on 10 US equity sectors and 10 European equity sectors (November 1975 to September 2010) and 9 G10 currencies against the dollar (November 1977 to September 2010). The library also has the authors' February 2014 slide deck of the same work (State Street, marked limited access), which is not kept here |
| **PDF** | `kinlaw-turkington-2014-correlation-surprise.pdf` (CC BY 3.0 per the publisher's Crossref record; the article states it is open access) |
| **BibTeX** | `kinlaw2014correlation` |
| **Status** | Reference: the decomposition is in "Isolating correlation surprises"; Tables 3–5 (next day) and 7–8 (next month) carry the results |

## What it is

A way to split a market "turbulence" reading into two parts, unusual size and unusual
co-movement, and evidence that the co-movement part predicts trouble.

- **Turbulence.** Kritzman and Li's financial turbulence score is the Mahalanobis
  distance of today's vector of asset returns from its historical mean, using the
  historical covariance matrix (here divided by the number of assets). It is a
  multivariate z-score: high when returns are large, or when assets that usually move
  together diverge, or when assets that usually diverge move together.
- **The decomposition.** *Magnitude surprise* is the same score computed with all
  correlations set to zero, so it only sees how large each return is. *Correlation
  surprise* is turbulence divided by magnitude surprise. Above 1 means the pattern of
  co-movement is unusual for its size; below 1 means it is typical. With two assets
  of equal volatility and correlation 0.5, both rising 5% gives a correlation surprise
  of 0.67, while one rising 5% and the other falling 5% gives 2.0, although the
  magnitude surprise is the same. Unlike a rolling pairwise correlation, it summarises
  a whole universe in one number.
- **On the day, they move in opposite directions.** Among the 20% of days with the
  highest magnitude surprise, the most extreme days tend to have *typical* correlations
  (magnitude surprise 17–43% lower on high-correlation-surprise days).
- **The next day, the order flips (Table 3).** After a top-20% magnitude day with
  correlation surprise above 1, next-day magnitude surprise is 21% higher in US
  equities, 41% in European equities and 38% in currencies than after a top-20% day
  with typical correlations (p = 0.06, 0.00 and 0.00).
- **Returns (Table 4).** After high magnitude plus high correlation surprise, next-day
  annualised returns are lower in all three markets than after high magnitude with low
  correlation surprise: S&P 500 −6.7% against +27.7% (p = 0.04, 607 days), MSCI Europe
  2.5% against 7.0% (p = 0.41), G10 carry −8.3% against −1.2% (p = 0.26). Only the US
  difference is statistically significant. Volatility is higher and the hit rate lowest
  after the joint signal. High magnitude surprise alone did *not* predict lower US
  returns.
- **Short volatility (Table 5).** Simulated short at-the-money straddles (priced with
  Black–Scholes, not traded prices) earn less after the joint signal: S&P 500 15.1%
  against 31.8% annualised (p = 0.14), DAX 9.1% against 15.1% (p = 0.40), G10 currencies
  −5.5% against 10.2% (p = 0.03).
- **Decay and a monthly version.** The extra next-day volatility in US equities falls
  from 0.6 to 0.1 in magnitude-surprise units by days 2–5; the effect lasts longest for
  the currency straddles. A monthly signal, weighting each day's correlation surprise
  by its magnitude surprise, gives the same direction of results with smaller
  differences.
- **September 2008 as an illustration.** On 9 days that month correlation surprise
  exceeded 1; the following days averaged magnitude surprise 8.7 and an S&P 500 return
  of −2.19%, against 4.0 and +0.86% after the other days. The authors call this
  anecdotal and say it was chosen with hindsight.

## Why it's in the library

**It turns "correlations are breaking down" into a single number you can monitor.** In a
risk-on/risk-off market the worry is not just that moves are large but that the usual
relationships stop holding. Correlation surprise measures exactly that, across any number
of assets, and is close to uncorrelated with volatility on the day, so it adds
information rather than restating it.

**The evidence is suggestive, not strong.** The volatility result holds in all three
markets. The return results are significant only for US equities and the currency
straddles; the others have the right sign but large p-values. The covariance matrices use
only past data, but the 80th-percentile magnitude threshold was chosen on the full
sample. Results are mostly next-day and fade within a week, so using them would need fast
reaction. The authors work for a firm that sells such indicators.

**The decomposition itself is the durable idea.** Splitting a Mahalanobis distance into a
diagonal (size) part and a ratio (co-movement) part is a cheap, general way to watch a
correlation matrix for regime change.

## Links

- [[papenbrock-schwendner-2015-risk-on-risk-off-correlation-regimes-and-networks]] — another way to detect risk-on/risk-off states from changes in the correlation structure
- [[kinlaw-kritzman-turkington-2021-a-new-index-of-the-business-cycle]] — the same authors' use of the Mahalanobis distance to measure the business cycle
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — why correlation estimated in calm periods fails in a crisis
- [[meucci-2009]] — measuring how many independent bets a portfolio holds, which a correlation breakdown changes
- [[czasonis-kritzman-turkington-2021-the-stock-bond-correlation]] — the same group's Mahalanobis "relevance" idea used to forecast the long-horizon stock–bond correlation
- [[kinlaw-et-al-2021-the-myth-of-diversification-reconsidered]] — the same authors on measuring correlation asymmetry across asset classes
- [[racicot-theoret-2018-multi-moment-risk-hedging-strategies-and-the-business-cycle]] — how hedge funds' co-skewness and co-kurtosis with the market shift after VIX shocks
