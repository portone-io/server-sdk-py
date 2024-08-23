import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class SucceededPaymentCancellation:
    """취소 완료 상태"""
    status: Literal["SUCCEEDED"]
    """결제 취소 내역 상태"""
    id: str
    """취소 내역 아이디"""
    pgCancellationId: Optional[str]
    """PG사 결제 취소 내역 아이디"""
    totalAmount: int
    """취소 총 금액"""
    taxFreeAmount: int
    """취소 금액 중 면세 금액"""
    vatAmount: int
    """취소 금액 중 부가세액"""
    easyPayDiscountAmount: Optional[int]
    """적립형 포인트의 환불 금액"""
    reason: str
    """취소 사유"""
    cancelledAt: Optional[str]
    """취소 시점"""
    requestedAt: str
    """취소 요청 시점"""
    receiptUrl: Optional[str]
    """취소 영수증 URL"""

