# Dispersion Trading (Lecture 10)

| | |
|---|---|
| **Authors** | Marco Avellaneda (NYU Courant Institute) |
| **Year** | 2009 (Spring semester, course G63.2936.001) |
| **Type** | Slides, 41pp. Lecture notes from a graduate course; the backtest slides reuse material from about 2001–2004 |
| **PDF** | Local copy only (course slides with no licence) |
| **BibTeX** | `avellaneda2009dispersion` |
| **Status** | Reference: the gamma P&L decomposition is the core; the Monte Carlo signal model and backtests are summarised briefly on the slides |

## What it is

Lecture slides on trading index options against options on the index's components.

- **The trade.** Sell index options and buy options on the components (or the reverse),
  delta-hedging the whole package with stock. Selling index volatility and buying component
  volatility is a bet that the components will move more independently than the index
  options price in. It is to options what index arbitrage is to stocks.
- **The fair-value relation.** Index variance is the weighted sum over pairs of component
  volatilities times their correlations: σ_I² = Σ p_i p_j σ_i σ_j ρ_ij. So index implied
  volatility carries an implied correlation, and dispersion trades that against realized
  correlation.
- **Intrinsic-value hedge.** Because max(I − K, 0) ≤ Σ w_i max(S_i − K_i, 0), a basket of
  component calls weighted like the index super-replicates the index call. It is exact only
  if the stocks are perfectly correlated. Choosing component strikes with equal
  log-moneyness (the same trick as Jamshidian's bond-option decomposition) gives roughly
  equal deltas.
- **Where the P&L comes from.** For each option, daily P&L ≈ θ × (n² − 1), with n the
  day's move in standard deviations. Summing over the package splits the gamma P&L into
  three parts: an **idiosyncratic** term (single stocks moving more or less than their
  implied volatilities), a **dispersion** term (cross-sectional spread of moves around the
  index, against implied correlation), and time decay. A "pure" long-dispersion package
  sets the idiosyncratic gamma to zero, leaving a bet on dispersion alone.
- **The risk profile.** Short index against long components is short gamma when all stocks
  move together and long gamma for moves that pull them apart. It loses on a large
  correlated move and gains when correlation falls. The slides add sensitivity to
  correlation ("rega") and to a uniform shift in volatilities.
- **A trading model.** Build a proxy for the index (by regression or by truncating at a
  capitalization level), calibrate a weighted Monte Carlo of the components to all their
  listed options (876 constraints for the 35-stock Morgan Stanley High-Tech index, Dec
  2000), price the index options with it and trade when the market's bid or offer is far
  from the model value. Backtests on OEX and QQQ for 2001–2003, targeting 1% daily
  volatility and including costs, are shown as P&L charts and a capacity estimate of
  roughly $100–200 million.

## Why it's in the library

**It makes implied correlation tradeable and shows exactly what you are exposed to.** The
gamma decomposition separates the single-stock volatility bet from the correlation bet,
which is the part people usually mean by dispersion.

**It shows that short correlation is crash risk.** A short-index, long-components book
loses on large moves in which everything falls together. Correlations rise in down markets
([[ang-chen-2002]]), so the trade's worst days arrive with the market's worst days. The
slides' risk charts make this visible.

**The backtests are illustrative.** They come from lecture slides on an early-2000s
sample, with few details of fills or option liquidity. Treat them as a demonstration of
the method, not evidence that the edge still exists.

## Links

- [[bossu-strasser-guichard-2005-just-what-you-need-to-know-about-variance-swaps]] — the
  same trade done with variance swaps, where the correlation exposure is cleaner
- [[ang-chen-2002]] — correlations rise in down markets, which is when short dispersion
  loses
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — what happens when a book is built
  on a correlation that breaks in a crisis
- [[plerou-et-al-2002]] — the market mode that dominates stock correlations, the factor a
  dispersion trade is short
- [[avellaneda-zhang-2010]] — the same author on another path-dependent volatility effect
- [[bloch-2016-a-practical-guide-to-quantitative-volatility-trading]] — a long practitioner treatment of dispersion trading, implied correlation and its model risks
