# Model Risk and the Great Financial Crisis: The Rise of Modern Model Risk Management

| | |
|---|---|
| **Authors** | Jeffrey A. Brown, Brad McGourty, Til Schuermann (Oliver Wyman) |
| **Year** | 2015 (draft of 7 January 2015) |
| **Type** | Practitioner essay, 12pp (SSRN 2557213). Published in *The New International Financial System* (World Scientific, 2015), from the Chicago Fed's 17th International Banking Conference |
| **PDF** | Local copy only (SSRN working paper, no open licence) |
| **BibTeX** | `brown2015modelrisk` |
| **Status** | Reference: §2 (the history and the crisis examples) and §3 (what model risk management now requires) |

## What it is

A short history of how US banks and their regulators came to treat model risk as a risk
in its own right, written by three consultants who build and validate bank models.

- **Three phases.** Before 2000: models spread through trading, valuation and credit,
  and the 1996 Basel market-risk amendment let banks use their own models for capital
  (without mentioning "model risk"). 2000 to the crisis: the OCC's 2000 guidance made
  independent model validation the norm, while securitisation and copula-based credit
  models grew fast. From 2011: Fed/OCC guidance on model risk management as a whole
  framework, alongside supervisory stress tests.
- **LTCM, 1998.** Its value-at-risk assumed constant volatility, normal returns, a short
  calibration window and a 10-day horizon. One trade (long corporates, short Treasuries)
  assumed a 96% correlation and an 8.1% monthly volatility; at 85% correlation the
  volatility would have been 19.2%, and the correlation had been 75% six years earlier.
- **The crisis.** The Gaussian copula was the default model for CDOs and similar products
  even though its limits were known: it needed different correlation parameters to price
  different tranches of the same deal, and in the May 2005 GM downgrade it gave hedges
  with the wrong sign (Duffie, 2007). One subprime tranche was only 70 bp wide at
  issuance. Banks' economic-capital models, calibrated to a 0.05% one-year default
  probability, also failed: of 16 institutions that published economic capital, 25% lost
  at least 1.5 times their pre-crisis estimate in the worst year.
- **After the crisis.** Stress testing (SCAP in 2009, CCAR from 2011) multiplied the
  number of models: a CCAR bank may build 50–150 models just for its submission, each
  needing validation. Regulators now run their own models of every large bank, which
  makes those models a potential source of systemic risk.

## Why it's in the library

**It is a compact account of how model error turned into a crisis.** The LTCM correlation
numbers and the copula tranche inconsistency are concrete examples of models that
worked in calm data and failed when the parameters they assumed fixed moved.

**The useful message is about process, not maths.** The models' flaws were known before
the crisis; what was missing was governance that forced anyone to act on them. The
authors' lifecycle view (development, validation, monitoring, retirement) applies to any
quantitative strategy, not just bank capital models.

**It is an essay, not a study.** The evidence is a handful of well-known cases and one
consultancy chart; the authors sell model-risk services. Read it as a history and a
checklist.

## Links

- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — the Gaussian copula story
  in detail, the central example here
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — why the copula's tail assumptions
  failed in 2007–08
- [[lipton-lopez-de-prado-2020-three-quant-lessons-from-covid-19]] — a later crisis read
  as a lesson about models built on calm-period data
