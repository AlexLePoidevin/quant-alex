# Manipulation in the VIX?

| | |
|---|---|
| **Authors** | John M. Griffin and Amin Shams (University of Texas at Austin) |
| **Year** | 2018 (*Review of Financial Studies* 31(4), 1377–1417); the copy is the working paper dated 23 May 2017 |
| **Type** | Empirical paper, 58pp. SPX option trades and quotes around monthly VIX settlement, January 2008 – April 2015, plus VSTOXX settlement data |
| **PDF** | Not hosted in this repository (SSRN working paper; the journal version is Oxford University Press) |
| **Find it** | [doi.org/10.1093/rfs/hhx085](https://doi.org/10.1093/rfs/hhx085) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Manipulation+in+the+VIX%3F%22+Griffin) |
| **BibTeX** | `griffin2018manipulation` |
| **Status** | Reference: §3 (volume patterns), §4 (VSTOXX comparison and hedging tests) and §5 (price deviations and dollar distortions) carry the results |

## What it is

A forensic study of the monthly settlement of VIX futures and options. The settlement value
is not the VIX at some moment of trading. It is computed from the prices of out-of-the-money
SPX options in a special opening auction (the SOQ) on settlement morning. Only out-of-the-money
options with a non-zero bid count, and the tails are cut where two consecutive zero-bid
strikes appear.

That design has the three features the manipulation literature warns about: a large, liquid
"upper-level" market (VIX futures and options) priced off a thin "lower-level" one (deep
out-of-the-money SPX options with wide spreads), cash settlement, and a short window. The
paper looks for the fingerprints a manipulator would leave:

- **Volume spikes only where they would move the VIX.** At the settlement auction, SPX option
  volume jumps, but only in the out-of-the-money options that enter the formula, not in
  in-the-money ones, and not in S&P 100 (OEX) or SPY options that have no volatility index
  tied to them.
- **Volume follows the formula's weights.** Deep out-of-the-money puts, which normally barely
  trade, see the most activity, matching their weight in the VIX. Strikes with a
  discontinuously higher weight (for example where strike spacing changes) show jumps in
  volume at settlement that are absent on other days.
- **Liquidity and hedging stories do not fit.** Out-of-the-money calls see *less* volume as
  they go further out (consistent with their lower VIX weight, not with pent-up demand).
  Open interest in deep puts jumps more than fourfold and is not unwound. There is no
  matching jump in related products, and no extra SPX trading in months without expiring VIX
  contracts.
- **The European control.** VSTOXX settlement averages the index over 11:30–12:00 CET and
  only counts options priced at €0.5 or more. At settlement, volume per minute in the €0.5
  option rises to about 130 times its usual level, and trades cluster at exact five-second
  intervals, when the index is computed.
- **Prices move, then revert.** The VIX at settlement differs from a benchmark VIX computed
  from mid-quotes just after the open (same strikes) by 31 basis points on average in absolute
  terms, about 1.5% of the settlement value. Applied to the VIX futures and in-the-money
  options exposed at settlement, that is about $1.81bn of distortion over 2008–April 2015
  ($1.95bn including the effect of which tail strikes are included).
- **It can pay.** Measured by vega, the VIX derivatives exposed at settlement are on average
  about 13 times the SPX options traded at settlement, so a trader holding a large share of the
  upper market could profit from moving the lower one.

The authors call manipulation "the most natural explanation" but say they cannot rule out
alternatives without trader-level data.

## Why it's in the library

Anyone who holds VIX futures or options to expiry is paid the settlement value, not the VIX
they watch on screen. This paper shows that number can sit tens of basis points away from
fair, systematically, because of how the settlement auction is built. It is also a clean case
study of a general point: a benchmark computed from thin markets can be pushed by trades in
those markets, even when it is set "by the market".

It complements the VIX construction notes: Osterrieder et al. show where the index formula is
biased, and this paper shows where the settlement process can be gamed.

## Links

- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — the VIX formula,
  its strike-selection rules and the separate settlement calculation, from raw quotes
- [[carr-wu-2006-a-tale-of-two-indices]] — why the VIX is a variance-swap rate built from an
  out-of-the-money option strip
- [[brenner-et-al-2007-the-market-for-volatility-trading-vix-futures]] — the early VIX futures
  market whose settlement is studied here
- [[easley-et-al-2011-microstructure-of-the-flash-crash]] — another case of thin liquidity in
  one market driving prices in a linked one
- [[filippou-et-al-2022-no-max-pain-no-max-gain]] — stock prices pulled toward the strike that
  minimises option payouts before expiry, another expiry-day distortion
