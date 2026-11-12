# Stock Volatility Predictability in Bull and Bear Markets

| | |
|---|---|
| **Authors** | Xingyi Li and Valeriy Zakamulin (University of Agder) |
| **Year** | 2020 (working paper dated April 2019) |
| **Type** | Journal article, *Quantitative Finance* 20(7), 1149–1167 (doi 10.1080/14697688.2020.1725101). The copy is the SSRN working paper (3370828), 35pp. Five-minute prices on 31 Dow stocks, 1998–2016 |
| **PDF** | Not hosted in this repository (SSRN version of a Taylor & Francis article, no open licence) |
| **Find it** | [doi.org/10.1080/14697688.2020.1725101](https://doi.org/10.1080/14697688.2020.1725101) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Stock+Volatility+Predictability+in+Bull+and+Bear+Markets%22+Li) |
| **BibTeX** | `li2020volbullbear` |
| **Status** | Reference: §2.2 (dating bull and bear markets), §3 and the conclusions carry the results |

## What it is

A test of whether volatility is easier to forecast in bear markets than in bull markets, in
the same way that recent work finds stock returns most predictable in bad times.

- **Data.** Five-minute prices for 31 current or former Dow Jones stocks with full histories
  from January 1998 to December 2016, used to build daily realised volatility. Bull and bear
  states of the S&P 500 are dated with two turning-point rules: Pagan and Sossounov's
  business-cycle-style algorithm, and Lunde and Timmermann's rule that a move of a set size
  (for example 20%) from the last peak or trough switches the state.
- **Models.** Four forecasting models, from simple to rich: EWMA (RiskMetrics) and GARCH(1,1)
  on daily returns, and HAR-RV and Realized GARCH, which also use the intraday realised
  volatility. Forecasts of weekly volatility are made out to 60 weeks ahead, and results for
  the 31 stocks are pooled ("meta-analysis") rather than reported stock by stock.
- **Findings.**
  - The forecast horizon, how far ahead a model still beats the historical mean, is much
    longer in bear states: beyond 60 weeks with high-frequency data, against about 12 weeks
    in bull states.
  - Accuracy is highest at the shortest horizon (about 75% of the variation explained) and
    decays with horizon, much faster in bull states.
  - Intraday data improve accuracy by almost 20% at the shortest horizon. In bull states the
    gain fades quickly with horizon; in bear states it persists.
  - Bias depends on the state. In bull markets every model overestimates future volatility,
    more so at longer horizons. In bear markets short-horizon forecasts underestimate it and
    long-horizon forecasts tend to overestimate it.

## Why it's in the library

It ties a practical quantity, how far ahead risk can be forecast, to the bull/bear state of
the market: volatility forecasts are most useful exactly in the turbulent periods when they
are most needed, and models fitted on calm data will overstate risk in calm markets.

Two caveats. The states are dated with turning-point algorithms that use the whole price
history, so a "bear state" is known only after the fact; the paper argues these states can be
identified in real time or with a small lag but does not test forecasts conditioned on states
known at the time. And accuracy is measured as the share of volatility variation explained
within each state, which naturally favours high-volatility, persistent periods such as bear
markets. The results are on 31 large US stocks over one 19-year sample.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — a four-state model of
  bull and bear markets, cited here as the alternative to turning-point dating
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — the same
  author's bull/bear switching model applied to trend following
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — regime switching in the level of
  implied volatility
- [[carr-wu-zhang-2019-using-machine-learning-to-predict-realized-variance]] — forecasting
  realised variance from option prices instead of from past volatility
- [[romero-2016-microstructure-noise-two-scales-realized-volatility]] — the measurement
  problems in realised volatility from intraday prices
