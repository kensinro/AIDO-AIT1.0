"""
AIDO-AIT 1.0 — minimal public reference implementation.

Purpose
-------
This file demonstrates only the manuscript-level governance lifecycle:
evidence-linked findings, process-separated challenge, explicit Human Gate,
authorized repair, regression, Final Lock and REOPEN.

It intentionally omits the private development rule libraries, domain adapters,
advanced orchestration, experience ledgers and later AIT 2.0 functionality.

This reference implementation is not the exact historical v5.8.1 evaluated
release. The exact historical package identity is recorded separately and may
be supplied through controlled reviewer verification.
"""

from __future__ import annotations
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import List, Optional
import hashlib
import json


class State(str, Enum):
    OPEN = "OPEN"
    CHALLENGED = "CHALLENGED"
    REPAIR_REQUIRED = "REPAIR_REQUIRED"
    REGRESSION_REQUIRED = "REGRESSION_REQUIRED"
    READY_FOR_LOCK = "READY_FOR_LOCK"
    FINAL_LOCKED = "FINAL_LOCKED"
    REOPENED = "REOPENED"


@dataclass
class EvidenceLink:
    evidence_id: str
    sha256: str
    role: str

    @classmethod
    def from_bytes(cls, evidence_id: str, payload: bytes, role: str) -> "EvidenceLink":
        return cls(
            evidence_id=evidence_id,
            sha256=hashlib.sha256(payload).hexdigest(),
            role=role,
        )


@dataclass
class Finding:
    finding_id: str
    statement: str
    claim_boundary: str
    evidence: List[EvidenceLink] = field(default_factory=list)
    challenger_note: Optional[str] = None
    human_decision: Optional[str] = None
    repair_note: Optional[str] = None
    regression_passed: bool = False
    state: State = State.OPEN

    def add_evidence(self, evidence: EvidenceLink) -> None:
        self.evidence.append(evidence)

    def challenge(self, note: str) -> None:
        self.challenger_note = note
        self.state = State.CHALLENGED

    def human_gate(self, decision: str) -> None:
        allowed = {"ACCEPT", "REJECT", "REPAIR", "DEFER"}
        if decision not in allowed:
            raise ValueError(f"Unsupported Human Gate decision: {decision}")
        self.human_decision = decision
        if decision == "REPAIR":
            self.state = State.REPAIR_REQUIRED
        elif decision == "ACCEPT":
            self.state = State.READY_FOR_LOCK
        else:
            self.state = State.OPEN

    def repair(self, note: str) -> None:
        if self.human_decision != "REPAIR":
            raise RuntimeError("Repair requires explicit Human Gate authorization.")
        self.repair_note = note
        self.regression_passed = False
        self.state = State.REGRESSION_REQUIRED

    def record_regression(self, passed: bool) -> None:
        if self.state != State.REGRESSION_REQUIRED:
            raise RuntimeError("Regression may only follow an authorized repair.")
        self.regression_passed = bool(passed)
        self.state = State.READY_FOR_LOCK if passed else State.REPAIR_REQUIRED


@dataclass
class AuditRecord:
    audit_id: str
    findings: List[Finding] = field(default_factory=list)
    lock_history: List[dict] = field(default_factory=list)
    state: State = State.OPEN

    def add_finding(self, finding: Finding) -> None:
        self.findings.append(finding)

    def final_lock(self, human_approval: bool, note: str = "") -> None:
        if not human_approval:
            raise RuntimeError("Human approval is required for Final Lock.")
        if any(f.state != State.READY_FOR_LOCK for f in self.findings):
            raise RuntimeError("All findings must be ready before Final Lock.")
        snapshot = {
            "audit_id": self.audit_id,
            "state_before_lock": self.state.value,
            "note": note,
            "findings": [asdict(f) for f in self.findings],
        }
        self.lock_history.append(snapshot)
        self.state = State.FINAL_LOCKED

    def reopen(self, reason: str) -> None:
        if self.state != State.FINAL_LOCKED:
            raise RuntimeError("Only a Final-Locked audit can be reopened.")
        self.lock_history.append({
            "audit_id": self.audit_id,
            "event": "REOPEN",
            "reason": reason,
        })
        self.state = State.REOPENED

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, default=str)
