# Tree! I am no Tree! I am a Low Dimensional Hyperbolic Embedding

| | |
|---|---|
| **Authors** | Rishi Sonthalia (University of Michigan), Anna C. Gilbert (Yale) |
| **Year** | 2020 |
| **Type** | Paper — *NeurIPS 2020* (34th Conference on Neural Information Processing Systems). This PDF is arXiv:2005.03847v4, 28pp with appendices. Code: github.com/rsonthal/TreeRep |
| **PDF** | `sonthalia-gilbert-2020-tree-i-am-no-tree-i-am-a-low-dimensional-hyperbolic-embedding.pdf` (in this folder) |
| **BibTeX** | `sonthalia2020tree` |
| **Status** | Reference — §2 (δ-hyperbolicity) and §4 (experiments) are the useful parts; §3's proofs can be skipped |

## What it is

A way to find the hierarchy hidden in a set of pairwise distances. Trees can't be drawn
faithfully in low-dimensional Euclidean space, but they fit naturally into hyperbolic
space, so hyperbolic embeddings have become the standard tool for hierarchical data. The
paper argues for doing it the other way round: **fit a tree to the distances first**, then
embed the tree if a hyperbolic picture is needed.

- **How tree-like are the distances?** Gromov's δ-hyperbolicity measures it, using the
  four-point condition on Gromov products. δ = 0 means the distances are exactly a tree's
  path lengths; larger δ means further from a tree. So δ is a test you can run before
  fitting anything.
- **TreeRep, the algorithm.** Any three points can be joined exactly by a tree with one
  extra internal (Steiner) node. Every other point falls into one of seven zones relative
  to that tree, decided by which Gromov products are equal. TreeRep sorts points into
  zones and recurses. If δ = 0 it recovers the original tree exactly, with the fewest
  nodes; otherwise it returns an approximating tree. Worst case O(n²), faster in practice.
- **It needs only the distances,** not a graph. Minimum spanning trees and low-stretch
  trees need a graph to start from and do badly when given only a metric.
- **Results:**
  - **Speed:** four to five orders of magnitude faster than learning hyperbolic
    embeddings by optimisation (Poincaré and Lorentz maps, PT), and about 20 times faster
    than neighbour joining.
  - **Quality vs other tree methods:** lower distortion than MST, low-stretch trees and
    the other tree-construction algorithms; competitive with neighbour joining, which wins
    on the graph datasets but is too slow at scale.
  - **Quality vs embeddings:** usually better mean average precision than 2-dimensional
    hyperbolic embeddings, and often better than 200-dimensional ones.
  - **Real data:** a sensible phylogenetic tree from immunological distances, and the
    lowest distortion on two single-cell RNA datasets, where neighbour joining and the
    embedding methods ran past 4 hours.

## Read with care

- **TreeRep is randomised.** Reported numbers average 20 runs; the best runs are in the
  appendix. Single runs vary.
- **Neighbour joining is still the quality benchmark.** On the graph datasets it beats
  TreeRep on both measures. The case for TreeRep is speed at scale, not accuracy.
- **A tree is only as good as δ is small.** On distances that aren't hierarchical, any
  tree distorts them; the method doesn't tell you when not to use it.
- **No financial data.** The tests are synthetic hyperbolic points, biology and social or
  citation graphs.

## Why it's in the library

**It gives a test for whether asset correlations really form a hierarchy.**
[[mantegna-1999]] builds a hierarchical tree of stocks from correlation distances,
d = √(2(1 − ρ)), using a minimum spanning tree. Hierarchical portfolio methods assume the
same thing. This paper gives two tools: δ-hyperbolicity to check how tree-like the
correlation distances actually are, and a fast tree fit that doesn't depend on a graph.
Its own results show MST does badly when the input is a metric, not a graph.

**A hierarchy is a dimension-reduction choice.** A tree, or a 2-dimensional hyperbolic
embedding, can represent hierarchical data far more faithfully than a few Euclidean
dimensions. That is an alternative to PCA-style factor models when the structure is
sectors within sectors, not a few broad factors.

**It sits beside the intrinsic-dimension estimators in this folder.** Both ask what
shape the data really has before choosing a model: [[levina-bickel-2004]] and
[[facco-et-al-2017]] measure how many dimensions, this measures how tree-like.

## Links

- [[mantegna-1999]] — hierarchical trees of stocks from correlation distances, built with
  a minimum spanning tree
- [[wikipedia-tree-graph-theory]] — the graph-theory background on trees
- [[czado-2019-analyzing-dependent-data-with-vine-copulas]] — vine copulas, another way of
  imposing a tree structure on dependence
- [[levina-bickel-2004]], [[facco-et-al-2017]] — the other "what shape is the data"
  measurements in this folder
- [[bronstein-bruna-cohen-velickovic-2021-geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges]]
  — the wider case for matching a model's geometry to the data's
