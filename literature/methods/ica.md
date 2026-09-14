# Independent Component Analysis

| | |
|---|---|
| **Source** | [Introduction to ICA: Independent Component Analysis](https://medium.com/data-science/introduction-to-ica-independent-component-analysis-b2c3c4720cd9) — Jonas Dieckmann, Towards Data Science |
| **Primary reference** | [[hyvarinen-oja-2000]] — Hyvärinen & Oja, *ICA: Algorithms and Applications*, Neural Networks 13(4–5) |
| **Status** | To read |

## What it is

The cocktail-party problem: several microphones record several simultaneous speakers, and
each recording is a different mixture of all of them. ICA recovers the sources.

Model the observations as a linear mixture of latent sources,

$$x = A s,$$

and recover both $A$ and $s$ knowing only $x$, under the assumption that the components of
$s$ are **statistically independent**. The usual procedure is three steps: centre, whiten
(typically via PCA), then rotate to maximise non-Gaussianity — measured by kurtosis or
negentropy. FastICA is the standard algorithm.

**Non-Gaussianity is not a convenience, it is the identifying assumption.** A rotation of
jointly Gaussian variables is still jointly Gaussian with the same covariance, so under
Gaussianity the mixing matrix is unrecoverable. ICA works precisely because real data isn't
Gaussian — which is also why it has traction on returns.

## Why it's in the library

This is the cleanest statement of a gap in the Fundamental Law's foundations:
**`BR` requires independent bets, and PCA delivers only *uncorrelated* ones.** For
non-Gaussian data those are different things, and returns are emphatically non-Gaussian. ICA
is the first principled step across that gap, and it is the technique behind the FX regime
work.

## ⚠️ What it does not do

**ICA does not tell you the dimension.** Because whitening is done with PCA, ICA inherits
whatever component count was chosen at that step — it **rotates within a subspace you have
already selected** to find a more interpretable basis. So it cannot answer "how many pipes
are there"; it can only make a given number of them more meaningful.

That is a useful division of labour worth keeping straight: **RMT decides how many
directions are real; ICA decides what basis to read them in.**

Two further ambiguities are inherent, not fixable: the **scale** and the **ordering** of the
recovered components are undetermined, so there is no natural "first" independent component
the way there is a first principal component.

## Links

- [[hyvarinen-oja-2000]] — the primary reference; read this for the actual algorithms
- [[marchenko-pastur-1967]] — decides the dimension ICA then rotates within
- [[meucci-2015-torsion]] — the other answer to "which uncorrelated basis?", from the
  portfolio side rather than the signal-processing side
