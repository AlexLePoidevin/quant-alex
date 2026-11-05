# Cross-Section of Mini Flash Crashes and Their Detection by a State-Space Approach

| | |
|---|---|
| **Authors** | Chyng Wen Tee, Christopher Ting (Singapore Management University) |
| **Year** | 2019 (undated manuscript; the PDF was built in June 2019) |
| **Type** | Working paper. US TAQ data, S&P 500 constituents, 2010–2013 |
| **PDF** | Local copy only (no licence stated) |
| **BibTeX** | `tee2019mini` |
| **Status** | Reference: §3 (the detector) and §4.3–4.4 (crash counts and cross-section) carry the results |

## What it is

A method for finding mini flash crashes in trade data, and a description of which stocks
get them.

- **Existing definitions are threshold rules.** The paper surveys five definitions in use.
  - The common one is from the data vendor Nanex: at least 10 ticks in one direction,
    within 1.5 seconds, for a price change above 0.8%.
  - Others are trades outside the previous second's quotes, the top 0.1% of model
    residuals, nonparametric jump tests, and V-shaped drops that reverse.
  - The authors show cases the Nanex rule misses: a 9.25% move over 6.5 seconds that was
    not strictly one-way, and a large spike with fewer than 10 ticks.
- **The detector.**
  - Treat each trade's log price as a noisy measurement of an unobserved true log price
    that follows a random walk. The walk's variance grows with the time between trades.
  - Track the true price with a Kalman filter. Set the process noise from a
    multiplicative-component GARCH, so the filter knows the time of day and the day's
    volatility level. That GARCH is a daily model times a diurnal pattern times an
    intraday component, after Engle and Sokalska (2012).
  - Flag a crash when a trade lands more than z standard errors from the filtered price.
    Bursts of trades at similar prices tighten the band, and a sudden run of trades away
    from it crosses the band.
- **Data.** Daily TAQ for 572 S&P 500 stocks over 2010–2013: more than 11 billion trades
  and about 2.9 trillion shares. A falling volume Herfindahl index shows trading
  spreading across more venues every year.
- **How many crashes.** The count depends steeply on the threshold: 182,877 at z = 2,
  22,121 at z = 4, 7,492 at z = 6 (used for the analysis), and 1,308 at z = 12.
- **When they happen.** Crash counts spike on news and event days:
  - the 6 May 2010 Flash Crash (454 crashes);
  - 8 August 2011 (204);
  - QE3 on 13 September 2012 (142);
  - the Knight Capital glitch, 1 August 2012 (114);
  - the hoax tweet of 23 April 2013;
  - several Federal Reserve announcements.
- **Which stocks.** Splitting the 7,492 crashes into quintiles of market cap, volatility,
  volume and price gives the same picture in every split. Larger, less volatile, more
  traded and higher-priced stocks have smaller percentage moves in a crash, spread over
  more ticks and more time. Distribution tests reject equality across quintiles, and a
  regression on all the characteristics plus exchange dummies agrees: adjusted R² is 0.22
  for the price change, 0.88 for the tick count and 0.43 for the time window.
- **The interpretation.** Because crashes cluster on information events, the authors read
  mini flash crashes as the market absorbing news faster than before. On this view they
  are a by-product of faster price discovery rather than evidence that high-speed trading
  harms markets.

## Why it's in the library

**It replaces three hand-set thresholds with one statistical one.** A crash becomes "a
trade the filter did not expect", scaled by local volatility and trading intensity. The
same idea (filter a noisy price, flag large standardised innovations) works for detecting
bad prints and jumps in any tick or bar series, not only for crash studies.

**The cross-section is a useful prior on where intraday tail events are worst.** Small,
volatile, thinly traded, low-priced names have the largest percentage dislocations. That
is the end of a universe where execution at a single moment is most exposed.

**Read the claims with the method's limits in mind.**
- The number of crashes is set by the choice of z, which moves the count by two orders of
  magnitude.
- The claim to catch "a much broader range" of crashes than threshold rules is shown with
  examples, not with a measured overlap against the Nanex list.
- The diurnal volatility pattern is estimated from the same sample, so the detector as run
  is not fully real-time.
- The information-efficiency reading is an interpretation of the event-day clustering, not
  a test of it.

## Links

- [[shi-et-al-2020-modeling-flash-crash-behavior-with-multivariate-hawkes-processes]] — the
  6 May 2010 crash modelled as contagion between stocks rather than as single-stock events
- [[romero-2016-microstructure-noise-two-scales-realized-volatility]] — the same
  "efficient price plus noise" model of trade prices, used to estimate volatility instead
  of to flag outliers
- [[merton-1976]] — jumps in prices, which a mini flash crash is at the scale of seconds
- [[demos-et-al-2015-some-statistical-properties-of-the-mini-flash-crashes]] — the statistical properties of single-stock mini flash crashes
