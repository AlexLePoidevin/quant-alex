# Joint Modeling of VIX and SPX Options at a Single and Common Maturity with Risk Management Applications

| | |
|---|---|
| **Authors** | Peter Carr (NYU Courant), Dilip B. Madan (University of Maryland) |
| **Year** | 2014 (working paper dated 4 January 2013; SSRN 2234761) |
| **Type** | Paper, *IIE Transactions* 46(11), 1125–1131. The local copy is the 17-page SSRN working paper |
| **PDF** | Local copy only (SSRN working paper of a journal article, no open licence) |
| **BibTeX** | `carr2014jointvix` |
| **Status** | Reference: §2 sets out the model, §3 the calibration to 20 October 2008, §4 the hedge of a realized-volatility call |

## What it is

A short paper that fits one model to two option markets at once: S&P 500 (SPX) options and
VIX options with the same expiry. The link between them is that VIX² is the price of a
one-month variance swap on the S&P 500, so the two smiles cannot be modelled separately
without leaving them inconsistent.

- **The scope is deliberately narrow.** The model covers one calibration date and one
  common maturity: two smiles, not a whole surface through time. The authors' defence is
  that the variance gamma model also began as a one-maturity fit before the Sato process
  extended it across maturities.
- **Three variables, one closed-form law.** The model jointly describes the log index s,
  the squared VIX v, and a hidden variable x standing for realized variance over the month.
  - x is gamma distributed with mean one.
  - Given x, v is gamma distributed with a shape that rises linearly in x. This is the
    "double gamma" model of the VIX: its mean and variance respond to the month's realized
    variance. Plain gamma models of the VIX failed to fit out-of-the-money VIX calls, which
    is why it uses two layers. The idea follows Gatheral's double lognormal.
  - Given (x, v), the log index is variance gamma (in the CGM form), with a drift and
    quadratic variation that are affine in x and v.
  - The joint characteristic function and the joint density of (s, x, v) are both in closed
    form. The model has 11 parameters.
- **Calibration.** There are VIX options but no options on VIX², so the model is first fit
  to VIX options. Prices for calls on the square are then generated from it, refit, and
  finally all 11 parameters are fit together to SPX and VIX options. The example date is 20
  October 2008, a month after Lehman, with the SPX at 984.41 and a one-month variance-swap
  quote of 51.08 vol. The figures show close fits to both smiles.
- **Risk-management use.** The target is a call on one-month realized volatility struck at
  60 vol.
  - The conditional law of realized variance given the SPX and VIX levels comes from Bayes'
    rule on the joint density.
  - The liability is priced at an ask, a distorted expectation using Cherny–Madan's
    minmaxvar distortion at stress level 0.25, not a risk-neutral mean.
  - A static portfolio of cash, SPX, VIX and options on both is fitted by least squares to
    that ask-price surface. The residual plot shows how well SPX and VIX options together
    span a realized-volatility payoff.

## Why it's in the library

- **It makes the VIX–SPX link concrete.** VIX options are options on a variance swap rate
  that is itself built from SPX options, so the two markets must be priced consistently.
  The paper is a compact example of one model doing both, and of the compromise (one date,
  one maturity) that tractability forces.
- **It hedges realized volatility with listed options.** Realized-volatility options have
  no listed market. The exercise shows how far a static book of SPX and VIX options can go
  towards replicating one, which is the practical problem behind volatility-swap and
  variance-swap desks.
- **Pricing at an ask rather than a mean.** The distorted-expectation ask price is a
  conservative valuation of a liability, an alternative to risk-neutral mid pricing that is
  rarely seen outside Madan's work.
- **Limits.** There is one calibration date, the model has 11 parameters, and no
  out-of-sample hedge test is run. The residuals are shown only against the model's own
  ask-price surface, so this is a demonstration rather than evidence that the hedge works.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — what
  long VIX futures and calls actually did inside a portfolio, the empirical side of the
  instruments modelled here
- [[merton-1976]] — jumps in the index, the reason a pure diffusion cannot fit both smiles
  and the motivation for Lévy models like variance gamma
