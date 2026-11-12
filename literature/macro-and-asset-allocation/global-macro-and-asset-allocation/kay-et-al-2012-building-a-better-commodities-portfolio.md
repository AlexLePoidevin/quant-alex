# Building a Better Commodities Portfolio

| | |
|---|---|
| **Authors** | Bradley Kay, Ari Levine, Yao Hua Ooi, Lasse H. Pedersen (AQR Capital Management) |
| **Year** | 2012 (Summer 2012) |
| **Type** | Manager white paper, AQR, 10pp. Data January 1970 to December 2011 |
| **PDF** | Not hosted in this repository (AQR document with no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Building+a+Better+Commodities+Portfolio%22+Kay) for the title and authors |
| **BibTeX** | `kay2012commodities` |
| **Status** | Reference: Section 2 (why hold commodities), Section 3 (risk balancing, volatility targeting, drawdown control) and Section 4 (carry, trend and fundamentals) |

## What it is

A short case for holding commodities in a different way from the standard indices. The
targets are the S&P GSCI and Dow Jones-UBS, which then held nearly 80% of long-only commodity
money (including physical precious metals).

- **Why hold commodities at all.** The paper gives three reasons:
  - **A positive return:** the Keynes argument is that producers pay a premium to hedge by
    selling futures.
  - **Low correlation with stocks and bonds:** lower than other "real" assets such as REITs,
    natural-resource equities and inflation-linked bonds.
  - **Inflation protection:** stocks and bonds had negative real returns in the third of
    months with the biggest positive inflation surprises, while the GSCI did well.
- **What is wrong with the standard indices.**
  - **Concentration:** weights by production or liquidity concentrate risk in energy, crude
    especially, and that risk has not earned a matching return.
  - **Unmanaged volatility:** realised volatility swings from calm to above 50–60% in bear
    markets.
- **The fixes proposed.**
  - **Risk balancing across six sectors**, so each contributes equally to portfolio risk. It
    pays because commodities are poorly correlated with each other. Over 1990–2011 the average
    pairwise correlation of ten major contracts was 0.22, against 0.62 for ten developed equity
    index futures and 0.53 for G6 10-year bond futures.
  - **Volatility targeting** to a constant 18%, the GSCI's long-run average, using short-term
    volatility estimates.
  - **Drawdown control:** exposure is cut as trailing losses approach 20%, down to a minimum
    of 50%, and rebuilt as returns recover. The paper argues this works because commodity bear
    markets tend to unfold gradually.
  - **Tactical tilts** on carry (roll yield), 12-month price trend, inventories and
    seasonality, macro demand by consuming region (Europe drinks over 40% of the world's
    coffee), and relative-value spreads such as the crude-products crack spread.
- **The costs.** These come in the paper's own words: more trading, larger weights in less
  liquid contracts, lower capacity, and long periods of tracking error against the passive
  indices.

## Why it's in the library

- **It applies risk-based portfolio construction to one asset class.** The building blocks are
  risk parity across sectors, volatility targeting and a drawdown rule. Commodities make the
  case clearly, because their sectors are so weakly correlated.
- **It sets out the commodity return drivers** (roll yield or carry, trend, inventories) that
  later commodity factor research builds on.
- **It is a manager's paper with hypothetical results.** No performance numbers for the
  combined portfolio appear in the text, only charts. The drawdown rule and the 18% target are
  design choices, fitted with hindsight over a sample containing only a few major commodity
  bear markets.

## Links

- [[neville-et-al-2021-the-best-strategies-for-inflationary-times]] — commodities as the
  asset class with the most reliable real returns in inflation surges, sector by sector
- [[meucci-2009]] — measuring how many independent bets a risk-balanced portfolio really holds
- [[harvey-et-al-2020-strategic-risk-management-out-of-sample-evidence-from-covid-19]] —
  volatility targeting tested out of sample in a crash
- [[aqr-2022-capital-market-assumptions-for-major-asset-classes]] — AQR's later expected
  return for a diversified commodity basket, 1.4% real
- [[rubbaniy-et-al-2022-safe-haven-properties-of-soft-commodities-during-covid-19]] — which soft commodities held their price in the 2020 pandemic
