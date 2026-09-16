# Lab 08 — BI and AI Serving

## What Ran
Built final Gold, BI, and AI serving outputs and validated schemas, keys, fact grain, reconciliation, feature availability, and future-label handling.

## Results
- BI fact grain: 75 trips.
- Dammam: 25 trips, SAR 670.40.
- Jeddah: 25 trips, SAR 625.20.
- Riyadh: 25 trips, SAR 585.00.
- Foreign keys and Gold/fact totals reconciled.
- Events were aggregated before joining.
- AI feature availability checks passed.
- Future label remained `UNOBSERVED` with `target_trip_count = None`.
- All serving checks passed.

## Evidence
- `Masar_All_Labs.ipynb`


## Interpretation
BI and AI outputs are produced from the same trusted lineage. BI totals reconcile correctly, while AI features respect point-in-time availability and do not fabricate unknown future labels.
