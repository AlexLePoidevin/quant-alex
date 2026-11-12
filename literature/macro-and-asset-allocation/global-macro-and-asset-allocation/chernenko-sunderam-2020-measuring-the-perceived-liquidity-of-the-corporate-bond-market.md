# Measuring the Perceived Liquidity of the Corporate Bond Market

| | |
|---|---|
| **Authors** | Sergey Chernenko (Purdue), Adi Sunderam (Harvard Business School) |
| **Year** | 2020 (May 2020) |
| **Type** | NBER Working Paper 27092, 45pp. Morningstar mutual-fund holdings, July 2009 – June 2016 for the main sample (July 2002 – June 2016 using monthly flows) |
| **PDF** | Not hosted in this repository (NBER working paper, all rights reserved) |
| **Find it** | [doi.org/10.3386/w27092](https://doi.org/10.3386/w27092) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Measuring+the+Perceived+Liquidity+of+the+Corporate+Bond+Market%22+Chernenko) |
| **BibTeX** | `chernenko2020liquidity` |
| **Status** | Reference: §2 (model and simulations), §4.3 (cross-section), §4.5 (across asset classes) and §4.7 (before, during and after the crisis) carry the results |

## What it is

A way to measure how liquid investors *think* a market is, without using any trade data.
The idea is revealed preference: open-end mutual funds hold cash so that they don't have
to sell bonds when investors redeem, and they need more of that cash buffer when their
bonds are harder to sell.

- **The model.** A fund facing normally distributed outflows chooses a cash reserve that
  trades the carrying cost of cash against the cost of selling illiquid bonds. The optimal
  cash ratio rises with flow volatility and with illiquidity, and, crucially, the *slope*
  of cash on flow volatility is steeper when the fund's assets are more illiquid. That
  slope is the measure.
- **Identification.** Regressions are run at the bond–fund–month level with bond-by-date
  fixed effects, so they compare the cash holdings of two funds holding the *same* bond
  at the same time but facing different flow volatility. Simulations, including a dynamic
  cash-management model (Connor and Leland, 1995), show the slope recovers the true
  ordering of illiquidity across bond categories.
- **The basic result.** A one-standard-deviation rise in flow volatility goes with a
  46 bp higher cash-to-assets ratio (median 320 bp). It survives controls for past and
  future flows and returns.
- **The cross-section.** Perceived illiquidity jumps at the investment-grade boundary
  (0.199 for BBB to 0.314 for BB). Unrated bonds look like junk. Rule 144A and secured
  bonds are perceived as less liquid. Among investment-grade bonds, higher-yielding bonds
  are perceived as less liquid even after controlling for rating, consistent with the
  illiquidity being priced (one standard deviation of offering yield adds about 35% to
  the slope).
- **Across asset classes.** Domestic equities are perceived as the most liquid; foreign
  equities about 50% less liquid (in the paper's words); corporate bonds almost seven times less liquid than US
  stocks (slope 0.137); municipal bonds less liquid still (0.336). Municipal bonds that
  have not traded for three months are only a little less liquid than other munis
  (about 6.5% of the slope), so trading volume is a poor proxy for liquidity there.
- **Over time.** For corporate bond funds the slope roughly doubled in the 2008–09
  crisis (0.066 to 0.124) and stayed high afterwards. Investment-grade perceived liquidity
  recovered to pre-crisis levels; speculative-grade stayed about 80% worse (0.170 vs
  0.092), and Rule 144A bonds about 140% worse. Over the same periods the trade-based
  Amihud measure shows full recovery.

## Why it's in the library

**Liquidity that only shows up when you need it is not in the trade data.** Transaction
measures only see trades that happened. If investors avoid trading the bonds they think
are hard to sell, or worry about a freeze that hasn't happened yet, those measures look
fine. This paper's answer to "has bond liquidity got worse since 2008?" is "yes for junk
and 144A bonds, according to the people who have to sell them", while trade-based
measures say no.

**It is a useful template.** Inferring a hidden quantity from how investors position for
it (here, cash buffers against redemptions) works in markets where prices and trades are
sparse: munis, loans, asset-backed securities.

**Limits to keep in mind.** The measure is market-level, not bond-level; it assumes funds
in different asset classes penalise cash drag similarly; and the time-series comparison
relies on a liquidity-premium control for the cost of holding cash. It is a 2020 working
paper.

## Links

- [[merton-1974-on-the-pricing-of-corporate-debt]] — the structural model of what a
  corporate bond's yield spread should be from default risk alone; the gap is where
  liquidity premia live
- [[collin-dufresne-daniel-2015-liquidity-and-return-reversals]] — liquidity measured
  from price reversals in equities, the transaction-based approach this paper argues
  misses perceived risk
- [[barth-mitchell-sun-2020-runs-to-banks-cash-sweeps-during-market-downturns]] — where
  investors' cash goes in a downturn, the other side of fund redemptions
- [[rosaler-et-al-2025-supervised-similarity-for-high-yield-bonds]] — another approach to
  the high-yield bond market, where trade data are thin
