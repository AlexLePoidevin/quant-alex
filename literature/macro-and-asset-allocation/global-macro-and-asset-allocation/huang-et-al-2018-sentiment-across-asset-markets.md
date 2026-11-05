# Sentiment Across Asset Markets

| | |
|---|---|
| **Authors** | Dashan Huang (Singapore Management University), Heikki Lehkonen (University of Jyväskylä), Kuntara Pukthuanthong (University of Missouri), Guofu Zhou (Washington University in St. Louis) |
| **Year** | 2018 (draft of 20 June 2018; first draft October 2017) |
| **Type** | Working paper, SSRN 3185140, 45pp. Monthly US data, January 1998 to December 2016 |
| **PDF** | Local copy only (SSRN working paper, no licence) |
| **BibTeX** | `huang2018sentiment` |
| **Status** | Reference: §3.1 (the sentiment data), §4.1–4.3 (own-market, cross-market and PLS regressions) and §4.5 (hard-to-value portfolios) carry the results |

## What it is

A study of news- and social-media sentiment in five US markets at once (stocks, bonds,
commodities, the dollar and housing), asking whether each market's sentiment predicts its
own next-month return, and whether sentiment spills across markets.

- **The data.** Thomson Reuters MarketPsych Indices: daily scores from thousands of news and
  social-media sources, built as positive minus negative weighted terms, with a separate
  lexicon per asset class. Stocks use the average across S&P 500 constituents; commodities
  an equal weight across the 17 components of the Thomson Reuters commodity index. The
  paper also "filters" each series by regressing out five macro variables (dividend–price
  ratio, dividend payout, the T-bill rate, the VIX and economic-policy uncertainty) and
  mostly uses the residual.
- **Own-market predictability.** A one-standard-deviation rise in filtered sentiment
  predicts the next month's excess return:
  - **up** for stocks (+0.62%), commodities (+1.22%) and housing (+0.09%);
  - **down** for bonds (−0.10%) and the dollar (−0.24%).

  In-sample R² is 8.6% for commodities and 1.4–2.2% for the rest. For stocks, the news
  measure stays significant alongside the Baker–Wurgler sentiment index, so it carries
  different information.
- **Spillovers.**
  - **Stocks:** in a regression with all five sentiments, stock returns load on stock, bond
    and commodity sentiment, and R² rises from 2.0% to 5.4%.
  - **Dollar:** its sentiment loses significance once stock or housing sentiment is
    included; the three are highly correlated, with stock–housing sentiment at about 0.7.
  - **Housing:** stock and housing sentiment predict each other in Granger tests. Housing
    returns respond to stock and bond sentiment.
- **Combining markets.** Partial least squares builds a market-specific index from all five
  sentiments. It raises predictive power for every market: by 32 basis points of monthly
  return for stocks, and less for the others. A single first principal component across
  markets does worse, and flips sign for commodities, which the authors read as commodity
  sentiment being segmented.
- **Horizons.** Stock sentiment predicts returns for up to six months, then reverses in the
  second year. Housing and commodity effects last six months with no reversal. With the
  combined index, dollar and housing predictability lasts about two years.
- **Validation.** Consistent with the idea that hard-to-value assets are more exposed to
  sentiment, the effects are strongest in high-beta stocks, long-maturity bonds (30-year
  returns fall 0.73% per standard deviation, about nine times the 2-year effect) and
  high-interest-rate currencies.

## Why it's in the library

**It treats sentiment as a cross-asset state variable.** Risk-on and risk-off moods move
stocks, the dollar, commodities and housing together, and this paper measures that from
text rather than from prices. The finding that bond and dollar sentiment predict returns
with the opposite sign to stocks fits the safe-haven pattern elsewhere in this section.

**Read it as a first pass.** It is a working paper, the sample is 19 years of monthly data,
and the effects are small, around 1–2% R² outside commodities. The PLS index is estimated
on the same sample it is evaluated on. The paper reports out-of-sample R² statistics
without fully describing the procedure. The measure is a commercial dataset, so the
results can't be checked without it.

## Links

- [[smales-2016-risk-on-risk-off-financial-market-response-to-investor-fear]] — how stocks, bonds and currencies respond to fear measured by the VIX
- [[kinlaw-turkington-2014-correlation-surprise]] — another way to read cross-asset risk-on/risk-off states, from returns rather than text
- [[stockl-kaiser-2020-higher-moments-matter]] — another cross-sectional state variable used to forecast the equity premium
- [[bekaert-hoerova-lo-duca-2013-risk-uncertainty-and-monetary-policy]] — risk appetite measured from the VIX, and how monetary policy moves it
