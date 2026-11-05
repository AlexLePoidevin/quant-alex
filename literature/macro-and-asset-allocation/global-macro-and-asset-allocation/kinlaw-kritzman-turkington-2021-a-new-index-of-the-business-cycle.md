# A New Index of the Business Cycle

| | |
|---|---|
| **Authors** | William Kinlaw, Mark Kritzman, David Turkington (State Street Associates; Windham Capital; MIT Sloan) |
| **Year** | 2021 |
| **Type** | Journal article, *Journal of Investment Management* 19(3), 4–19. Monthly US data, index from 1956 to June 2020 using real-time (vintage) data |
| **PDF** | Local copy only (© JOIM) |
| **BibTeX** | `kinlaw2021business` |
| **Status** | Reference: §3 (index construction), §4 (time-varying variable importance) and §5 (event study, recession frequencies, ROC comparisons) |

## What it is

A recession index that asks whether today's economy looks more like past recessions or
like past booms, using the Mahalanobis distance.

- **The Mahalanobis distance** measures how unusual a point is relative to a group,
  allowing for each variable's volatility and the correlations between them. The same
  authors used it earlier as a measure of financial turbulence.
- **Inputs.** Four series: industrial production growth, nonfarm payroll growth, the
  stock market's one-year return, and the yield-curve slope (10-year minus short rate).
- **Two reference groups.** Months in NBER recessions, and months of robust growth
  (industrial production growth in the top quarter of its prior ten years). Each group
  gets its own means and covariance matrix.
- **The index.** Current conditions are scored against both groups. The two distances
  are turned into normal likelihoods, and the index is the recession likelihood as a
  share of the two: the relative probability of recession versus boom.
- **Variable importance moves with conditions.** Because the index is a ratio of two
  likelihoods, the weight on each input depends on where the economy is. The authors
  compute it by differentiating the index, unlike a probit or logit, whose weights are
  fixed coefficients.
- **Results.**
  - The index rises ahead of every recession since 1956. It was 76% in November 2019,
    93% in March 2020 and 98% in June 2020.
  - When it is above 50% (and rising by more than one standard deviation over its past
    year), a recession followed within six months 59% of the time. Above 70%, it was 77%
    of the time.
  - The yield curve, conditioned the same way, is informative only at about 18 months.
  - In out-of-sample ROC tests the index beats a logit model using the same inputs in
    the middle of the range, and beats the Conference Board Leading Index at moderate and
    aggressive thresholds. It does slightly worse at cautious ones.

## Why it's in the library

**It is a simple, transparent regime classifier.** Separating the recession and boom
distributions, rather than fitting one regression to everything, is a clean idea, and it
works with only four inputs.

**It treats regimes as different covariance structures.** Variables move together
differently in recessions and booms, and the index uses that. The same thinking applies
to classifying market regimes from asset returns.

**Caveats.** There are only about ten recessions since 1956. The thresholds and
standardised-shift filter are chosen by the authors, and the comparison set is limited
to two rivals. Some of the index's strength comes from the stock market and payroll
inputs, which move as a recession starts, so it is closer to a nowcast than a long-range
forecast.

## Links

- [[liu-moench-2016-what-predicts-us-recessions]] — a probit-and-ROC test of many leading
  indicators against the term spread
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — regimes in stock
  returns rather than the economy
- [[botte-bao-2021-a-machine-learning-approach-to-regime-modeling]] — regimes from a
  mixture of normal distributions fitted to factor returns
- [[azqueta-gavaldon-et-al-2020-nowcasting-business-cycle-turning-points]] — a network-based alternative for reading the business cycle from markets
