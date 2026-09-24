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
