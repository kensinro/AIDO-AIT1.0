# AIDO-AIT 1.0 — Minimal Public MVP

This repository provides the **minimal public reference implementation of AIDO-AIT 1.0**, a human-governed framework for traceable scientific audit, process-separated challenge, controlled repair, regression, and versioned **audit-run closure**.

The repository is intended to support scientific inspection and reproducibility of the accompanying manuscript. It does **not** represent the complete AIDO-AIT development or product codebase.

## Authority boundary

AIT audits scientific claims and evidence. The public lifecycle demonstrated here ends in an **audit-run lock**: a versioned record of the audited evidence state, findings, human adjudication, and closure metadata.

**The audit-run lock is not manuscript Final Lock.** Manuscript Final Lock, publication acceptance, and other downstream scientific or editorial decisions remain outside AIT authority.

## Scientific-state formalism boundary

The manuscript may express scientific-state assignment, admissible state sets, and wording ceilings at a governance/formal decision level. The public reference MVP demonstrates only the bounded audit-run workflow needed for inspection of the reported lifecycle. It is **not** a generalized production scientific-state engine, and it does not claim uniform machine serialization of every governance-level scientific-state representation across the historical calibration programme.

## Public purpose

This package demonstrates the manuscript-level audit-governance mechanics:

- evidence-linked audit findings;
- process-separated Challenger review;
- explicit Human Gate authority;
- authorized repair;
- post-repair regression;
- versioned audit-run lock;
- REOPEN while preserving prior audit history.

## Repository structure

- `reference_mvp/` — minimal public reference implementation;
- `tests/` — regression tests for the public reference lifecycle;
- `examples/` — synthetic example audit record;
- `manuscript_support/` — public-safe calibration and provenance summaries;
- `REPRODUCE.md` — minimal reproduction instructions;
- `PUBLIC_DISCLOSURE_BOUNDARY.md` — disclosure boundary for the public tier;
- `RIGHTS_AND_ACCESS_NOTICE.md` — current rights and access notice;
- `SHA256_MANIFEST.csv` — file-level integrity manifest.

## Reproduce the Minimal Public MVP

Install the minimal dependency and run the public tests:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

Expected result:

```text
8 passed
```

These tests verify the **Minimal Public MVP audit-run lifecycle only**. They do not replace the historical 49-test evaluated-release evidence described in the manuscript.

## Historical evaluated implementation

The manuscript preserves a historical evaluated AIDO-AIT 1.0 MVP release, **v5.8.1**, as provenance for earlier release-governance and recursive-audit evidence.

Its version-locked SHA-256 is:

```text
3054301dea44a33b7b028f58effebf4daa6b853c40f25bf60ca7f40990bd8795
```

The preserved release-level regression result is:

```text
49 passed
```

The exact historical source archive is **not included in this public tier**. It is retained separately for controlled editor/reviewer verification.

This historical release identifier is preserved as evidence lineage. It does not define the current manuscript authority model, and it should not be interpreted as the uniform runtime for all calibration cases.

## Calibration scope

The manuscript evaluates AIDO-AIT across heterogeneous calibration cases spanning internal end-to-end audits, published software-method audits, and non-software scientific objects.

Only public-safe summaries and provenance records needed for manuscript inspection are included here. Private audit archives and copyrighted third-party source materials are not redistributed.

## Rights, access and development boundary

This repository contains the **Minimal Public MVP** accompanying the AIDO-AIT 1.0 manuscript.

It is provided for scientific inspection, reproducibility, methodological evaluation, and peer review. This repository is intentionally limited to the minimum reference implementation required to demonstrate the published AIDO-AIT 1.0 audit lifecycle.

### Public scope

The public repository includes only the components necessary to demonstrate:

- evidence-linked audit findings;
- process-separated Challenger review;
- explicit Human Gate authority;
- authorized repair;
- post-repair regression;
- versioned audit-run lock;
- REOPEN while preserving prior audit history;
- public-safe calibration summaries and provenance records.

### Not included

This repository is **not** the complete AIDO-AIT development or product codebase.

The following remain outside the public repository:

- later AIDO-AIT development branches;
- advanced audit rules and rule libraries;
- internal orchestration logic;
- experience and development ledgers;
- unpublished audit cases;
- private calibration archives;
- future research-lifecycle, impact-assessment, journal-strategy, domain-reasoning, and learning-based extensions;
- commercial or product-integration components.

The exact historical implementation used for deeper manuscript verification is maintained separately under controlled access and is not part of this public Minimal MVP.

### Rights and licensing

Copyright © 2026 Sin Guan Kong. All rights reserved.

No open-source software license is granted at the current submission stage.

Except for rights necessarily provided through GitHub's Terms of Service and rights available under applicable law, no additional permission is granted to copy, redistribute, sublicense, commercialize, or create derivative software from this repository without permission from the copyright holder.

See [`RIGHTS_AND_ACCESS_NOTICE.md`](RIGHTS_AND_ACCESS_NOTICE.md) for the current repository access boundary.

### Contact

Research collaboration, institutional evaluation, licensing, and technology-transfer enquiries are welcome.

## Citation

Please cite the associated AIDO-AIT 1.0 manuscript when using or discussing this reference implementation. Machine-readable citation metadata are provided in `CITATION.cff`.
