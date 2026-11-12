# The Impact of Monetary Policy on the Specialness of U.S. Treasuries

| | |
|---|---|
| **Authors** | Ritt Keerati (Columbia Business School) |
| **Year** | 2020 (27 July 2020; SSRN 3682897) |
| **Type** | Empirical working paper, 62pp. (21pp. of text plus tables and appendices). G10 countries, 2000–2019, around scheduled Fed and ECB announcements |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3682897](https://doi.org/10.2139/ssrn.3682897) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Impact+of+Monetary+Policy+on+the+Specialness+of+U.S.+Treasuries%22+Keerati) |
| **BibTeX** | `keerati2020specialness` |
| **Status** | Reference: §3 (the U.S. Treasury Premium and its decomposition), §4 (event-study design), §5 (Fed shocks) and the Conclusion |

## What it is

An event study of how Fed and ECB policy surprises move the "specialness" of US Treasuries:
how much cheaper the US government can borrow in dollars than other rich-country governments.

- **The measure.** The U.S. Treasury Premium of Du, Im and Schreger (2018): the gap between
  the US Treasury yield and a foreign government bond yield swapped into dollars, i.e. a
  deviation from covered interest parity between government bond yields. It splits into
  three parts: the US swap spread (a proxy for the convenience yield of Treasuries), the
  foreign swap spread, and the cross-currency basis.
- **The design.** Policy surprises are the first principal component of rate changes in a
  30-minute window around each scheduled FOMC announcement (a longer window for the ECB).
  The response is the two-day change in the premium, to allow for time zones. Daily
  premium data for ten G10 countries, 2000–2019.
- **Fed tightening makes Treasuries more special.** A surprise that would raise the one-year
  Treasury yield by 100bp raises the premium by 31–50bp across maturities on average.
  Treasury yields rise, but swap (benchmark) rates rise more, so the convenience yield of
  Treasuries goes up.
- **Before and after 2008.** Before the crisis the effect was roughly parallel across
  maturities (30–46bp), and came almost entirely from the US convenience yield. After it,
  the effect slopes down: about +80bp at one year but only +20bp at ten years. Tightening
  now also lowers foreign bonds' convenience yields and widens the dollar cross-currency
  basis (a dollar shortage).
- **The ECB cannot do the same.** ECB surprises move Bund yields and euro swap rates by
  similar amounts, leaving the premium little changed except weakly at one year.
- **By country.** After 2008 the effect is largest against commodity currencies and smallest
  against safe-haven ones, with Swiss bonds looking like the closest substitute for
  Treasuries.

## Why it's in the library

**It shows the Fed controls the supply of the world's safe asset.** Tightening makes dollar
safe assets scarcer and more valuable, in a way no other central bank can match. That is the
mechanism behind the dollar's strength in Fed hiking cycles and in flights to safety.

**It connects monetary policy to cross-currency funding stress.** The post-2008 widening of
the cross-currency basis after Fed tightening is the same dollar-shortage channel that swap
lines and repo facilities are used to relieve in crises.

**A single-author working paper with a known identification issue.** The author notes that
the alternative policy-shock measure and the premium both use Treasury yields, which could
bias the estimates, and argues the different windows mitigate this; the text at that point
swaps which variable uses the 30-minute and which the two-day window. The results have not
been through journal review.

## Links

- [[durdu-martin-zer-2019-us-monetary-policy-in-global-banking-crises]] — US monetary policy surprises and their effect on banking crises abroad
- [[brooks-2021-what-drives-bond-yields]] — the components of government bond yields that the swap spread and convenience yield sit inside
- [[carr-fisher-ruf-2014-on-the-hedging-of-options-on-exploding-exchange-rates]] — FX pricing when one currency can collapse, a reminder that "safe" status is relative
