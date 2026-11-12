# Systemic Risk and Bank Business Models

| | |
|---|---|
| **Authors** | Maarten R. C. van Oordt (De Nederlandsche Bank), Chen Zhou (De Nederlandsche Bank; Erasmus University Rotterdam) |
| **Year** | 2014 (DNB Working Paper No. 442, October 2014); published in the *Journal of Applied Econometrics* 34(3), 365–384, 2019 |
| **Type** | Working paper, 41pp. US bank holding companies, 1991–2011, 11,597 bank-quarters |
| **PDF** | Not hosted in this repository (DNB/SSRN working paper, no open licence) |
| **Find it** | [doi.org/10.1002/jae.2666](https://doi.org/10.1002/jae.2666) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Systemic+Risk+and+Bank+Business+Models%22+Oordt) |
| **BibTeX** | `vanoordt2014systemic` |
| **Status** | Reference: §2 (the tail beta and its decomposition) and §4.1–4.2 (size and non-interest income) carry the results; Figure 3 summarises them |

## What it is

A way to measure how much a single bank falls when the whole financial sector crashes, and
to split that number into two parts that regulators usually mix up.

- **The measure: a tail beta.** Regress a bank's stock return on the return of a
  financial-sector index, but only on days when the sector suffers an extreme loss (beyond
  its Value-at-Risk at a small probability). The slope, β_T, says how much the bank loses
  per unit of sector loss in a crisis. It is proportional to Acharya et al.'s Marginal
  Expected Shortfall (MES), the standard systemic-risk measure, so it ranks banks the same
  way.
- **Estimated with extreme value theory.** Crisis days are few, so OLS on them is noisy.
  The authors' EVT estimator writes β_T as (tail dependence)^(1/ζ) × (bank VaR / sector
  VaR), where ζ is the sector's tail index (Hill estimator). Each piece has a standard
  EVT estimator, and the whole thing stays consistent under volatility clustering.
- **The decomposition.** In logs, systemic risk = **bank tail risk** (how big the bank's
  own extreme losses are relative to the sector's) + **systemic linkage** (how much of the
  bank's tail risk coincides with sector crashes). Across banks the two are almost
  unrelated, so knowing one tells you little about the other.
- **Data.** Daily CRSP returns on US bank holding companies with four-year rolling
  windows, 1991–2011, matched to FR Y-9C balance-sheet data. The average β_T is 0.91
  (range 0.13–3.71). On average 63% of a bank's tail risk is systemic linkage (range
  18–92%).
- **Main findings.**
  - **Size:** a bank twice as large has about 6% higher systemic risk. Its own tail risk
    is about 2% *lower*, but its tail dependence with the sector is about 8% higher. So
    large banks look safer one at a time and are more dangerous together.
  - **Non-interest income:** a 1 percentage-point higher share of non-interest income
    goes with about 0.4% higher systemic risk. Trading revenue and "other" non-interest
    income barely affect a bank's own tail risk but raise its linkage to the system.
  - **Classic soundness indicators** such as non-performing loans and low profitability
    predict the bank's own tail risk, which is what microprudential supervision watches.

## Why it's in the library

- **It separates two things "tail risk" can mean.** How fat an asset's own left tail is,
  and how much its bad days coincide with everyone else's, are different quantities. Only
  the second adds risk to a diversified book in a crash. The same split applies to any
  portfolio asset, not just banks.
- **A practical tail-dependence estimator.** The EVT tail beta works with the few crisis
  observations real data offer. It is a usable alternative to fitting a full copula when
  the question is only "how much does this fall when the market crashes?"
- **Evidence that diversification and safety pull apart in the tail.** Large, diversified
  banks are individually less risky but more tied to the system, a balance-sheet version
  of correlations going to one in a crisis.

The empirical work is careful (two-way clustered errors, robustness checks with bank fixed
effects), but it is one country and one sector over a sample dominated by the 2008 crisis,
and the tail beta is backward-looking.

## Links

- [[hartmann-straetmans-de-vries-2004-asset-market-linkages-in-crisis-periods]] — the earlier EVT measure of extreme co-crashes across stock and bond markets; this paper uses the same machinery bank by bank
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — why dependence in the tail, not average correlation, is what breaks in a crisis
- [[ang-chen-2002]] — asymmetric correlations: assets move together more in down markets
- [[barbon-buraschi-2021-gamma-fragility]] — another source of crash amplification that only shows up in the tail
