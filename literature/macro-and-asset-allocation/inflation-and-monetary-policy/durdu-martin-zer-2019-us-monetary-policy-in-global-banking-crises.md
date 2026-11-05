# The Role of U.S. Monetary Policy in Global Banking Crises

| | |
|---|---|
| **Authors** | C. Bora Durdu, Alex Martin, Ilknur Zer (Federal Reserve Board) |
| **Year** | 2019 |
| **Type** | Working paper: Finance and Economics Discussion Series 2019-039, Board of Governors of the Federal Reserve System, 34pp. doi:10.17016/FEDS.2019.039 |
| **PDF** | `durdu-martin-zer-2019-us-monetary-policy-in-global-banking-crises.pdf` (work of Federal Reserve Board staff, a US government work) |
| **BibTeX** | `durdu2019monetary` |
| **Status** | Reference: §4.1 (baseline logits, Table 2), §4.2 (capital flows) and §4.4 (subsamples) carry the results |

## What it is

A panel study of whether US rate rises cause banking crises abroad, using 69 countries
from 1870 to 2010 and the Reinhart–Rogoff list of 239 systemic banking crises.

- **The test.** A panel logit of "a banking crisis starts this year" on a country's
  exposure to the US interacted with the change in US policy. Policy is proxied by the
  change in the 3-month Treasury yield over the long sample. From 1990 it is replaced by
  measured surprises: Gertler–Karadi fed funds futures, Rogers et al. eurodollar futures
  and Romer–Romer narrative shocks. Country and year fixed effects are included, with
  standard errors clustered both ways.
- **Two kinds of exposure.** *Direct* exposure is trade with the US as a share of total
  trade, and later dollar-denominated net debt. *Indirect*, global integration is trade
  openness and, later, the Chinn–Ito capital-account index. Both trade measures are also
  instrumented with gravity-model predictions (distance, language, borders) to deal with
  the fact that trade and crises affect each other.
- **Result 1: direct exposure turns US tightening into crisis risk.** For countries tied
  directly to the US, a 1-point US tightening raises the probability of a banking crisis
  by about 1% to 7% (marginal effects, depending on the specification). The effect
  survives the gravity instruments, the post-1990 surprise measures, OLS and probit
  versions, alternative crisis databases, and excluding the world wars, the Depression
  and the Great Recession.
- **Result 2: global integration is ambiguous.** For countries that are open but not tied
  to the US in particular, the coefficient is negative in some specifications and
  insignificant in others. The authors read this as diversification: such countries may
  even receive the capital leaving the directly exposed ones.
- **The channel is capital flows.** US tightening cuts portfolio inflows to directly
  exposed countries. When the adjustment is disorderly (a sudden stop), crisis odds rise.
  Splitting the sample shows this is an emerging-market effect: the interaction is not
  significant for developed countries. The effect is larger for countries that peg to the
  dollar.

## Why it's in the library

It is the long-history evidence behind a common macro claim: Fed hiking cycles are
dangerous for the rest of the world mainly through the dollar and through capital that
leaves. It explains why emerging-market stress tends to cluster in US tightening cycles
(1980–82, 1994, the 2013 taper tantrum, 2018).

Limits worth knowing:
- Banking crises are rare (about one per 37 years for a typical OECD country). So the
  results rest on a few hundred events in an annual panel, with crude policy proxies before
  1990.
- The effect is on the probability of a crisis starting. It doesn't say anything about
  asset returns or timing within the year.
- It is a discussion paper, not the refereed version.

## Links

- [[christensen-madsen-2022-the-us-dollar-and-fed-tightening-cycles]] — what the dollar itself did in the last four Fed hiking cycles: no consistent rise
- [[soros-2013]] — reflexivity: credit booms and busts that feed on their own financing conditions
- [[keerati-2020-the-impact-of-monetary-policy-on-the-specialness-of-us-treasuries]] — Fed tightening raises the convenience yield of Treasuries relative to other G10 bonds and, since 2008, widens the dollar cross-currency basis
- [[menand-2021-the-federal-reserve-and-the-2020-economic-and-financial-crisis]] — what the Fed did in the 2020 crisis, including swap lines and repo for foreign central banks, and the legal basis for it
