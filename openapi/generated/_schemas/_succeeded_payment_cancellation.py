import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class SucceededPaymentCancellation:
    """취소 완료 상태"""
    status: Literal["SUCCEEDED"] = dataclasses.field()
    """결제 취소 내역 상태"""
    id: str = dataclasses.field()
    """취소 내역 아이디"""
    pg_cancellation_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "pgCancellationId", "serde_skip_if": lambda value: value is None})
    """PG사 결제 취소 내역 아이디"""
    total_amount: int = dataclasses.field(metadata={"serde_rename": "totalAmount"})
    """취소 총 금액"""
    tax_free_amount: int = dataclasses.field(metadata={"serde_rename": "taxFreeAmount"})
    """취소 금액 중 면세 금액"""
    vat_amount: int = dataclasses.field(metadata={"serde_rename": "vatAmount"})
    """취소 금액 중 부가세액"""
    easy_pay_discount_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "easyPayDiscountAmount", "serde_skip_if": lambda value: value is None})
    """적립형 포인트의 환불 금액"""
    reason: str = dataclasses.field()
    """취소 사유"""
    cancelled_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "cancelledAt", "serde_skip_if": lambda value: value is None})
    """취소 시점"""
    requested_at: str = dataclasses.field(metadata={"serde_rename": "requestedAt"})
    """취소 요청 시점"""
    receipt_url: Optional[str] = dataclasses.field(metadata={"serde_rename": "receiptUrl", "serde_skip_if": lambda value: value is None})
    """취소 영수증 URL"""

