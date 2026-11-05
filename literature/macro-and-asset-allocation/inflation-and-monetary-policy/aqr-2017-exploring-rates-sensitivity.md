# Exploring Rates Sensitivity

| | |
|---|---|
| **Authors** | AQR Capital Management (*Alternative Thinking*, no named authors) |
| **Year** | 2017 (Second Quarter issue) |
| **Type** | Manager research note, 16pp. US data 1972–2016 |
| **PDF** | Local copy only (AQR publication, "not to be reproduced or redistributed") |
| **BibTeX** | `aqr2017rates` |
| **Status** | Reference: the hiking-cycle Sharpe ratios (Exhibit 3), the real-yield/inflation map (Exhibit 4) and the +1.8% rising-rates scenario (Exhibit 7) carry the results |

## What it is

AQR splits "rates" into three things and asks how a range of assets and strategies
have reacted to each since 1972:

- **Short rates:** a regime indicator for Fed hiking cycles. Eight hiking cycles cover
  about a third of the 45-year sample.
- **Real bond yields:** the 10-year Treasury yield minus survey-based expected inflation.
- **Expected inflation:** survey forecasts, rather than TIPS breakevens, because TIPS
  data are synthetic before 1997 and distorted by liquidity at times such as 2008.

It covers 8 asset classes, 4 long/short US equity styles (value, momentum, low risk,
profitability, each with and without industry exposure), multi-asset trend following,
60/40 and a simple risk parity portfolio. Returns are gross of costs.

Main findings:

- **Hiking cycles.** Every asset class did worse during hiking periods than outside
  them, except commodities, which earned essentially all their excess return during
  hikes. Most asset classes underperformed cash during hikes, bonds most of all. Risk
  parity was no more sensitive to hiking than 60/40: its larger bond exposure was offset
  by its commodity exposure. Among equity styles, value did better during hikes, and
  trend following outperformed.
- **Real yields and inflation.** Equities have a negative long-run sensitivity to
  expected inflation, commodities a positive one; TIPS respond to real yields but not
  inflation. 60/40 and risk parity have similar inflation sensitivity, but risk parity is
  more exposed to real yields.
- **Industry exposure matters for defensive styles.** Low-risk and profitability
  portfolios behave like bonds largely because they overweight bond-like sectors such as
  utilities; industry-neutral versions are much less rate-sensitive.
- **Time variation.** The rolling stock–bond correlation flipped sign around 20 years
  before publication, as inflation uncertainty faded and growth uncertainty took over.
  Equities' response to rising yields has therefore changed sign over the sample.
- **Non-linearity.** Equities and real estate suffer from sharp rises in expected
  inflation but gain little from sharp falls; commodities and TIPS offer upside
  protection.
- **A rising-rates scenario.** A two-standard-deviation 12-month rise in the 10-year
  yield (+1.8%) would, on the betas estimated, give negative expected excess returns for
  nominal bonds, TIPS and industry-unconstrained defensive equity styles, above-average
  returns for commodities, and still-positive expected returns for 60/40 and risk parity.
  The authors stress that the equity estimate has a very wide historical range.

## Why it's in the library

It is a clear, data-heavy map of how assets have behaved across monetary regimes, with
the useful decomposition of a nominal yield into expected real short rate, bond risk
premium and expected inflation. It is also an early statement of the stock–bond
correlation flipping with the inflation regime, a theme the rest of this section returns
to.

It is a manager's note: the strategies are AQR's own hypothetical backtests, the
long-run expected returns in the scenario are assumed rather than estimated, and the
authors themselves say the empirical sensitivities may be specific to the sample. Treat
the direction of the effects as the finding, not the precise numbers.

## Links

- [[aqr-2020-fire-and-ice-inflation-and-deflation]] — the same team's later and broader
  study of inflation sensitivities, with trend and macro momentum added
- [[chen-roll-ross-1986]] — the classic test of whether inflation and other macro
  variables are priced in stocks
- [[keller-keuning-2023-haa]] — a tactical rule that switches on rising yields and
  inflation, the practical response to the sensitivities measured here
