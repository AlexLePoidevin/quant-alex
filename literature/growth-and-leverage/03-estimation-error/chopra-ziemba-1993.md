# The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice

| | |
|---|---|
| **Authors** | Vijay K. Chopra; William T. Ziemba |
| **Year** | 1993 |
| **Type** | Paper — *Journal of Portfolio Management* 19(2) |
| **BibTeX** | `chopra1993effect` |
| **Status** | To read |

## Key takeaway

A numerical experiment. Perturb each input to a mean-variance optimisation in turn, measure
the cash-equivalent loss, and compare. The headline: at moderate risk tolerance, errors in
**means** cost roughly an order of magnitude more than errors in variances, and about twice
that again relative to errors in covariances. Usually quoted as **"10 : 2 : 1"**.

## Why it's here

Honestly? **Because everyone cites it**, so you need to know what it does and does not say
before someone cites it at you. It is not here because the article needs it.

## Where it's weak

**1. The famous ratio is a calibration, not a constant.** It is the output of one experiment
at one risk tolerance on one asset set. The ratio scales roughly *linearly* with risk
tolerance — the paper shows this itself — so "10×" without the risk-tolerance parameter
attached is close to meaningless. It is nonetheless quoted bare, essentially always.

**2. The qualitative result is calculus, not a finding.** Mean-variance utility is **linear**
in `μ` and **quadratic** in `Σ`. Perturbing the first-order term hurts more than perturbing
the second-order one. That the first-order term dominates was never in question; the paper
puts a number on it, and the number turns out to be conditional. The discovery framing
belongs to its citers, not to Chopra and Ziemba.

**3. The inference the field drew from it does not follow.** "Errors in means are costly"
became "don't estimate means" — minimum-variance, risk parity, equal weight, a whole
industry of not forecasting returns. That is a non-sequitur. Setting `μ` to a constant is
not abstaining from an estimate; it is asserting a different one, usually a worse one, and
the paper never measures *its* cash-equivalent loss. The conclusion the result actually
supports is **shrinkage** — Black-Litterman, James-Stein, Bayesian priors — not abstention.

**4. For this article it is the wrong tool, and a weaker one.** The leverage problem is
one-dimensional, so the sampling distribution is available directly. With `σ` known:

```
f* = (mu - r)/sigma^2       =>       SE(f*) = 1/(sigma * sqrt(T))
```

At `σ = 16%`, `μ − r = 5%` — so `f* = 1.95`:

| Years of data | SE(f*) | as % of f* | 95% CI on f* |
|---|---|---|---|
| 4 | 3.12 | **160%** | [−4.17, +8.08] |
| 10 | 1.98 | 101% | [−1.92, +5.83] |
| 25 | 1.25 | 64% | [−0.50, +4.40] |
| 100 | 0.62 | 32% | [+0.73, +3.18] |

Four years of daily data cannot tell you whether optimal leverage is `+8` or *negative*.
Pinning `f*` to ±50% of itself needs **157 years**; to ±25%, **629 years**.

That is a far more damning statement than "means matter ten times more than variances", it
is exact rather than calibrated, it arrives with the whole distribution rather than a
ratio, and it is one line of algebra. **Derive it; don't cite this.** The citation would be
borrowed authority for a weaker claim.

**What survives.** The one genuinely useful thing here is the asymmetry it points at, which
the 1-D derivation then makes precise: `f*` is *linear* in the parameter you cannot
estimate, while the penalty for overshooting `f*` is *quadratic* and one-sided. Uncertainty
in `μ` therefore argues for **less** leverage before any preference argument is made — and
that, not the 10 : 2 : 1, is the sentence worth carrying into the article.
