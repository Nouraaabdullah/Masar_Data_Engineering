# Lab 06 — Data Quality and Quarantine

## What Ran
Applied Great Expectations checks to trusted and invalid candidate data, blocked failed promotion, and stored bad records in a Delta quarantine table.

## Results
- Approved rows: 75.
- Trusted data passed validation.
- Invalid mixed candidate failed validation.
- Failed candidate was not promoted.
- 7 invalid records were quarantined.
- Reasons included missing trip ID, invalid fare, unknown driver, invalid timestamp, duration, distance, and city.
- Source Silver remained unchanged.

## Evidence
- `Masar_All_Labs.ipynb`


## Interpretation
Invalid records are not silently accepted or deleted. They are quarantined with clear reason codes while trusted data remains protected.
