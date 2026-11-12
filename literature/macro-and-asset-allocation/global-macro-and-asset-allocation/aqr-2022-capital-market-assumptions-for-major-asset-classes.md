# Capital Market Assumptions for Major Asset Classes (1Q 2022)

| | |
|---|---|
| **Authors** | AQR Portfolio Solutions Group (thanks to Alfie Brixton, Pete Hecht, Thomas Maloney, Nick McQuinn; comments from Antti Ilmanen) |
| **Year** | 2022 (estimates as of 31 December 2021; published January 2022) |
| **Type** | Manager white paper, *Alternative Thinking* Q1 2022, 17pp |
| **PDF** | Not hosted in this repository (AQR document, "not to be reproduced or redistributed without the written consent of AQR") |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Capital+Market+Assumptions+for+Major+Asset+Classes+%281Q+2022%29%22+Group) for the title and authors |
| **BibTeX** | `aqr2022cma` |
| **Status** | Reference: Exhibits 1–5 (estimates and method), the alternative risk premia section, and "Revisiting the 5% Solution" (Exhibits 9–12) |

## What it is

AQR's annual 5- to 10-year expected real returns for the main asset classes. The 2022 edition
adds a look back at its own decade-old forecast, which turned out badly wrong.

- **The method is yield-based, with no mean reversion assumed.**
  - **Equities:** an average of two estimates. One is half the cyclically adjusted earnings
    yield (adjusted Shiller E/P) plus 1.5% real EPS growth. The other is the net total payout
    yield plus a long-run aggregate growth estimate.
  - **Government bonds:** yield plus rolldown, minus a survey forecast of inflation.
  - **Credit:** spreads are cut by 50% for default losses, downgrades and index rules.
  - **Commodities:** the long-run excess return of an equal-weighted futures basket, about 3%
    over cash since 1877.
  - **Private equity:** a discounted-cash-flow model with leverage and fees.
- **The headline estimates at end-2021:**
  - The expected real return of a US 60/40 portfolio is about 2%, under half its average of
    nearly 5% since 1900.
  - Real cash returns are negative in every major market, so expected premia over cash are
    close to normal even though absolute expected returns are low.
  - Commodities are expected to return 1.4% real, and gold has earned about the same as cash
    since 1975.
  - US buyout private equity is put at 5.7% real, net of fees.
  - A diversified multi-asset, multi-style long-short premia portfolio is assumed to reach a
    Sharpe ratio of 0.7–0.8 net. A single style in a single asset class gets only 0.2–0.3.
- **Uncertainty is large.** Based on history, there is a 50% chance realised 10-year equity
  returns miss the estimate by more than 3% a year.
- **The look back.** In 2012 AQR forecast 2.4% real for a US 60/40 portfolio. It delivered
  8.5% a year over 2012–2021 (6.8% for a global version). AQR breaks the miss down: mostly
  "rich markets got richer" (valuation expansion), plus EPS growth above the assumed 1.5%.
- **Practical suggestions.** It ends with ways to raise expected returns:
  - diversifying into commodities and long-short premia;
  - modest leverage, or a risk-parity sleeve as a way to add leverage indirectly;
  - tilting toward styles such as value, which it judged extremely cheap at the time.

## Why it's in the library

- **It shows how to build medium-term expected returns from yields.** The yield-based approach
  gives a transparent, conservative starting point for strategic allocation, and the error
  bands are stated next to the numbers.
- **The look back is the most useful part.** It shows that forecasts based on starting yields
  can be right about the long run and badly wrong about the next decade. When valuations keep
  expanding, they become self-fulfilling for a while.
- **It is AQR marketing as well as research.** The practical suggestions (risk parity, style
  premia, a value overweight) are AQR's own products, and the style-premia Sharpe ratio of
  0.7–0.8 is an assumption, not a measured result.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the counter-argument to adding risk
  parity and volatility-sized leverage: they may amount to a hidden short-volatility trade
- [[neville-et-al-2021-the-best-strategies-for-inflationary-times]] — what happened to
  stocks, bonds and commodities when inflation surged, which matters for yield-based
  forecasts
- [[keller-keuning-2023-haa]] — a tactical alternative to holding a static 60/40 when
  yields are rising
