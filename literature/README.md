# Literature

Reading notes on quantitative finance, grouped by **subject**. Each note covers one source.
It records what the source says, why it matters, and how it links to the others. Where the
source is freely redistributable, or is a lecture note, the PDF sits next to the note.

The sections are not in a set order: start wherever the question you have is. Each
section has a README that lists its subfolders and the question each one answers, and the
notes link across sections freely.

| Section | What's in it |
|---|---|
| [`active-management`](active-management/) | The fundamental law, skill versus scale, active share, the rise of passive |
| [`compounding-leverage-and-position-sizing`](compounding-leverage-and-position-sizing/) | Volatility drag, the Kelly criterion, leveraged ETFs, ergodicity |
| [`correlation-and-dependence`](correlation-and-dependence/) | Random matrix theory, covariance shrinkage, copulas and tail dependence, why assets move together |
| [`dimensionality-reduction-and-machine-learning`](dimensionality-reduction-and-machine-learning/) | PCA, ICA, kernel PCA, diffusion maps, intrinsic dimension, quantum cognition ML, information bottleneck, tree ensembles vs deep learning, neural tangent kernel, generalisation, energy-based models, commonsense reasoning and language models, ML trading strategies |
| [`factor-models-and-asset-pricing`](factor-models-and-asset-pricing/) | Single-index models to Fama–French, APT, how much of a return is common, the factor zoo, ML factor models |
| [`mathematical-foundations`](mathematical-foundations/) | Probability and statistics textbooks, stochastic calculus, eigenvectors and principal axes, optimisation |
| [`portfolio-construction-and-risk`](portfolio-construction-and-risk/) | Mean-variance and estimation error, diversification and effective number of bets, tail risk and CVaR |
| [`reflexivity-and-market-history`](reflexivity-and-market-history/) | Soros on reflexivity: why a market's statistics are not fixed parameters |
| [`reinforcement-learning`](reinforcement-learning/) | Policy optimisation, distributional RL, recurrent agents, continual learning and loss of plasticity, meta-learning under non-stationarity, RL trading agents |
| [`tactical-asset-allocation`](tactical-asset-allocation/) | Published momentum/TAA rule-sets (Keller–Keuning family and others) and the evidence on them |
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
