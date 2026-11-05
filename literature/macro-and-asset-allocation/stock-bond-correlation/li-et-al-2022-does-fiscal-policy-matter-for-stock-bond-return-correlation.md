# Does Fiscal Policy Matter for Stock-Bond Return Correlation?

| | |
|---|---|
| **Authors** | Erica X.N. Li (CKGSB), Tao Zha (Federal Reserve Bank of Atlanta, Emory, NBER), Ji Zhang (Tsinghua PBCSF), Hao Zhou (SUSTech, Tsinghua PBCSF) |
| **Year** | 2022 (this copy dated 3 March 2022; published in *Journal of Monetary Economics* 128, 2022, pp. 20–34) |
| **Type** | SSRN working paper (3106141), 62pp. General-equilibrium (New Keynesian) model, US data 1971–2018 |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `li2022fiscal` |
| **Status** | Reference: §2 (stylised facts by policy regime), §4.2–4.5 (variance decomposition and correlations) and §5 (robustness) carry the results |

## What it is

A macro model that explains why US stocks and Treasuries moved together before about 2001
and opposite each other afterwards, by a change in which arm of policy was in charge.

- **The facts it targets.** Split US data at 2001Q2. In 1971Q1–2001Q1 the daily
  correlation between stock returns and 5-year Treasury returns was 0.21; in
  2001Q2–2018Q4 it was −0.31. Over the same split the correlation between consumption
  growth and inflation went from −0.44 to 0.27. The 5-year bond still earned a positive
  excess return in both periods (1.87% and 2.03% a year), even though after 2001 it was a
  hedge for stocks.
- **The two policy regimes.** In the "M regime" monetary policy is active (rates rise more
  than one-for-one with inflation; the paper uses a coefficient of 2.74) and fiscal policy
  is passive (taxes adjust to stabilise debt). In the "F regime" fiscal policy is active
  (taxes do not respond to debt) and monetary policy is passive (coefficient 0.50), so the
  price level adjusts to keep the government's budget balanced. The estimates follow
  Bianchi and Ilut (2017), which dates a switch from M to F in the early 2000s.
- **The mechanism.** The model has four shocks: technology, investment efficiency,
  monetary and fiscal policy. In the M regime the technology shock dominates: it raises
  consumption and lowers inflation; rates fall; stocks and bonds both rally, so their
  correlation is positive. In the F regime the technology shock is muted and the investment
  shock dominates: it raises output and tax receipts, so the price level falls, rates fall
  and bonds rally, while short-run consumption and stock prices fall, so the correlation
  turns negative.
- **Why bonds still pay a premium.** Risk premiums depend on what drives the pricing
  kernel, and the technology shock drives almost all of it in both regimes. So bonds keep a
  positive premium even when they hedge stocks. The model's correlations are 0.51 (M) and
  −0.57 (F) for stocks and bonds, and −0.65 and 0.14 for consumption and inflation.
- **Robustness.** The signs survive eight shocks instead of four, the zero lower bound
  treated as an extreme F regime, other preferences, a lower risk aversion with a
  preference shock, and a range of shock sizes. Only the two parameters that define the
  regimes (the inflation response and the tax response to debt) are essential.

## Why it's in the library

**It gives a structural reason for the stock–bond correlation flip.** Most explanations
point to monetary policy or to inflation becoming procyclical. This one says the regime
that sets the price level changed, and with it which shocks drive both markets. If the
correlation depends on the policy regime, a regime change can flip it back, which is the
risk in any portfolio that relies on bonds to hedge equities.

**It is a calibrated model, not a test.** The parameters are set to match moments, the
regime dates are taken from another paper, and the model explains only about half the bond
premium and a third of the equity premium. Risk aversion is set to 55 in the baseline (10
with an added preference shock). The authors say themselves that they do not compare their
explanation against the alternatives. Read it as one coherent story for the facts, next to
the competing ones.

## Links

- [[zeng-zhao-2022-expectation-driven-term-structure-of-equity-and-bond-yields]] — a different explanation of the same flip, through subjective growth expectations rather than policy regimes
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — risk parity and balanced portfolios as a bet that bonds keep hedging stocks
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — what happens when a correlation a portfolio relies on changes
- [[chen-roll-ross-1986]] — inflation and growth as macro risks priced in stock returns
- [[ang-chen-2002]] — correlations that change with market conditions
- [[baele-van-holle-2017-stock-bond-correlations-macroeconomic-regimes-and-monetary-policy]] — the monetary-policy-regime account of the same sign flip
- [[barthelemy-mengus-plantin-2021-the-central-bank-the-treasury-or-the-market]] — theory of when fiscal policy rather than the central bank sets inflation
- [[cieslak-vissing-jorgensen-2021-the-economics-of-the-fed-put]] — the Fed's asymmetric response to stock falls, one mechanism behind the post-2000 bond hedge
- [[shen-weisberger-2021-us-stock-bond-correlation-macroeconomic-drivers]] — a practitioner's version of the fiscal-versus-monetary explanation, with portfolio arithmetic
