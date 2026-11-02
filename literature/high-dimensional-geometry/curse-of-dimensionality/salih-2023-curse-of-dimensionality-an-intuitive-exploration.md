# Curse of Dimensionality: An Intuitive Exploration

| | |
|---|---|
| **Author** | Salih Salih |
| **Year** | 2023 (30 December) |
| **Type** | Blog post — *Towards Data Science*, 11 min |
| **Link** | https://towardsdatascience.com/curse-of-dimensionality-an-intuitive-exploration-1fbf155e1411/ |
| **BibTeX** | `salih2023curse` |
| **Status** | Explainer — for the substance cite [[altman-krzywinski-2018-the-curses-of-dimensionality]] and [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] |

## What it is

The follow-up to [[salih-2023-the-surprising-behavior-of-data-in-higher-dimensions]]. The
first post covered the upside of high dimension; this one covers the curse, the term
Bellman coined in dynamic programming. It focuses on two problems and illustrates each with
a Python simulation.

- **Sparsity: "islands in an ocean of emptiness".** Volume grows exponentially with each
  added dimension, so points that were close drift apart and clustering methods that need
  dense neighbourhoods struggle.
- **Distances stop discriminating.**
  - *Simulation 1:* 1,000 uniform points in [1, 100]ᵖ for p = 1 to 100. In 3D the pairwise
    distances and the distances to a random reference point are widely spread; in 100D
    they bunch together. The mean distance grows with p while the standard deviation stays
    roughly flat, so the spread shrinks relative to the mean.
  - *Simulation 2:* 500 uniform points in [0, 1]ᵖ. The normalised gap
    (max distance − mean distance) / max distance falls steadily as p rises to 100: the
    typical distance approaches the largest one.
  - The post stresses that *relative* distances are what neighbour and clustering methods
    (k-means, DBSCAN) use, and those are what collapse.
- **Why it happens: the law of large numbers.** A squared Euclidean distance is a sum of p
  per-coordinate terms. Like the average of many dice rolls settling at 3.5, the sum settles
  at its expected value, so every pair ends up about the same distance apart. A third
  simulation shows that two random Gaussian vectors in 100 dimensions are almost orthogonal
  (|cos θ| < 0.1), which the post uses as the intuition for the independence the argument
  needs. A Manhattan street grid is the analogy: moving along one street doesn't change
  your position on another.
- **Practical consequences:** overfitting (spurious correlations among many features), hard
  pattern-finding in sparse data, and higher compute and memory cost.
- **Remedies:**
  - PCA, which keeps global linear structure and variance;
  - manifold learning such as Isomap, which keeps local non-linear structure, on the view
    that high-dimensional data often lies near a lower-dimensional manifold;
  - feature selection, regularisation, and more samples where possible.

## Why it's in the library

**It gives the reason, not just the picture.** The law-of-large-numbers argument is the
informal version of Beyer et al.'s theorem: when every coordinate adds independent noise to
a distance, the distance's spread grows like √p while its mean grows like p, so the ratio
collapses. Seeing it that way also shows the escape route. Coordinates that are correlated,
or that carry signal rather than noise, don't average out, which is why intrinsic dimension
matters more than column count.

**Near-orthogonality has a direct reading for signals.** In high dimension, random vectors
are almost uncorrelated by default. A low correlation between two long, noisy signal
vectors is therefore weak evidence that they carry different information, and a high one is
strong evidence that they don't.

**The two simulations are easy to reuse.** Run the distance-spread and max-versus-mean
checks on an actual feature matrix before trusting a k-NN or clustering step on it.

## Links

- [[salih-2023-the-surprising-behavior-of-data-in-higher-dimensions]] — part one: volume
  in the corners, and the kernel trick
- [[altman-krzywinski-2018-the-curses-of-dimensionality]] — the four separate curses, each
  with a simulation
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — the theorem this post's
  law-of-large-numbers argument sketches
- [[aggarwal-hinneburg-keim-2001-surprising-behavior-of-distance-metrics]] — Manhattan (L₁)
  keeps more contrast than Euclidean as dimension grows
- [[levina-bickel-2004]], [[facco-et-al-2017]] — estimate the intrinsic dimension, the
  number that actually governs these effects
- [[coifman-lafon-2006]] — diffusion maps, a manifold-learning method in the same family as
  the Isomap the post recommends
