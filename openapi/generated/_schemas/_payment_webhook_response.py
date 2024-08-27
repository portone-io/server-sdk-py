import dataclasses

@dataclasses.dataclass
class PaymentWebhookResponse:
    """웹훅 응답 정보"""
    code: str = dataclasses.field()
    """응답 HTTP 코드"""
    header: str = dataclasses.field()
    """응답 헤더"""
    body: str = dataclasses.field()
    """응답 본문"""
    responded_at: str = dataclasses.field(metadata={"serde_rename": "respondedAt"})
    """응답 시점"""

