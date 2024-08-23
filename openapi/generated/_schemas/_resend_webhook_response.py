import dataclasses
from portone_server_sdk._openapi._schemas._payment_webhook import PaymentWebhook

@dataclasses.dataclass
class ResendWebhookResponse:
    """웹훅 재발송 응답 정보"""
    webhook: PaymentWebhook
    """재발송 웹훅 정보"""

