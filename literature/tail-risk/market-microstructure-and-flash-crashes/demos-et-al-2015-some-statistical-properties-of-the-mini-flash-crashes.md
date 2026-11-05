# Some Statistical Properties of the Mini Flash Crashes

| | |
|---|---|
| **Authors** | Guilherme Demos; Sergio Da Silva (Federal University of Santa Catarina); Raul Matsushita (University of Brasilia) |
| **Year** | 2015 |
| **Type** | Paper — *Mathematical Finance Letters* 2015:3, 19pp |
| **PDF** | `demos-et-al-2015-some-statistical-properties-of-the-mini-flash-crashes.pdf` (in this folder; open access, CC BY) |
| **BibTeX** | `demos2015mini` |
| **Status** | Reference — the concluding remarks list the five findings; Tables 2–6 hold the numbers |

## What it is

A descriptive study of the price series around 14 "mini flash crashes" in single US
stocks in 2011–2012 (Apple, Cisco, Citigroup, Jazz Pharmaceuticals, Pall and others),
plus the Dow Jones index on 6 May 2010. Each series covers a few days to a month around
the crash, sampled at roughly 370 observations a day from Bloomberg.

The paper reports five findings:

1. **Returns are not normal.** Normality is rejected for every series (Lilliefors,
   Cramér–von Mises, Jarque–Bera). Excess kurtosis ranges from about 7.6 (Pfizer) to 473
   (Jazz Pharmaceuticals).
2. **Tails follow power laws.** None of the series shows the exponential tail decay of a
   normal distribution. The Dow and three stocks have tail exponents inside the
   Lévy-stable range (below 2); Washington Post is close to the "cubic law" (exponent 3);
   Enstar is above 3.
3. **Chaos and log-periodicity "cannot be dismissed at first".** A Lyapunov-exponent
   stability test does not reject its null of chaos, and log-periodic power-law curves
   (Sornette's crash model) can be fitted to every series.
4. **On second thoughts, they are not good models.** Long memory is clear for only three
   stocks, and Shannon entropy values look like a random series rather than a
   deterministic one. That undercuts both chaos and log-periodicity.
5. **A threshold GARCH fits the data well but misses the tails.** Monte Carlo fits look
   good, yet the GARCH models don't reproduce the power-law tail decay, the entropy or
   the long memory of the individual stocks.

## Why it's in the library

**It shows what a crash does to return statistics.** Around a mini flash crash, a few
observations dominate everything: kurtosis in the hundreds, normality rejected at any
level, power-law tails. Any risk number estimated on a window that contains one of these
events is mostly a number about that event.

**It is a fair warning about fitting crash models.** The log-periodic fits all "work",
and the paper itself then finds reasons not to believe them. That is the general problem
with flexible crash-prediction curves fitted after the fact.

**Read the chaos result carefully.** Every largest Lyapunov exponent in Table 4 is
negative. A negative exponent means nearby paths converge, which is the opposite of
chaos. The paper's "cannot reject chaos" comes from a stability regression on those
exponents, not from finding positive ones. The data windows are also short, sampled at
roughly one-minute rather than true tick frequency, and each is chosen because it
contains a crash, so the tail estimates are conditional on that selection.

## Links

- [[pekar-pcolar-2022]] — normality rejected for daily index returns too, and which
  fat-tailed distributions fit best
- [[merton-1976]] — jumps as an explicit model for the discontinuities these series show
- [[mantegna-1999]] — econophysics on stock-market data, the tradition this paper works in
- [[flora-reno-2020-v-shapes]] — a test that decides whether a crash-and-rebound like
  these is an inefficiency rather than just a fat-tailed draw
- [[tee-ting-2019-cross-section-of-mini-flash-crashes]] — a large cross-section of mini flash crashes and which stocks suffer them
- [[li-deng-2007-machine-learning-approach-to-predict-turning-points]] — a forecasting paper that assumes the deterministic chaos this paper's Lyapunov estimates argue against
