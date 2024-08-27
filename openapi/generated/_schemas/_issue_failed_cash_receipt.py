import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class IssueFailedCashReceipt:
    """발급 실패"""
    status: Literal["ISSUE_FAILED"] = dataclasses.field()
    """현금영수증 상태"""
    merchant_id: str = dataclasses.field(metadata={"serde_rename": "merchantId"})
    """고객사 아이디"""
    store_id: str = dataclasses.field(metadata={"serde_rename": "storeId"})
    """상점 아이디"""
    payment_id: str = dataclasses.field(metadata={"serde_rename": "paymentId"})
    """결제 건 아이디"""
    channel: Optional[SelectedChannel] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """현금영수증 발급에 사용된 채널"""
    order_name: str = dataclasses.field(metadata={"serde_rename": "orderName"})
    """주문명"""
    is_manual: bool = dataclasses.field(metadata={"serde_rename": "isManual"})
    """수동 발급 여부"""

