# Broken Boundary / Web security

**Assessment 01 · Offline code-review lab**

`portal.py` models a document endpoint. It reads one JSON request from stdin and returns a JSON response; it does not start a server. The `evidence/portal.json` fixture contains fictional sessions and documents.

The intended policy is simple: an active session may read only documents belonging to the session's own organization. A caller-supplied organization must never expand that access.

## Your task

Use the active session `S-ROOK`. Find a request that returns the `ward-9` document even though Rook belongs to `ward-7`. Identify the untrusted request field responsible for the boundary failure.

Run the provided legitimate request from this track directory:

```sh
python3 portal.py < request.example.json
```

Then prepare your own reproducer. Reading the fixture is permitted; this is a code-review assessment, not a hidden-secret exercise.

## Deliverables

- Complete `answer.json` with the requesting account, cross-organization document ID, untrusted field name, and the authorization boundary (`organization`). Use the exact identifiers in the fixture.
- Include the reproducing request and explain how data flows through the authorization check.
- Provide a patch that enforces the policy using trusted session data.
- Include tests covering a legitimate request, a cross-organization request, a forged organization field, an inactive session, and an unknown document.

From the repository root, check the fixed findings:

```sh
python3 threshold/verify.py web /path/to/answer.json
```

The checker does not evaluate your patch. Its behavior and tests are part of manual review.

[All tracks](../../README.md)
