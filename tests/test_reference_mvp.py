import pytest
from reference_mvp.ait_reference_mvp import AuditRecord, EvidenceLink, Finding, State

def finding():
    f = Finding("F01", "Example claim", "Bounded to supplied evidence.")
    f.add_evidence(EvidenceLink.from_bytes("E01", b"evidence", "SUPPORT"))
    return f

def test_evidence_hash_is_deterministic():
    assert EvidenceLink.from_bytes("E01", b"abc", "SUPPORT").sha256 == EvidenceLink.from_bytes("E01", b"abc", "SUPPORT").sha256

def test_challenge_is_observable():
    f=finding(); f.challenge("Source mismatch")
    assert f.state == State.CHALLENGED and f.challenger_note == "Source mismatch"

def test_repair_requires_human_authorization():
    with pytest.raises(RuntimeError): finding().repair("unauthorized")

def test_authorized_repair_requires_regression():
    f=finding(); f.human_gate("REPAIR"); f.repair("corrected source binding")
    assert f.state == State.REGRESSION_REQUIRED

def test_failed_regression_returns_to_repair():
    f=finding(); f.human_gate("REPAIR"); f.repair("repair"); f.record_regression(False)
    assert f.state == State.REPAIR_REQUIRED

def test_passed_regression_can_reach_audit_run_lock_ready():
    f=finding(); f.human_gate("REPAIR"); f.repair("repair"); f.record_regression(True)
    assert f.state == State.READY_FOR_AUDIT_RUN_LOCK

def test_audit_run_lock_requires_human_approval():
    a=AuditRecord("A1",[finding()]); a.findings[0].human_gate("ACCEPT")
    with pytest.raises(RuntimeError): a.lock_audit_run(False)

def test_reopen_preserves_audit_run_lock_history():
    a=AuditRecord("A1",[finding()]); a.findings[0].human_gate("ACCEPT")
    a.lock_audit_run(True,"human approved audit-run closure")
    assert a.state == State.AUDIT_RUN_LOCKED and len(a.lock_history)==1
    assert "manuscript Final Lock" in a.lock_history[0]["authority_boundary"]
    a.reopen("new material evidence")
    assert a.state == State.REOPENED and len(a.lock_history)==2
