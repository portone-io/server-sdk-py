import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class RequestedPaymentCancellation:
    """취소 요청 상태"""
    status: Literal["REQUESTED"]
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

