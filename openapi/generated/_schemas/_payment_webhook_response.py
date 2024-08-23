import dataclasses

@dataclasses.dataclass
class PaymentWebhookResponse:
    """웹훅 응답 정보"""
    code: str
    """응답 HTTP 코드"""
    header: str
    """응답 헤더"""
    body: str
    """응답 본문"""
    respondedAt: str
    """응답 시점"""

