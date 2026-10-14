# Literature

Reading notes on quantitative finance, grouped by **subject**. Each note covers one source.
It records what the source says, why it matters, and how it links to the others. Where the
source is freely redistributable, or is a lecture note, the PDF sits next to the note.

The sections are numbered as a rough **learning path**. Mathematical foundations come first.
Then come the questions in order: what drives returns (factor models), how assets move
together (correlation and dependence), how to find structure in data (dimensionality
reduction and ML), and how to build, size and run a portfolio from that structure. Every
section has a README that lists its subfolders and the question each one answers.

| # | Section | What's in it |
|---|---|---|
| 01 | [`01-mathematical-foundations`](01-mathematical-foundations/) | Probability and statistics textbooks, stochastic calculus, eigenvectors and principal axes, optimisation |
| 02 | [`02-factor-models-and-asset-pricing`](02-factor-models-and-asset-pricing/) | Single-index models to Fama–French, APT, how much of a return is common, the factor zoo, ML factor models |
| 03 | [`03-correlation-and-dependence`](03-correlation-and-dependence/) | Random matrix theory, covariance shrinkage, copulas and tail dependence, why assets move together |
| 04 | [`04-dimensionality-reduction-and-machine-learning`](04-dimensionality-reduction-and-machine-learning/) | PCA, ICA, kernel PCA, diffusion maps, intrinsic dimension, quantum cognition ML |
| 05 | [`05-portfolio-construction-and-risk`](05-portfolio-construction-and-risk/) | Mean-variance and estimation error, diversification and effective number of bets, tail risk and CVaR |
| 06 | [`06-compounding-leverage-and-position-sizing`](06-compounding-leverage-and-position-sizing/) | Volatility drag, the Kelly criterion, leveraged ETFs, ergodicity |
| 07 | [`07-active-management`](07-active-management/) | The fundamental law, skill versus scale, active share, the rise of passive |
| 08 | [`08-tactical-asset-allocation`](08-tactical-asset-allocation/) | Published momentum/TAA rule-sets (Keller–Keuning family and others) and the evidence on them |
| 09 | [`09-reflexivity-and-market-history`](09-reflexivity-and-market-history/) | Soros on reflexivity: why a market's statistics are not fixed parameters |
| — | [`podcasts-and-videos`](podcasts-and-videos/) | Lectures, interviews and documentaries, organised by person |

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
