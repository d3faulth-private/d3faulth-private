# The Threshold

**D3FAULTH / The Collective / Entry assessment 01**

Practical skill. Clear reasoning. Collective purpose.

Choose **one** track below. Work through the supplied material, check your result locally, and prepare a writeup that another researcher can reproduce. The full assessment includes your reasoning and supporting work.

**Exercises: open. Private applications: pending.** Contact details will be added to the [profile](../README.md#contact). Keep your submission locally until then; do not post answers or personal details in public Issues or pull requests.

## Choose your track

| Track | Assignment | What you demonstrate |
| :-- | :-- | :-- |
| [Web security — Broken Boundary](tracks/web/README.md) | Inspect an offline document portal, reproduce an authorization flaw, and propose a fix. | Access control, code review, regression testing |
| [Reverse engineering — Signal](tracks/reversing/README.md) | Reverse a byte transformation and recover its accepted input. | Program analysis, bitwise operations, reproducibility |
| [Forensics — Altered Record](tracks/forensics/README.md) | Compare two records and reconstruct a confirmed change from noisy audit evidence. | Timeline analysis, evidence handling, uncertainty |
| [Linux — Inherited Trust](tracks/linux/README.md) | Trace a service's trust boundary through file and directory permissions. | Linux permissions, service hardening, precise remediation |
| [Tool development — Quiet Signal](tracks/tooling/README.md) | Build a log analyzer that handles invalid records, duplicates, and time windows. | Reliable parsing, automation, meaningful tests |

All organizations, accounts, records, and events in these exercises are fictional. The scope is the files in `threshold/`; no external system, live service, account, or network scanning is part of an assignment. The scripts use Python's standard library, make no network connections, and do not require administrator privileges.

## Get started

Clone or download this repository, then open a terminal in its root:

```sh
git clone https://github.com/d3faulth-private/d3faulth-private.git
cd d3faulth-private
python3 threshold/verify.py --list
```

Use **Python 3.10 or newer**. On Windows, `py -3` can be used instead of `python3`. You can read every assignment without running code; the web/reversing demos and the result checker are optional local helpers.

1. Read one assignment and its supplied evidence.
2. Copy that track's `answer.example.json` to your own `answer.json` and replace the example values.
3. Run its local check, for example:

```sh
python3 threshold/verify.py web /path/to/answer.json
```

The checker reads only the answer file, prints a result, and exits. Use the exact field names, identifiers, JSON types, and array order described in the assignment; object-key order is ignored. Include no extra fields.

A matching result means the deterministic findings match; it does **not** verify expertise, authorship, or membership. These are public exercises with public checkers. Review includes your writeup and a follow-up variation.

## Prepare your submission

Use [APPLICATION.md](APPLICATION.md) as a template. Include your handle, chosen track, `answer.json`, reproducible steps, and the supporting code or patch required by that assignment. Explain uncertainty and disclose external references, collaborators, tools, and AI assistance.

**Complete the task → explain the reasoning → private review → invitation.**

Read [REVIEW.md](REVIEW.md) for the review criteria. Invitation and access to private tools or Anonymous OS are separate decisions. No payment, real name, password, access token, or identity document is needed for this assessment.

## Hack The Box

Your HTB profile and an eligible retired-machine writeup can support an application. The Threshold uses original fixtures and does not include HTB tasks or answers. Please follow [HTB's publishing guidelines](https://help.hackthebox.com/en/articles/5188925-streaming-writeups-walkthrough-guidelines) for any supporting material.

[Back to D3FAULTH](../README.md)
