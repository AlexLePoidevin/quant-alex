# Econometric Tests of Asset Price Bubbles: Taking Stock

| | |
|---|---|
| **Authors** | Refet S. Gürkaynak (Federal Reserve Board at the time) |
| **Year** | 2008 (Journal of Economic Surveys 22(1), 166–186); the copy here is FEDS Working Paper 2005-04, January 2005, 34pp |
| **Type** | Survey paper |
| **PDF** | Not hosted in this repository (Federal Reserve Board staff working paper with no stated licence; the journal version is Wiley) |
| **Find it** | [doi.org/10.1111/j.1467-6419.2007.00530.x](https://doi.org/10.1111/j.1467-6419.2007.00530.x) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Econometric+Tests+of+Asset+Price+Bubbles%3A+Taking+Stock%22+G%C3%BCrkaynak) |
| **BibTeX** | `gurkaynak2008bubbles` |
| **Status** | Reference: §3 (the tests) and §4 (conclusion) |

## What it is

A survey of econometric tests for *rational* bubbles in stock prices: prices above the
present value of expected dividends that investors pay because they expect to sell higher.
Its answer to "can a bubble be detected?" is no, not with any confidence.

- **Variance-bounds tests** (Shiller; LeRoy–Porter). They show prices are more volatile than
  the constant-discount-rate model allows, but were not designed to identify a bubble.
- **West's two-step tests.** Estimate the dividend process and the discount rate separately,
  then attribute any gap to a bubble. They find one only after ruling out every other
  misspecification, and expected regime changes in fundamentals look the same in the data.
- **Unit-root and cointegration tests** (Diba–Grossman). A bubble cannot start after trading
  begins, so it would make prices more non-stationary than dividends; they find prices and
  dividends cointegrated, so no bubble. Evans (1991) shows these tests almost never detect
  a bubble that periodically collapses to a small value and regrows.
- **Regime-switching tests of collapsing bubbles.** Different switching specifications give
  different answers on the same S&P 500 data.
- **Intrinsic bubbles** (Froot–Obstfeld). A bubble tied to the level of dividends fits the
  nonlinear price–dividend relation, but Driffill and Sola show that regime-switching
  dividends with no bubble fit equally well.
- **The bubble as an unobserved component** (Wu). The estimated bubble is often negative,
  which theory rules out, so it is picking up model failure.

## Why it's in the library

**It is the standard reference for the joint-hypothesis problem in bubble detection.**
Every test is a test of "no bubble *and* this model of fundamentals". For almost every paper
that finds a bubble there is another that fits the data as well without one. What the tests
do establish is where the simple present-value model fails.

**It covers rational bubbles only.** Behavioural and inefficient-market accounts, and the
later right-tailed unit-root tests of Phillips and co-authors, are outside its scope.

## Links

- [[west-1988-bubbles-fads-and-stock-price-volatility-tests]] — the earlier survey of the volatility tests this one starts from
- [[schatz-sornette-2020-inefficient-bubbles-and-efficient-drawdowns]] — a framework that defines bubbles through market inefficiency and a crash, to avoid the joint-hypothesis problem
- [[bashchenko-marchal-2020-deep-learning-for-asset-bubbles-detection]] — detecting bubbles from the volatility function alone, without a model of fundamentals
- [[campbell-1991]] — time-varying expected returns, the main non-bubble explanation of price swings
- [[phillips-shi-2018-real-time-monitoring-of-asset-markets-bubbles-and-crises]] — the recursive explosive-root test that became the standard real-time bubble detector after this survey
