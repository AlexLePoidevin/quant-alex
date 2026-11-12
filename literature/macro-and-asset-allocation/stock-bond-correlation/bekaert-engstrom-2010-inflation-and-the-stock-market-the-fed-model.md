# Inflation and the Stock Market: Understanding the "Fed Model"

| | |
|---|---|
| **Authors** | Geert Bekaert (Columbia, NBER), Eric Engstrom (Federal Reserve Board) |
| **Year** | 2010 (the copy is the April 2009 SSRN draft) |
| **Type** | Journal article, *Journal of Monetary Economics* 57(3), 278–294, doi:10.1016/j.jmoneco.2010.02.004. Working paper version 40pp |
| **PDF** | Not hosted in this repository (SSRN draft, no open licence) |
| **Find it** | [doi.org/10.1016/j.jmoneco.2010.02.004](https://doi.org/10.1016/j.jmoneco.2010.02.004) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Inflation+and+the+Stock+Market%3A+Understanding+the+%22Fed+Model%22%22+Bekaert) |
| **BibTeX** | `bekaert2010fedmodel` |
| **Status** | Reference: §1, §3.2 and Table 2 (US decomposition), §4 (20-country test) and §6 carry the results |

## What it is

An explanation of why the dividend yield on US stocks moves so closely with the nominal
10-year Treasury yield, the regularity practitioners call the "Fed model".

- **The puzzle.** Over 1968Q4–2007 the correlation between the two yields is 0.78 (90%
  bootstrap interval 0.34–0.90). Yet 55% of the bond yield's variance is expected
  inflation, a nominal quantity, while 80% of the equity yield's variance is the equity
  risk premium, a real one. For them to co-move, expected inflation must move with the
  equity premium.
- **The usual answer is money illusion.** Modigliani and Cohn (1979), and later Campbell
  and Vuolteenaho, argue that investors discount real cash flows at nominal rates, so
  stocks are underpriced when inflation is high.
- **This paper's answer is risk.** A nine-variable VAR (Campbell–Shiller decomposition,
  survey inflation expectations, a Campbell–Cochrane habit measure of risk aversion and
  forecaster disagreement about GDP growth as economic uncertainty) finds that 79% of the
  yields' comovement runs through the equity premium. About 86% of the premium's
  covariance with expected inflation is spanned by risk aversion and uncertainty, which
  are high when inflation is high. The unexplained remainder, the most money illusion can
  account for, is about 10%.
- **Stagflation is the link.** In US data high inflation has tended to arrive with
  recessions, when uncertainty and risk aversion push equity premiums up.
- **An out-of-sample check across countries.** In 20 countries (1987–2005), the
  equity-bond yield correlation is higher where stagflation is more frequent (cross-country
  correlation 0.50). Inflation on its own loses significance once stagflation is included.
  The authors flag the small sample and pre-estimated regressors and use a Monte Carlo to
  correct the t-statistics.
- **2008–09 fits.** A recession with low expected inflation gave very low equity–bond yield
  correlations, as the story predicts.

## Why it's in the library

**It explains the macro regime behind the stock–bond correlation.** Stocks and bonds move
together when inflation shocks and recessions coincide, and apart when recessions arrive
with low inflation. That is the stagflation-versus-growth-shock distinction the other
notes in this folder rely on.

**It is a caution about the Fed model as a valuation tool.** The correlation is real, but
it comes from risk premiums that rise with stagflation, not from stocks being mispriced
against bonds. Comparing the earnings yield with the bond yield therefore says little
about whether stocks are cheap.

**The result rests on one quarterly sample and a residual.** The equity premium is backed
out as what cash flows and real rates don't explain, and the VAR is large for 157
quarters. The robustness checks (VAR(2), zeroed coefficients, other uncertainty proxies,
earnings instead of dividends) leave the main split intact.

## Links

- [[campbell-pflueger-viceira-2020-macroeconomic-drivers-of-bond-and-equity-risks]] — the stock–bond correlation tied to monetary-policy regimes
- [[zeng-zhao-2022-expectation-driven-term-structure-of-equity-and-bond-yields]] — equity and bond yields modelled jointly from expectations
- [[brixton-thapar-maloney-2021-when-stock-bond-diversification-fails]] — the inflation regimes in which stocks and bonds fall together
- [[fang-liu-roussanov-2022-getting-to-the-core-inflation-risks-across-asset-classes]] — which component of inflation (core or energy) moves stocks and bonds together
- [[calderini-skilton-2021-macro-economic-drivers-of-the-bond-stock-correlation]] — a practitioner decomposition of the stock–bond correlation into growth, policy and risk-premium shocks
- [[burkhardt-hasseltoft-2012-understanding-asset-correlations]] — a rational, regime-switching explanation for why the Fed-model correlation flipped sign after 2000
