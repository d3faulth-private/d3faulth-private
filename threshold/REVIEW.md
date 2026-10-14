# Reviewing a Threshold submission

**Review has not opened yet.** A private contact channel must be published before applications can be accepted. There is no automatic invitation or repository-access system.

## Review process

1. Confirm that the applicant completed one of the five tracks and provided its required supporting work.
2. Reproduce the result and evaluate the reasoning using the rubric below. The local checker validates only the fixed answer fields.
3. Ask the applicant to explain a key decision and handle a small variation of the task. This distinguishes understanding from a copied result.
4. Discuss how they would contribute and work with others. Agree on scope and expectations.
5. D3FAULTH makes the invitation decision. Access to private repositories, tools, and OS builds is granted separately as needed.

## Rubric

| Area | Points | Evidence |
| :-- | --: | :-- |
| Technical correctness | 35 | Correct findings; supporting code or patch behaves as described. |
| Reasoning and evidence | 30 | Explains why the result follows; separates facts from assumptions. |
| Reproducibility | 20 | Clear steps, useful tests, and enough context to repeat the work. |
| Collaboration and judgment | 15 | Constructive communication, honest attribution, and care with scope and personal information. |

A useful review benchmark is **75/100**, with no area scoring zero and all required deliverables present. This is a review guide, not an automatic acceptance promise. Give specific feedback where a submission falls short. A matching answer alone is insufficient.

## Suggested follow-up variations

- **Web:** change a document's organization and verify that both permitted and denied requests still behave correctly after the patch.
- **Reversing:** change the transform constants and ask how the inverse must change.
- **Forensics:** remove one audit event and ask which conclusions are still supported.
- **Linux:** change ownership of the parent directory and ask how the trust boundary changes.
- **Tooling:** add an offset timestamp, a conflicting duplicate, and an event at the window boundary; ask the applicant to predict and then verify the output.

Do not request real credentials, access to an applicant's device, attacks on third-party services, or identifying personal documents. Use the supplied exercises and consent-based collaboration to assess technical ability.
