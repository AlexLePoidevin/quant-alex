# How Do Factor Premia Vary Over Time? A Century of Evidence

| | |
|---|---|
| **Authors** | Antti Ilmanen, Ronen Israel, Rachel Lee (AQR), Tobias J. Moskowitz (Yale, NBER, AQR), Ashwin Thapar (AQR) |
| **Year** | 2021 (*Journal of Investment Management* 19(4), 15–57; earlier SSRN title "Factor Premia and Factor Timing: A Century of Evidence", 2019) |
| **Type** | Journal article, 43pp. Data July 1926 – November 2020 |
| **PDF** | Local copy only (the published JOIM version, © JOIM 2021) |
| **BibTeX** | `ilmanen2021factorpremia` |
| **Status** | Reference: Table 1 (century of premia), Table 2 (pre/original/post-sample test) and Table 4 (factor timing economics) carry the results |

## What it is

Four factors (value, momentum, carry and defensive) built the same simple way in six
asset classes (US stocks, international stocks, equity indices, government bonds,
currencies and commodities), with data going back to 1926 for most of them.

- **The premia are real.** Every factor has a positive premium in every asset class.
  Pooled across asset classes the Sharpe ratios are 0.53 (value), 0.64 (momentum), 0.57
  (carry) and 0.68 (defensive), with t-statistics from 5.1 to over 6.6. The combined
  multifactor, multi-asset portfolio has a Sharpe ratio of 1.46 (t = 14.2).
- **They vary over time, mostly through risk.** Structural break tests reject a constant
  mean for 8 of 20 factor-by-asset-class portfolios, and variance changes are found for
  every factor. By contrast, a constant equity premium cannot be rejected. Factor
  correlations move around but never all rise at once, and show no upward trend.
- **A new overfitting test.** The century of data lets them split each factor's history
  into three parts: before the original study's sample (which could not have been mined
  or traded on), the original sample, and after publication. Comparing pre-sample with
  original isolates data mining; comparing pre-sample with post-publication isolates
  arbitrage by informed traders. Value's out-of-sample Sharpe ratio is 49% lower than in
  its original sample and momentum's about 23% lower; the pre-sample comparison points to
  overfitting. Post-publication returns are no worse than pre-sample returns (p-values of
  0.70 for momentum, 0.31 for carry, 0.83 for the multifactor portfolio), so they find
  little evidence that arbitrage has eroded the premia, contrary to McLean and Pontiff.
- **Not macro risk.** Liquidity, sentiment, volatility, business-cycle, growth, monetary
  policy, political uncertainty and crash-risk variables explain almost none of the
  factor returns, which challenges risk-based macro explanations.
- **Factor timing barely pays.** With full-sample (look-ahead) parameters a timing model
  lifts the static portfolio's Sharpe ratio from 1.48 to 1.73. Estimated out of sample it
  lifts it only to 1.51, and the extra turnover breaks even at about 1.8–1.9 basis points
  per dollar traded, likely below real costs. Value spreads, business-cycle, growth
  momentum and CAPE signals are the only ones that help out of sample.

## Why it's in the library

It is the long-sample answer to two questions every factor investor faces: is the
premium a data-mining artefact, and can it be timed? The answers (mostly real but partly
overfit; varies but hard to time profitably) are a strong prior for staying with a
diversified static factor allocation. The pre-sample test is a clean idea worth
reusing: data from before a factor was discovered is the one sample no researcher could
have fitted.

The authors work at AQR, which sells factor products, and the long histories rely on
reconstructed pre-1970s data in some asset classes. The timing results are reported
gross, with the cost argument done by break-even rather than a cost model.

## Links

- [[mclean-pontiff-2016]] — the post-publication decay study this paper's pre-sample
  test is designed to separate into overfitting and arbitrage
- [[harvey-liu-zhu-2016]] — multiple testing and the factor zoo, the overfitting concern
  this paper tests with out-of-sample history
- [[hou-xue-zhang-2020]] — replication of anomalies in US equities, a complementary
  check on how many factors survive
- [[chen-roll-ross-1986]] — macro factors in stock returns, the kind of risk explanation
  this paper finds little support for
- [[blitz-2021-the-quant-crisis-of-2018-2020]] — a close look at the worst recent factor drawdown
- [[graham-harvey-2018-the-equity-risk-premium-in-2018]] — survey-based equity premium expectations that barely move with the business cycle
- [[rahelan-2019-taking-the-stag-out-of-stagflation]] — trend-timing equity factors across 23 countries, which adds nothing after costs
