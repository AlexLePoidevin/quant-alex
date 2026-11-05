# Oil and Fiscal Policy Regimes

| | |
|---|---|
| **Authors** | Hilde C. Bjørnland (BI Norwegian Business School; Norges Bank), Roberto Casarin (Ca' Foscari Venice), Marco Lorusso (Newcastle University), Francesco Ravazzolo (Free University of Bozen-Bolzano; BI) |
| **Year** | 2021 (dated 11 January 2021) |
| **Type** | Working paper, CAMA Working Paper 10/2021 (ANU), also SSRN 3769785, 88pp. including appendices |
| **PDF** | Local copy only (working paper, no licence stated) |
| **BibTeX** | `bjornland2021oil` |
| **Status** | Reference: §1 (identification idea), §4 (regime volatilities and the regime probabilities in Figures 7–8) and §5 carry the findings; the long appendices hold the data construction and country results |

## What it is

A macroeconomics paper on how oil-exporting governments spend: do they save in booms and
spend in busts (countercyclical, the textbook advice), or spend as the oil money comes in
(procyclical)? Instead of assuming one behaviour for the whole sample, it lets each country
switch between the two.

- **The model.** A Bayesian Markov-switching panel VAR for 23 oil producers (including
  Norway, Russia, Saudi Arabia, the US, the UK, Canada and most of OPEC), which together
  produced 84% of world oil over 1965–2019. Variables per country: government spending,
  oil revenue and the non-oil balance (all relative to GDP), public employment, the real
  oil price and the real exchange rate, in quarterly growth rates (annual data split into
  quarters). 138 variables in all.
- **How regimes are identified.** A *procyclical* regime is one where oil revenue and
  spending grow or shrink together; a *countercyclical* one is where they move in opposite
  directions. These are imposed as sign restrictions on the regime means; volatilities are
  left free.
- **Findings.**
  - Every group of countries switches between the two regimes several times. Neither "oil
    states are always procyclical" nor "they have become less procyclical over time" holds.
  - Oil revenue and spending are more volatile in the countercyclical regime, plausibly
    because revenue falls are abrupt.
  - In procyclical periods, non-OECD and OPEC countries spend more aggressively than OECD
    countries, which save more of the windfall. Procyclical probabilities correlate 0.89
    between non-OECD and OPEC but only 0.17 between OECD and non-OECD.
  - Episodes that stand out: OECD loosening after the Asian crisis (1996–97); non-OECD
    spending during the 2002–07 oil boom; all groups moving procyclical in the recovery
    after the 2014–15 oil collapse. Norway is procyclical in the 1990s and from about 2011
    to 2015 despite its 2001 spending rule.

## Why it's in the library

It is a clean example of regime-switching applied to policy rather than prices, with the
regimes defined by an economic restriction (sign of co-movement) rather than left to the
data. For markets, the link is indirect: procyclical spending by oil exporters amplifies
oil-price booms and busts in their economies and currencies, and how governments react to
an oil shock is part of why it spreads.

It says nothing directly about asset returns, and some results are reported only as
figures. The authors note their 68% posterior bands are available on request.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — Markov switching
  applied to market states rather than policy
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — a two-regime switching model for
  volatility
