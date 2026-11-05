# Searching for Safe-Haven Assets During the COVID-19 Pandemic

| | |
|---|---|
| **Authors** | Qiang Ji (Chinese Academy of Sciences), Dayong Zhang (Southwestern University of Finance and Economics), Yuqian Zhao (University of Essex) |
| **Year** | 2020 |
| **Type** | Working paper, SSRN 3602780, 27pp. Published as *International Review of Financial Analysis* 71 (2020), 101526 |
| **PDF** | Local copy only (SSRN preprint; the journal version is Elsevier, no open licence) |
| **BibTeX** | `ji2020safehaven` |
| **Status** | Reference: §3 (the two tests), Tables 2–3 (tail changes for single assets and two-asset portfolios) and Table 4 / Figure 5 (cross-quantilograms) carry the results |

## What it is

An early check on which of the usual safe havens actually held up in the first COVID
crash, using two tail-focused tests instead of correlations.

- **Candidates and markets.** Gold (LBMA), bitcoin (CoinDesk), EUR/USD, CNY/USD, WTI
  crude futures and soybean futures, each tested against the MSCI US, MSCI Europe and
  MSCI China equity indexes. Daily data, August 2019 to March 2020: August–November 2019
  is the "normal" training sample and December 2019–March 2020 the COVID test sample,
  roughly 87 trading days each.
- **Test 1: has the left tail moved?** A sequential monitoring test (Hoga and Wied 2017)
  watches the 5% quantile of each return series and flags the day it breaks from the
  training-sample level. The three equity indexes broke in March 2020 (US on 9 March,
  China on 23 March, Europe on 24 March), as did crude oil (18 March) and EUR/USD. Gold,
  bitcoin, CNY/USD and soybeans showed no break. A GARCH VaR at 5% was hit 8% of COVID
  days for US and China equities and crude, against roughly 5% for gold and soybeans.
- **Test 2: does adding the asset fix the equity tail?** Two-asset mean-variance portfolios
  of each equity index with each candidate are monitored the same way. Only the gold and
  soybean portfolios show no left-tail break at any of the 5%, 10%, 15% and 20% quantiles,
  and only those two have positive (daily) Sharpe ratios in the COVID sample (gold about
  0.07, soybeans about 0.01). Bitcoin, crude and both currencies leave breaks in some
  combinations.
- **Test 3: cross-quantilograms.** Whether an equity index's bad days predict the
  candidate's bad days the next day (Han et al. 2016). Bitcoin, CNY/USD and crude acted as
  safe havens before COVID but lost that role during it; gold, EUR/USD and soybeans kept it
  or improved. The paper reads gold and soybeans as the robust havens, and explains
  soybeans by food-security demand in a health crisis that also crushed oil demand.

## Why it's in the library

**It is a clean statement of the safe-haven test.** A hedge only has to be uncorrelated on
average; a safe haven has to hold its value, or rise, when equities are in their left tail.
Testing quantiles directly, rather than average correlations, is the right shape of test.

**The answer depends on the crisis.** Bitcoin and the yuan looked like havens in the calm
months and stopped being so in March 2020, while an agricultural commodity worked. That
supports the view, also in [[baur-trench-2022-not-all-gold-shines-in-crisis-times]], that
safe-haven status is crisis-specific rather than a fixed property of an asset.

**The evidence is thin.** About 87 COVID-period observations per series, one crisis, a
test window that ends on 31 March 2020 (before the April oil collapse and the rebound),
and portfolio Sharpe ratios that are daily and tiny. Some of Table 3 is also odd: the
bitcoin and crude portfolios report identical Sharpe ratios for every equity index, which
suggests the optimiser put the whole weight on equities in those cases. The training
period is printed as ending "30 November 2020"; it means 2019. Read the results as
suggestive, not as a settled list of havens.

## Links

- [[baur-trench-2022-not-all-gold-shines-in-crisis-times]] — gold rose in the COVID crash
  while gold-mining stocks fell with the market: the same crisis, a different notion of
  "gold"
- [[baur-2021-is-gold-a-safe-haven-in-all-currencies]] — whether gold's safe-haven role
  depends on which currency the investor measures in
- [[baur-kuck-2020-the-timing-of-the-flight-to-gold]] — intraday evidence on when, inside a
  crash, money moves into gold
- [[hartmann-straetmans-de-vries-2004-asset-market-linkages-in-crisis-periods]] — joint
  crash probabilities across stock and bond markets, the tail-dependence view of the same
  question
- [[ang-chen-2002]] — correlations rise in down markets, which is why havens have to be
  tested in the tail
- [[rubbaniy-et-al-2022-safe-haven-properties-of-soft-commodities-during-covid-19]] — soft commodities against a COVID fear index rather than against stock losses
