# Mathematical Statistics with Applications

| | |
|---|---|
| **Authors** | Dennis D. Wackerly, William Mendenhall III, Richard L. Scheaffer (University of Florida) |
| **Year** | 2008 |
| **Type** | Undergraduate/early-graduate textbook — Thomson Brooks/Cole, 7th edition, 939pp |
| **Origin** | The standard calculus-based mathematical statistics sequence |
| **PDF** | `wackerly-2008-mathematical-statistics.pdf` (in this folder) |
| **BibTeX** | `wackerly2008mathstat` |
| **Status** | Reference |

## What it is

The full calculus-based inference sequence, in sixteen chapters that build in one direction:

1–2. What statistics is; probability
3–4. Discrete and continuous random variables and their distributions
5–6. Multivariate distributions; **functions of random variables**
7. **Sampling distributions and the central limit theorem**
8–9. **Estimation; properties of point estimators and methods of estimation**
10. **Hypothesis testing**
11. Linear models and estimation by least squares
12–14. Design of experiments; analysis of variance; categorical data
15. Nonparametric statistics
16. Bayesian methods for inference

The spine is chapters 6 → 7 → 8/9 → 10: derive the distribution of a function of random
variables, specialise that to a statistic computed from a sample, ask what makes such a
statistic a good estimator, then ask when an observed value is far enough from a
hypothesised one to act on. Everything before is the probability needed to do it and
everything after is application.

It is a teaching text rather than a research monograph — Casella & Berger or Lehmann is the
step up in rigour — and its value here is precisely that: it derives the standard results
rather than citing them.

## Why it's in the library

**Chapter 7 is the reason the noise floor exists.** Every Sharpe ratio in this repository
is quoted with a standard error, and that `SE(SR) ≈ √((1 + SR²/2)/T)` is a sampling
distribution — the distribution of a statistic computed from a finite sample, which is
exactly what chapter 7 constructs. The habit of asking "how much of this number is the
sample?" before "is this strategy good?" is a chapter 7 habit. A seventeen-year backtest
carrying ±0.24 and a two-year one carrying ±0.67 is the same fact restated.

**Chapters 8 and 9 are the vocabulary for estimation error.** Bias, variance, consistency,
efficiency, sufficiency, the Rao–Blackwell theorem, maximum likelihood, and the
mean-square-error decomposition are the terms in which the entire mean-variance critique is
stated. [[michaud-1989]] and [[chopra-ziemba-1993]] argue that `w ∝ Σ⁻¹μ` is unstable
because the plug-in estimates of `μ` and `Σ` carry sampling variance the optimiser then
treats as signal — a claim that only means anything once estimator variance is a defined
object. [[ledoit-wolf-2004]] answers it by deliberately accepting bias to buy a larger
reduction in variance, which is the bias–variance tradeoff of chapter 8 used as a design
principle rather than as an exercise.

**Chapter 10 is what gets deflated.** The t-statistic, the p-value, and the Type I/Type II
error framing are constructed here for a single pre-specified test. [[harvey-liu-zhu-2016]]
is the argument that the finance literature ran this machinery thousands of times and kept
reporting the single-test threshold; the deflated Sharpe and PBO tooling used in this
research is the correction. The correction is unreadable without the thing being corrected.

**Chapter 16 is where shrinkage comes from.** Priors, posteriors and Bayes estimators are
the formal statement of "pull the noisy estimate toward a structured target," which is what
every covariance-shrinkage and hierarchical-weighting scheme is doing whether or not it
says so.

**Chapter 11 is the factor-model machinery.** Least squares, its distributional
assumptions, and inference on the coefficients are what a factor regression is — the
apparatus behind [[sharpe-1963]] and everything downstream in `factor-structure/`.

## Links

- [[chopra-ziemba-1993]] — estimation error in the optimiser's inputs, quantified; the
  applied payoff of chapters 8–9
- [[michaud-1989]] — mean-variance optimisation as an error-maximiser, the qualitative
  version of the same point
- [[ledoit-wolf-2004]] — the bias–variance tradeoff of chapter 8 turned into a covariance
  estimator
- [[harvey-liu-zhu-2016]] — what happens to chapter 10's thresholds when the test is run
  thousands of times
- [[marchenko-pastur-1967]] — the sampling distribution of an entire covariance matrix's
  eigenvalues, where chapter 7's logic goes when the statistic is high-dimensional
- [[nemirovski-2023-linear-optimization]] — the other half of the toolkit: once the inputs
  are understood to be uncertain, this is how the optimisation is written to price that
