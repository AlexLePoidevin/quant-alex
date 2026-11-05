# Understanding Momentum and Reversal

| | |
|---|---|
| **Authors** | Bryan T. Kelly (Yale; AQR), Tobias J. Moskowitz (Yale; AQR), Seth Pruitt (Arizona State) |
| **Year** | 2021 (*Journal of Financial Economics* 140(3), 726–743; this copy is the February 2021 preprint, SSRN 3610814) |
| **Type** | Journal article, 32pp. US stocks 1966–2014, 36 characteristics, 12,813 stocks |
| **PDF** | Local copy only (SSRN preprint of an Elsevier journal article, no open licence) |
| **BibTeX** | `kelly2021momentum` |
| **Status** | Reference: §2 (past returns predict betas), §4 (Tables 2–3, in- and out-of-sample) carry the results |

## What it is

A test of whether price momentum and long-term reversal are compensation for risk that
changes over time, rather than anomalies. The tool is instrumented PCA (IPCA), the
conditional factor model of Kelly, Pruitt and Su (2019), in which each stock's factor
loadings are a linear function of its observable characteristics, so loadings update as
characteristics change.

- **Step one: past returns predict future betas.** In stock-month panel regressions, the
  standard 12-to-2-month momentum signal predicts a stock's realised market beta over the
  next one to twelve months (coefficient 0.23, t ≈ 12). Moving from the 10th to the 90th
  momentum percentile raises market beta by about 0.18. Long-term reversal (3–5-year past
  return) predicts betas with about half the strength; short-term (one-month) reversal
  barely does, which the authors read as a liquidity effect rather than risk.
- **Why the conditional CAPM is not enough.** A 0.18 beta spread times a 6% market premium
  explains about 1.1 points of an 8–9% momentum premium. So the paper needs a multifactor
  conditional model.
- **The model.** Five latent IPCA factors, loadings driven by the 36 characteristics
  (including momentum and reversal themselves). Expected returns are β′λ: exposures times
  factor premia.
- **Main result.** Classic quintile momentum earns 8.3% a year (t = 3.3, Sharpe 0.48).
  Its alpha against the static Fama–French five factors is 9.2% (t = 3.0); against the
  dynamic IPCA factors it is −3.2% (t = −1.2). "Residual" momentum, sorted only on the
  part of past returns the conditional factors don't explain, earns a marginal 4.4%.
- **Prediction.** Stock-level monthly predictive R² is 0.02% from momentum, 0.01% from
  long-term reversal and 0.32% from the model's expected return. Adding momentum to the
  model adds nothing (joint R² 0.32%); momentum's coefficient loses significance and can
  flip sign.
- **Out of sample.** Re-estimating the model each month on an expanding window from 1971,
  the out-of-sample R² is 0.28%. A long-short quintile sort on the model's expected returns
  earns 30.9% a year with a Sharpe ratio of 2.29, against 33.6% and 2.39 in sample. These
  are gross returns from a 36-characteristic model, before trading costs.
- **Against Grundy and Martin (2001).** That paper found momentum lives in residual
  returns. Kelly, Moskowitz and Pruitt argue this came from slow rolling betas on
  misspecified factors, which push the time-varying risk premium into the residual.

## Why it's in the library

**It gives momentum a risk-based reading.** Stocks that have trended up carry more exposure
to priced factors over the following year, and a model whose betas move with
characteristics prices most of the momentum and long-term reversal spread. Whether that
is "risk" in an economic sense is left open: the latent factors are not named.

**It is the applied companion to IPCA.** Where Kelly, Pruitt and Su set out the method,
this paper uses it to dissolve one of the best-known anomalies, and shows why conditional
betas matter: the identity of top and bottom momentum stocks turns over about 38% a month,
which static betas cannot follow.

**The trading numbers need context.** A 2.3 Sharpe ratio from a model-based sort is a
statement about what the 36 characteristics jointly predict, gross of costs and with
heavy turnover. The paper's point is explanatory, not a strategy claim.

## Links

- [[kelly-pruitt-su-2019]] — the IPCA method this paper applies
- [[gu-kelly-xiu-2021]] — the nonlinear (autoencoder) extension of conditional latent-factor models
- [[carhart-1997]] — the momentum factor added to Fama–French
- [[fama-french-2015]] — the static five-factor model that leaves momentum's 9.2% alpha unexplained
- [[harvey-liu-zhu-2016]] — why a factor's t-statistic needs a higher bar after decades of searching
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — trend following in the time series rather than the cross-section, derived from a bull/bear model
- [[asness-et-al-2014-fact-fiction-and-momentum-investing]] — the evidence on momentum's size, long and short legs, costs and crashes
- [[blitz-huij-martens-2011-residual-momentum]] — stripping momentum's time-varying factor exposures out of the signal itself
- [[geczy-samonov-2017-two-centuries-of-multi-asset-momentum]] — momentum and long-run reversal across six asset classes since 1800, with betas that swing with the market state
- [[medhat-schmeling-2022-short-term-momentum]] — momentum at the one-month horizon among high-turnover stocks
