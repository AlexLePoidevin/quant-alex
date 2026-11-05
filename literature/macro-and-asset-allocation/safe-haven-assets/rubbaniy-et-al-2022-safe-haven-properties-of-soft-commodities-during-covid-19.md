# Safe-Haven Properties of Soft Commodities During Times of Covid-19

| | |
|---|---|
| **Authors** | Ghulame Rubbaniy, Konstantinos Syriopoulos, Aristeidis Samitas (Zayed University), Ali Awais Khalid (University of Lahore) |
| **Year** | 2022. The copy is the SSRN preprint (3740588, file dated May 2021, marked as not peer reviewed); published in *Journal of Commodity Markets* 27 (2022), 100223 |
| **Type** | Working paper, 35pp. Daily data, 27 January to 3 September 2020 |
| **PDF** | Local copy only (SSRN preprint, no open licence) |
| **BibTeX** | `rubbaniy2022soft` |
| **Status** | Reference: §2.2 (the fear index) and §3 with Figures 2–13 (the wavelet coherence plots) carry the results |

## What it is

A test of whether six soft commodities (wheat, corn, cotton, cocoa, coffee and sugar), spot
and futures, held their value as COVID-19 fear rose in 2020.

- **The fear measure.** The Global COVID-19 Fear Index of Salisu and Akanni averages a cases
  index and a deaths index. Each compares the current global count with the count 14 days
  earlier: current ÷ (current + 14-day-lagged) × 100. Higher values mean the pandemic is
  growing faster.
- **Method.** Wavelet coherence between each commodity price and the fear index, which shows
  where in time and at which cycle length (from a few days to about two months) the two move
  together. Arrows show whether they move together or in opposite directions, and which
  leads. Significance comes from Monte Carlo simulation. The sample is 159 daily
  observations.
- **Spot prices.** Wheat, corn, cotton and cocoa move with the fear index in the first months
  (wheat for about 60 days, corn about 70, cotton about 30), turning negative later. Coffee is
  weakly negative and sugar clearly negative.
- **Futures.** Corn, cotton and cocoa futures move with the fear index. Wheat futures move
  against it, unlike wheat spot. Sugar futures move against it.
- **The authors' reading.** Staple foods are safe havens during a pandemic because of
  hoarding and steady demand. Coffee and sugar are not, which they attribute to closed
  restaurants and consumers switching to healthier food.

## Why it's in the library

**It is an example of how loosely "safe haven" is used.** The usual definition is an asset
that holds its value when stocks fall. This paper never uses stock market data: it measures
co-movement with a pandemic-growth index and then recommends the commodities to equity
investors. That gap is the main thing to take from it.

**As data, it says staple prices held up in early 2020.** That is a narrow, descriptive
result for one episode.

**The results are inconsistent.** Wheat spot is called a haven while wheat futures move the
other way. Coffee futures are called a haven though the authors describe their co-movement
as weak. The text discusses days 150 to 169 of a 159-observation sample. The explanations
(immunity diets, chocolate for well-being) are asserted, not tested. And wavelet coherence
on price levels over seven months has very few cycles to estimate the longer horizons from.

## Links

- [[baur-mcdermott-2013-financial-turmoil-and-safe-haven-assets]] — safe havens defined by
  how they behave on the worst stock market days, the test this paper does not run
- [[baur-dimpfl-2022-a-safe-haven-index]] — a benchmark for safe havens built from gold,
  currencies and government bonds
- [[ji-zhang-zhao-2020-searching-for-safe-haven-assets-during-covid-19]] — safe havens in the
  COVID crash tested directly against stock market losses
- [[kay-et-al-2012-building-a-better-commodities-portfolio]] — how to hold commodities as an
  asset class, rather than a single commodity on a story
- [[gormsen-koijen-2020-coronavirus-impact-on-stock-prices-and-growth-expectations]] — what
  the COVID crash did to stock prices and growth expectations
