# Investing in Gold – Market Timing or Buy-and-Hold?

| | |
|---|---|
| **Authors** | Dirk G. Baur (University of Western Australia), Hubert Dichtl, Wolfgang Drobetz, Viktoria-Sophie Wendt (University of Hamburg) |
| **Year** | 2020. Published in *International Review of Financial Analysis* 71, 101281. The copy is the November 2018 SSRN draft (SSRN 3202658) |
| **Type** | Journal article (working-paper version), 33pp |
| **PDF** | Local copy only (SSRN working paper; the journal version is Elsevier copyright) |
| **BibTeX** | `baur2020goldtiming` |
| **Status** | Reference: §3.1 (the signals), Table 4 (the SPA tests) and §4.3 (sub-periods) carry the result |

## What it is

A large test of whether gold can be timed, with the multiple-testing correction that most
timing studies leave out.

- **The candidate rules.** Monthly signals that are either "in gold" or "in cash", in three
  families:
  - *seasonal*: every one of the 2¹² = 4,096 combinations of months to hold gold, which
    includes the "autumn effect" (September and November only);
  - *technical*: ten moving-average crossovers and eight time-series momentum rules
    (1 to 48 months);
  - *fundamental*: eleven predictive regressions on macro variables (rolling 120-month
    windows), plus their mean forecast, a kitchen-sink regression, LASSO and principal
    components.
- **The test.** Evaluation runs from January 1990 to December 2017 (data from 1980), with
  20 bp turnover costs. Each family is compared with a benchmark using Hansen's
  superior-predictive-ability (SPA) test and its step-wise and false-discovery extensions.
  These ask whether the *best* rule beats the benchmark once you account for having looked
  at all the others.
- **In-sample, timing looks good.** The best seasonal rules get the direction right at
  least 57% of the time and beat buy-and-hold by more than 0.19 percentage points a month.
  The best technical and fundamental rules beat it by about 2.3 percentage points a year,
  and the best seasonal rule by at least 2.7.
- **After the correction, it does not.** No family beats a random walk on direction or
  buy-and-hold on returns once data snooping is accounted for. The best seasonal rule's
  pairwise p-value of 0.087 becomes a consistent SPA p-value of 0.746. The best technical
  rule (one-month against 48-month moving average) only reaches 10% significance even
  pairwise. Sharpe ratios look a little better for timing, but mostly because time in cash
  lowers volatility.
- **Sub-periods.** Timing helped in 1990–2001, when gold lost 0.25% a month and the
  fundamental signals were in gold only 22 of 144 months. Nothing beat buy-and-hold in the
  2002–2012 boom. Nothing helped in 2013–2017 either, despite gold losing 0.42% a month.
  Picking the right sub-period would itself require foresight.

## Why it's in the library

**It is a worked example of what a data-snooping correction does to a backtest.** The same
rules that look like 2–3% a year of alpha in a table have no significance once you count
how many rules were tried. It is a good template for testing any family of timing rules.

**It is evidence that the gold market is hard to time.** Seasonal, trend and macro signals
all fail the corrected test. The authors read this as gold being informationally efficient
with respect to these signals, consistent with earlier forecasting studies.

**It shows statistical accuracy and economic value coming apart.** Rules that predict the
sign of next month's return better than chance do not necessarily make money, and the
periods where they predict best are not the periods where they pay best.

## Links

- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] —
  avoiding the rule search entirely
- [[harvey-liu-zhu-2016]] — the multiple-testing problem across the factor literature
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a
  trend rule derived from a model rather than picked from many
- [[daly-2005-tactical-asset-allocation-to-gold]] — a single in-sample gold timing rule of
  exactly the kind this test is designed to catch
- [[erb-harvey-viskanta-2020-gold-the-golden-constant-and-massive-passives]] — gold's real
  price as a valuation signal, with no claim of timing
- [[peterson-2018-when-to-own-stocks-and-when-to-own-gold]] — a single stocks-versus-gold switching rule, worth judging by this paper's standard
