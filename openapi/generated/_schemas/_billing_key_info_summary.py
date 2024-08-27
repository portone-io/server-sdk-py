import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class BillingKeyInfoSummary:
    """BillingKeyInfoSummary"""
    billing_key: str = dataclasses.field(metadata={"serde_rename": "billingKey"})
    """발급된 빌링키"""
    channels: Optional[list[SelectedChannel]] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """발급된 채널"""
    issued_at: str = dataclasses.field(metadata={"serde_rename": "issuedAt"})
    """빌링크 발급 완료 시점"""

