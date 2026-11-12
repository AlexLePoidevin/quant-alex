# The Myth of Diversification Reconsidered

| | |
|---|---|
| **Authors** | William Kinlaw, Mark Kritzman, Sébastien Page and David Turkington (State Street Associates, Windham/MIT, T. Rowe Price) |
| **Year** | 2021 |
| **Type** | Journal article, *Journal of Portfolio Management* 47(8), 124–137 |
| **PDF** | Not hosted in this repository (JPM reprint; reproduction prohibited without the publisher's permission) |
| **Find it** | [doi.org/10.3905/jpm.2021.1.273](https://doi.org/10.3905/jpm.2021.1.273) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Myth+of+Diversification+Reconsidered%22+Kinlaw) |
| **BibTeX** | `kinlaw2021myth` |
| **Status** | Reference: read in full; Exhibits 3, 8 and 9 carry the argument |

## What it is

A correction to how downside correlation is usually measured, and an empirical map of
correlation asymmetry across six asset classes (monthly, 1976–2019; emerging markets from
1988).

- **What investors want.** Diversification when the main growth asset falls, and the
  opposite ("unification") when it rises. Mean–variance treats correlation as one symmetric
  number and so cannot tell these apart.
- **The artefact.** Correlations measured on a slice of the data fall mechanically even
  for a normal distribution. With a full-sample correlation of 0.50, conditioning on one
  asset being below its mean gives 0.33; conditioning on both being below gives 0.27; at a
  one-standard-deviation threshold, 0.25 and 0.18. Any "correlations go to one" claim has to
  be measured against these expected values.
- **The flaw in exceedance correlation.** Studies in the Longin–Solnik line (including
  Ang–Chen) condition on both assets doing badly, which throws away exactly the months when
  diversification worked: one asset down, the other up. The authors condition on the main
  asset alone.
- **What it changes.** For US and foreign equities (correlation 0.66) the two methods agree:
  correlation is higher than normal on the downside and lower on the upside, the
  undesirable kind (summary score 0.32). For US equities and corporate bonds the methods
  disagree: the joint method shows bad asymmetry, the single-asset method shows corporates
  decoupling on the downside. Conditioned on US equities, emerging and foreign equities and
  commodities are poor complements; Treasuries are the only asset that helps against every
  other asset class, with the caveat that near-zero rates in 2021 limit how far they can
  rally.
- **Using it.** A "full-scale" optimisation that maximises a utility with a sharp penalty
  below a 25% loss, run on simulated data, ends up holding more US equities and Treasuries
  and almost no commodities or corporate bonds than a mean–variance portfolio with the
  same 7% expected return, cutting the average loss beyond −25%.

## Why it's in the library

It is the measurement fix for a claim the crisis and diversification notes here keep
making: check the expected conditional correlation under normality before calling a
correlation shift real, and condition on the asset you are trying to hedge. That changes
which assets count as diversifiers, especially for low-correlation pairs. The empirical
results are in-sample over one long sample with a few dozen extreme months per threshold,
and the portfolio example uses illustrative expected returns, so the asset rankings are
descriptive, not a forecast.

## Links

- [[ang-chen-2002]] — the joint-exceedance correlation measure this paper argues against
- [[hartmann-straetmans-de-vries-2004-asset-market-linkages-in-crisis-periods]] — co-crash probabilities across stock and bond markets
- [[kinlaw-turkington-2014-correlation-surprise]] — the same authors on unusual co-movement as a warning signal
- [[markowitz-1952]] — the symmetric-correlation framework being qualified
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — what goes wrong when dependence is modelled as symmetric and normal
- [[brixton-thapar-maloney-2021-when-stock-bond-diversification-fails]] — when the stock–bond hedge itself breaks down
- [[page-panariello-2018-when-diversification-fails]] — the post-2008 update of the downside-correlation evidence across asset classes, hedge-fund styles and risk factors
