# Gold and Geopolitical Risk

| | |
|---|---|
| **Authors** | Dirk G. Baur (University of Western Australia), Lee A. Smales (Curtin University) |
| **Year** | 2018 (January working paper, SSRN 3109136; published as "Hedging geopolitical risk with precious metals", *Journal of Banking & Finance* 117, 2020) |
| **Type** | Working paper, 25pp. Monthly data, January 1985 to November 2017 |
| **PDF** | Local copy only (SSRN working paper, no open licence) |
| **BibTeX** | `baur2018geopolitical` |
| **Status** | Reference: §3 (Tables 2–4: baseline, threats versus acts, high versus low risk) |

## What it is

A test of whether gold rises when geopolitical risk rises, as opposed to financial
stress, which is what most safe-haven studies measure.

- **The risk measure.** The Caldara–Iacoviello Geopolitical Risk (GPR) index counts
  articles about wars, terrorism and tensions between states in 11 major newspapers,
  scaled to 100 for 2000–2009. It peaked at 536 in March 2003 (the Iraq invasion). Two
  sub-indexes separate threats (war threats, nuclear tensions, terror threats) from acts
  (wars starting, attacks happening).
- **The test.** Monthly regressions of gold, silver, platinum, palladium, copper and S&P 500
  returns on the change in GPR, with credit spread, term spread and industrial production
  as controls.
- **Gold alone rises with geopolitical risk.** A one-standard-deviation rise in GPR goes
  with a 0.80% gold return in the same month. Silver, platinum and palladium show
  negative, insignificant coefficients; copper and stocks fall. Bitcoin's coefficient is
  positive but insignificant.
- **Threats, not acts.** Gold responds to rising geopolitical threats; actual events go
  with slightly negative gold returns, which the authors liken to "buy the rumour, sell the
  fact".
- **Concentrated in tense periods.** The relationship holds when GPR is in its top quintile
  and fades in calm periods. It is significant in every ten-year sub-sample but not in
  every five-year one; in 2005–2010, around the financial crisis, gold tracked the VIX
  rather than GPR.
- **Different from financial fear.** GPR still explains gold returns after adding the VIX.
  In an EGARCH model, geopolitical risk raises the volatility of the other metals and of
  stocks but not of gold.

## Why it's in the library

**It separates two reasons to hold gold.** Gold as a hedge against geopolitical shocks is
distinct from gold as a crisis asset when markets fall: the two respond to different
news, and in the 2008 sample the financial channel dominated.

**The effect is modest and monthly.** A 0.8% move per standard deviation of a newspaper
index, estimated on 33 years of monthly data, is evidence of a tendency, not a reliable
hedge for a particular event. Gold's response to realised events was, if anything,
negative.

## Links

- [[beber-et-al-2013-switching-risk-off-fx-correlations-and-risk-premia]] — risk-off episodes dated from FX correlation regimes, another way of measuring flight to safety
- [[cole-2018-what-is-water-in-markets]] — a manager's account of crisis behaviour across assets
- [[ang-chen-2002]] — asymmetric correlations: why an asset that diversifies in calm markets may not in a crash
- [[kaczmarek-et-al-2022-false-safe-haven-assets]] — gold fails as a safe haven inside a volatility-targeting strategy, 2010–2020
