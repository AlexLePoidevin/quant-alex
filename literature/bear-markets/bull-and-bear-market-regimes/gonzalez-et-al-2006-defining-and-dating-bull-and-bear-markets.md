# Defining and Dating Bull and Bear Markets: Two Centuries of Evidence

| | |
|---|---|
| **Authors** | Liliana Gonzalez (Rhode Island), Philip Hoang (ANU), John G. Powell (Massey), Jing Shi (ANU) |
| **Year** | 2006 |
| **Type** | Journal article, *Multinational Finance Journal* 10(1/2), 81–116 (2006). doi:10.17578/10-1/2-3. The copy is the journal version posted to SSRN (2625037) in 2015 |
| **PDF** | `gonzalez-et-al-2006-defining-and-dating-bull-and-bear-markets.pdf` (kept locally; © Multinational Finance Society, all rights reserved) |
| **Find it** | [doi.org/10.17578/10-1/2-3](https://doi.org/10.17578/10-1/2-3) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Defining+and+Dating+Bull+and+Bear+Markets%3A+Two+Centuries+of+Evidence%22+Gonzalez) |
| **BibTeX** | `gonzalez2006bullbear` |
| **Status** | Reference: Tables 1A–1B and 2 (turning-point dates), Table 3 (durations against a random walk) and Table 5 (out-of-sample trading rules) carry the results |

## What it is

A formal definition of bull and bear markets as persistent shifts in the mean return,
dated with two rule-based methods on US monthly stock prices from January 1800 to December
2001.

- **The definition.** Returns are normal with constant volatility, but the mean switches
  between regimes. A turning point is a switch in the mean that lasts long enough to count
  as "persistent".
- **BB method.** An adaptation of the Bry–Boschan business-cycle algorithm: a peak (trough)
  is higher (lower) than the five months on either side, and each phase must move the index
  at least 10%. Applied in real time, it needs a six-month lag.
- **CC method.** A count-cusum rule: for each month, count how many of the six overlapping
  six-month windows around it beat the 25-year rolling median return. A switch is declared
  when the count crosses three and then reaches one or five, with a five-month minimum
  phase unless a month moves 20%.
- **Agreement.** The two methods classify the same state in 84% of months. Bull-market
  turns since 1950 mostly coincide; CC calls bear markets earlier in 8 cases out of 12,
  for example flagging a low-return state from April 1999.
- **Durations.** Bull markets last about 20–22 months on average and bear markets 15–18.
  The market spends just under 60% of months in bull markets. For the BB method, both bull
  and bear phases last longer than a random walk with constant drift would produce, which
  the authors read as evidence that the mean really does switch.
- **Return gap.** Months that both methods call bull average +2.1% a month; months both
  call bear average −2.1%. Over 70% of bull months are positive and under 40% of bear months.
  Bear-month volatility is less than 10% higher than bull-month volatility.
- **Trading rules, 1934–2001.** Holding the index only after a lagged bull signal
  (otherwise Treasury bills) roughly halves volatility for a small return cost. A version
  that doubles the index position in bull markets earns about 50% more than buy-and-hold at
  similar risk. Monthly Sharpe ratios for buy-and-hold are 0.19 (1934–67) and 0.10
  (1968–2001); the BB "conservative" rule gets 0.25 and 0.18.

## Why it's in the library

- **Bull and bear defined by the mean, not the volatility.** This is the counterpart to the
  Markov-switching papers, where volatility does most of the work. Here bear markets are
  barely more volatile than bull markets; what differs is the average return.
- **Long history.** Two centuries of dated turning points, with the full list of phases in
  the tables, is a useful reference.
- **What to discount.** The ±2.1% gap and the claim that phase dummies explain a third of
  return variation are close to true by construction: the phases are defined from the same
  returns. The out-of-sample trading rules are the fair test, and their results are mixed
  in places. In 1934–67 the CC conservative rule has a slightly lower Sharpe ratio than
  buy-and-hold (0.189 against 0.193), and in 1968–2001 the BB conservative rule earned more
  than buy-and-hold, not less as the text says. The table labelled Table 2 repeats Table 1B
  rather than giving the summary statistics the text describes.

## Links

- [[maheu-mccurdy-2000-identifying-bull-and-bear-markets-in-stock-returns]] — the
  Markov-switching alternative, in which bear markets are the high-volatility state and the
  market spends 90% of the time in bull markets
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — four states instead of
  two, separating bear rallies and bull corrections
- [[zegadlo-2022-identifying-bull-and-bear-market-regimes-rule-based]] — a later rule-based
  dating method in the same spirit
- [[yang-wagner-2014-optimal-probabilistic-market-timing-using-bull-bear-cycle-statistics]]
  — timing rules built from bull and bear cycle statistics
- [[schultz-2002-bear-market-investing-strategies]] — the practitioner Dow Theory view of bull
  and bear phases that this formalises
