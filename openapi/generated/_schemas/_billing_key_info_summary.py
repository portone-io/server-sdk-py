import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class BillingKeyInfoSummary:
    """BillingKeyInfoSummary"""
    billingKey: str
    """발급된 빌링키"""
    channels: Optional[list[SelectedChannel]]
    """발급된 채널"""
    issuedAt: str
    """빌링크 발급 완료 시점"""

