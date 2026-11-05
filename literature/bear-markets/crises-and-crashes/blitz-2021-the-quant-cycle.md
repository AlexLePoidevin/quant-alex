# The Quant Cycle

| | |
|---|---|
| **Authors** | David Blitz (Robeco Quantitative Investments) |
| **Year** | 2021 |
| **Type** | Journal article, *Journal of Portfolio Management* 48(2), 26–43; the local copy is the September 2021 SSRN working paper (3930006) |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `blitz2021quantcycle` |
| **Status** | Reference: read in full; the "Defining the Quant Cycle" section and Exhibits 10–13 carry the argument |

## What it is

An attempt to describe the boom-and-bust behaviour of equity factors with a cycle read off
the factor returns themselves, instead of from the business cycle. It uses eight US factors
(two each for value, quality, momentum and low risk) from July 1963 to December 2020, and
a reduced set back to 1929.

- **Macro states explain little.** NBER recessions (12% of months) move the market (+8.8%
  a year in expansions, −7.4% in recessions) but not factors; an equal mix of the eight is
  about the same in both. The Neville et al. inflation regimes (25% of months) and the ISM
  above or below 50 barely separate factor returns either. The Baker–Wurgler sentiment
  index does better, but factor premiums are still positive in every sentiment state.
- **The cycle.** A normal stage, about two-thirds of the time, broken roughly once a decade
  by a growth rally or value crash lasting about two years, followed by a reversal. A bear
  reversal (growth stocks crash, as in 2000–02) is good for almost every factor; a bull
  reversal (beaten-down stocks rebound, as in 2009) hurts momentum and quality, and the
  equal mix loses heavily. Growth rallies hurt value but usually help momentum about as
  much, with 2018–2020 the exception.
- **Transitions.** The unconditional chance of leaving the normal stage within 12 months is
  about 16% (a normal stage of about six years); the shorter stages have about a 50% chance
  of moving on within a year.
- **Before 1963.** The 1930s have four value crashes and bull reversals in quick
  succession, followed by an unusually long calm, so the post-1963 regularity may not hold
  over the long run.

## Why it's in the library

It is the factor-investing version of the bull-and-bear dating problem in this section:
regimes defined by the asset's own drawdowns rather than by the economy. The useful
message is that value and momentum diversify each other through most stages, and that
bull reversals are the stage that hurts a multi-factor book. The weakness is that the
stages are dated by eye after the fact; the author calls it "part art and part science",
says the number of transitions is too small to estimate conditional probabilities, and
leaves real-time identification for future work. Its "explanatory power" is therefore
in-sample by construction.

## Links

- [[ilmanen-et-al-2021-how-do-factor-premia-vary-over-time]] — the macro-timing evidence this paper builds on
- [[maheu-mccurdy-2000-identifying-bull-and-bear-markets-in-stock-returns]] — bull and bear states for the market itself
- [[neville-et-al-2021-the-best-strategies-for-inflationary-times]] — the inflation-regime definition reused here
- [[kelly-moskowitz-pruitt-2021-understanding-momentum-and-reversal]] — why momentum crashes in rebounds
- [[fama-french-1993]] — the value factor whose drawdowns define the cycle
