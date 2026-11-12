# Runs to Banks: The Role of Cash Sweeps During Market Downturns

| | |
|---|---|
| **Authors** | James R. Barth (Auburn University), Mark Mitchell (CNH Partners; Chicago Booth), Yanfei Sun (Ryerson University) |
| **Year** | 2020 (draft dated 9 September 2020) |
| **Type** | Working paper, SSRN 3690525, 51pp |
| **PDF** | Not hosted in this repository (SSRN draft, no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Runs+to+Banks%3A+The+Role+of+Cash+Sweeps+During+Market+Downturns%22+Barth) for the title and authors |
| **BibTeX** | `barth2020sweeps` |
| **Status** | Reference: Section 4 (TD Ameritrade monthly and aggregate quarterly regressions) and Section 5 (deposit volatility) carry the results |

## What it is

An empirical study of where retail money goes when stocks fall. Since the late 1990s,
brokerages "sweep" clients' idle cash into deposits at affiliated or partner banks, so a
retail sell-off shows up as a deposit inflow at banks.

- **Data.** Monthly sweep deposits at TD Ameritrade's program banks (2009–2020, 125
  months) and estimated aggregate sweep deposits across US banks (quarterly, 1984–2020,
  with a focus on 2000–2020).
- **Asymmetry.** Sweep deposit growth rises when the market falls, but barely moves when
  it rises: in a piecewise regression the slope is −0.757 for negative market months and
  +0.091 for positive ones. Average monthly sweep growth is 2.58% in down months against
  0.51% in up months. In March 2020 TD Ameritrade's sweep balances rose 26.5% (from
  $122.1bn to $153.4bn) as the market fell 13.8%; Schwab issued $1.1bn of debt to capitalise
  its banks for the inflow.
- **Aggregate.** The stock-market coefficient for sweep deposits is more than six times that
  for total deposits, and over 2000–2020 the market stops explaining total deposits once
  sweep and brokered deposits are removed: sweeps drive the familiar inverse link between
  stocks and bank deposits.
- **Stabilising, not destabilising.** Despite regulators' long-standing worry about brokered
  deposits, sweep deposits arrive exactly when corporate credit-line drawdowns hit banks;
  only non-sweep brokered deposits add to deposit volatility.
- **Rates.** A 25bp rise in the Fed funds rate cuts sweep deposit growth by about 4.35
  percentage points, a much stronger deposits-channel response than in bank data overall.

## Why it's in the library

It traces one concrete mechanism of risk-off: households de-risk, and the cash physically
moves from brokerages to banks. That flow is part of why banks are funded in a sell-off and
part of why cash, not only Treasuries, is the destination in a flight to safety.

The firm-level evidence is one self-directed brokerage over about a decade, and the
authors note its clients may react more than most. The aggregate sweep data are estimates,
and in the aggregate data the asymmetry is not robust: it appears over 1984–2020 but
reverses over 2000–2020. Mark Mitchell is at CNH Partners, an AQR affiliate.

## Links

- [[boyarchenko-larsen-whelan-2023-the-overnight-drift]] — another trace of investor selling in a sell-off, and of its reversal
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — the bull and bear market regimes in which these flows occur
- [[cole-2018-what-is-water-in-markets]] — liquidity, not volatility, as the thing that disappears in a crisis
