# Intraday Market Predictability: A Machine Learning Approach

| | |
|---|---|
| **Authors** | Dillon Huddleston, Fred Liu and Lars Stentoft (University of Western Ontario) |
| **Year** | 2021 (working paper dated 16 February 2021; published in *Journal of Financial Econometrics* 21(2), 485–527, 2023) |
| **Type** | Working paper, 56pp. TAQ five-minute data, February 1993–October 2016 |
| **PDF** | Not hosted in this repository (SSRN 3726765 working paper; journal version © Oxford University Press) |
| **Find it** | [doi.org/10.1093/jjfinec/nbab007](https://doi.org/10.1093/jjfinec/nbab007) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Intraday+Market+Predictability%3A+A+Machine+Learning+Approach%22+Huddleston) |
| **BibTeX** | `huddleston2021intraday` |
| **Status** | Reference: §3 (out-of-sample R², strategy returns with and without costs) and §4 (time of day, volatility, crises, AR benchmarks) carry the results |

## What it is

Can the next five-minute return of the S&P 500 (proxied by SPY) be predicted from the
previous five-minute returns of SPY and its 500 constituents? The authors fit lasso, elastic
net, principal component regression, random forest, gradient-boosted trees, a neural
network, and the mean and median of these, on an expanding window, retrained through the
sample. Opening and closing intervals are excluded from evaluation.

- **Statistical fit.** Out-of-sample R² reaches about 2.0% for lasso, elastic net and the
  ensembles over 1993–2016, but most of it comes from before decimalisation (1993–2000).
  It is about 1% in 2001–04 and much smaller, though still positive for some models, in
  2005–16.
- **Before costs.** A strategy that goes long or short SPY on the sign of each forecast
  earns very large gross returns (around 190–205% a year, Sharpe 2.7–2.9, for the best
  models), again concentrated pre-2001.
- **After costs.** Trading only when the forecast exceeds the quoted NBBO spread, the
  ensemble median reaches a Sharpe ratio of 0.98 over the full sample against 0.48 for
  buying SPY. In 2005–16 PCR and random forest earn 9% and 8% a year (Sharpe 0.88 and 0.81)
  and the median ensemble 0.68, against 0.46 for SPY.
- **Where it comes from.** Predictability is higher in the middle of the day, when markets
  are volatile or illiquid, and in the 2008 and euro-debt crises, which the authors read as
  slow-moving capital. Constituent returns beat autoregressive models on SPY's own lags, and
  adding characteristics such as momentum, volatility or spreads mostly makes forecasts worse.

## Why it's in the library

It is a careful large-scale test of short-horizon predictability with an honest
breakdown by period. The headline numbers are dominated by the eighths-and-sixteenths tick
era; what is left in the modern market is a thin edge that survives the quoted spread in
some models. The finding that the cross-section of constituents carries information the
index's own past returns do not is the part most relevant to building short-horizon signals.

Costs are the quoted spread only, with no market impact, latency or fees, and hyperparameters
are tuned on a validation set within the same history.

## Links

- [[gu-kelly-xiu-2021]] — the same set of machine-learning models applied to monthly
  stock returns
- [[boyarchenko-larsen-whelan-2023-the-overnight-drift]] — another intraday return pattern
  in index futures, and how much of it survives the spread
- [[collin-dufresne-daniel-2015-liquidity-and-return-reversals]] — short-horizon price
  pressure and reversal in large stocks
- [[romero-2016-microstructure-noise-two-scales-realized-volatility]] — why bid-ask noise
  dominates very short returns, the problem the cost filter here addresses
