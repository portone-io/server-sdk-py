import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._cash_receipt_type import CashReceiptType
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class CancelledCashReceipt:
    """발급 취소"""
    status: Literal["CANCELLED"] = dataclasses.field()
    """현금영수증 상태"""
    merchant_id: str = dataclasses.field(metadata={"serde_rename": "merchantId"})
    """고객사 아이디"""
    store_id: str = dataclasses.field(metadata={"serde_rename": "storeId"})
    """상점 아이디"""
    payment_id: str = dataclasses.field(metadata={"serde_rename": "paymentId"})
    """결제 건 아이디"""
    channel: SelectedChannel = dataclasses.field()
    """현금영수증 발급에 사용된 채널"""
    amount: int = dataclasses.field()
    """결제 금액"""
    tax_free_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "taxFreeAmount"})
    """면세액"""
    vat_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "vatAmount"})
    """부가세액"""
    currency: Currency = dataclasses.field()
    """통화"""
    order_name: str = dataclasses.field(metadata={"serde_rename": "orderName"})
    """주문명"""
    is_manual: bool = dataclasses.field(metadata={"serde_rename": "isManual"})
    """수동 발급 여부"""
    type: Optional[CashReceiptType] = dataclasses.field()
    """현금영수증 유형"""
    pg_receipt_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "pgReceiptId"})
    """PG사 현금영수증 아이디"""
    issue_number: str = dataclasses.field(metadata={"serde_rename": "issueNumber"})
    """승인번호"""
    url: Optional[str] = dataclasses.field()
    """현금영수증 URL"""
    issued_at: str = dataclasses.field(metadata={"serde_rename": "issuedAt"})
    """발급 시점"""
    cancelled_at: str = dataclasses.field(metadata={"serde_rename": "cancelledAt"})
    """취소 시점"""

