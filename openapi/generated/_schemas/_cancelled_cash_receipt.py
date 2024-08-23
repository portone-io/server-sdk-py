import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._cash_receipt_type import CashReceiptType
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class CancelledCashReceipt:
    """발급 취소"""
    status: Literal["CANCELLED"]
    """현금영수증 상태"""
    merchantId: str
    """고객사 아이디"""
    storeId: str
    """상점 아이디"""
    paymentId: str
    """결제 건 아이디"""
    channel: SelectedChannel
    """현금영수증 발급에 사용된 채널"""
    amount: int
    """결제 금액"""
    taxFreeAmount: Optional[int]
    """면세액"""
    vatAmount: Optional[int]
    """부가세액"""
    currency: Currency
    """통화"""
    orderName: str
    """주문명"""
    isManual: bool
    """수동 발급 여부"""
    type: Optional[CashReceiptType]
    """현금영수증 유형"""
    pgReceiptId: Optional[str]
    """PG사 현금영수증 아이디"""
    issueNumber: str
    """승인번호"""
    url: Optional[str]
    """현금영수증 URL"""
    issuedAt: str
    """발급 시점"""
    cancelledAt: str
    """취소 시점"""

