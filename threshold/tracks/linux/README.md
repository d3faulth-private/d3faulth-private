# Inherited Trust / Linux

**Assessment 01 · Static permissions review**

Review the four text files in `evidence/`. They describe a fictional Linux system. Do not install the unit, change your machine's permissions, or execute the shell snippet. All conclusions can be drawn from the supplied snapshot.

Rook is an ordinary member of `contributors`. The service's configuration file is root-owned and is not directly writable by that group. Determine whether this is sufficient to preserve the service's trust boundary.

## Deliverables

- Complete `answer.json` with the service user, the writable directory that matters, the full configuration path under an unprivileged account's control, and the unprivileged group.
- Explain the distinction between modifying a file's contents and replacing its directory entry.
- Explain the effect of `source` in the service's execution context.
- Propose ownership/mode changes and a safer configuration-reading design. Explain how you would check the fix using an isolated test fixture without changing the host system.

From the repository root:

```sh
python3 threshold/verify.py linux /path/to/answer.json
```

[All tracks](../../README.md)
