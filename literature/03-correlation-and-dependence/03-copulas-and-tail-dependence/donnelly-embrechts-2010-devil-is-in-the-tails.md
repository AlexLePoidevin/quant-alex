# The Devil Is in the Tails: Actuarial Mathematics and the Subprime Mortgage Crisis

| | |
|---|---|
| **Authors** | Catherine Donnelly, Paul Embrechts (RiskLab, ETH Zürich) |
| **Year** | 2010 (manuscript dated 4 January 2010) |
| **Type** | Journal article — *ASTIN Bulletin* 40(1): 1–33, doi:10.2143/AST.40.1.2049222. Author manuscript from the Heriot-Watt repository, 30pp |
| **PDF** | `donnelly-embrechts-2010-devil-is-in-the-tails.pdf` (in this folder) |
| **BibTeX** | `donnelly2010devil` |
| **Status** | Reference |

## What it is

The mathematicians' answer to the "formula that killed Wall Street" story. Salmon's 2009
*Wired* piece and the 2009 *Financial Times* article "Of couples and copulas" blamed David
Li's Gaussian copula for the crisis. Embrechts is one of the Zürich group that had warned
about the pitfalls of correlation since 1999. The paper argues that the problem was
mathematics being misused, not mathematics itself: "a misplaced reliance on
*unsophisticated* mathematics". It is written for actuaries, so it explains the
credit-market background from first principles.

It covers:

1. **The crisis and securitisation (§2–3):** subprime origination, MBS, CDO tranching.
2. **Copulas (§4):** Sklar's theorem and a comparison of Gaussian and Gumbel copulas. Both
   use N(0,1) margins and both have linear correlation of about 0.7 and Kendall's τ of
   about 0.5. In 5000 draws, the Gaussian gives 43 points with both X > 2 and Y > 2; the
   Gumbel gives 70. Beyond 3 the counts are **1 against 5**. The conclusion: *a scalar
   dependence measure together with the margins does not determine the joint
   distribution*, and the copula alone decides how often extremes happen together.
3. **The Li model (§4.3–4.4):** joint default times
   P[T₁ ≤ t₁, …, T_d ≤ t_d] = C(F₁(t₁), …, F_d(t_d)) with C Gaussian, plus CDS and
   synthetic CDOs.
4. **Three drawbacks (§5):**
   - **No default clustering.** The Gaussian copula has upper tail dependence λ_u = 0 for
     any ρ < 1 (Sibuya 1960), so extreme defaults become asymptotically independent. The
     Gumbel copula has λ_u = 2 − 2^{1/θ}, which is about 0.59 at θ = 2. The authors show
     the effect appears at finite thresholds, not only in the limit.
   - **Inconsistent implied correlation across tranches.** Correlation should be a
     property of the portfolio, yet each tranche implies a different value, and some
     tranches imply none at all. It broke openly in **May 2005**: after Ford and GM were
     downgraded, the equity-short/mezzanine-long delta hedges moved the wrong way.
   - **No economic factors, so no real stress testing.** "Copula technology is inherently
     static". It "fails miserably exactly when one needs it". And "calibration" is too
     often "a substitute for bad or insufficient statistical modeling".
5. **Valuation (§6):** a 125-name example. As correlation rises, equity-tranche expected
   loss falls and senior-tranche expected loss rises. The **mezzanine has no monotone
   relationship** with correlation, and its sign depends on the default probability. A
   CDO² is built from such mezzanine tranches: about 22,500 underlying bonds and 22,500
   pages of contracts.
6. **AIG (§8):** how a 400-person subsidiary nearly sank a 100,000-person insurer. It
   wrote CDS on super-senior tranches that were treated as risk-free, and nobody modelled
   the liquidity risk of its collateral-posting terms.

## Why it's in the library

**It is the clearest short proof that correlation doesn't determine tail risk.** The
Gaussian-against-Gumbel comparison holds the margins and the correlation (both Pearson and
Kendall) fixed and still finds five times as many joint 3σ events. That is the elliptical
trap in one figure. Any risk number built from a correlation matrix (PCA, effective number
of bets, mean-variance) silently picks the Gaussian copula's answer for the tail.

**It is the counterpoint to [[mackenzie-spears-2014-formula-that-killed-wall-street]].**
MacKenzie & Spears explain *how* the Gaussian copula spread: practical bricolage,
computing limits, and calibration to market prices. Donnelly & Embrechts explain *why it
was wrong*, as people who said so at the time. Read together, they show the model's flaws
were public, cited in the 2005 *Wall Street Journal* front-page story, and ignored because
the model was fast and needed only one parameter.

**The mezzanine result is a lesson about non-monotone sensitivity.** A position whose
exposure to a parameter changes sign with the regime can't be hedged by that parameter
and can't be stress-tested by moving it in one direction. Many quantities computed from a
correlation estimate behave this way.

**"Calibration is not validation"** appears here in nearly those words, from the
risk-management side. It's the same discipline any backtest needs: a model fitted to
reproduce what it is evaluated on has not been tested.

## Links

- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — the history of the same
  model, from the sociology-of-finance side
- [[nelsen-2006-introduction-to-copulas]] — Sklar's theorem, Kendall's τ, and the tail
  dependence coefficient used in §5.1
- [[munnix-schafer-2011-copula-dependencies]] — equity tail dependence measured above the
  Gaussian copula's
- [[wikipedia-copula-statistics]] — Gumbel and other Archimedean generators, Gaussian
  copula density
- [[ang-chen-2002]] — correlations that rise in down markets, the equity version of
  default clustering
- [[artzner-delbaen-eber-heath-1999]], [[rockafellar-uryasev-2000]] — risk measures that
  look at the tail instead of a single correlation
