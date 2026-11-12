# Alice's Adventures in Factorland: Three Blunders That Plague Factor Investing

| | |
|---|---|
| **Authors** | Rob Arnott, Campbell R. Harvey, Vitali Kalesnik, Juhani Linnainmaa |
| **Year** | 2019 (*Journal of Portfolio Management* 45(4), 18–36; this copy is SSRN 3331680) |
| **Type** | Research article, 35pp including an online appendix on each factor's rationale. US stocks, July 1963–June 2018 |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [doi.org/10.3905/jpm.2019.45.4.018](https://doi.org/10.3905/jpm.2019.45.4.018) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Alice%27s+Adventures+in+Factorland%3A+Three+Blunders+That+Plague+Factor+Investing%22+Arnott) |
| **BibTeX** | `arnott2019factorland` |
| **Status** | Reference: Exhibits 1, 5 and 6 (returns before and after publication and since 2003), Exhibit 8 (non-normality), Exhibits 11–13 (drawdown and bad-luck bootstraps) |

## What it is

A practitioner-academic paper (Research Affiliates with Harvey and Linnainmaa) on why factor
investing disappoints. It studies 15 popular factors plus 33 others, each built as a
Fama–French long-short portfolio scaled to 10% volatility, and names three blunders.

- **Expecting too much.** Factor returns are inflated by data mining, crowding after
  publication, trading costs and valuation drift over the backtest. Across all 46 factors,
  average market-adjusted returns in the 10 years after each original sample ends are less
  than half those in the 10 years before. Since mid-2003, no popular factor except the market
  has a statistically significant excess return; equal-weight portfolios of factors 1–6,
  7–14 and the other 33 earned 3.10%, 2.89% and 5.29% a year, against 7.38%, 7.28% and
  10.28% over the full sample.
- **Underestimating the tails.** Monthly factor returns are skewed and fat-tailed, momentum
  and illiquidity most of all. For 11 of the 14 factors, the worst month should happen less
  than once in 2,000 years under normality. Momentum fell 44% from its 2009 peak, with −24%
  in April 2009 alone, an "8-sigma" month.
- **Trusting diversification.** Factor betas and cross-correlations change through time.
  Portfolios of factors that looked market-neutral, with betas near −1 in the early 2000s,
  had their negative betas vanish in 2008–09, and the combined factor portfolio's worst month
  (−16.0%) was almost the average of its components' worst months (−17.0%). The 2008–09
  factor crash came as markets rebounded in March–April 2009.
- **Bootstraps.** The worst drawdown of the six-factor portfolio (33%) looks like a 2.7% event
  under normal simulation but happens in over a quarter of 12-month block bootstraps, which
  keep serial and cross-correlation. The post-2003 shortfall of factor portfolios has a
  p-value of about 0.1–0.3% against pre-2003 history even in block bootstraps, while the US
  market's post-2003 Sharpe ratio (0.68) was twice its earlier level, also unusual.

## Why it's in the library

It ties the factor-zoo literature to risk management. The multiple-testing argument
(Harvey–Liu–Zhu) explains part of the post-publication decay; this paper adds the
operational point that the drawdown and correlation risks of a factor book are much larger
than a normal model of the backtest says, and they arrive together in a crisis. The
authors' conclusion is balanced rather than dismissive: they read the post-2003 period as
partly data-mining and crowding, partly bad luck, and caution against both extrapolating
backtests and abandoning factors. It is argued from the authors' own factor construction,
and Research Affiliates sells factor products.

## Links

- [[harvey-liu-zhu-2016]] — the factor-zoo count and the higher t-statistic hurdle this paper
  builds on
- [[mclean-pontiff-2016]] — the post-publication decline in anomaly returns
- [[hou-xue-zhang-2020]] — most anomalies fail to replicate once microcaps are excluded
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] —
  setting trading rules without searching many backtests
- [[ang-chen-2002]] — correlations that rise in down markets, the same failure of
  diversification for stocks
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — strategies sized on calm-period
  statistics that fail together in a shock
- [[asness-et-al-2014-fact-fiction-and-momentum-investing]] — the case for momentum as a robust factor, from the people who run it
- [[blitz-2021-the-quant-crisis-of-2018-2020]] — the 2018–2020 factor drawdown, when diversifying across factors failed
- [[hoffstein-faber-braun-2020-rebalance-timing-luck-of-smart-beta]] — rebalance dates alone move factor-index returns by up to 2% a year
- [[khandani-lo-2011-what-happened-to-the-quants-in-august-2007]] — the 2007 quant meltdown as a case of crowded factor bets unwinding together
- [[rahelan-2019-taking-the-stag-out-of-stagflation]] — a factor-timing backtest whose regime predictor was chosen in-sample, an example of the problems described here
