# Literature

Reading notes on quantitative finance, grouped by **subject**. Each note covers one source.
It records what the source says, why it matters, and how it links to the others. Where the
source is freely redistributable, or is a lecture note, the PDF sits next to the note.

The sections are not in a set order: start wherever the question you have is. Each
section has a README that lists its subfolders and the question each one answers, and the
notes link across sections freely.

| Section | What's in it |
|---|---|
| [`active-management`](active-management/) | The fundamental law, skill versus scale, active share, the rise of passive, and tactical asset allocation rule-sets (Keller–Keuning family and others) |
| [`bear-markets`](bear-markets/) | Dating and forecasting bull and bear markets, bear rallies and reversals, risk-on/risk-off, bubbles, crises from 1907 to COVID, and Soros on reflexivity |
| [`compounding-leverage-and-position-sizing`](compounding-leverage-and-position-sizing/) | Volatility drag, the Kelly criterion, leveraged ETFs, ergodicity |
| [`correlation-and-dependence`](correlation-and-dependence/) | Random matrix theory, covariance shrinkage, copulas and tail dependence, why assets move together |
| [`factor-models-and-asset-pricing`](factor-models-and-asset-pricing/) | Single-index models to Fama–French, APT, how much of a return is common, the factor zoo, ML factor models |
| [`high-dimensional-geometry`](high-dimensional-geometry/) | The curse of dimensionality (distance concentration, hubness), intrinsic dimension, manifold learning and embeddings, PCA, ICA and kernel PCA |
| [`machine-learning`](machine-learning/) | Neural tangent kernel and generalisation, tree ensembles vs deep learning, representation learning (energy-based models, information bottleneck, language models), quantum cognition ML |
| [`macro-and-asset-allocation`](macro-and-asset-allocation/) | Gold and the dollar, inflation and monetary policy, the stock–bond correlation, safe-haven assets, global macro and asset allocation |
| [`mathematical-foundations`](mathematical-foundations/) | Probability and statistics textbooks, stochastic calculus, eigenvectors and principal axes, optimisation |
| [`momentum-and-trend-following`](momentum-and-trend-following/) | Time-series and cross-sectional momentum, trend filters, momentum crashes, machine learning for trends |
| [`portfolio-construction-and-risk`](portfolio-construction-and-risk/) | Mean-variance and estimation error, diversification and effective number of bets, tail risk and CVaR |
| [`reinforcement-learning`](reinforcement-learning/) | Policy optimisation, distributional RL, recurrent agents, continual learning and loss of plasticity, meta-learning under non-stationarity |
| [`tail-risk`](tail-risk/) | Tail hedging, defensive strategies (trend, rebalancing, volatility targeting), hidden short-volatility trades and dealer gamma, flash crashes and market microstructure |
| [`volatility-and-derivatives`](volatility-and-derivatives/) | The VIX and its futures, variance and volatility swaps, the variance risk premium, Lévy and stochastic-volatility option models, the FX smile and vanna-volga, exotic options and static hedging |
| [`podcasts-and-videos`](podcasts-and-videos/) | Lectures, interviews and documentaries, organised by person |

[`refs.bib`](refs.bib) holds a BibTeX entry for every source. Each note names its key.

## Reading a note

- **Status** says how far to trust a note. *Reference* or *Read* means it was written from
  the source. *To read* means it was written from the source's reputation and has not been
  checked against the text yet, so verify page numbers and volumes before citing.
- **Explainers** (blog posts, slides, Wikipedia) are kept next to the primary source they
  explain, and their notes say what to cite instead.
- **`[[name]]`** links to another note by filename, wherever it is filed. Search the repo
  for `name.md` to open it.
- Links point across sections freely. The folders are a way to browse, not a strict
  hierarchy. A paper is filed where someone learning the subject would look for it first.
