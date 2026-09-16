# Engineering Decisions

## 1. Preserve Bronze as Append-Only

**Decision:** Keep repeated source deliveries in Bronze.

**Why:** Bronze represents what arrived, not the final business truth. The trip replay increased Bronze from 72 to 144 rows while still representing 72 business trips.

**Consequence:** Deduplication is performed in Silver instead of deleting Bronze history.

---

## 2. Use Silver as the Trusted Business Layer

**Decision:** Produce one canonical trusted trip per business key.

**Why:** Replays must not create duplicate trusted trips, while genuine late-arriving records must be retained.

**Evidence:** Base and rerun remained at 72 rows; after late data the trusted result became 75 rows and remained 75 after replay.

---

## 3. Use Delta Lake for Trusted Tables

**Decision:** Use Delta instead of manually overwriting data files.

**Why:** The project requires ACID commits, schema controls, MERGE, version history, time travel and restore.

**Evidence:** Corrections created a new Delta version while preserving 75 business rows, and previous versions remained readable.

---

## 4. Use Persistent Streaming Checkpoints

**Decision:** Give the Kafka Structured Streaming query persistent checkpoint state.

**Why:** Restarting the stream should resume processing without silently duplicating the logical event set.

**Evidence:** Restart and checkpoint checks passed, and unique event IDs remained controlled across replay phases.

---

## 5. Block or Quarantine Invalid Data

**Decision:** Do not silently accept invalid candidate records.

**Why:** Trusted outputs should only contain validated data.

**Evidence:** The contaminated candidate failed validation, seven records were quarantined with reason codes, and 75 approved rows remained.

---

## 6. Serve BI and AI from the Same Trusted Lineage

**Decision:** Build BI and AI products from the same trusted Silver/Gold lineage.

**Why:** Separate pipelines can create conflicting definitions of the same business truth.

**Evidence:** BI totals reconciled with trusted data, while AI feature availability and non-fabricated future-label checks passed.

---

## Limitations

The project uses a small synthetic dataset and a local environment.

Local timings, Kafka behaviour and recovery exercises should not be interpreted as production-scale performance, high availability or legal-compliance evidence.
