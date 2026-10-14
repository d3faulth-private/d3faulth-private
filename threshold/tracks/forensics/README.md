# Altered Record / Forensics

**Assessment 01 · Fictional procurement records**

The evidence directory contains an original CSV, a published CSV, and an unsorted audit export. Establish what changed and identify the earliest **confirmed committed replacement of `ledger-Q3`** that connects those exact file contents.

Times carry different UTC offsets. A prepared, denied, or failed event is not proof of a committed change. `CRD` is a fictional currency.

## Deliverables

- Complete `answer.json`: changed record ID, signed amount difference (`published - original`, as an integer), commit event ID, commit time normalized to `YYYY-MM-DDTHH:MM:SSZ`, and the actor recorded on that event.
- Calculate the SHA-256 of both files and connect those hashes to the relevant audit events.
- Build a concise UTC timeline with citations to event IDs.
- Explain what the records establish, which distracting events you excluded and why, and what additional evidence would be needed to attribute the change to a person. A service-account label does not establish a person's identity or motive.

From the repository root:

```sh
python3 threshold/verify.py forensics /path/to/answer.json
```

[All tracks](../../README.md)
