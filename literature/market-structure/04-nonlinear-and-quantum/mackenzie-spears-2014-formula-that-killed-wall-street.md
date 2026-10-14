# 'The Formula That Killed Wall Street': The Gaussian Copula and Modelling Practices in Investment Banking

| | |
|---|---|
| **Authors** | Donald MacKenzie, Taylor Spears (University of Edinburgh) |
| **Year** | 2014 (manuscript dated 2013) |
| **Type** | Journal article — *Social Studies of Science* 44: 393–417. Author manuscript, 44pp |
| **Data** | 114 interviews with credit-market participants (29 with quants, 29 conducted before the 2007 crisis); technical literature, mainly *Risk* magazine; Vasicek's private papers; email exchanges with David X. Li |
| **PDF** | `mackenzie-spears-2014-formula-that-killed-wall-street.pdf` (in this folder) |
| **BibTeX** | `mackenzie2014formula` |
| **Status** | Reference |

## What it is

A history of the Gaussian copula family of credit models, written by sociologists of
finance. It responds to Felix Salmon's 2009 *Wired* piece that blamed Li's formula for the
crisis. This is the first of two companion papers. It covers how the models were built;
the companion paper covers their role in the crisis.

The lineage:

1. **Vasicek, 1987–91 (KMV):** the *large homogeneous pool* model. Asset values follow
   geometric Brownian motion and share one pairwise correlation ρ. As the number of loans n
   goes to infinity, the loss fraction L satisfies
   P[L ≤ x] = N( (√(1−ρ)·N⁻¹(x) − N⁻¹(p)) / √ρ ).
   Gaussian dependence was chosen because it was the most familiar option, not because data
   supported it: "there was almost no direct empirical data to guide his modelling."
2. **CreditMetrics, J.P. Morgan 1997:** the same framework, computed by Monte Carlo with
   correlated normal random numbers. It is one-period, and was recognised as a Gaussian
   copula only later.
3. **Li, 1999–2000:** borrowed the copula from actuarial science. Frees, Carriere & Valdez
   (1996) had used copulas for "broken heart" joint mortality in annuity pricing. Li applied
   the same idea to default as death, coupling the survival-time distribution of each firm
   (taken from CDS and bond prices) into a joint distribution. The Gaussian copula won
   because it was continuous with CreditMetrics and easy to simulate, not because it fit the
   data. The paper notes that the Zürich group (Embrechts, McNeil & Straumann, 1999) was
   already warning that correlation has pitfalls.
4. **Semi-analytic one-factor copulas, 2001–03:** Gregory & Laurent at BNP, and Andersen,
   Sidenius & Basu at Bank of America. Conditional on one common factor ("the state of the
   economy"), defaults are independent. This removed the need for Monte Carlo. The driver was
   computing power: daily delta hedging of synthetic CDO tranches with CDS needed fast
   models, and banks were limited by overnight run times, air-conditioning and the London
   power supply.
5. **Implied and base correlation, 2003–05:** standardised index tranches (TRAC-X, CDX)
   gave market prices, so correlation was backed out of prices instead of being estimated.
   Correlation became something traders traded. Compound correlation sometimes produced two
   solutions or none. J.P. Morgan's *base correlation* (cumulative 0–x% tranches) fixed that
   and became the industry standard.

The sociological argument is that the Gaussian copula was **not** a product of
derivatives-desk no-arbitrage culture, the risk-neutral pricing tradition of Black–Scholes
and Harrison–Kreps–Pliska. The quants were *bricoleurs* who used what worked within
organisational and hardware limits, and many distrusted the model privately. A model that
"fits the market exactly" after calibration was treated as validated. Empirical data played
little part in the story.

## Why it's in the library

**It shows correlation becoming the whole model.** Vasicek's figures (p = 0.02, ρ from
0.01 to 0.99) show the loss distribution changing from a tight peak to a bimodal shape as
correlation rises. At high ρ the pool behaves like a single asset. That is the credit
version of the variance-concentration story in the spectral-decomposition piece. Expected
loss stays the same, and the whole tail is set by one dependence parameter.

**The one-factor Gaussian copula is a single-factor covariance model.** Conditional
independence given one common factor is the credit equivalent of PC1 as the market mode.
The model's weakness is the one [[munnix-schafer-2011-copula-dependencies]] measures
in equities: a Gaussian copula has zero tail dependence (Nelsen §5.4), so a correlation
parameter fitted in normal times says nothing about joint defaults in a crash. This is the
historical case of what the elliptical-trap argument warns about.

**It is a case study in calibration being mistaken for validation.** Backing out an implied
correlation that reproduces market prices exactly tells you nothing about whether the
model's dependence structure is right. The base-correlation skew was itself evidence of
misspecification. The same applies to any backtest fitted to its own evaluation window
(`docs/BACKTEST_CRIMES.md` in Vinland Saga makes the same point).

**It corrects the popular story.** Salmon's version, one formula and one author, is too
simple. The authors note that the main channel into the crisis ran through *simpler* uses
of the Gaussian copula, at the rating agencies and in ABS CDOs, rather than the
sophisticated investment-bank models. The details are in the companion paper.

## Links

- [[nelsen-2006-introduction-to-copulas]] — Sklar's theorem and the tail-dependence result
  the Gaussian copula fails
- [[wikipedia-copula-statistics]] — the Gaussian copula density and the brief 2008 note
  this paper supplies the history for
- [[munnix-schafer-2011-copula-dependencies]] — equity tail dependence measured above the
  Gaussian copula's
- [[finance-tutoring-2024-sklar-theorem]] — the informal theorem Li's application rests on
- [[laloux-et-al-1999]], [[bouchaud-potters-2009]] — the equity-correlation view of the
  same one-factor structure
