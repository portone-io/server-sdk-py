import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._cash_receipt_type import CashReceiptType
from portone_server_sdk._openapi._schemas._currency import Currency

@dataclasses.dataclass
class CancelledPaymentCashReceipt:
    """취소된 현금영수증"""
    status: Literal["CANCELLED"] = dataclasses.field()
    """결제 건 내 현금영수증 상태"""
    type: Optional[CashReceiptType] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """현금영수증 유형"""
    pg_receipt_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "pgReceiptId", "serde_skip_if": lambda value: value is None})
    """PG사 영수증 발급 아이디"""
    issue_number: str = dataclasses.field(metadata={"serde_rename": "issueNumber"})
    """승인 번호"""
    total_amount: int = dataclasses.field(metadata={"serde_rename": "totalAmount"})
    """총 금액"""
    tax_free_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "taxFreeAmount", "serde_skip_if": lambda value: value is None})
    """면세액"""
    currency: Currency = dataclasses.field()
    """통화"""
    url: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """현금영수증 URL"""
    issued_at: str = dataclasses.field(metadata={"serde_rename": "issuedAt"})
    """발급 시점"""
    cancelled_at: str = dataclasses.field(metadata={"serde_rename": "cancelledAt"})
    """취소 시점"""

