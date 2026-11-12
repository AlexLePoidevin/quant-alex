# Increased Tail Dependence in Global Public Real Estate Markets

| | |
|---|---|
| **Authors** | Yang Deng (Sun Yat-sen University), Helen X. H. Bao (Cambridge), Pu Gong (Huazhong University of Science and Technology) |
| **Year** | 2018 (SSRN 3162813; the paper is undated, with data to 2014) |
| **Type** | Working paper, 24pp. Daily real estate and stock indices for seven countries, March 2000 – December 2014 |
| **PDF** | Not hosted in this repository (SSRN working paper, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3162813](https://doi.org/10.2139/ssrn.3162813) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Increased+Tail+Dependence+in+Global+Public+Real+Estate+Markets%22+Deng) |
| **BibTeX** | `deng2018realestate` |
| **Status** | Reference: Tables 5–7 (tail dependence by sub-period) and Figure 2 (time-varying estimates) carry the results |

## What it is

A copula study of how often listed real estate markets crash (and boom) together, before,
during and after the 2007–09 crisis.

- **Data.** Daily listed real estate indices and the main stock index for the US, Hong
  Kong, Japan, Australia, Singapore, the UK and France, about 3,850 days. Returns are
  fat-tailed and skewed in every market.
- **Method.** Each return series is filtered with an AR(1)-GJR-GARCH(1,1) model, the
  residuals are turned into uniform ranks with their empirical distribution, and pairs are
  linked with the symmetrised Joe–Clayton copula, which gives separate upper- and
  lower-tail dependence coefficients (the probability that one market is extreme given the
  other is). The authors also fit Patton's time-varying version. The SJC copula beats the
  Gaussian copula on AIC for 19 of 21 pairs.
- **Real estate against real estate.** Of 21 country pairs, only 2 showed upper-tail and
  4 lower-tail dependence in 2000–2006. In 2007–2009 the counts rose to 12 and 15, and in
  2010–2014 lower-tail dependence spread to 19 pairs. So the crisis made joint crashes far
  more common and the change did not reverse. Within-region pairs are the most dependent
  (UK–France reaches 0.54 upper and 0.61 lower tail dependence during the crisis), while
  the US stays tail-independent of most other markets even in the crisis.
- **Two peaks.** The time-varying estimates show lower-tail dependence peaking in
  2008–2009 and again in 2011–2012, the second presumably the European debt crisis, and in
  Asian pairs as well as European ones.
- **Mixed assets.** A country's stocks and its own listed real estate are tail-dependent
  throughout, more so after 2007 everywhere except Hong Kong. Stocks in one country
  against real estate in another are much less dependent, and the post-crisis increase is
  smaller. The authors' conclusion: real-estate-only international portfolios lost most
  of their crash protection, while mixing stocks and real estate across regions still
  diversifies.

## Why it's in the library

**It is a clear example of diversification failing exactly when it is needed.** Linear
correlations can stay modest while the chance of joint crashes rises sharply, and here it
rose and stayed high after the crisis.

**It shows the copula toolkit applied end to end.** GARCH filtering, empirical margins,
an asymmetric copula with separate upper and lower tails, and a time-varying version: the
same pipeline used elsewhere for equities and FX.

**Limits.** The crisis dating is the authors' choice, though the time-varying estimates
broadly agree with it. The UK's REIT regime only started in 2007, so its earlier series
is a property-stock index rather than REITs. Results are dependence coefficients, not a
portfolio test. One passage cites Table 6 for counts that only fit Table 7 (the 42
cross-country pairs), apparently a labelling slip.

## Links

- [[hartmann-straetmans-de-vries-2004-asset-market-linkages-in-crisis-periods]] — joint crashes across stock and bond markets measured with extreme-value methods
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — why dependence in the tails, not average correlation, is what breaks portfolios
- [[nelsen-2006-introduction-to-copulas]] — the copula theory, including tail dependence
- [[ang-chen-2002]] — asymmetric correlations in falling markets
