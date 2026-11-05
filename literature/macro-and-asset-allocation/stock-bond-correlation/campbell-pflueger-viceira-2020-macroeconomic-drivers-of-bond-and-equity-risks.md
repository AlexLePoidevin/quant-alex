# Macroeconomic Drivers of Bond and Equity Risks

| | |
|---|---|
| **Authors** | John Y. Campbell (Harvard), Carolin Pflueger (UBC), Luis M. Viceira (Harvard Business School) |
| **Year** | 2020 (the copy is HBS Working Paper 14-031, May 2019 draft) |
| **Type** | Journal article, *Journal of Political Economy* 128(8), 3148–3185. doi:10.1086/707766. Earlier title: "Monetary Policy Drivers of Bond and Equity Risks" |
| **PDF** | Local copy only (working paper; "may not be reproduced without permission") |
| **BibTeX** | `campbell2020macro` |
| **Status** | Reference: §1 (summary), §4.2 (break tests), §5.3 Table 4 (bond–stock comovement) and §5.4 (risk-premium decomposition) carry the results |

## What it is

A macro-finance model that explains why US Treasuries went from moving with stocks in the
1980s and 1990s to hedging them after 2000.

- **The empirical break.** A test for an unknown break date in the relation between
  inflation and the output gap, on US data 1979Q3–2011Q4, finds a break in 2001Q2. Before
  it, inflation rose when output was weak (an inflation–output beta of −0.32, correlation
  −0.28): a stagflationary regime. After it, inflation rose in expansions (beta 0.33,
  correlation 0.65). A separate break test on daily bond and stock returns dates the change
  in their relation to December 2000.
- **Why that flips the bond–stock correlation.** Nominal bond prices fall when inflation
  rises; stock prices rise with output. If inflation is high when output is low, bonds lose
  in bad times and are risky. If inflation is high when output is high, bonds gain in bad
  times and hedge.
- **The model.** A version of Campbell–Cochrane habit preferences built so that the
  consumption Euler equation is exactly log-linear, as in New Keynesian models. That makes
  it possible to price bonds and stocks inside a standard macro model with simple,
  homoskedastic dynamics for the output gap, inflation and the Fed funds rate. Risk premia
  still vary over time because risk aversion rises in recessions. The macro parameters are
  estimated separately for 1979Q3–2001Q1 and 2001Q2–2011Q4 from macro data only; no asset
  returns are used.
- **Fit.** The model's quarterly bond–stock correlation is 0.50 in the first period (data
  0.21) and −0.66 in the second (data −0.64), although asset returns were not targeted. The
  model's stock beta of bonds moves from 0.14 to −0.16. Bond return volatility falls from
  period 1 to period 2, as in the data.
- **Risk premia amplify the flip.** Switching off time-varying bond risk premia cuts the
  bond–stock covariance by about 30% in each period. Switching off stock risk premia cuts
  it by 71% in period 1 and 81% in period 2. When risk aversion rises in a downturn, there
  is a flight to safety. That hurts bonds when they are risky and helps them when they are
  safe.

## Why it's in the library

- **The macro reason the 60/40 hedge works or fails.** Whether bonds protect a stock
  portfolio depends on whether inflation is pro- or counter-cyclical. The model says the
  post-2000 negative stock–bond correlation is a feature of a regime in which inflation
  rises in good times, not a law of markets. A return to supply-shock inflation, as in the
  1970s and early 1980s, would make bonds risky again.
- **A regime you can watch.** The inflation–output-gap correlation is an observable macro
  quantity. It gives a reason, not just a rolling estimate, for expecting the stock–bond
  correlation to change sign.
- **Limits.** The model is estimated on two sub-periods split at a known break and treats
  each as a stable regime. It does not model when or how the regime switches. Its sample
  ends in 2011.

## Links

- [[ang-chen-2002]] — correlations that rise in down markets, the equity-only version of
  the hedging question
- [[campbell-1991]] — Campbell's earlier variance decomposition of stock returns into
  cash-flow and expected-return news, the method used in §5.4
- [[baele-van-holle-2017-stock-bond-correlations-macroeconomic-regimes-and-monetary-policy]] — ten-country evidence that monetary-policy regimes, not inflation cyclicality alone, set the sign of the stock–bond correlation
- [[burkhardt-hasseltoft-2012-understanding-asset-correlations]] — the same sign change traced to the growth–inflation correlation in a regime-switching long-run-risk model
- [[calderini-skilton-2021-macro-economic-drivers-of-the-bond-stock-correlation]] — a practitioner split of the correlation into growth, policy and premium shocks
- [[durham-2019-us-treasury-bond-betas-1961-2019]] — daily evidence that the negative stock–bond correlation since 1998 is also more variable, and that long Treasuries are not a convex hedge on the worst days
- [[fang-liu-roussanov-2022-getting-to-the-core-inflation-risks-across-asset-classes]] — the same sign change in the stock–bond correlation traced to core versus energy inflation
