# Tree (graph theory) — Wikipedia

| | |
|---|---|
| **Author** | Wikipedia contributors |
| **Year** | Living page; read at revision 1378024853 (accessed 2026-10-18) |
| **Type** | Encyclopedia article |
| **Link** | https://en.wikipedia.org/wiki/Tree_(graph_theory) — pinned: https://en.wikipedia.org/w/index.php?title=Tree_(graph_theory)&oldid=1378024853 |
| **BibTeX** | `wiki_tree_graph_theory` |
| **Status** | Reference card — background for vine copulas; cite [[czado-2019-analyzing-dependent-data-with-vine-copulas]] for how trees are used |

## What it is

The definitions page for trees, used here as a glossary:

- **Equivalent definitions.** A tree is a connected graph with no cycles. On n vertices that
  is the same as: connected with n − 1 edges; acyclic with n − 1 edges; a unique simple path
  between any two vertices; removing any edge disconnects it; adding any edge creates a
  cycle. The **n − 1 edges** fact is the one that matters below.
- **Forests, rooted and ordered trees, polytrees.** A forest is a disjoint union of trees,
  and the number of trees in it is V − E. A polytree is a directed graph whose underlying
  undirected graph is a tree.
- **Leaves, paths and stars.** Every tree with n > 1 has at least two leaves. A path has
  exactly two; a star has n − 1, the most possible.
- **Spanning trees.** Every connected graph has one: a tree on all its vertices using only
  its edges.
- **Counting.** Cayley's formula gives n^{n−2} labelled trees on n vertices. The matrix tree
  theorem counts spanning trees in a general graph. Unlabelled trees have no closed formula,
  only Otter's asymptotic t(n) ~ C·αⁿ·n^{−5/2} with α ≈ 2.956.

## Read with care

- **Nothing on finance or statistics**, and nothing on algorithms. The minimum and maximum
  spanning tree constructions (Kruskal, Prim) are on separate pages.
- Most of the page is combinatorics (Prüfer sequences, rooted-tree recurrences, the list of
  tree types) that has no use here.

## Why it's in the library

**A vine copula is a nested sequence of trees, and the vocabulary comes from here.** On d
assets, tree T₁ has the d assets as vertices and d − 1 edges, each edge a pair copula. Tree
T₂ has those d − 1 edges as its vertices and d − 2 edges, and so on down to one edge. That
adds up to d(d − 1)/2 pair copulas, one for each entry of the correlation matrix. A
**D-vine** is the case where T₁ is a path; a **C-vine** is the case where each tree is a
star, with one asset at the centre (useful when one asset, such as the index, drives the
rest).

**Cayley's formula shows why vine structure is chosen greedily.** There are d^{d−2} candidate
first trees alone: 10⁸ for d = 10 assets and about 10⁴¹ for 30. Searching over them is out
of the question, so Dißmann's algorithm takes the maximum spanning tree on |Kendall's τ| at
each level. The same counting explains why vine model selection is a multiple-testing
problem: the tree is a choice made from the data.

**The same object is in the correlation-network notes.** [[mantegna-1999]] builds the
minimum spanning tree on the correlation distance √(2(1 − ρ)), keeping n − 1 of the n(n − 1)/2
links. Dißmann's first tree is the rank-correlation version of the same construction, with a
copula fitted to each kept edge.

## Links

- [[czado-2019-analyzing-dependent-data-with-vine-copulas]] — regular vines, C- and
  D-vines, and Dißmann's tree-by-tree selection
- [[mantegna-1999]] — the correlation minimum spanning tree for stocks
- [[wikipedia-copula-statistics]] — the companion reference card for the copula side
- [[munnix-schafer-2011-copula-dependencies]] — the pairwise dependence that vine edges model
