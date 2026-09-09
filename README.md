# Quant Research

A working literature library for quantitative finance research. One note per paper, plus a
BibTeX file that feeds the write-ups. Notes are opinionated summaries, not neutral abstracts.

Structure: `literature/<section>/<author-year>.md`. Citations live in [`refs.bib`](refs.bib).

---

## Passive vs Active Portfolio Management

### 1 · Foundations & the Fundamental Law

Where active return comes from, and how information becomes a portfolio. **IR = IC × √Breadth.**

| Paper | Authors | Year |
|---|---|---|
| [Active Portfolio Management](literature/01-foundations/grinold-kahn-1999.md) | Grinold; Kahn | 1999 |
| [Information, Security Selection, Portfolio Construction, and Active Equity Management](literature/01-foundations/guerard-et-al.md) | Guerard; Blay; Mo; Hoang; Chen | — |

### 2 · Market Equilibrium & the Skill-Scale Debate

Why skill can be real and persistent outperformance still absent — capital chases alpha
until returns to scale bind.

| Paper | Authors | Year |
|---|---|---|
| [Mutual Fund Flows and Performance in Rational Markets](literature/02-skill-scale/berk-green-2004.md) | Berk; Green | 2004 |
| [On the Size of the Active Management Industry](literature/02-skill-scale/pastor-stambaugh-2012.md) | Pástor; Stambaugh | 2012 |
| [Scale and Skill in Active Management](literature/02-skill-scale/pastor-stambaugh-taylor-2015.md) | Pástor; Stambaugh; Taylor | 2015 |

### 3 · Measuring Active Conviction

How much of a portfolio actually deviates from the benchmark — separating genuine active
bets from closet indexing.

| Paper | Authors | Year |
|---|---|---|
| [How Active Is Your Fund Manager?](literature/03-active-conviction/cremers-petajisto-2009.md) | Cremers; Petajisto | 2009 |
| [Indexing and Active Fund Management: International Evidence](literature/03-active-conviction/cremers-et-al-2016.md) | Cremers; Ferreira; Matos; Starks | 2016 |

### 4 · The Rise of Passive Investing

What the growth of indexing does to the opportunity set — and to measured manager skill.

| Paper | Authors | Year |
|---|---|---|
| [The Rise of Passive Investing and Active Mutual Fund Skill](literature/04-rise-of-passive/huang-rise-of-passive.md) | Huang | — |

### 5 · Active/Passive Allocation

Treating the active-vs-passive split as a decision to be sized and timed, not a one-off choice.

| Paper | Authors | Year |
|---|---|---|
| [The Better-of-Two Strategy for Active Management](literature/05-allocation/fox-hammond-2020.md) | Fox; Hammond | 2020 |

---

## Adding a paper

1. Drop a note in the right `literature/<section>/` folder, named `<first-author>-<year>.md`.
2. Copy the header table from any existing note.
3. Add the entry to `refs.bib`.
4. Add a row to the section table above.

## Conventions

- **Status** — `To read` / `Reading` / `Read` / `Cited`.
- **Used in** — which write-up cites it, if any.
- Years marked `—` are unconfirmed working papers.
