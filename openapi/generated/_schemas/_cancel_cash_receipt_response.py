import dataclasses

@dataclasses.dataclass
class CancelCashReceiptResponse:
    """현금 영수증 취소 성공 응답"""
    cancelled_amount: int = dataclasses.field(metadata={"serde_rename": "cancelledAmount"})
    """취소 금액"""
    cancelled_at: str = dataclasses.field(metadata={"serde_rename": "cancelledAt"})
    """현금 영수증 취소 완료 시점"""

