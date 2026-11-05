# Testing for Asset Price Bubbles Using Options Data

| | |
|---|---|
| **Authors** | Nicola Fusari (Johns Hopkins), Robert Jarrow (Cornell, Kamakura), Sujan Lamichhane (IMF) |
| **Year** | 2025 (Journal of Business & Economic Statistics 43(4), 807–821); the copy here is the working paper, first version August 2020, updated May 2022 (SSRN 3670999) |
| **Type** | Working paper (option pricing, empirical), 57pp |
| **PDF** | Local copy only (SSRN working paper; the journal version is Taylor & Francis) |
| **BibTeX** | `fusari2025options` |
| **Status** | Reference: §2 (why puts and calls price bubbles differently), §3.3–3.4 (the estimator and test), Table 3, and §6 (dot-com and GameStop) |

## What it is

A way to detect a bubble in a stock or index from a single day's option prices, with no
price history needed.

- **The theory.** In the "local martingale" theory of bubbles (Jarrow, Protter and
  Shimbo), an asset has a bubble when its discounted price is a strict local martingale
  under the risk-neutral measure: the price is above the expected discounted value of its
  cash flows. In that case put options are still priced at their risk-neutral value, but
  call options can carry a bubble of their own. If put–call parity holds, the call's
  bubble is linked to the stock's bubble and gives a lower bound on it.
- **The procedure.** Each day, for each asset:
  1. fit a flexible stochastic-volatility-with-jumps model (the "G-SVJD", which nests
     Merton, Heston and Bates and allows strict local martingales) to *put* prices only;
  2. use the fitted model to price the calls;
  3. the call bubble is market price minus model price, averaged across strikes and
     expressed as a percentage of the stock price. It is set to zero whenever the model
     price falls inside the bid–ask spread.
- **The test.** Bubbles cannot be negative in this theory, so negative estimates are
  treated as pure noise. Their spread over the previous 180 days sets a threshold of
  1.65 standard deviations, and a bubble is significant above it.
- **Results, 2014–2018 (OptionMetrics, 7–50-day options).**
  - **Model fit.** Put-pricing errors are small: about 0.5–0.6 implied-volatility points
    for the S&P 500 and Nasdaq-100, about 1 point for Amazon and Facebook.
  - **The indexes.** Significant call bubbles appear on under 1% of days for the S&P 500
    and Nasdaq-100.
  - **The two stocks.** Amazon and Facebook show them on roughly 5–8% of days, clustered
    in mid-2015 to early 2016 and in 2018, typically 10–20 basis points of the stock
    price.
  - **What goes with a bubble.** Estimated bubbles rise with risk-neutral volatility
    (correlation about 0.55–0.58) and with trading volume, and are larger in the two
    weeks before earnings announcements.
- **Big rallies are not bubbles here.** Amazon rose more than 140% and Facebook nearly
  100% between early 2016 and late 2017 with few significant bubble days. In this theory,
  a bubble needs volatility to rise faster than the price, not just a fast rise.
- **Case studies.** The Nasdaq-100 shows a persistent, significant bubble from March 2000
  through 2001, fading in 2002. GameStop shows significant bubbles from mid-December 2020,
  when the stock was still under $15, rising in late January 2021 to a lower bound of
  more than 1.5% of the share price.

## Why it's in the library

**It is forward-looking and needs no long history.** Price-based tests such as PSY need
years of data to spot an explosive path. This method reads the market's own pricing of
upside and downside on a given day, so in principle it can flag a bubble as it forms.

**It separates "it went up a lot" from "it's a bubble".** The finding that big rallies in
Amazon, Facebook and the indexes did not show up as bubbles is a useful corrective to
calling every strong rally a bubble.

**The caveats are substantial:**

- **Model risk.** The bubble is the gap between market call prices and a model fitted to
  puts, so any misfit of the model shows up as a "bubble". Treating negative estimates as noise
  and the bid–ask filter help, but cannot rule this out. The individual parameters, which
  determine whether the model is a strict local martingale at all, have large standard
  errors.
- **The flag rate.** A 1.65-standard-deviation threshold would flag about 5% of days by
  chance if the errors were normal. The 5–8% for the two stocks is not far above that.
  The indexes' rate of under 1% suggests the threshold is conservative there.
- **Put–call parity.** The link from a call bubble to a stock bubble assumes put–call
  parity holds. Short-sale costs and early exercise of American options can break it, and
  the paper argues these effects make the test more conservative.
- **"Real time" in principle only.** Estimating one asset on one day took between two and
  16 hours on the authors' hardware.

## Links

- [[bashchenko-marchal-2020-deep-learning-for-asset-bubbles-detection]] — the same strict-local-martingale definition of a bubble, detected with a neural network on prices instead of options
- [[jarrow-1992-market-manipulation-bubbles-corners-and-short-squeezes]] — Jarrow's earlier work on how large traders can create price paths that look like bubbles
- [[phillips-shi-2018-real-time-monitoring-of-asset-markets-bubbles-and-crises]] — the main price-based alternative
- [[merton-1976]] — the jump-diffusion model nested in the paper's option-pricing model
- [[bakshi-madan-panayotov-2015-heterogeneity-in-beliefs-and-volatility-tail-behavior]] — another paper that uses option prices to read investors' disagreement
- [[barbon-buraschi-2021-gamma-fragility]] — option-market positioning and its effect on the underlying, relevant to the GameStop episode
