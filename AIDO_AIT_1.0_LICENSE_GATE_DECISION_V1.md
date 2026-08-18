# AIDO-AIT 1.0 — License Gate Decision V1

**Date:** 2026-08-18  
**State:** PRE-SUBMISSION / HUMAN FINAL LOCK = FALSE  
**Purpose:** protect commercial/IP optionality without delaying manuscript submission.

## Decision for the immediate submission window

**Do not add a permissive open-source license tonight.**

For the Minimal Public MVP, retain copyright and grant no additional open-source
license at this stage. Keep the repository public for scientific inspection and
reproducibility, while disclosing the licensing restriction in the repository
and manuscript.

This is an interim submission-stage decision, not a permanent refusal to license.

## Why

1. The public repository is intentionally only a **Minimal Public MVP**.
2. Nature Computational Science requires central custom code to be available to
   editors/reviewers and requires access restrictions to be disclosed, but it
   does not require an OSI-approved license at initial submission. It encourages
   an OSI-approved license for publication-stage code release.
3. GitHub states that without a software license, default copyright law applies
   and the author retains rights, while GitHub's Terms of Service still allow
   public viewing and forking through GitHub functionality.
4. A permissive license such as MIT/Apache-2.0 would grant substantially broader
   reuse rights than needed for manuscript verification.
5. A non-commercial source-available license would protect commercial use more
   aggressively but is not OSI-approved and could create unnecessary journal
   friction.
6. AGPL-3.0 remains a strong publication-stage candidate if the author later
   chooses open source: it is OSI-approved and requires source availability for
   modified versions offered over a network. It does not prohibit commercial use.

## Three-tier licensing boundary

### Tier 1 — Minimal Public MVP
Current state: **copyright retained; no open-source license granted yet**.

Public purpose:
- inspectability;
- reproducibility of the minimal reference implementation;
- manuscript support.

### Tier 2 — Controlled Reviewer Package
Current state: **controlled access only**.

The exact historical evaluated v5.8.1 package and deeper audit records are
provided for confidential editor/reviewer verification as required.

### Tier 3 — Private Development / Commercial Core
Current state: **private / proprietary**.

Includes later development branches, advanced rules/orchestration, experience
ledgers, unpublished cases, AIT 2.0 functionality and future product know-how.

## Publication-stage options

When/if the manuscript proceeds beyond initial editorial assessment:

- **AGPL-3.0** — preferred open-source candidate if strong copyleft/network
  reciprocity is desired.
- **MPL-2.0** — weaker file-level copyleft if broader adoption is prioritized.
- **PolyForm Noncommercial 1.0.0** — source-available/noncommercial option, but
  not OSI-approved and therefore less aligned with Nature's stated preference.
- **No additional license** — strongest copyright retention, but may reduce
  downstream scientific reuse and may attract editorial questions.

## Patent caveat

The Minimal Public MVP repository is already publicly visible. A later license
choice does not undo that public disclosure. Public disclosure before a patent
filing can affect novelty in many jurisdictions, although some jurisdictions
provide limited grace periods.

No additional undisclosed technical or commercial core should be published
without a separate IP decision.

## Human Gate

This document recommends the **interim no-open-source-license state** for
submission. A permanent license choice remains a Human Gate decision.
