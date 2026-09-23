# Empirical Distribution of Daily Stock Returns of Selected Developing and Emerging Markets with Application to Financial Risk Management

| | |
|---|---|
| **Authors** | Juraj Pekár; Mário Pčolár (University of Economics in Bratislava) |
| **Year** | 2022 (published online 27 Sep 2021) |
| **Type** | Paper — *Central European Journal of Operations Research* 30, 699–731 |
| **DOI** | [10.1007/s10100-021-00771-4](https://doi.org/10.1007/s10100-021-00771-4) |
| **PDF** | `pekar-pcolar-2022.pdf` (in this folder) |
| **BibTeX** | `pekar2022empirical` |
| **Status** | Read |

## Key takeaway

Thirty blue-chip market indices, developed and emerging, local currency, 1990s to present.
Five candidate distributions fitted against the normal: the **generalized lambda (gld)**,
two parameterisations of the **skewed generalized t (sgt)**, the **exponential power
(GED)**, and **Hansen's skewed t**. Fit judged by Anderson–Darling, Kolmogorov–Smirnov,
AIC and BIC, then carried through to a **CVaR** comparison against historical CVaR.

- Normality is rejected everywhere. Returns show mild, **mostly negative** skewness and
  heavy kurtosis — a longer left tail than the normal allows.
- **Every** alternative beats the normal. The interesting question is which.
- **gld wins**: best by BIC in **99%** of series, and the most stable fit across subperiod
  lengths (they re-fit on 2-year, 5-year and longer windows). By AIC, sgt_2, gld and sgt_1
  are comparable.
- For CVaR, gld again gives the best estimates, and accuracy improves with sample size.
- **Emerging markets are more skewed on average**, but there is *no significant difference*
  in goodness of fit between emerging and developed markets — the same families work in
  both. Estimates are nonetheless somewhat better in developed markets.

## Why it's here

The empirical grounding for `04-tails-and-jumps`. [[artzner-delbaen-eber-heath-1999]] says
*use* CVaR and [[rockafellar-uryasev-2000]] says how to *optimise* it; neither tells you
what distribution to put underneath. This does, across thirty markets rather than the usual
single index — the breadth is what makes it worth keeping.

Also the right template for a question posed elsewhere: their emerging-versus-developed
comparison asks whether two classes of market differ in **kind** or only in **scale**, and
finds the same distributional families fit both. That is exactly the form the bitcoin
question takes.

## Where it's weak

⚠️ **gld is worst precisely where a tail model has to be right.** Their own result: at
α = 0.5%, gld **overestimates** CVaR for most series. That is the deepest quantile — the
one a tail-risk measure exists to capture. A distribution that wins on aggregate fit and
misses the 0.5% tail has won on the bulk, and the bulk is not what CVaR is for.

⚠️ **No out-of-sample validation.** Fit is AD/KS/AIC/BIC computed in-sample, and the CVaR
comparison is against historical CVaR **on the same data**. There is no exceedance
backtest — no Kupiec unconditional coverage, no Christoffersen independence test — which is
the standard way to judge a VaR/CVaR model. The subperiod re-fits are a stability check,
not out-of-sample evidence. Credit where due: Anderson–Darling weights tail discrepancies
more heavily than KS, so the assessment is not purely bulk-driven. But AIC and BIC are, and
the headline "99% of series" is a BIC result.

⚠️ **gld has no closed-form density.** It is defined through its quantile function, so
estimation is awkward and four parameters are buying the flexibility. BIC penalises that and
gld still wins, which is a real point in its favour — but this is not a parsimonious model,
and implementing it is more work than the ranking implies.

⚠️ **Descriptive, not predictive.** The paper establishes which distribution *described*
history best. It does not show that a gld fitted on one period forecasts the next. For
position sizing or a risk limit, that is the only question, and it is not asked here.
