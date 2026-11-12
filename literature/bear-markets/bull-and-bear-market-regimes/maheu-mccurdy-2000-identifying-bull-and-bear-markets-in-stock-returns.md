# Identifying Bull and Bear Markets in Stock Returns

| | |
|---|---|
| **Authors** | John M. Maheu (University of Alberta), Thomas H. McCurdy (University of Toronto) |
| **Year** | 2000 |
| **Type** | Journal article, *Journal of Business & Economic Statistics* 18(1), 100–112. doi:10.1080/07350015.2000.10524851 |
| **PDF** | Not hosted in this repository (scanned journal version, "reproduced with permission of the copyright owner") |
| **Find it** | [doi.org/10.1080/07350015.2000.10524851](https://doi.org/10.1080/07350015.2000.10524851) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Identifying+Bull+and+Bear+Markets+in+Stock+Returns%22+Maheu) |
| **BibTeX** | `maheu2000bullbear` |
| **Status** | Reference: Table 5 (estimates), Figures 2–3 (filtered bull probabilities) and §5 (discussion of duration dependence) carry the results |

## What it is

A two-state Markov-switching model of monthly US stock returns, 1834–1995, in which the
chance of leaving a state depends on how long the market has been in it.

- **Data.** Monthly total returns from Schwert's series (1834–1925) joined to the CRSP
  value-weighted index (1926–1995). The sample starts in 1834 because volatility before
  then is much lower, which would need a third state.
- **The models.** Returns follow an AR(5) whose mean and variance depend on a hidden state.
  The probability of staying in a state is a logistic function of how many months the
  state has lasted, up to a cap τ chosen by likelihood (12 to 16 months). Four versions add
  state-dependent variance, ARCH, and finally duration inside the mean and variance
  themselves (DDMS-DD).
- **Bull and bear.** The two states sort cleanly into a high-return, low-volatility state
  (labelled bull) and a low-return, high-volatility state (labelled bear). In the
  state-dependent-variance model, monthly volatility is 3.6% in the bull state and 10.2% in
  the bear state. The market spends about 90% of the time in the bull state.
- **Duration dependence.** In both states the chance of switching out falls the longer the
  state has lasted: bull markets gain momentum. In the DDMS-ARCH model a bear market only
  becomes persistent after four consecutive months in it.
- **Gains come early.** In the most general model the expected monthly return in a bull
  market is 2.78% in its first month and falls to 0.68% if the bull market lasts 16 months.
  Bear-market volatility rises with duration.
- **Dating.** The filter puts the turn before the 1929 crash in May 1929, with the bear
  state lasting to May 1934. It also flags 1987, the rest of the 1930s, 1855, 1860–61, 1907 and
  1974.
- **Robustness.** Results hold in the sub-samples 1834–1925, 1926–1995 and 1947–1995,
  though duration dependence in switching is not significant in 1947–1995.

## Why it's in the library

- **The classic statistical definition of a bear market.** Bull and bear states fall out of
  the data, as a high-return calm state and a low-return volatile state, rather than being
  defined by a 20% rule. Volatility does most of the work in telling them apart, which is
  why later work keeps finding volatility to be the best regime signal.
- **"The best gains come at the start of a bull market."** This is a testable claim about
  timing: being out of the market at the turn from bear to bull is expensive.
- **What it is not.** The dating uses the full-sample smoother, so it uses future data. It
  shows what the regimes were, not that they could have been recognised in real time. The
  authors also say their results do not fully support a rational-bubble explanation of the
  duration effects.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — the same authors'
  later four-state version, with bull corrections and bear rallies, on weekly data to 2010
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a two-state
  bull/bear model turned into an optimal trend-following rule
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — two-regime switching applied to
  the VIX
- [[ang-chen-2002]] — asymmetric correlations in down markets, another way bear and bull
  states differ
- [[blitz-2021-the-quant-cycle]] — bull and bear stages for equity factors rather than the market
- [[mcgee-2021-can-market-regimes-really-be-timed-with-historical-volatility]] — whether recent volatility, the feature that separates the states here, can time the market in real time
