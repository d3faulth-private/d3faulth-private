# Signal / Reverse engineering

**Assessment 01 · Offline program analysis**

`signal.py` transforms bytes and compares the output to a fixed target. Recover the exact UTF-8 input that is accepted. You may inspect every part of the source.

## Deliverables

- Complete `answer.json` with the recovered `phrase`.
- Write an inverse transformation that derives the input from the target and constants.
- Explain the order of inverse operations and why the rotation must be limited to eight bits.
- Demonstrate that your input passes and a one-character mutation fails. A patch that makes every input pass is not a solution.

Test a candidate locally from this track directory:

```sh
python3 signal.py YOUR_CANDIDATE
```

Then check your answer from the repository root:

```sh
python3 threshold/verify.py reversing /path/to/answer.json
```

[All tracks](../../README.md)
