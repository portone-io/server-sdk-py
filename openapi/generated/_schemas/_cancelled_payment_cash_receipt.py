import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._cash_receipt_type import CashReceiptType
from portone_server_sdk._openapi._schemas._currency import Currency

@dataclasses.dataclass
class CancelledPaymentCashReceipt:
    """취소된 현금영수증"""
    status: Literal["CANCELLED"]
    """결제 건 내 현금영수증 상태"""
    type: Optional[CashReceiptType]
    """현금영수증 유형"""
    pgReceiptId: Optional[str]
    """PG사 영수증 발급 아이디"""
    issueNumber: str
    """승인 번호"""
    totalAmount: int
    """총 금액"""
    taxFreeAmount: Optional[int]
    """면세액"""
    currency: Currency
    """통화"""
    url: Optional[str]
    """현금영수증 URL"""
    issuedAt: str
    """발급 시점"""
    cancelledAt: str
    """취소 시점"""

