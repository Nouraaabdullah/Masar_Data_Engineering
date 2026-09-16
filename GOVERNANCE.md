# Governance

## Data Classification

All data used in this project is synthetic and fictional.

No real rider, driver, location, credential or personal data is included.

## Lineage

The project follows this lineage:

Source files  
→ Bronze Delta  
→ Typed Staging  
→ Silver trusted trips  
→ Quality-approved data  
→ Gold  
→ BI and AI outputs

Kafka GPS events are ingested through Spark Structured Streaming and Delta before being used by downstream serving logic.

## Ownership

This repository is maintained as a student data engineering project.

The pipeline code, executed notebooks and generated evidence are maintained in this repository.

No production organizational ownership model or IAM system was implemented.

## Intended Access

- **Bronze:** intended for data-engineering and audit/debugging use because it preserves raw delivery history.
- **Silver:** trusted internal business data for downstream transformations.
- **Gold / BI:** curated analytical outputs.
- **AI features:** feature-ready data with point-in-time checks.
- **Quarantine:** intended for investigation of rejected records.

These are intended access boundaries for the project; production permissions were not implemented.

## Data Quality

Invalid candidates are not silently promoted.

Lab 06 demonstrated:

- Great Expectations validation.
- Promotion blocking.
- Delta quarantine.
- Explicit rejection reason codes.
- 75 approved rows.
- 7 quarantined invalid test records.

## Retention and Recovery

Bronze is append-only so source delivery history is retained.

Delta history supports previous-version reads and restore.

The maintenance lab tested a **168-hour VACUUM dry run** and deleted **0 files**.

No production legal-retention period is claimed by this project.

## Repository Safety

Heavy generated tables, `outputs/`, handoff ZIPs, virtual environments, JARs and caches are excluded from normal Git commits.

Small redacted reports and executed notebook outputs are retained as review evidence.
