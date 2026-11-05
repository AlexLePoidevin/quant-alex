# The Effectiveness of Asset Classes in Hedging Risk

| | |
|---|---|
| **Authors** | Luis Garcia-Feijoo (Florida Atlantic University), Gerald R. Jensen (Northern Illinois University), Robert R. Johnson |
| **Year** | 2012 (*Journal of Portfolio Management* 38(3), 40–55, Spring 2012) |
| **Type** | Journal article, 16pp. Monthly total returns, January 1970 – December 2010 |
| **PDF** | Local copy only (JPM download, Institutional Investor copyright) |
| **BibTeX** | `garciafeijoo2012hedging` |
| **Status** | Reference: Exhibits 4–5 (extreme equity months), 6–7 (extreme bond months) and 9 (inflationary environments) carry the results |

## What it is

A 41-year comparison of which asset classes protect US equity and bond portfolios, both in
normal months and in the worst months.

- **Assets.** US equities (CRSP value-weighted), the US Aggregate bond index, NAREIT (all,
  mortgage and hybrid REITs), developed (EAFE) and emerging equities, the GSCI and its five
  components (energy, industrial metals, precious metals, agriculture, livestock), and
  T-bills.
- **Method.** Regress each asset's monthly return on equity (or bond) returns plus dummies
  for the top and bottom 5% equity (or bond) months, and count how often each asset has a
  bottom-5% month at the same time.
- **Bonds are the hedge.** Bonds have a weak normal-times link to equities (beta 0.12) and
  do unusually well in the worst equity months (bottom-5% coefficient 1.08). They fall
  into their own bottom 5% in only 5% of the worst equity months, the lowest of any asset.
  The result holds in both halves of the sample and in both inflation regimes.
- **Gold helps; energy hurts.** Gold co-crashed in about 10% of the worst equity months, and
  commodities overall in under 30%. But energy, and so the energy-heavy GSCI, tends to fall
  sharply in extreme equity months (not significant, but large on average): it would have
  compounded a crash. Precious metals, agriculture and industrial metals offset extreme
  moves on average. Industrial metals are the most correlated with equities.
- **Real estate and foreign equities do not hedge.** REIT betas to equities are 0.59–0.68,
  and NAREIT returns are about 3.5% below normal in extreme down months. Foreign equities
  and REITs each co-crash more than 40% of the time; EAFE in 65% of the worst US months.
- **Inflation regimes.** Using an ex ante classification of Fed policy (tightening as
  inflationary, easing as not), commodities hedge equities much better in inflationary
  periods, especially energy and precious metals. Precious metals are the most consistent
  across regimes.
- **For bond investors.** Commodities are uncorrelated with bonds normally but tend to fall
  in extreme bond months; T-bills do well in extreme bond months.

## Why it's in the library

- **A long-sample scorecard of crisis hedges.** It covers the 1970s inflation as well as the
  disinflation era, so it shows which hedges depended on the regime.
- **It separates "diversifier" from "crisis hedge".** Commodities diversify in normal times,
  but energy is unreliable in crashes, so a broad commodity index is a weaker tail hedge
  than its correlation suggests.

The bond result relies on 1970–2010, mostly a falling-rate period, and bonds failed as a
hedge in 2022. The extreme-month dummies use the full sample, so they describe history
rather than a rule investors could have followed.

## Links

- [[harvey-et-al-2019-the-best-of-strategies-for-the-worst-of-times]] — a later scorecard of crisis hedges including puts, trend and quality
- [[brixton-thapar-maloney-2021-when-stock-bond-diversification-fails]] — when inflation news makes bonds stop hedging
- [[neville-et-al-2021-the-best-strategies-for-inflationary-times]] — asset returns in inflation regimes since 1926
- [[baur-2021-is-gold-a-safe-haven-in-all-currencies]] — gold's safe-haven role measured currency by currency
- [[hartmann-straetmans-de-vries-2004-asset-market-linkages-in-crisis-periods]] — extreme-value estimates of joint stock and bond crashes
