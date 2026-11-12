# Heterogeneous Expectations in Asset Pricing: Empirical Evidence from the S&P500

| | |
|---|---|
| **Authors** | Carl Chiarella, Xue-Zhong He (University of Technology Sydney), Remco C.J. Zwinkels (Erasmus University Rotterdam) |
| **Year** | 2014 (Journal of Economic Behavior & Organization 105, 1–16); the copy here is the accepted manuscript |
| **Type** | Empirical paper (estimated heterogeneous agent model) |
| **PDF** | Not hosted in this repository (Elsevier accepted manuscript) |
| **Find it** | [doi.org/10.1016/j.jebo.2014.03.003](https://doi.org/10.1016/j.jebo.2014.03.003) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Heterogeneous+Expectations+in+Asset+Pricing%3A+Empirical+Evidence+from+the+S%26P500%22+Chiarella) |
| **BibTeX** | `chiarella2014heterogeneous` |
| **Status** | Reference: §2 (model), §4 (Tables 2–4, estimates) and §5 (simulations) |

## What it is

An attempt to estimate, rather than simulate, a model in which the market is made of two
kinds of boundedly rational traders, and to see whether it can produce bubbles like the
late-1990s IT bubble.

- **The model.** Fundamentalists expect the price to revert to a fundamental value;
  chartists extrapolate the gap between the price and a slow moving average (a geometric
  decay of past prices). A market maker moves the price in response to excess demand. Each
  month traders switch towards whichever rule has been more profitable, with an "intensity
  of choice" parameter governing how fast.
- **Data.** Monthly S&P 500 prices and earnings, January 1970 to October 2012 (502 months
  used). The fundamental value is built from earnings and an expected earnings yield; the
  index sits close to it until 1995, far above it through the IT bubble, and below it at
  the end of the sample.
- **Estimates (quasi-maximum likelihood).** Prices revert to fundamental at about 3.0% a
  month; chartists extrapolate the gap to their moving average at about 5.1% a month, with
  long memory (decay 0.92). Allowing switching improves the likelihood significantly over
  fixed shares, and without switching the chartist term is no longer significant. The
  intensity-of-choice parameter itself is not significantly different from zero, which the
  authors attribute to the tanh switching function.
- **Simulations.** Without noise the estimated system is stable and converges. With noise of
  the estimated size it produces long-lasting deviations from fundamental (up to about a
  hundred periods), with the market share swinging between the two groups.

## Why it's in the library

**It gives the fads-and-feedback story an estimated form.** Bubbles here come from traders
moving towards trend-following after it has paid, not from rational speculation, and the
model reproduces long, large departures from fundamental value.

**The evidence is in-sample and model-dependent.** The fundamental value is the authors'
construction, the switching parameter is not significant on its own, and the authors note
that a simpler statistical model might fit as well. It shows the model is consistent with
the data, not that it is the right one.

## Links

- [[west-1988-bubbles-fads-and-stock-price-volatility-tests]] — the fads explanation of excess volatility this paper tries to estimate
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — the moving-average trend rule from the trader's side
- [[sarkissian-2019-statistical-mechanics-of-price-stabilization-and-destabilization]] — another model where feedback in order flow turns small moves into crashes
- [[schatz-sornette-2020-inefficient-bubbles-and-efficient-drawdowns]] — positive-feedback bubbles that end in a drawdown
- [[cividino-westphal-sornette-2023-multiasset-financial-bubbles-in-an-agent-based-model]] — a simulated many-stock version of the fundamentalist-versus-trend-follower market, where rebalancing spreads bubbles between assets
