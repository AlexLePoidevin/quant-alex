# Is Market Fear Persistent? A Long-Memory Analysis

| | |
|---|---|
| **Authors** | Guglielmo Maria Caporale (Brunel), Luis Gil-Alana (Navarra), Alex Plastun (Sumy State) |
| **Year** | 2018 (*Finance Research Letters* 27, 140–147); the copy is CESifo Working Paper 6534, June 2017 |
| **Type** | Empirical paper, 20pp. VIX daily and monthly, 2004–2016 |
| **PDF** | Local copy only (CESifo/SSRN working paper; the journal version is Elsevier) |
| **BibTeX** | `caporale2018fear` |
| **Status** | Reference: Table 1 (Hurst exponents) and Tables 2–4 (fractional integration by sub-period) carry the results |

## What it is

A short test of whether the VIX has long memory, and whether that memory changes between
calm and crisis periods. The sample is 2004–2016, split into pre-crisis (2004–06), crisis
(2007–09) and post-crisis (2010–16).

- **Two methods.** R/S analysis gives a Hurst exponent H for the daily and monthly *changes*
  in the VIX. Fractional integration estimates d, the order of integration, for the VIX
  *level*, using Robinson's parametric test and a local Whittle estimator.
- **Changes in the VIX are anti-persistent in normal times.** Daily H is 0.41–0.46 in every
  period (below 0.5 means a rise tends to be followed by a fall). Monthly H is 0.36 before
  the crisis and 0.47 after it, but 0.70 during 2007–09.
- **The level is mean-reverting but highly persistent.** Estimates of d for the level sit
  between 0.5 and 1 in most cases (non-stationary but mean-reverting). In the crisis
  sub-period d is near 1 and a unit root cannot be rejected (for example 0.88 daily and
  0.96 monthly in the uncorrelated-errors model; 0.96–1.08 daily with the semiparametric
  estimator). Before and after the crisis d is clearly below 1.
- **The authors' reading.** Fear normally overshoots and corrects, but in a crisis it feeds
  on itself. They suggest this may help explain bubbles and anti-bubbles, and that the
  anti-persistence could be traded.

## Why it's in the library

It puts a number on something the VIX notes take for granted: volatility spikes revert in
calm markets but stop reverting in a crisis. That matters for anyone who sells volatility
after a spike or sizes a hedge from the VIX's usual half-life.

The evidence is thin, and the note should be read with these limits in mind:

- One crisis (2007–09) defines the "crisis regime", with three years of data and 36 monthly
  points. The monthly confidence intervals are wide (crisis d from 0.68 to 1.52).
- No trading test is run, so the claim that anti-persistence offers abnormal profits is not
  shown.
- The paper writes the link between H and d as H = d − 0.5. The usual relation is
  H = d + 0.5, which is what makes the level results (d between 0.5 and 1) and the return
  results (H below 0.5) consistent with each other.
- The review calls Black Monday 1987 a "flash crash"; it was a one-day crash, not a flash
  crash in the 2010 sense.

## Links

- [[marabel-2011-volatility-regimes-for-the-vix-index]] — the same idea modelled directly:
  the VIX as a two-regime Markov-switching process
- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — how the VIX is
  built and where its level is biased
- [[carr-wu-2017-leverage-effect-volatility-feedback-and-self-exciting-market-disruptions]] —
  self-exciting jumps, one mechanism by which volatility stops mean-reverting in a crisis
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — a manager's case
  that the VIX's own distribution is changing
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — volatility suppression that holds until
  a shock reverses it
