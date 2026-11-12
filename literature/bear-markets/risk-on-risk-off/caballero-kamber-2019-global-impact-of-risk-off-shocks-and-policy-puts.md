# On the Global Impact of Risk-off Shocks and Policy-put Frameworks

| | |
|---|---|
| **Authors** | Ricardo J. Caballero (MIT; NBER), Gunes Kamber (BIS; Reserve Bank of New Zealand) |
| **Year** | 2019 (March 2019; first draft February 2018) |
| **Type** | BIS Working Paper No. 772, also SSRN 3349510 and NBER w26031, 57pp. Structural VARs on weekly data, about 1999–2017 |
| **PDF** | Not hosted in this repository (BIS working paper, no open licence) |
| **Find it** | [doi.org/10.3386/w26031](https://doi.org/10.3386/w26031) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22On+the+Global+Impact+of+Risk-off+Shocks+and+Policy-put+Frameworks%22+Caballero) |
| **BibTeX** | `caballero2019riskoff` |
| **Status** | Reference: the ten numbered claims in §1, §3 (US and other developed markets) and §4 (emerging markets) carry the evidence |

## What it is

An empirical study of what a global "risk-off" shock (a jump in the VIX) does to stock,
bond and currency markets, and how much central banks' responses limited the damage before
and after rates hit zero.

- **The idea.** Following Caballero and Simsek's risk-centric model: when fear rises,
  investors will only hold risky assets at a lower price. A central bank can offset this by
  cutting rates. At the zero lower bound it cannot, so prices must fall further and drag
  demand with them, unless the central bank absorbs risk itself (asset purchases) or raises
  the expected recovery (forward guidance). A credible commitment to do this is the
  *policy put*.
- **The method.** Weekly VARs with the VIX ordered first, so a risk-off shock is a VIX move
  not caused by the other variables that week. Two samples: early 1999 to September 2008
  (rates could be cut) and April 2009 onwards (zero lower bound and quantitative easing).
  The shock is set to 15 VIX points, the average of the three largest weekly rises.
- **Main findings.**
  - Risk-off shocks are global: their correlation is 0.91 between the US and the euro area
    and 0.83 between the US and Japan.
  - A 15-point VIX shock lowers US stocks by about 14%.
  - Before 2008 the Fed cut by a little over 100bp in response; the 1-year yield fell by
    nearly 100bp and the 10-year by about 40bp at a lag of 16 weeks. After 2009, with short
    rates stuck, the 10-year still fell by a similar amount but immediately.
  - The half-life of the VIX shock roughly halved after the crisis, from 10 weeks to 5,
    which the authors attribute to confidence in the policy put.
  - Emerging markets suffer capital outflows, higher long rates and weaker currencies in a
    risk-off episode. These effects were milder in the unconventional-policy period, and
    milder still for richer, more integrated economies with small current-account deficits,
    large reserves or their own safe assets.
  - Europe's periphery benefited mainly after "whatever it takes"; Japan, with rates
    already low, benefited less and its currency rose.

## Why it's in the library

It quantifies the policy put that bear-market and risk-off discussions take for granted:
how far a fear shock pushes stocks down, and how much faster it fades when markets believe
the central bank will step in. It also explains why emerging markets are hit through their
bond yields and currencies rather than just their stocks.

The authors call much of their evidence circumstantial. The identification is a simple
ordering (an external-instrument check is in the appendix), the post-2009 sample is
short, and attributing the shorter shock half-life to policy credibility is an
interpretation, not a test. The data stop before the 2020 episode.

## Links

- [[beber-et-al-2013-switching-risk-off-fx-correlations-and-risk-premia]] — risk-off
  episodes dated from FX correlation regimes, and what they do to carry trades
- [[carr-wu-2006-a-tale-of-two-indices]] — what the VIX measures, the fear gauge used here
  to define a shock
- [[soros-2013]] — feedback between beliefs and prices, the mechanism behind a policy put
- [[bekaert-hoerova-lo-duca-2013-risk-uncertainty-and-monetary-policy]] — evidence that easier policy lowers the risk-aversion part of the VIX
- [[cieslak-vissing-jorgensen-2021-the-economics-of-the-fed-put]] — the US evidence: stock falls predict Fed cuts through growth downgrades, and why the Fed watches the market
