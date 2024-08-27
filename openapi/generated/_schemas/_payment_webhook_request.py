import dataclasses
from typing import Optional

@dataclasses.dataclass
class PaymentWebhookRequest:
    """웹훅 요청 정보"""
    header: Optional[str] = dataclasses.field()
    """요청 헤더"""
    body: str = dataclasses.field()
    """요청 본문"""
    requested_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "requestedAt"})
    """요청 시점"""

