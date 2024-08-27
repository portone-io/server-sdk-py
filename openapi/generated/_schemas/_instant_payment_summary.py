import dataclasses

@dataclasses.dataclass
class InstantPaymentSummary:
    """수기 결제가 완료된 결제 건 요약 정보"""
    pg_tx_id: str = dataclasses.field(metadata={"serde_rename": "pgTxId"})
    """PG사 결제 아이디"""
    paid_at: str = dataclasses.field(metadata={"serde_rename": "paidAt"})
    """결제 완료 시점"""

