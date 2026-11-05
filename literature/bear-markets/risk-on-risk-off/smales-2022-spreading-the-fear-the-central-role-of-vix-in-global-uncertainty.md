# Spreading the Fear: The Central Role of CBOE VIX in Global Stock Market Uncertainty

| | |
|---|---|
| **Authors** | Lee A. Smales (University of Western Australia) |
| **Year** | 2022 (*Global Finance Journal* 51, 100679); the copy is the SSRN working paper dated 29 March 2021 |
| **Type** | Empirical paper, 33pp. Daily implied-volatility indices for the G7 (2001–2020) and BRICS (2011–2019) |
| **PDF** | Local copy only (SSRN working paper; the journal version is Elsevier) |
| **BibTeX** | `smales2022fear` |
| **Status** | Reference: Table 2 (correlations by regime), Tables 3–4 (VAR and variance decomposition), Table 7 (Granger causality), Table 8 (principal components) |

## What it is

A study of how stock-market "fear" moves between countries, measured by each market's
implied-volatility index: VIX (US), VDAX (Germany), VCAC (France), VFTSE (UK), VXJ (Japan), plus
Canada and Italy on shorter samples, and Brazil, China, India and South Africa from 2011.

- **Correlations rise in bad times.** Average pairwise correlation of daily changes is 0.395
  over 2001–2020, 0.507 in NBER recessions and 0.600 in the COVID crisis (0.826 among the
  European indices). A rolling one-year average moves between about 0.30 and 0.60.
- **Fear flows out of the US, not into it.** In a VAR of daily percentage changes, lagged VIX
  changes predict every other index for at least two days, and Granger causality runs one
  way. VIX innovations explain 16% (France) to 34% (Germany) of the forecast variance of the
  other indices; no other market explains more than 0.1% of the VIX. European indices
  influence each other in both directions.
- **The two crises differ.** The VIX coefficient on other markets rises from 0.19 on average
  to 0.43 in the GFC and 0.38 in COVID. In the GFC the extra comovement comes from the US; in
  COVID it is spread more widely, especially within Europe.
- **Common factor.** The first principal component explains 56.8% of G7 implied-volatility
  changes over the full sample, and about 5 points more in each crisis.
- **Emerging markets.** The VIX also leads the BRICS indices, explaining about 22% of their
  variance on average. The Brazil and China indices are built from US-listed ETFs, which the
  author notes makes them hard to interpret.

## Why it's in the library

It documents the basic shape of risk-off episodes in volatility terms: when fear rises,
markets move together, and the US VIX is the first mover. That is the reason the VIX can stand
in for global risk appetite in many risk-on/risk-off measures, and why international
diversification gives least protection when it is needed.

One caution on the main result: closing times differ. The US closes after Europe, so news that
moves the VIX in the US afternoon can only reach European indices the next day. That alone
would make lagged VIX changes "predict" Europe, and Europe not predict the VIX. The paper shifts
Japan and India by a day for this but not Europe, arguing that most macro news arrives while
both are open. The one-way direction is therefore partly a timing effect, though the size of
the US share in the variance decomposition is still informative.

## Links

- [[hartmann-straetmans-de-vries-2004-asset-market-linkages-in-crisis-periods]] — crash
  co-movement across stock and bond markets measured with extreme-value methods
- [[ang-chen-2002]] — correlations between stocks rise in down markets
- [[beber-et-al-2013-switching-risk-off-fx-correlations-and-risk-premia]] — risk-off episodes
  dated from switches in FX correlation regimes
- [[caporale-et-al-2018-is-market-fear-persistent]] — whether the VIX itself has memory, and
  how that changes in a crisis
- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — how the VIX is
  computed
