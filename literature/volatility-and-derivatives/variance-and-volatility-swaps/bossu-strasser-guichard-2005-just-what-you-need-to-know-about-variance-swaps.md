# Just What You Need to Know About Variance Swaps

| | |
|---|---|
| **Authors** | Sébastien Bossu; Eva Strasser; Régis Guichard (JPMorgan, London: Equity Derivatives Investor Marketing and Quantitative Research & Development) |
| **Year** | 2005 (first published February 2005; this version May 2005) |
| **Type** | Bank research note, 30pp. A condensed version appeared as Bossu, "Introduction to Variance Swaps", *Wilmott Magazine*, March 2006 (written at Dresdner Kleinwort Wasserstein) |
| **PDF** | Not hosted in this repository (JPMorgan copyright, "All rights reserved") |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Just+What+You+Need+to+Know+About+Variance+Swaps%22+Bossu) for the title and authors |
| **BibTeX** | `bossu2005variance` |
| **Status** | Reference: §1 (contract, rules of thumb, uses, mark-to-market) and §2 (why a delta-hedged option is a gamma-weighted variance swap, and the 1/K² replication) carry the content; §3 adds the dividend and jump corrections |

## What it is

The standard practitioner introduction to variance swaps. It is written in three layers:
facts for investors, an intuitive derivation for traders, and the continuous-time results
for quants.

- **The contract.** At maturity the buyer receives realized variance minus a fixed strike,
  times a notional. Realized variance is 252 times the average squared daily log return,
  with no mean subtracted. Dropping the mean makes variance additive over time: 3-month
  variance plus 9-month variance starting in 3 months equals 1-year variance. Notionals are
  quoted in vega terms, with variance notional = vega notional / (2 × strike), so a 1-point
  miss on volatility pays roughly the vega notional.
- **Convexity and the strike.** The payoff is convex in volatility, so the long side gains
  more on a vol spike than it loses on a vol collapse. That convexity is paid for in a strike
  above at-the-money volatility, more so when the skew is steep. In practice the fair strike
  sits near the implied volatility of the 90% put.
- **Rules of thumb.** For a skew that is linear in strike (Demeterfi, Derman, Kamal and Zou,
  1999), K_var ≈ σ_ATMF √(1 + 3T × skew²). The worked example (20% ATM, 2 years, a 2-point
  90–100 skew) gives about 22.3%. The note warns that this only works when the skew is not
  steep.
- **Uses.** Directional bets on realized or implied volatility; forward volatility built
  from a calendar spread of two variance swaps (exact, because variance is additive); spreads
  between correlated indices (DAX against EuroStoxx 50); and **dispersion**, selling index
  variance against buying the variance of the components, which is a short position in
  correlation.
- **Mark-to-market and Greeks.** Value at time t is the time-weighted mix of variance
  realized so far and the current fair strike for the remaining period. Vega decays linearly
  to zero at maturity. The note gives rough rules for sensitivity to skew and to dividends.
- **The key idea: a delta-hedged option is a variance swap with the wrong weights.** The
  daily P&L of a delta-hedged option is ½ × dollar gamma × (squared return − implied
  variance × dt). Summed to maturity, that is a variance swap whose weights are the option's
  dollar gamma along the path. That is why an option seller can lose money even when
  realized volatility comes in below implied: the worked example sells a 110% call at 30%
  vol, sees 27.5% realized, and still loses because the stock sat near the strike (gamma at
  its peak) just as volatility jumped from 20% to 40%.
- **Static replication.** Weight out-of-the-money puts and calls by 1/K² and their combined
  dollar gamma is flat across spot levels, so the portfolio pays realized variance whatever
  the path. Equivalently, variance is replicated by a log contract plus delta-hedging, and
  the log contract is built from the strip of options. The EuroStoxx example prices a
  one-year swap from 5%-spaced strikes at 16.62% against 16.54% from a more accurate method,
  with the 90% put at 17.3%.
- **Dividends and jumps.** Discrete dividends add variance that does not vanish as
  monitoring becomes continuous. Jumps break the replication: the option strip then prices
  the diffusive part of variance and misprices the jump contribution, by an amount that
  depends on jump size and frequency (a Merton jump-diffusion is worked through).

## Why it's in the library

**It is the clearest account of what volatility trading actually is.** The P&L identity
(gamma × (realized − implied variance)) and the 1/K² replication are the base for
everything else in this section. The VIX is the square root of the same option strip,
priced for 30 days; a variance swap settles on the variance that is then realized; and
"selling volatility" means collecting the gap between the two.

**It explains the cost and the danger of short-volatility strategies.** Selling variance
earns the spread between implied and realized volatility, which is usually positive, "the
derivative house has the statistical edge". The convexity means the seller's losses in a
volatility spike are larger than the gains in calm periods. This is the instrument-level
version of the argument in [[cole-2017-volatility-and-the-alchemy-of-risk]].

**It is a bank's investor-marketing note.** The maths is standard and correct, and the
examples are illustrative rather than evidence about returns. The "statistical edge" claim
is asserted, not measured here.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  buyer's side of the same trade, measured: what long volatility cost a 60/40 portfolio
  over 2006–2017
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the market-wide version of selling
  variance: strategies that collect the implied–realized gap and lose together when it flips
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — how the VIX index
  is built from the same 1/K²-weighted option strip
- [[merton-1976]] — the jump-diffusion used in §3.4 to show where the replication fails
- [[avellaneda-zhang-2010]] — another product whose payoff depends on realized variance
  along the path: leveraged ETFs and volatility drag
