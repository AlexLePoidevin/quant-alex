# A Macroprudential View on Portfolio Rebalancing and Compression

| | |
|---|---|
| **Authors** | Luitgard Anna Maria Veraart, Yuliang Zhang (London School of Economics, Department of Mathematics) |
| **Year** | 2021 (version of 4 June 2021) |
| **Type** | Working paper. SSRN 3860262, 68pp (29pp of text plus proofs and worked examples). Theory: network models of variation-margin payments, no empirical data |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `veraart2021rebalancing` |
| **Status** | Reference: §1 (setting and literature), §4 (main results, Theorems 4.1 and 4.11), §5 (policy implications) and §6 (conclusion); proofs skimmed |

## What it is

A mathematical study of whether two "post-trade risk reduction" services in OTC derivatives
markets make the banking system safer. Despite the title, *rebalancing* here is not an
investor resetting portfolio weights. It means dealers adding new, market-risk-neutral trades
among themselves to cut counterparty exposures. *Compression* means tearing up offsetting
contracts to cut gross notional.

- **Setting.** Banks are linked by derivative contracts. When prices move they owe each
  other variation margin, and a bank short of liquidity may pay only part of what it owes,
  passing the shortfall on. Systemic risk is measured in a clearing model in the
  Eisenberg–Noe tradition, extended by Rogers–Veraart.
- **Formal definitions.** The paper gives what it says is the first formal definition of
  portfolio rebalancing and of optimal rebalancing, and shows how they relate to
  compression.
- **When rebalancing helps.** Rebalancing reduces systemic risk if none of the banks taking
  part defaults, either in the original network or in the rebalanced one (Theorem 4.1).
- **When it can hurt.** Rebalancing rewires the network, so losses travel along new paths.
  The worked examples show cases where cutting each bank's own counterparty exposure creates
  new defaults elsewhere. Lower gross notional is not the same thing as lower contagion.
- **Worst case.** If stressed banks hold back payments strategically, the system can settle
  at its worst equilibrium (zero recovery). In that case compression still always reduces
  systemic risk (Theorem 4.11), but rebalancing can make things worse even in a network that
  had no defaults beforehand.
- **Policy.** These services lower the variation margin that changes hands when markets
  move, which dampens the procyclicality of margin calls. The authors relate this to March
  2020, when gross variation margin flows rose from three or four times normal to ten or
  twelve times. They suggest letting mainly low-default-risk firms take part, and turning
  some of the collateral saved into liquidity buffers.

## Why it's in the library

**It is about how stress spreads through the plumbing in a selloff.** In a crash, margin
calls drain liquidity just when funding is scarce. The paper shows that tools which make each
participant safer can still make the system less safe, because contagion depends on the
shape of the network, not on the total size of exposures.

**Not about portfolio rebalancing in the investor's sense.** For calendar or threshold
rebalancing of an asset mix, see the Man Group rebalancing papers linked below.

**Limits.** Pure theory: stylised networks, illustrative examples and no data on actual
rebalancing or compression cycles.

## Links

- [[geithner-metrick-2018-ten-years-after-the-financial-crisis]] — runs and liquidity as the core problem in a financial crisis
- [[granger-et-al-2014-rebalancing-risk]] — rebalancing in the investor's sense, as a short-volatility position
- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — how a dependence model turned risk-reduction tools into a systemic risk
