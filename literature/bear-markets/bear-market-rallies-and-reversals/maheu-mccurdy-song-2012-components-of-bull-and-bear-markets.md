# Components of Bull and Bear Markets: Bull Corrections and Bear Rallies

| | |
|---|---|
| **Authors** | John M. Maheu (Toronto), Thomas H. McCurdy (Rotman, Toronto), Yong Song (UTS) |
| **Year** | 2012 |
| **Type** | Paper. *Journal of Business & Economic Statistics* 30(3), 391–403 (doi 10.1080/07350015.2012.680412); the copy is the February 2012 SSRN version (1939486), 36pp |
| **PDF** | Local copy only (SSRN download of a Taylor & Francis journal article; no open licence) |
| **BibTeX** | `maheu2012components` |
| **Status** | Reference: §2.2 (the 4-state model), §4.1 (Tables 3–6: states, durations, cumulative returns), §4.3 (1929, 1987, 2007–09) and §4.4 (VaR, long-horizon forecasts, real-time dating) carry the results |

## What it is

A Markov-switching model of weekly S&P 500 returns (1885–2010, 6,498 weeks) with **four
states instead of two**: bear, bear rally, bull correction and bull. A bear regime is made of
bear and bear-rally states; a bull regime of bull-correction and bull states. A bear rally can
fall back into the bear state or exit to a bull market, and a bull correction can recover or
turn into a bear market. That gives the model the vocabulary practitioners already use ("is this
a bear market rally or a new bull market?") as a probability model with Bayesian estimation.

What it finds:

- **Regimes are long once rallies are allowed inside them.** A 2-state model on weekly data
  switches too often (bull markets last only about 83 weeks). The 4-state model gives a bull
  regime of 256 weeks (just under five years) and a bear regime of 78 weeks (about 1.5 years),
  with average cumulative returns of +33% and about −10%.
- **Bear rallies are large.** The bear state averages a cumulative −12.4%, and bear rallies give
  back +7.1% of it. Bull corrections average −2.1% against +7.9% in the bull state. The market
  spends about 16% of the time in bear rallies and 30% in bull corrections.
- **A bear rally looks like a bull market on returns but not on volatility.** The bear-rally
  mean (0.23% a week) is close to the bull state's, but its volatility is about twice as high.
  The model does not call a new bull market until volatility falls back to bull-market levels.
- **Turning points go through the in-between states.** Given that a bull market has just
  started, the probability that the previous state was a bear rally is 0.93; given that a bear
  market has just started, the previous state was a bull correction with probability 0.87.
  Exits are asymmetric: a bull correction returns to the bull state far more often than it
  becomes a bear market.
- **Dated episodes.** Smoothed (full-sample) states put a bull correction from mid-July 2007,
  the bear state from early September 2008, a bear rally from the third week of March 2009, and
  the bull state from mid-November 2009. 1929 and 1987 both enter the bear regime through a bull
  correction; 1933–37 is classed as one long bear rally.
- **Out of sample.** Re-estimated with data up to each week, the model moves into the bear
  regime in the first week of October 2008 (bull-regime probability falls from 0.85 to near
  zero) and leans to a bull market from early December 2009. Its 5% VaR rises sharply in
  September–October 2008, where a normal benchmark badly understates losses. For cumulative
  return forecasts at 3, 6 and 12 months it beats GARCH(1,1), a 2-state model and an
  unrestricted 4-state model by wide margins in log predictive likelihood; GARCH wins at one
  month.

Model comparison by marginal likelihood strongly favours the 4-state model (log Bayes factor
163 against the 2-state model, 6.8 against an unrestricted 4-state model).

## Why it's in the library

It is the cleanest statistical definition of a **bear market rally**: a positive-return,
high-volatility state inside a bear regime, distinct from a bull market by its volatility
rather than its direction. That makes it a reference for any rule that tries to tell a rally
from a recovery, and it explains why trend filters get whipsawed in bear markets. Rallies are
part of the bear regime, so price direction alone keeps flipping.

The dated episodes mix in-sample and real-time results. The 2007–09 dates in §4.3 are smoothed
with the full sample; the real-time dating in §4.4 is later (October 2008 rather than September)
and is the fair test. The model is fitted on one index with no costs or trading rule, so it is a
regime description and forecasting tool, not a strategy.

## Links

- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a two-state
  bull/bear Markov model used to derive the optimal trend rule; this paper shows why two states
  switch too often on weekly data
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — regime switching applied to volatility
  itself, the variable that separates bear rallies from bull markets here
- [[ang-chen-2002]] — correlations that rise in down markets, another way bear regimes differ
  from bull ones
- [[johannsen-2016-dead-cat-bounce]] — a behavioural explanation for why bear rallies happen
- [[schultz-2002-bear-market-investing-strategies]] — the practitioner (Dow Theory) account of
  secondary reactions that this model formalises
- [[boyarchenko-larsen-whelan-2023-the-overnight-drift]] — sell-offs followed by overnight
  reversals, a high-frequency version of the asymmetric rebound
- [[bilokon-et-al-2021-market-regime-classification-with-signatures]] — a model-free alternative: clustering price paths without fixing the number of regimes
- [[garg-et-al-2021-momentum-turning-points]] — four observable phases (bull, correction, bear, rebound) from 1- and 12-month returns, and how a trend rule should react to each
- [[goetzmann-kim-2018-negative-bubbles-what-happens-after-a-crash]] — rebounds after severe crashes across 101 markets since 1692
- [[haase-neuenkirch-2023-predictability-of-bull-and-bear-markets]] — forecasting bull and bear regimes in real time with time-varying transition probabilities
- [[li-zakamulin-2020-stock-volatility-predictability-in-bull-and-bear-markets]] — how far ahead volatility can be forecast in bull versus bear states
- [[liu-moench-2016-what-predicts-us-recessions]] — which indicators predict economic recessions, the business-cycle side of bull and bear markets
- [[maheu-mccurdy-2000-identifying-bull-and-bear-markets-in-stock-returns]] — the authors' earlier two-state, duration-dependent model on monthly data back to 1834
- [[maheu-mccurdy-song-2021-bull-and-bear-markets-during-the-covid-19-pandemic]] — the same model applied to the 2020 crash and recovery, where it classified the rebound as a bear rally
- [[peterson-2018-when-to-own-stocks-and-when-to-own-gold]] — secular (decade-long) bull and bear markets dated by valuation against gold, with a stocks-or-gold switching rule
- [[zegadlo-2022-identifying-bull-and-bear-market-regimes-rule-based]] — a rule-based (non-Markov) way to date bull and bear markets, with bull corrections as regimes within regimes
