# Anomaly Detection in the Presence of Irrelevant Features

| | |
|---|---|
| **Authors** | Marat Freytsis, Maxim Perelstein, Yik Chuen San (Cornell University) |
| **Year** | 2024 |
| **Type** | Paper — *Journal of High Energy Physics* 2024(2), 220. Open access, CC BY 4.0 (SCOAP3). arXiv:2310.13057, 22pp |
| **PDF** | `freytsis-perelstein-san-2024-anomaly-detection-in-the-presence-of-irrelevant-features.pdf` (in this folder) |
| **BibTeX** | `freytsis2024anomaly` |
| **Status** | Reference — §2.1 (what "irrelevant" means), §3 (the classifier result) and §4.1 (copula density estimation) carry the ideas; the rest is the particle-physics setup |

## What it is

A test of what happens to anomaly detectors when most of the input features carry no
signal, and a case that gradient-boosted trees cope far better than neural networks.

- **The setting.** A search for a new particle in collider data: a small excess of signal
  events hidden in a narrow window of one variable (the dijet mass), with four physically
  motivated features that tell signal from background. The signal is 0.6% of events in
  the window. The authors then append 4 or 16 pure-noise Gaussian features to every event,
  the same for signal and background, to mimic a search where nobody knows in advance
  which features matter.
- **Irrelevant, made precise.** For the classifier, a feature is irrelevant if it says
  nothing about whether an event falls inside the window. For the density method, it must
  be independent of the window variable and the useful features, with the same
  distribution in signal and background.
- **Classifier: trees hold up, networks collapse.** The classifier learns to tell
  in-window events from those just outside it (Classification Without Labels). With no
  noise features, XGBoost and a 3×64 network perform about the same. With 16 noise
  features the network is essentially useless, while XGBoost still improves signal
  significance about 7-fold at its best point.
- **Retune after adding features.** With hyperparameters tuned on the clean data, XGBoost
  loses some performance as noise is added. Re-tuning on the noisy data recovers most of
  the original performance. XGBoost's default settings overfit badly at this signal level,
  so tuning was needed in any case.
- **Feature importance shows why.** Across 10 independently tuned models, the four real
  features get far more importance than the 16 noise columns. The trees mostly decline to
  split on noise, which acts as built-in feature selection.
- **Density estimation with boosted trees and a copula.** The second method estimates the
  data density inside the window and compares it with a background density interpolated
  linearly from either side; their ratio flags signal. The density is fitted in two
  stages: each feature's own distribution first, then the dependence between features (the
  copula, by Sklar's theorem). Independent noise features drop out of the ratio. The tree
  model learns not to cut along them, while a normalising flow (MAF) on the same data
  falls to random-guess performance at 16 noise features. The tree version is barely
  affected.
- **Where it weakens.** When the useful features are made to depend on the window
  variable, the authors first remove that dependence with a fitted transform. Trees still
  beat the flow, but they are less robust to noise than before. The fitted transform also
  finds spurious in-sample patterns in the noise features.

## Why it's in the library

**It is the cleanest controlled test of the noise-feature effect.** Grinsztajn et al.
found that networks are hurt by uninformative columns and trees are not, across many
benchmarks. Here the same effect is isolated: identical data with 0, 4 and 16 pure-noise
columns appended, and a low signal-to-noise target. Financial prediction problems look
like this, with a weak signal and many candidate features of which most add nothing.

**Tuning on one feature set does not carry over to another.** Hyperparameters tuned
before features were added lost part of the performance; re-tuning recovered it. After
adding or removing features, the model needs re-tuning before the comparison means
anything.

**Fitting a transform in-sample can create signal in pure noise.** The decorrelation step
searched for parameters that minimised in-sample dependence and fitted chance patterns in
the noise columns. Any preprocessing fitted to the data belongs inside the validation
loop, not before it.

**The copula split is a useful pattern beyond physics.** Fitting each variable's own
distribution separately from the dependence between variables is how copula models of
joint returns work. This paper shows that a tree model fitted in copula space ignores
features that add nothing to the dependence.

## Links

- [[bengio-delalleau-simard-2010-decision-trees-do-not-generalize-to-new-variations]] — the
  cost of the same region-by-region mechanism: no generalisation to unseen combinations
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — the benchmark finding (networks are not robust to uninformative features) that this
  paper isolates and builds on
- [[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] — XGBoost
  against deep tabular models on 11 datasets
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — why adding dimensions that
  carry no information degrades methods that treat all features together
- [[radovanovic-nanopoulos-ivanovic-2010-hubs-in-space-popular-nearest-neighbors-in-high-dimensional-data]]
  — another way high dimension distorts methods that use every feature
