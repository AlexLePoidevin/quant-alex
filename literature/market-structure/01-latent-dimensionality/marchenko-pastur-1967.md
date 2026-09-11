# Distribution of Eigenvalues for Some Sets of Random Matrices

| | |
|---|---|
| **Authors** | Vladimir A. Marchenko; Leonid A. Pastur |
| **Year** | 1967 |
| **Type** | Paper — *Matematicheskii Sbornik* 72(4), 507–536 |
| **BibTeX** | `marchenko1967distribution` |
| **Status** | To read |

## Key takeaway

The limiting eigenvalue density of a sample covariance matrix built from **pure noise**.
With N variables and T observations, ratio q = N/T, the eigenvalues fall inside
[(1−√q)², (1+√q)²]. Anything outside that band is not noise.

## Why it's here

The load-bearing result of the whole series. It converts "markets have latent structure"
from an assertion into a **test**: plot the spectrum, draw the MP band, count the escapers.

## Hands-on companion

[An Empirical view of Marchenko-Pastur Theorem](https://medium.com/swlh/an-empirical-view-of-marchenko-pastur-theorem-1f564af5603d)
— *The Startup* (Medium), Oct 2021. Python walkthrough: simulate a pure-noise matrix,
recover the MP density empirically, then use the band to separate signal from noise in a
correlation matrix (the denoising setup from López de Prado's work).

The 1967 paper is the theorem; this is the simulation that makes it obvious. Useful as a
sanity check when building the Part 02 spectrum figure — if a synthetic noise matrix
doesn't reproduce the band, the estimator is wrong before any real data is involved.
