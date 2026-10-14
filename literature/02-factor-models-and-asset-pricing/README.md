# Factor models and asset pricing

The **formal model** of equity returns: a return decomposes into exposures to a small number
of shared forces plus a residual. Theory, what the factors empirically are, how much of a
return each type explains, and the counterweight.

Distinct from `../03-correlation-and-dependence/01-random-matrix-theory/`, which covers the **methods**
for estimating that structure from data (RMT, eigenvalue counting). **Model here,
measurement there.**

| Section | Question |
|---|---|
| `01-origins` | Where "returns have factor structure" came from |
| `02-theory` | Why structure must exist, and what "a factor" formally is |
| `03-what-the-factors-are` | The types: market, industry, macroeconomic, characteristic, specific |
| `04-how-much-is-common` | How much of a return is shared vs the company's own |
| `05-factor-zoo` | How many of the published factors are real |
| `06-machine-learning-factor-models` | Factor models with time-varying, nonlinear loadings: IPCA and autoencoders |

> ⚠️ **Standing caveat.** Notes marked *To read* were written from general knowledge of what
> each paper is known for, not from the paper itself. Volumes, issues and page numbers are
> from recall. **Verify before citing in print.** Notes marked *Read* were written from the
> source.

Cross-topic: [[markowitz-1952]], where the covariance matrix enters finance, is in
`../05-portfolio-construction-and-risk/01-mean-variance-and-estimation-error/`.
[[ang-chen-2002]] (correlations rise in downturns) is in
`../03-correlation-and-dependence/03-copulas-and-tail-dependence/`, and
[[pindyck-rotemberg-1993]] (excess comovement) is in
`../03-correlation-and-dependence/04-why-assets-move-together/`.
