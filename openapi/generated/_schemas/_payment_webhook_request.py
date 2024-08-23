import dataclasses
from typing import Optional

@dataclasses.dataclass
class PaymentWebhookRequest:
    """웹훅 요청 정보"""
    header: Optional[str]
    """요청 헤더"""
    body: str
    """요청 본문"""
    requestedAt: Optional[str]
    """요청 시점"""

