# Tail Risk Hedging: Contrasting Put and Trend Strategies

| | |
|---|---|
| **Authors** | Antti Ilmanen, Ashwin Thapar, Harsha Tummala, Dan Villalon (AQR Capital Management) |
| **Year** | 2021 |
| **Type** | Journal article, *Journal of Systematic Investing* (EQDerivatives), 2021, 16pp |
| **PDF** | Not hosted in this repository (© 2021 EQDerivatives, Inc.; no reproduction without permission) |
| **Find it** | [doi.org/10.52354/jsi.1.1.vi](https://doi.org/10.52354/jsi.1.1.vi) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Tail+Risk+Hedging%3A+Contrasting+Put+and+Trend+Strategies%22+Ilmanen) |
| **BibTeX** | `ilmanen2021tailhedging` |
| **Status** | Reference: Figure 1 (long-run cost), Figure 2 (robustness across put strategies) and Figure 3 (slow and fast tail events) carry the evidence |

## What it is

A side-by-side comparison of two ways to hedge equity crashes: buying index puts ("Put",
a 5% out-of-the-money one-month S&P 500 put bought mid-month and rolled at expiry, scaled
to 10% volatility) and multi-asset trend following ("Trend", 1-, 3- and 12-month signals
across four asset classes, 10% volatility, net of estimated costs). January 1985 to 2020.

- **Long-run cost.** Put loses money in every decade of the sample, through 1987, 1998,
  2001, 2008 and 2020; Trend earns a positive return over 35 years, though muted in the
  2010s. Six put variants from 1996 (different maturities, strikes, delta-hedged or not)
  show the same pattern of steady losses with occasional spikes. The CBOE Eurekahedge Tail
  Risk Index, a peer index of live managers since 2008, landed between the two (about −2%
  a year, −8% a year in the 2010s).
- **Tail performance.** Over the eight worst slow S&P 500 drawdowns, Put was profitable in
  seven and Trend in six; over the ten worst months, Put in all ten and Trend in nine.
- **Why Trend catches crashes.** None of the ten worst S&P 500 months was the *first* month
  of its drawdown, and half were the last (for example October 2008 was month 12 of 16,
  September 2002 month 30 of 30). Bad months tend to come after earlier trouble, so trend
  followers are often already short. October 1987 (month 2 of 3) is the main exception.
- **Theory.** A negative return on puts is what asset pricing predicts for insurance that
  pays in bad times; Trend is a return-seeking strategy whose crash protection is a
  by-product and not guaranteed.

## Why it's in the library

It is the most direct comparison here of the two standard tail hedges, and the
"worst month is rarely the first month" observation explains why trend following has
behaved like crash insurance more often than its mechanics would suggest.

The authors manage trend-following funds and draw the conclusion in Trend's favour
"except for investors who focus primarily on fast market drawdowns". Both series are
backtests; the put strategy is a deliberately simple benchmark that active tail managers
claim to beat; and with eight slow events and ten fast ones, the hit-rate comparison rests
on very few observations, as the paper acknowledges.

## Links

- [[mcquinn-thapar-villalon-2021-portfolio-protection-its-a-long-term-story]] — the companion AQR paper: puts protect against fast crashes, diversifiers against long bad periods
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]] — a long-volatility manager's view of why rule-based puts bleed and how to trade them instead
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — VIX calls compared with S&P 500 puts as the tail hedge
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — the optimal trend rule when markets switch between bull and bear states
- [[carr-wu-2009-variance-risk-premia]] — the variance risk premium behind the persistent cost of puts
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the case that volatility-sized strategies, which trade like trend following, can amplify crashes
- [[bhansali-holdom-2021-diversifying-diversification]] — puts, trend, bonds, gold and safe-haven currencies combined into one basket of crash hedges
- [[chang-holdom-bhansali-2021-tail-risk-hedging-performance-measuring-what-counts]] — a put-programme manager on measuring hedge performance at the portfolio level
- [[fung-hsieh-2001-the-risk-in-hedge-fund-strategies-trend-followers]] — why trend behaves like an option position: trend followers modelled as lookback straddles
- [[sepp-2018-trend-following-strategies-for-tail-risk-hedging-and-alpha-generation]] — trend's convexity measured by frequency and half-life: fast crashes escape it
