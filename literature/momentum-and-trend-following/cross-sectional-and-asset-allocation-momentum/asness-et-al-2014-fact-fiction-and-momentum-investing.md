# Fact, Fiction and Momentum Investing

| | |
|---|---|
| **Authors** | Clifford S. Asness, Andrea Frazzini, Ronen Israel (AQR); Tobias J. Moskowitz (Chicago Booth) |
| **Year** | 2014 (draft dated 9 May 2014) |
| **Type** | Journal article, *Journal of Portfolio Management* 40(5), 75–92 (40th anniversary issue). Doi 10.3905/jpm.2014.40.5.075. 26pp |
| **PDF** | Local copy only (author draft; no open licence) |
| **BibTeX** | `asness2014factfiction` |
| **Status** | Reference: Tables 1–5 (Kenneth French data, 1927–2013) carry the evidence; the rest is argument from cited papers |

## What it is

A myth-busting essay on cross-sectional equity momentum: winners minus losers, measured as
the past twelve-month return skipping the most recent month. It takes ten common criticisms
and answers each with the simplest public data (Kenneth French's UMD factor and its long and
short legs) plus the authors' own published work.

- **"Too small and sporadic."** Over 1927–2013, UMD earned 8.3% a year gross (Sharpe 0.50),
  against 4.7% for value (HML, 0.39) and 2.9% for size (SMB, 0.26). Since publication
  (1991–2013) it still earned 6.3% (0.36). It was positive in 81% of rolling one-year
  windows. A 60/40 HML/UMD mix had a Sharpe ratio of 0.80.
- **"Only works on the short side."** On market-adjusted returns, the long side contributed
  5.5% and the short side 5.1% of UMD's 10.6% over 1927–2013, roughly half each in every
  subperiod. So long-only investors can capture it.
- **"Only works in small caps."** UMD earned 9.8% in small caps and 6.8% in large caps.
  The authors point out that the size dependence is much stronger for value (5.9% against
  3.5%). Over 1991–2013, value among large caps had a Sharpe ratio of 0.06 against 0.51 in
  small caps, while momentum had 0.24 against 0.45.
- **Costs and taxes.** These rely on cited work rather than new tests. Frazzini, Israel and
  Moskowitz's real execution data put momentum's per-dollar trading costs low enough that it
  survives them. Its tax burden is about the same as value's, because momentum realises
  losses short-term and gains long-term, while value carries dividend income.
- **Crashes and volatility.** Momentum's worst drawdown was −77%, with its sharpest crashes
  in 1932 and 2009, against −43% for value, but only −30% for the 60/40 value–momentum mix. Citing Daniel and
  Moskowitz, they place the crashes in sharp rebounds after bear markets, when the short leg
  is full of beaten-down, high-beta stocks.
- **"No theory."** Both risk-based and behavioural explanations exist (underreaction,
  delayed overreaction). The authors say neither is settled, and that the same is true of
  size and value.

## Why it's in the library

It is the standard short reference for what cross-sectional momentum is, how big it has
been, and which objections hold up. Two points matter most in practice:

- **It is a portfolio component, not a standalone bet.** The −77% drawdown is real. The
  case rests on combining momentum with value, whose crashes fall at different times.
- **Read the authors' position honestly.** AQR runs momentum strategies, the tone is
  advocacy, and the cost and tax rebuttals depend on AQR's own execution data, which
  outsiders cannot check. The return tables are reproducible from French's site; the
  implementability claims are not.

It also defines the line between cross-sectional momentum (relative to peers) and trend
following (an asset against its own past), which the time-series notes in this section rely on.

## Links

- [[kelly-moskowitz-pruitt-2021-understanding-momentum-and-reversal]] — momentum's returns explained by predictable changes in stocks' factor exposures
- [[arnott-et-al-2019-alices-adventures-in-factorland]] — a sceptical counterpoint on factor returns after publication and factor crashes
- [[ilmanen-et-al-2021-how-do-factor-premia-vary-over-time]] — a century of evidence on momentum and other factor premia across asset classes
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — time-series momentum (trend), the absolute-return cousin of this strategy
