import dataclasses

@dataclasses.dataclass
class InstantPaymentSummary:
    """수기 결제가 완료된 결제 건 요약 정보"""
    pgTxId: str
    """PG사 결제 아이디"""
    paidAt: str
    """결제 완료 시점"""

