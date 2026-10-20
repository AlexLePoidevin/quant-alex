# Tabular Data: Deep Learning is Not All You Need

| | |
|---|---|
| **Authors** | Ravid Shwartz-Ziv, Amitai Armon (IT AI Group, Intel) |
| **Year** | 2022 (arXiv v2, 23 November 2021) |
| **Type** | Paper — *Information Fusion* 81 (2022), 84–90, doi:10.1016/j.inffus.2021.11.011. arXiv:2106.03253v2, 13pp |
| **PDF** | `shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need.pdf` (in this folder) |
| **BibTeX** | `shwartzziv2022tabular` |
| **Status** | Reference |

## What it is

A head-to-head test of four deep architectures built for tabular data (TabNet, NODE,
DNF-Net, and a Kaggle 1D-CNN) against XGBoost, on 11 datasets with one tuning protocol.

- **Design.** Nine datasets come from the deep models' own papers (three each from TabNet,
  DNF-Net and NODE), plus two Kaggle datasets that none of them used. Each model gets 1,000
  steps of HyperOpt Bayesian search on a validation set, starting from its paper's
  hyperparameters, with the original splits and four seeds.
- **Each deep model wins mainly on its own paper's datasets.** On datasets it hadn't been
  shown on, it is worse. Average deterioration against the best model on its unseen
  datasets (Table 3): NODE 14.2%, DNF-Net 12.0%, TabNet 10.5%, 1D-CNN 7.6%, **XGBoost 3.3%**.
  On 8 of the 11 datasets, XGBoost beats the deep models that hadn't seen them.
- **The authors' explanation is selection bias in the original papers.** Each paper showed
  datasets its model did well on, and tuned harder there. Their reproductions match the
  published numbers on the original datasets, which rules out an implementation problem.
- **An ensemble of XGBoost and the deep models is best** (2.3% deterioration). Weights come
  from normalised validation loss. Deep models alone (6.9%) and a classical ensemble of
  XGBoost, SVM and CatBoost (3.2%) are both worse. Three models picked by validation loss get
  nearly all of the gain (Fig. 1).
- **XGBoost is far easier to tune.** It reaches its plateau in fewer HyperOpt iterations,
  and each iteration is more than ten times faster (Fig. 2).

## Read with care

- **Eleven datasets, all i.i.d.-style cross-sections.** None is a financial time series or a
  low signal-to-noise problem; a 1% difference in cross-entropy on Higgs says little about a
  return forecast with an R² near zero.
- **The ensemble's edge is small and uneven.** It loses to single models on several
  datasets (TabNet on Rossmann and Higgs, NODE on Higgs and Epsilon, DNF-Net on Gas, XGBoost
  on Eye Movements), and it is selected and weighted using the same validation sets.
- **The tuning-effort result rests on one dataset** (Shrutime) and one optimiser. The
  authors note that XGBoost's default hyperparameters may simply have been chosen on many
  more datasets.
- **It predates the stronger 2021–2022 deep tabular baselines** (FT-Transformer, tuned MLPs
  with regularisation cocktails). Those narrowed the gap without overturning the conclusion,
  which the larger benchmark of Grinsztajn, Oyallon & Varoquaux (NeurIPS 2022) confirmed.

## Why it's in the library

**It is the citation for "start with gradient-boosted trees on tabular features".** A panel
of engineered features (momentum, volatility, rank and cross-sectional transforms) is
tabular data: heterogeneous columns in different units, no spatial or sequential locality,
and many weak or irrelevant inputs. That is where trees do well and deep nets have no
built-in advantage.

**The selection-bias finding is a backtesting lesson.** Each deep model looked best on the
data its authors chose and tuned on, and degraded on fresh data. That is a model-selection
version of the multiple-testing problem: compare models on datasets none of them was
developed on, with the same tuning budget, before believing a published edge.

**The ensemble result says diversity across model families matters more than more of the
same family.** Trees plus neural nets beat either group alone, while an ensemble of
classical models did not help. Adding a different kind of learner adds information;
adding another tree model mostly doesn't.

## Links

- [[gu-kelly-xiu-2021]] — autoencoder factor models, the deep-learning approach for
  return panels that tree models should be compared with
- [[kelly-pruitt-su-2019]] — IPCA, the linear baseline for the same problem
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — why distance-based methods
  struggle on wide feature sets, where trees, which split one feature at a time, don't
