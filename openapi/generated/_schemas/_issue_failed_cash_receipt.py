import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class IssueFailedCashReceipt:
    """발급 실패"""
    status: Literal["ISSUE_FAILED"]
    """현금영수증 상태"""
    merchantId: str
    """고객사 아이디"""
    storeId: str
    """상점 아이디"""
    paymentId: str
    """결제 건 아이디"""
    channel: Optional[SelectedChannel]
    """현금영수증 발급에 사용된 채널"""
    orderName: str
    """주문명"""
    isManual: bool
    """수동 발급 여부"""

