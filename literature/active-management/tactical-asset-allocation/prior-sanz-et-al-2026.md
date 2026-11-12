# The Long-Term Efficiency of Tactical Asset Allocation: Evidence from 86 Systematic Strategies (1995–2025)

| | |
|---|---|
| **Authors** | Francesc Prior-Sanz; Emili Vizuete-Luciano; Alexander Cruz-Zayash; Marc Ferrer-Canteli |
| **Year** | 2026 (October issue) |
| **Type** | Peer-reviewed — *International Review of Economics & Finance*, vol. 111, art. 105748 |
| **DOI** | [10.1016/j.iref.2026.105748](https://doi.org/10.1016/j.iref.2026.105748) |
| **Find it** | Use the link above, or [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Long-Term+Efficiency+of+Tactical+Asset+Allocation%3A+Evidence+from+86+Systematic+Strategies+%281995%E2%80%932025%29%22+Prior-Sanz) for the title and authors |
| **BibTeX** | `priorsanz2026taa` |
| **Status** | ⚠️ Not yet read — filed on sight |

## Why this is filed here

This is the only **peer-reviewed, large-sample** study in a folder otherwise made of
practitioner papers, blog posts and undisclosed rule-sets. Eighty-six systematic strategies
over **thirty years**, in a finance journal, is a different evidentiary object from a single
author backtesting a single rule on the window that happens to exist.

Two things make it directly relevant to the work in
`substack_posts/taa-series/`:

**It spans 1995–2025, so it contains the crashes ours does not.** Every backtest in the
series starts January 2009 — one month after the S&P bottomed — because Optimum 3 holds
SCZ, which did not trade until December 2007, and a twelve-month lookback pushes the first
signal to the end of 2008. These are crash-protection strategies tested on a sample with no
crash. A 1995 start covers the dot-com unwind and 2008, and whatever it reports about
drawdown behaviour in those episodes is evidence we cannot generate.

**Eighty-six strategies is a multiple-testing sample.** The single largest caveat on the
series is that each of these strategies was published *because* it backtested well, and
nothing in a careful reimplementation removes that. A study covering 86 of them at once can
speak to the cross-sectional distribution — how many survive out of sample, and by how
much — which is exactly the question an individual replication cannot answer.

## To check on reading

- Which strategies are in the 86, and whether the five here are among them
- Whether returns are reported net of costs, and at what rate
- How they handle ETF inception — index proxies, or start dates staggered per strategy
- Whether they deflate for multiple testing (DSR, PBO or equivalent), given the sample size
- The drawdown behaviour reported for 2000–02 and 2008 specifically

## Links

- [[keller-keuning-2016-paa]], [[keller-butler-2014-eaa]], [[gpm]], [[kda]], [[optimum3]] —
  the individual strategies this would put in context
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — why a 9–10 month moving-average window is optimal in a two-state bull/bear model of the S&P 500
