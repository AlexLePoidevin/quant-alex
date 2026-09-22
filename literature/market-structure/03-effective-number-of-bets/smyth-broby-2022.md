# An eigenvalue distribution derived 'Stability Measure' for evaluating Minimum Variance portfolios

| | |
|---|---|
| **Authors** | William Smyth; Daniel Broby (Ulster University Business School) |
| **Year** | 2022 (published online 2 Dec 2022) |
| **Type** | Paper — *Quantitative Finance* 23(3), 521–537. Open access, CC BY-NC-ND |
| **DOI** | [10.1080/14697688.2022.2149420](https://doi.org/10.1080/14697688.2022.2149420) |
| **PDF** | https://pure.ulster.ac.uk/ws/portalfiles/portal/110078520/An_eigenvalue_distribution.pdf |
| **BibTeX** | `smyth2022eigenvalue` |
| **Status** | Read |

## Key takeaway

**Turn Marchenko–Pastur from a one-off test into a rolling monitor, and use it to time
rebalancing rather than to clean the matrix.**

The method is a fit, and the fitted parameter *is* the measure. Take the empirical
correlation matrix of an index's constituents, eigendecompose it, put a Gaussian KDE over
the eigenvalue distribution, then optimise the MP **process-variance parameter σ²** to
minimise the distance between the analytic MP density and that KDE. The optimising value
`ν = σ²_opt` is the Stability Measure — in effect an eigenvalue-derived signal-to-noise
ratio at time *t*.

- `q = T/N` held at **1.5** throughout (N ≈ 500 constituents ⟹ T = 750 daily observations,
  roughly three years).
- ν recomputed **weekly**. Stability is defined as weekly relative change in ν staying
  inside a **±5%** band; excursions outside it mark a break in stationarity.
- Validated first on synthetic data — Gaussian, uniform, Cauchy and t — with and without
  injected signal, before touching markets. Then S&P 400 / 500 / 600 and Russell 1000,
  2006–2021.
- COVID appears as a near-discontinuity **simultaneously in all four indices**, followed by
  rapid re-equilibration into a new stationary regime.
- The practical claim: stability monitoring works on a *core subset* of constituents, so it
  runs at far higher frequency than rebalancing itself and acts as a **trigger to modify
  the rebalancing schedule**.

## Why it's here

Filed with `ledoit-wolf-2004` rather than in `../01-latent-dimensionality/` deliberately.
MP is the instrument, but the object is **estimation risk in a portfolio you actually
hold**, and the output is an operational decision. Ledoit–Wolf and this paper answer the
same complaint — the sample covariance is too noisy to optimise on — in opposite
directions: **shrink the estimate**, versus **measure how noisy it currently is and act
when that changes**. Worth holding side by side.

It also lands on the temporal axis this section owes the reader. Every naive count of
breadth is too high in *both* directions, and a rebalancing schedule chosen by the calendar
rather than by the data is the temporal version of that error. This is a concrete proposal
for choosing it from the data instead.

Cites Chopra & Ziemba, Klein & Bawa, El Karoui (2010) and Bun–Bouchaud–Potters (2017) on
estimation error — the same thread running into `../../growth-and-leverage/03-estimation-error/`.

## Read it against these

⚠️ **ν is fitted, not measured.** It is the value of MP's variance parameter that makes the
analytic density best match the empirical one — so Δν says *how far the best-fitting MP had
to move*, which absorbs **any** change in the shape of the spectrum, not only a change in
process variance. Nothing in the paper discusses excluding the market mode before the fit,
and for an index correlation matrix λ₁ is the dominant feature of the spectrum by an order
of magnitude. Whether ν tracks stability or tracks how badly MP fits the bulk that month is
the first question to put to it.

⚠️ **The windows overlap almost completely.** q = 1.5 at N = 500 means a 750-day window,
recomputed weekly: consecutive estimates share ~99% of their data by construction. Δν is
therefore autocorrelated before the market does anything, and the ±5% band is partly a
property of that overlap. The distributional claims about weekly Δν need discounting
accordingly.

⚠️ **New and lightly cited.** 2022, few citations. This is a candidate technique, not an
established one like Laloux or Plerou. The synthetic-data validation is a real point in its
favour — they check the estimator reproduces known answers before pointing it at markets,
which is the right order.
