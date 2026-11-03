# Supervised Similarity for Firm Linkages

| | |
|---|---|
| **Authors** | Ryan Samson, Adrian Banner, Luca Candelori, Sebastien Cottrell, Tiziana Di Matteo, Paul Duchnowski, Vahagn Kirakosyan, Jose Marques, Kharen Musaelian, Stefano Pasquali, Ryan Stever, Dario Villani (Qognitive; Intech Investment Management; King's College London; Domyn; Deutsche Bank) |
| **Year** | 2025 |
| **Type** | Article — *Risk.net*, Cutting Edge: Investments, October 2025, 6pp |
| **Link** | [qognitiveai.com/papers/firm_linkages.pdf](https://www.qognitiveai.com/papers/firm_linkages.pdf) (Risk.net reprint) |
| **BibTeX** | `samson2025linkages` |
| **Status** | Reference — short; the similarity construction and Tables B and D carry the result |

## What it is

A way to decide which firms are economically linked from their accounting
characteristics alone, and a test of whether those links carry **momentum spillover**: the
past returns of a firm's close relatives predicting its own future return, because news
reaches linked stocks slowly. Earlier work built such links from industry, supply chains,
shared analyst coverage or geography.

- **Characteristic vector linkages (CVLs).** Describe each firm by 16 accounting and
  valuation ratios (accruals, book-to-price, earnings-to-price, leverage, profit margin,
  operating cash flow and so on), each demeaned within its industry so links are not just
  industry membership. Two firms with similar vectors are treated as linked.
- **Euclidean similarity.** The plain version: distance between the two characteristic
  vectors, turned into a similarity with S = exp(−D²/σ²) (σ = 1). Nothing is learned.
- **QCML similarity.** The learned version. A QCML model maps each firm's vector to a
  quantum ground state (Hilbert space of dimension 12), trained to forecast 63-day forward
  returns, with a penalty that keeps the states close to the inputs. Distance between two
  firms is the Bures distance between their states, √(2 − 2|⟨ψᵢ|ψⱼ⟩|), turned into a
  similarity the same way (σ = 16, chosen so the median distances match the Euclidean
  ones). The forecast itself is not used; only the learned geometry is. 50 models with
  different seeds, each on a random 10% of names, are averaged.
- **The spillover signal.** For each firm, take the similarity-weighted average of other
  firms' past returns over 21, 63, 126 or 252 days, plus a composite of all four. Signals
  are industry-demeaned and standardised.
- **Test design.** About 1,500 large, liquid US stocks. QCML trained once on October 2007 –
  August 2013, then frozen; tested January 2014 – June 2024. Signals become mean-variance
  portfolios with zero exposure to beta, size, momentum, short-term reversal, subindustry
  momentum, analyst coverage, the existing analyst-coverage spillover signal and industry,
  smoothed over 21 days, before transaction costs.
- **Results (Sharpe, full period, Tables B and D).** Euclidean: 1.35 (21-day), 1.03, 0.71,
  0.73 (252-day), composite 1.24. QCML: 1.38, 1.14, 1.04, 1.10, composite 1.42. The two
  signals correlate 0.74–0.78. QCML's advantage grows with the return horizon, and its
  signals decay more slowly (half-life 90.9 days against 36.3 at 252 days; 23.5 against
  14.8 for the composite). The conclusion quotes slightly different figures (1.12 vs 0.76,
  1.43 vs 1.26); the tables are used here.
- **The last sub-period is weak.** In January 2021 – June 2024 both composites are near zero
  (Euclidean 0.00, QCML 0.08); most of the performance comes from 2017–2020 (composites
  2.41 and 2.31).

## Why it's in the library

**Characteristics as a similarity measure is a simple, testable idea.** Firms that look alike
on their fundamentals, after removing industry, may move together and react to the same
news. This is the same intuition as building covariance from firm descriptors
([[rosenberg-1974]]) and the characteristics-versus-covariances debate
([[daniel-titman-1997]]), used here to define a network of linked firms rather than a risk
model.

**Learned similarity versus plain distance is the right comparison.** The paper benchmarks
the learned QCML distance against the obvious Euclidean baseline on identical inputs and
controls, and the gain is modest at short horizons and larger at long ones. Any learned
metric, from a QCML model, an autoencoder or a random-forest proximity, should be judged
against the plain distance on the same features.

**The controls show what "new" means.** The portfolios are built to have no exposure to the
known spillover signal from shared analyst coverage, to momentum and to industry, so what
remains is the part those don't explain. The near-zero results after 2021 are part of the
evidence as much as the full-period Sharpe ratios.

## Links

- [[rosaler-et-al-2025-supervised-similarity-for-high-yield-bonds]] — the same supervised
  QCML similarity applied to corporate bonds, which this paper adapts to equities
- [[samson-et-al-2024-quantum-cognition-machine-learning-financial-forecasting]] — the
  QCML training and forecasting set-up, the same universe and the same
  zero-exposure portfolio test
- [[abanov-et-al-2025-quantum-geometry-of-data]] — the geometry of the learned states that
  the fidelity and Bures distance are measured in
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — the QCML
  model's energy and its components, cited for the training loss
- [[rosenberg-1974]] — covariance built from firm descriptors, the risk-model ancestor of
  characteristic-based linkage
- [[daniel-titman-1997]] — whether characteristics or covariances explain returns
- [[markowitz-1952]] — the mean-variance weights used to turn signals into portfolios
- [[harvey-liu-zhu-2016]] — the multiple-testing bar for a new return signal
