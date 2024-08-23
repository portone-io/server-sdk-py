import dataclasses

@dataclasses.dataclass
class CancelCashReceiptResponse:
    """현금 영수증 취소 성공 응답"""
    cancelledAmount: int
    """취소 금액"""
    cancelledAt: str
    """현금 영수증 취소 완료 시점"""

