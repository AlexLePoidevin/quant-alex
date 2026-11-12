# The Impact of Skew on Performance and Bias

| | |
|---|---|
| **Authors** | Zachary Dugan and Alexander Greyserman (ISAM; Johns Hopkins, Columbia) |
| **Year** | 2019 (January 2019 working paper; published in *Journal of Behavioral and Experimental Finance* 22, 232–238) |
| **Type** | Simulation study by a trend-following manager's research team, 18pp (SSRN 3315740) |
| **PDF** | Not hosted in this repository (SSRN working paper, no open licence) |
| **Find it** | [doi.org/10.1016/j.jbef.2019.03.008](https://doi.org/10.1016/j.jbef.2019.03.008) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Impact+of+Skew+on+Performance+and+Bias%22+Dugan) |
| **BibTeX** | `dugan2019skew` |
| **Status** | Reference: read in full; Exhibits 8, 10, 11 and 14 carry the results |

## What it is

A Monte Carlo study of how the skewness of a return stream changes what investors see
over short and long windows. Daily returns are drawn from gamma (and, as a check,
skew-normal) distributions tuned to a given annual return, 20% volatility and a chosen
skew, and long simulated histories are compared window by window.

- **Short windows favour negative skew.** Two streams with the same 20-year Sharpe ratio
  (1.0) and volatility, one with zero skew and one with skew between −10 and +10: over
  windows from 5 days to 2 years, the most negatively skewed stream beats the zero-skew
  one up to 56% of the time and the most positively skewed one only about 44%.
- **Even a worse strategy can look better.** A stream with Sharpe 0.8 and positive skew
  is set against one with Sharpe 0.4 and skew −1.6. Over short windows the
  positive-skew stream, with twice the risk-adjusted return, underperforms; even over
  2-year windows it wins only about 60% of the time. With 16% a year and skew +1.6, about
  60% of days are negative, against under 40% for 8% a year and skew −1.6.
- **Long windows punish negative skew.** At Sharpe 0.8 and 20% volatility, skew barely
  changes the average maximum drawdown inside two years. Over about 5 years skew +3 gives
  14% and skew −3 gives 30%; over 20 years, 22% against 45%. The longest drawdown over
  about 18 years is 36 months at skew +3 and 42 months at skew −3.
- **Skew changes how volatility feeds drawdowns.** Moving volatility from 5% to 30% raises
  the 20-year maximum drawdown by 28% at skew +2 and by 46% at skew −2.

## Why it's in the library

It puts numbers on a point that sits behind several notes in this section: strategies that
sell insurance look best exactly when they are being judged most often, and long-volatility
or trend strategies look worst. The drawdown tables are a useful companion to Man Group's
drawdown arithmetic for normal returns. The limits are plain: the return streams are
simulated i.i.d. draws with skew imposed by construction, not fitted to any real strategy,
the behavioural argument (loss aversion, recency bias) is asserted from the literature rather
than tested, and the authors run a trend-following fund, so the conclusion that positive
skew deserves patience is also their pitch.

## Links

- [[van-hemert-et-al-2020-drawdowns]] — drawdown depth and duration for normal returns, which this extends to skewed ones
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — the positively skewed strategy this paper is written to defend
- [[bessembinder-2020-extreme-stock-market-performers-expect-some-drawdowns]] — large drawdowns even in the best long-run outcomes
- [[harvey-et-al-2018-the-impact-of-volatility-targeting]] — volatility scaling as a way to shrink the left tail
