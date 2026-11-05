# Bull and Bear Markets During the COVID-19 Pandemic

| | |
|---|---|
| **Authors** | John M. Maheu (McMaster), Thomas H. McCurdy (Toronto), Yong Song (Melbourne) |
| **Year** | 2021 |
| **Type** | Journal article, *Finance Research Letters* 42, 102091 (2021). doi:10.1016/j.frl.2021.102091. Preprint arXiv:2012.01623 (econ.EM), SSRN 3747168 |
| **PDF** | `maheu-mccurdy-song-2021-bull-and-bear-markets-during-the-covid-19-pandemic.pdf`: the arXiv version (v1, November 2020, CC BY 4.0). Same model, dates and numbers as the journal version, plus a longer appendix |
| **BibTeX** | `maheu2021covid` |
| **Status** | Reference: Table 2 (state estimates), Table 4 (2020 timing strategies) and Figures 2–4 (smoothed and one-week-ahead state probabilities) carry the results |

## What it is

The authors' four-state bull/bear model from 2012, re-estimated on weekly US stock returns
from 1885 to November 2020 and used to date and forecast the 2020 COVID crash and recovery.

- **The model.** Weekly returns are normal within each of four hidden states: bear
  (negative mean), bear rally (positive mean), bull correction (negative mean) and bull
  (positive mean). The transition matrix stops a bear-regime state jumping straight into a
  bull correction and vice versa, so a new regime must start from a bear or bull state.
  Long-run restrictions keep the bear regime's average return negative and the bull
  regime's positive. Estimation is Bayesian (Gibbs sampling).
- **Full-sample states.** Weekly mean returns are −0.94% (bear), 0.23% (bear rally),
  −0.11% (bull correction) and 0.52% (bull), with volatilities 5.60%, 2.44%, 1.85% and
  1.09%. Bear rallies and bull markets both go up, but a bear rally is more than twice as
  volatile, which is how the model tells them apart. Regime changes almost always pass
  through a bear rally or a bull correction; jumping straight from bull to bear is rare.
  The bull regime holds about 67% of the time in the long run.
- **2020 dating.** Bull at the start of the year, a bull correction from late January, a
  decisive bear state by 26 February, and a bear rally from 22 April. At the end of the
  sample (25 November) the bear-rally probability was still 0.824: prices had recovered,
  but volatility was too high and too variable for a bull market. The press was by then
  calling a new bull market. A two-state model did call the summer of 2020 a bull market,
  which is the point of having four states.
- **Real-time forecasts.** One-week-ahead state forecasts, re-estimated each week on past
  data only, track the smoothed states closely. The main miss is July to September 2020,
  when the forecasts gave a bull regime a sizeable probability that hindsight rejects.
- **Timing strategies, 2 January to 25 November 2020.** Buy-and-hold earned 13.1% a year
  annualised (Sharpe 0.566). Holding the market when the forecast bull-regime probability
  exceeds 0.5 earned −0.9% (Sharpe −0.048). Holding it when either a bear rally or a bull
  state is forecast above 0.5 earned 22.0% (Sharpe 1.203), with three or four trades.
  Letting the two thresholds differ pushes the return to 28%.
- **Model comparison.** On 2020 predictive likelihood the four-state model beats a
  Student-t version, an unrestricted version, a two-state model and GARCH(1,1). Its value
  at risk adjusts faster than GARCH's after March 2020.

## Why it's in the library

- **The bear-rally state in action.** The 2012 paper argued bear rallies should be modelled
  separately. This one shows it mattering in a live episode: the model refused to call the
  2020 recovery a bull market because its volatility looked like a bear rally's.
- **Volatility separates the regimes.** As in the authors' 2000 paper, it is the variance,
  not the trend, that identifies the state. A rising market with bear-market volatility is
  still classified as a bear regime.
- **The strategy evidence is thin.** The timing results cover eleven months of one market,
  and the winning rule (hold in bear rallies too) only won because 2020 rebounded fast. The
  bull-regime rule, the natural one, lost money. The 28% figure comes from searching over
  thresholds within the same eleven months. The appendix says the rule also helped over
  2007–2009 but gives no figures in the main text.
- **A small inconsistency.** The introduction dates the start of the bear rally to 3 June;
  the results section, figure and conclusion say 22 April.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — the four-state model
  this applies, estimated on 1885–2010
- [[maheu-mccurdy-2000-identifying-bull-and-bear-markets-in-stock-returns]] — the authors'
  original two-state model with duration dependence
- [[zegadlo-2022-identifying-bull-and-bear-market-regimes-rule-based]] — a rule-based way to
  date regimes within regimes, the alternative to a Markov-switching model
- [[yang-wagner-2014-optimal-probabilistic-market-timing-using-bull-bear-cycle-statistics]]
  — another bull/bear timing rule, which fails in exactly the bear-rally case this model
  handles
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a two-state
  bull/bear model turned into an optimal trend rule
- [[conlon-mcgee-2020-safe-haven-or-risky-hazard-bitcoin-during-the-covid-19-bear-market]] — whether Bitcoin protected an equity investor in the 2020 bear market
