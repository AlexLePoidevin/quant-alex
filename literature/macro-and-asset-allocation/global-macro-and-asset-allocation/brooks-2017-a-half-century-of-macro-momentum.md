# A Half Century of Macro Momentum

| | |
|---|---|
| **Authors** | Jordan Brooks (AQR Capital Management) |
| **Year** | 2017 (August 2017) |
| **Type** | Manager white paper, AQR, 24pp. Hypothetical backtest 1970–2016, gross of fees and costs |
| **PDF** | Not hosted in this repository (AQR document with no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22A+Half+Century+of+Macro+Momentum%22+Brooks) for the title and authors |
| **BibTeX** | `brooks2017macro` |
| **Status** | Reference: signal construction (Exhibit 1, Appendices B–C), decade-by-decade results (Exhibits 2–3), bear-market and rising-yield behaviour (Exhibits 4–5), and the comparison with trend (Exhibits 6–7) |

## What it is

A systematic version of discretionary global macro investing. The idea is to go long assets
whose fundamental macroeconomic trends are improving and short those whose trends are getting
worse. The author calls this "macro momentum". The premise is the same as trend following:
markets react slowly to news. Here, though, positions follow the economic news itself, not the
price moves the news causes.

- **What it trades:** equity indices, currencies, 10-year government bonds and 3-month rates.
- **The four themes and their signals:**
  - **Business cycle:** one-year changes in consensus GDP-growth forecasts and in CPI-inflation
    forecasts, half each.
  - **International trade:** one-year changes in spot FX.
  - **Monetary policy** and **risk sentiment**.
- **Signs differ by asset class.** Rising growth is bullish for a country's equities and
  currency but bearish for its bonds.
- **Portfolio construction:** every theme and asset-class pair is run both long-short
  (market-neutral) and directional. That gives 32 sub-portfolios, each scaled to 10%
  volatility and averaged with equal weights.
- **Results (hypothetical, gross).**
  - **Over time:** the strategy had positive excess returns in every decade since 1970.
    Its correlation with US equities and bonds was low to negative.
  - **Breadth:** themes and asset classes each contributed, and their average pairwise
    correlation was about 0.1.
  - **Crisis behaviour:** it shows a "smile" against equities. In the ten worst equity
    quarters since 1970 (equities −19.9% on average) it returned 13.7% on average, and in the
    ten largest rises in real yields it averaged 12%.
  - **Against trend:** correlation with a matched trend strategy was 0.4, and each strategy
    was positive during the other's five worst drawdowns. A 50/50 mix reached a Sharpe ratio
    of 1.4, against 1.1–1.2 for each strategy alone.
  - **The worst episode** was the tech bubble, April 1999 to December 2000: macro momentum
    lost 22% while trend gained 17%, because fundamentals and prices pointed in opposite
    directions.

## Why it's in the library

- **It is a clean statement of fundamental momentum at the asset-class level.** It sits next
  to trend following in the defensive-strategies material. The paper's case is that
  fundamental trends and price trends overlap but turn at different times, which is why the
  two diversify each other.
- **Its crisis behaviour has an economic story.** Big equity bear markets tend to follow
  worsening growth, tightening policy and souring risk sentiment, so a macro-momentum book
  is usually already short when the fall comes.
- **Read it as a backtest from a manager that runs these strategies.** The results are
  gross of costs and hypothetical. Survey forecasts from the 1970s are sparse, and the author
  himself says hindsight bias probably overstates the Sharpe ratios even though the signals
  are deliberately simple.

## Links

- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — price trend
  following, the strategy macro momentum is compared with
- [[harvey-et-al-2020-strategic-risk-management-out-of-sample-evidence-from-covid-19]] —
  trend's behaviour in a very fast crash
- [[chen-roll-ross-1986]] — macroeconomic state variables (growth, inflation, the term
  structure) as priced risks
- [[aqr-2022-capital-market-assumptions-for-major-asset-classes]] — AQR's own expected
  returns for diversified multi-asset premia like this one
- [[kessler-scherer-2013-momentum-and-macroeconomic-state-variables]] — price momentum across asset classes, which also earns most in recessions; same name, different signal
