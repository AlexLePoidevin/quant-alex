# A Copula Approach on the Dynamics of Statistical Dependencies in the US Stock Market

| | |
|---|---|
| **Authors** | Michael C. Münnix (Duisburg-Essen; Boston University), Rudi Schäfer (Duisburg-Essen) |
| **Year** | 2011 |
| **Type** | Preprint — arXiv:1102.1099v2 [q-fin.ST], 3 March 2011, 7pp |
| **Data** | 428 continuously listed S&P 500 constituents, 2007–2010, NYSE TAQ intraday |
| **PDF** | `munnix-schafer-2011-copula-dependencies.pdf` (in this folder) |
| **BibTeX** | `munnix2011copula` |
| **Status** | Reference |

## What it is

An empirical measurement of the *dependence structure* of US equities, separated from the
*marginal distributions* of the returns. That separation is the whole point of a copula:
Sklar's theorem lets a joint distribution be written as its marginals plus a function
coupling them, so questions about co-movement can be asked without heavy tails in the
individual series contaminating the answer.

The authors compute the average pairwise empirical copula across the index at several
return intervals from 30 minutes upward and compare it against the Gaussian copula implied
by an ordinary correlation coefficient. Three findings:

- **Tail dependence exceeds the Gaussian.** Extreme moves are far more jointly likely than
  a correlation coefficient implies, and the gap widens as the return interval shortens.
- **Average correlation and tail dependence are close to linearly related** — but with many
  outliers, and the relation breaks down at the smallest quantiles, which are the ones that
  matter for loss.
- **Anti-correlated extremes are present**: the copula is not merely a fattened Gaussian.

## Why it's in the library

**It is the empirical answer to the question a correlation coefficient cannot be asked.**
Pearson's ρ summarises the whole joint distribution in one number, and that number is
sufficient *only* if the dependence is Gaussian. This paper measures how wrong that
sufficiency assumption is, on intraday data, at index scale. The practical statement —
*extreme events are much more correlated than a linear correlation assumes* — is the
quantitative form of the thing every risk model discovers the hard way.

**It separates two failures usually conflated.** Heavy tails in a single asset
([[plerou-et-al-2002]]) and heavy *joint* tails across assets are different defects with
different remedies. Shrinking a covariance matrix ([[ledoit-wolf-2004]]) or cleaning its
spectrum ([[laloux-et-al-1999]], [[bouchaud-potters-2009]]) improves the estimate of a
linear object; neither repairs a dependence structure that was never linear. The copula is
where that distinction becomes visible.

**It sits directly under the diversification arithmetic.** Any statement about an effective
number of bets ([[meucci-2009]]) is computed from a covariance matrix and therefore
inherits the Gaussian dependence assumption. If tail dependence is systematically higher
than that assumption, the bet count is overstated precisely in the states where it is being
relied upon.

## Links

- [[ledoit-wolf-2004]] — improves the *estimate* of the linear dependence; orthogonal to
  whether linear dependence was the right object
- [[laloux-et-al-1999]], [[bouchaud-potters-2009]] — cleaning the correlation spectrum,
  with the same caveat
- [[plerou-et-al-2002]] — heavy tails in the marginals, the defect a copula factors out
- [[meucci-2009]] — the diversification measure that inherits the Gaussian assumption
- [[artzner-delbaen-eber-heath-1999]], [[rockafellar-uryasev-2000]] — risk measures that
  live in the tail this paper shows is fatter than assumed
- [[hyvarinen-oja-2000]] — the other route to non-Gaussian structure, via independence
  rather than via the copula
