# The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice

| | |
|---|---|
| **Authors** | Vijay K. Chopra; William T. Ziemba |
| **Year** | 1993 |
| **Type** | Paper — *Journal of Portfolio Management* 19(2) |
| **BibTeX** | `chopra1993effect` |
| **Status** | To read |

## Key takeaway

Quantifies the cash-equivalent loss from estimation error in each input separately.
The result everyone cites: at moderate risk tolerance, errors in **means** cost roughly an
order of magnitude more than errors in variances, and about twice that again relative to
errors in covariances. The ratio widens further as risk tolerance rises.

## Why it's here

⭐ **The strongest single argument for running fractional Kelly, and it is not about risk
aversion.** `f* = (mu - r)/sigma^2` is *linear* in the mean — the input this paper shows is
the one you can least afford to get wrong — while the penalty for overshooting `f*` is
quadratic and one-sided. Uncertainty in `mu` therefore pushes optimal leverage **down**
before any preference argument is made.

Cross-check against the noise floor in the sibling project: `SE(SR) ≈ √((252 + SR²/2)/N)`
gives roughly ±0.5 on a four-year Sharpe estimate. Since `f* = SR/sigma`, that is `f*`
known to about ±100%.
