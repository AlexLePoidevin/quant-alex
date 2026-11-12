# V-shapes

| | |
|---|---|
| **Authors** | Maria Flora; Roberto Renò (University of Verona) |
| **Year** | 2020 (working paper dated 17 September 2020) |
| **Type** | Working paper, SSRN 3554122, 38pp |
| **PDF** | Not hosted in this repository (SSRN download with no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22V-shapes%22+Flora) for the title and authors |
| **BibTeX** | `flora2020vshapes` |
| **Status** | Reference: §2 (why volatility and jumps can't detect inefficiency), §3 (the V-statistic), §5 (SPY 2019–2020) and §6 (Italian bonds, May 2018) carry the paper |

## What it is

A test for one specific kind of market failure: a price that runs away from fundamentals
and then comes back. The authors call this a V-shape (a Λ-shape for a transient surge)
and define it by the **drift** changing sign suddenly, not by volatility or jumps.

- **Why not volatility?** In their stylised model the traded price is the efficient
  price plus a friction term plus noise. A perfectly efficient market that gets news jumps
  to the new level and its volatility spikes. A frictional but working market drifts
  smoothly to the new level ("gradual jump") and its volatility also spikes. Only the
  inefficient market overshoots and comes back. Volatility and jumps appear in all
  three, so they can't tell them apart. A drift that flips sign can (Proposition 1).
- **The V-statistic.** Building on Christensen, Oomen and Renò's drift-burst test, they
  compute a kernel-weighted drift-to-volatility t-statistic on the left of a time point
  and another on the right, and multiply them (scaled by √bandwidth). Same-sign drifts
  (a trend) make it positive. A sign flip (a V or Λ) makes it negative. The bandwidth is
  read as the duration of the inefficiency. Theorem 1 shows it diverges only when the
  drift explodes on both sides, and goes to zero for a one-sided gradual jump.
- **Confidence bands.** The asymptotic null (product of two normals) is too loose for
  real data and for testing many points at once. They bootstrap instead, from zero-drift
  simulations of an EGARCH(1,1) fitted to the data, which keeps stochastic volatility in
  the null.
- **Simulations.** At 1% the test rejects about 1% under pure Brownian motion and under a
  jump or gradual jump with no news, and 11.6%–87.4% under the V-shape models depending
  on volatility and whether fundamentals also moved.
- **May 6, 2010.** On E-mini S&P 500 futures the minimum V-statistic is −24.6. The
  bootstrap probability that a pure volatility move produced it is about 0.006%.
- **SPY, January 2019 to August 2020 (408 days, 1-second grid).** At the Covid low (23
  March 2020) the V-statistic is only borderline at the 5% level, so the authors can't call
  the crash itself inefficient beyond 30 minutes. Across the sample, with a 30-minute
  bandwidth, there are 35 days significant at 5% (20 expected by chance), 28 of them
  V-shapes, and 11 at 1% (4 expected), 10 of them V-shapes. More appear at 5- and
  1-minute bandwidths. Returns after a V's low are significantly positive for up to four
  hours.
- **Italian government bonds, 29 May 2018.** A political shock (cabinet formation) hit
  just before Treasury auctions on 28–30 May. Five bonds show significant V-statistics
  (p-values 1.5%–9.8%) with a two-day bandwidth. Realized volatility, an Amihud-type
  price-impact measure, the Roll spread and quoted bid–ask spreads all spike and stay
  high for weeks. A three-regime Markov-switching model, used to price what a working
  market would have paid, puts the loss to the Treasury on the three bonds auctioned on
  30 May at about €434m (range €250m–650m). That is roughly what Lou et al. estimate the
  US Treasury loses to auction concessions in a whole year.

## Why it's in the library

**It separates two things that tail-risk measures lump together.** A large, fast price
move can be the market working (news priced quickly) or the market failing (overshoot
and reversal). Volatility, jumps and drawdown measures see both as risk. The V-statistic
picks out the second, which is the one where someone forced to trade at the low gives
wealth to whoever supplies liquidity.

**It makes "flash crash" a testable statement.** Instead of eyeballing a chart, the
statistic gives a duration (the bandwidth) and a bootstrap p-value. The SPY result is a
useful calibration: in a liquid index ETF, V-shapes are frequent but short (under 30
minutes), and even the March 2020 crash doesn't register as one at longer horizons.

**It ties the reversal to liquidity theory.** The paper reads the Italian episode through
Grossman–Miller: a large sale into a market with few, risk-averse market makers needs a
price concession that is reversed later. Fragmented bond markets and auction supply make
the reversal last days instead of minutes.

**It's a working paper with one case study.** The wealth-transfer figure depends on a
regime-switching counterfactual, and the bootstrap null depends on EGARCH fitting the
volatility well. The software is available only on request.

## Links

- [[merton-1976]] — jumps in prices: the paper's argument is that a jump on its own is
  consistent with an efficient market, and only a reversing drift is not
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — a practitioner's account of how
  forced, volatility-driven selling turns shocks into crashes
- [[rockafellar-uryasev-2000]] — CVaR measures the size of the loss, not whether the price
  that caused it was efficient
- [[poitras-2012-what-happened-may-6-2010-anatomy-of-the-flash-crash]] — the 6 May 2010 event the V-statistic is tested on
- [[kim-et-al-2021-investigation-of-flash-crash-via-topological-data-analysis]] — a topological anomaly score on the same day
