# Coronavirus: Impact on Stock Prices and Growth Expectations

| | |
|---|---|
| **Authors** | Niels J. Gormsen; Ralph S. J. Koijen (University of Chicago Booth) |
| **Year** | 2020 (this version 3 August 2020; published *Review of Asset Pricing Studies* 10(4), 574–597) |
| **Type** | Paper, 34pp. S&P 500, Euro Stoxx 50 and Nikkei 225 stock and dividend futures prices, 1 January to 20 July 2020, with a comparison to the 2008 crisis |
| **PDF** | Not hosted in this repository (working-paper version of a journal article, no open licence) |
| **Find it** | [doi.org/10.1093/rapstu/raaa013](https://doi.org/10.1093/rapstu/raaa013) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Coronavirus%3A+Impact+on+Stock+Prices+and+Growth+Expectations%22+Gormsen) |
| **BibTeX** | `gormsen2020coronavirus` |
| **Status** | Reference: §2–3 (dividend futures and the lower bound), §4 (GDP mapping) and §5 (splitting the stock-market fall into near and distant dividends) |

## What it is

A real-time reading of the COVID-19 crash that uses dividend futures to separate what
investors expected to happen to growth from what happened to discount rates.

- **The problem.** A stock index is the discounted value of all future dividends. A 30%
  fall could mean dividends will be much lower, or that investors now demand a higher
  return. The first 10 years of dividends are only about 20% of the S&P 500's value, so
  a 30% fall caused by growth alone would require either no dividends for a decade or a
  permanent 30% cut. Most of a market move is usually discount-rate news (Shiller;
  Campbell and Shiller).
- **The tool.** Dividend futures pay the index's dividends for a single calendar year,
  so they price each year's dividends separately, out to about 7–10 years. Their price
  falls either because expected dividends for that year fall or because the required
  excess return rises.
- **A lower bound on growth revisions.** If the required excess return has not fallen
  since 1 January, the percentage fall in a dividend future is a lower bound on the
  revision to expected dividends for that year. The bound is model-free: it uses only
  market prices. At its worst it shows dividends revised down by as much as 17% in the
  US and Japan and 28% in the EU at the two-year horizon, with the EU and Japanese curves
  rising again at longer horizons (catch-up growth). In the 2008 crisis the same bound,
  measured July–November 2008, turned out to be close to the dividends actually paid.
- **A point estimate.** A regression of realised dividend growth on the two-year
  "equity yield" from dividend futures (fitted on 2006–2017, R² 0.58) turns prices into
  forecasts. By 20 July 2020 expected dividend growth over the next year was down 8% in
  the US and Japan and 14% in the EU relative to 1 January. Mapped to GDP with a
  regression fitted on below-average-growth periods (dividends move about four times as
  much as GDP in downturns), expected GDP growth was down about 2% in the US and Japan
  and 3% in the EU, from troughs of roughly 6%, 5% and 8% at the end of March.
- **What moved the stock market.** From the 19 February peak to 5 March the index fell
  while near-dated dividend futures barely moved, so the fall came from distant
  dividends, which the authors attribute to higher discount rates. The 24 March
  fiscal-stimulus news lifted stocks about 10% in a week while short-dated dividend
  futures slightly *fell*: the rally came from long-dated value, not near-term cash
  flows. By 20 July the S&P 500 was $135 below its peak, of which $112 is explained by
  lower values for the first 10 years of dividends; the distant dividends were roughly
  back to their pre-crisis value.
- **Liquidity check.** Euro Stoxx 50 dividend futures volume rose to about 100,000
  contracts a day at the peak (from about 20,000 in 2019) and the bid-ask spread on the
  2021 contract averaged 0.27%, so the prices were not artefacts of a frozen market.

## Why it's in the library

**It is a clean case study of what drives a crash.** The shock had a known cause and an
expected short duration, which makes it unusually easy to read the market's
reaction. The result matches the long-standing finding that most index movement is
discount-rate news: the first leg down and most of the recovery happened in the value of
dividends far in the future, while near-term dividend expectations moved more slowly and
less.

**Dividend futures are a useful extra signal in a selloff.** They give a term structure
of growth expectations by horizon, updated daily, which equity prices alone cannot. The
lower bound needs only the assumption that risk premia did not fall, which is safe in a
crash.

**Its limits.** The point estimates rely on a forecasting regression fitted on about a
decade of data and on a US-estimated mapping from dividends to GDP applied to all three
regions; the authors warn the relationship may not hold in an unprecedented episode.
Payout restrictions on firms receiving government support could also depress dividends
without signalling weaker growth.

## Links

- [[campbell-1991]] — the variance decomposition behind the claim that most stock-market moves are discount-rate news, not cash-flow news
- [[lipton-lopez-de-prado-2020-three-quant-lessons-from-covid-19]] — another view of the same crash, from the quant-model side
- [[conlon-mcgee-2020-safe-haven-or-risky-hazard-bitcoin-during-the-covid-19-bear-market]] — Bitcoin fell with stocks in the same crash and raised portfolio tail risk
