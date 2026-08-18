# AIDO-AIT 1.0 — Minimal Public MVP

This repository is the **minimum public reference implementation** accompanying
the AIDO-AIT 1.0 manuscript.

It is intentionally smaller than the private development system and smaller
than the controlled reviewer-verification package.

## Public purpose

This package exists to demonstrate the published governance mechanics:

- evidence-linked findings;
- process-separated challenge;
- explicit Human Gate authority;
- authorized repair;
- post-repair regression;
- versioned Final Lock;
- REOPEN without deletion of earlier lock history.

Run:

```bash
python -m pytest -q
```

The public reference tests are **demonstration/regression tests for this minimal
reference implementation**. They are not the manuscript's historical 49-test
suite and are not system-level performance estimates.

## Historical evaluated implementation

The manuscript's historical evaluated AIT release is v5.8.1, SHA-256:

`3054301dea44a33b7b028f58effebf4daa6b853c40f25bf60ca7f40990bd8795`

Its preserved release record is **49 passed**. The exact full historical package
is intentionally not included in this public tier; it is retained in the
controlled reviewer-verification package.

## What is intentionally not public

This repository does not include:

- later AIT laboratory/development branches;
- AIT 2.0 extensions;
- AIT-R, AIT-I or AIT-JF;
- private rule libraries or advanced orchestration;
- internal experience ledgers;
- unpublished audit cases;
- private AIT1/AIT2 development archives;
- copyrighted source papers or third-party attachments;
- controlled reviewer evidence packages.

This repository is a scientific reference implementation, not the complete
development or product codebase.

## Licensing status

No public software license has yet been selected. See `LICENSE_PENDING.md`.
Do not interpret public visibility as an open-source license grant.

Research collaboration, institutional evaluation, licensing and
technology-transfer enquiries are welcome.
