# The Surprising Behavior of Data in Higher Dimensions

| | |
|---|---|
| **Author** | Salih Salih |
| **Year** | 2023 (15 December) |
| **Type** | Blog post — *Towards Data Science*, 8 min |
| **Link** | https://towardsdatascience.com/the-surprising-behavior-of-data-in-higher-dimensions-1c49bca9bbee/ |
| **BibTeX** | `salih2023surprising` |
| **Status** | Explainer — for the substance cite [[altman-krzywinski-2018-the-curses-of-dimensionality]] |

## What it is

A beginner's introduction to how geometry changes as the dimension grows. It covers the
"blessings" side; the author promises the curse for a follow-up post.

- **The middle of a cube empties out.** Take a unit cube and call everything more than x
  from every face "the middle". The chance that a uniform point lands there is (1 − 2x)ⁿ.
  With x = 0.1 that is 0.8 in 1D, 0.64 in 2D, 0.512 in 3D, 0.41 in 4D, 0.33 in 5D and
  about 0.11 in 10D.
- **The inscribed ball vanishes.** A Python plot of the volume of the unit ball,
  πⁿᐟ² / Γ(n/2 + 1), divided by the volume of the cube of side 2, 2ⁿ, for n = 1 to 20.
  The ratio is π/4 ≈ 0.79 in 2D, about 0.0025 in 10D and about 2.5 × 10⁻⁸ in 20D, so almost
  all the volume is in the corners.
- **The paper-and-DVD analogy.** A DVD cannot pass through a square hole whose diagonal is
  shorter than the disc, until the paper is folded. Using a third dimension makes a
  two-dimensional impossibility possible. It cites a kirigami paper by Weiwei Lin et al. and
  a video by The Action Lab.
- **The kernel trick.** The same idea in SVMs: data that no single threshold separates in
  1D (class 1 at x ≤ 9 and x ≥ 23, class 0 in between) becomes linearly separable after
  mapping x → (x, x²). It notes correctly that real kernels compute inner products in the
  lifted space without building it.

## Why it's in the library

**The two calculations are the fastest way to see the problem.** (1 − 2x)ⁿ and the
ball-to-cube ratio take one line each and show why uniform coverage of a feature space is
hopeless past a handful of dimensions. They make good figures for explaining to someone else
why a "nearby" historical analogue is rarely nearby.

**The kernel example is a reminder that a feature transform is a choice of geometry.**
Adding x² made the classes separable only because the boundary really was quadratic. A
lift chosen without that prior adds dimensions and invites overfitting.

## Links

- [[altman-krzywinski-2018-the-curses-of-dimensionality]] — the four separate curses, each
  with a simulation; the more careful companion to this post
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — the theorem behind distances
  concentrating
- [[aggarwal-hinneburg-keim-2001-surprising-behavior-of-distance-metrics]] — how the choice
  of norm changes the rate
- [[kernel-pca]] — the kernel trick applied to PCA
