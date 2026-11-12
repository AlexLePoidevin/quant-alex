# The Timing of the Flight to Gold: An Intra-day Analysis of Gold and the S&P500

| | |
|---|---|
| **Authors** | Dirk G. Baur (UWA Business School), Konstantin Kuck (University of Hohenheim) |
| **Year** | 2020 (*Finance Research Letters* 33, 101187; doi:10.1016/j.frl.2019.05.005). The copy is the SSRN 3243111 version dated 19 April 2019 |
| **Type** | Short empirical paper, 17pp |
| **PDF** | Not hosted in this repository (SSRN working-paper version; the journal version is Elsevier) |
| **Find it** | [doi.org/10.1016/j.frl.2019.05.005](https://doi.org/10.1016/j.frl.2019.05.005) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Timing+of+the+Flight+to+Gold%3A+An+Intra-day+Analysis+of+Gold+and+the+S%26P500%22+Baur) |
| **BibTeX** | `baur2020flightgold` |
| **Status** | Reference: §2.2 (the ten extreme days), §2.3 (average paths) and §2.4 (Tables 6–7) carry the results |

## What it is

The first look at gold's "safe haven" behaviour at intraday speed. It asks how fast gold
reacts when stocks crash, using 5-minute S&P 500, gold spot and front gold futures prices
from January 2007 to July 2018 (Thomson Reuters tick data, bid-ask midpoints).

- **On ordinary days gold barely relates to stocks.** The 5-minute correlation is about
  +0.10. Gold is more volatile while US stocks are trading than outside those hours, which
  suggests equity trading carries news that matters for gold.
- **The ten worst days.** "Extreme" days are those where the S&P 500 fell more than 4.5%
  from open to close: ten days, nine of them in 2008 (−4.6% to −8.9%, average −6.4%). On
  those days gold rose about 1% on average from the US open to the next open. Gold also
  fell on some of them (19 November and 1 December 2008), which the authors read as
  investors selling gold to cover equity losses later in the crisis.
- **The timing.** Average cumulative gold returns turn and stay positive once the S&P 500
  is down more than about 3% in the first four hours. Gold keeps rising after the US
  close on crash days. The 30-minute correlation turns negative towards the end of extreme
  days.
- **The regression.** A GJR-GARCH "safe haven" regression of 5-minute gold returns on S&P
  returns, with extra slopes for S&P drops beyond −0.3%, −0.5%, −0.75% and −1%. Only the
  largest bucket (58 five-minute drops below −1%) has a significantly negative extra slope,
  which cancels gold's normal small positive link to stocks. In those moments gold is a
  "weak" safe haven (uncorrelated), not one that rallies hard. Quantile regressions agree,
  with the strongest effect when gold itself has its largest gains.
- **Crashes are slow.** Large daily equity losses build up over several hours rather than
  in single 5-minute bars, so the "flight to gold" also builds over hours.

## Why it's in the library

It pins down what gold actually does on a crash day. On average the move is small (about
+1% against a −6% equity day), it starts only once the fall is large and persistent, and
it is not reliable across the worst days of 2008. That matters for anyone holding gold as
crash protection: it is protection against a drawn-out sell-off more than a fast one, and
it can be sold alongside stocks when investors need cash.

Limits: the extreme-day results rest on ten days, nine of them from one crisis. There
are no out-of-sample tests, and the safe-haven regression's thresholds are set by hand.

## Links

- [[peterson-2018-when-to-own-stocks-and-when-to-own-gold]] — gold as the long-horizon risk-off asset in secular bear markets, rather than a crash-day hedge
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the other common crash hedge, long VIX, and what it did in 2008 versus its cost in calm years
- [[easley-et-al-2011-microstructure-of-the-flash-crash]] — 6 May 2010, one of the two news days this paper plots, where gold moved before US stocks opened on the news
- [[boyarchenko-larsen-whelan-2023-the-overnight-drift]] — another intraday study of what happens to prices after heavy selling at the US close
- [[baur-mcdermott-2013-financial-turmoil-and-safe-haven-assets]] — daily evidence that Treasuries rally the same day as a stock crash while gold responds the day after
- [[baur-tran-2014-the-long-run-relationship-of-gold-and-silver]] — the same author on gold and silver: a long-run link that exists mainly because of bubbles and crises
- [[erb-harvey-2013-the-golden-dilemma]] — the broader case against gold as an inflation hedge or reliable safe haven, with stocks and gold both falling in 17% of months
- [[erb-harvey-2016-the-golden-constant]] — a fair-value model for gold from its long-run real price, and why perfect inflation forecasts barely help predict gold returns
