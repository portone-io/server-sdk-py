import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._payment_webhook_payment_status import PaymentWebhookPaymentStatus
from portone_server_sdk._openapi._schemas._payment_webhook_request import PaymentWebhookRequest
from portone_server_sdk._openapi._schemas._payment_webhook_response import PaymentWebhookResponse
from portone_server_sdk._openapi._schemas._payment_webhook_status import PaymentWebhookStatus
from portone_server_sdk._openapi._schemas._payment_webhook_trigger import PaymentWebhookTrigger

@dataclasses.dataclass
class PaymentWebhook:
    """성공 웹훅 내역"""
    payment_status: Optional[PaymentWebhookPaymentStatus] = dataclasses.field(metadata={"serde_rename": "paymentStatus", "serde_skip_if": lambda value: value is None})
    """웹훅 발송 시 결제 건 상태
    
    V1 결제 건인 경우, 값이 존재하지 않습니다.
    """
    id: str = dataclasses.field()
    """웹훅 아이디"""
    status: Optional[PaymentWebhookStatus] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """웹훅 상태"""
    url: str = dataclasses.field()
    """웹훅이 발송된 url
    
    V1 결제 건인 경우, 값이 존재하지 않습니다.
    """
    is_async: Optional[bool] = dataclasses.field(metadata={"serde_rename": "isAsync", "serde_skip_if": lambda value: value is None})
    """비동기 웹훅 여부
    
    V1 결제 건인 경우, 값이 존재하지 않습니다.
    """
    current_execution_count: Optional[int] = dataclasses.field(metadata={"serde_rename": "currentExecutionCount", "serde_skip_if": lambda value: value is None})
    """현재 발송 횟수"""
    max_execution_count: Optional[int] = dataclasses.field(metadata={"serde_rename": "maxExecutionCount", "serde_skip_if": lambda value: value is None})
    """최대 발송 횟수"""
    trigger: Optional[PaymentWebhookTrigger] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """웹훅 실행 맥락"""
    request: Optional[PaymentWebhookRequest] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """웹훅 요청 정보"""
    response: Optional[PaymentWebhookResponse] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """웹훅 응답 정보"""
    triggered_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "triggeredAt", "serde_skip_if": lambda value: value is None})
    """웹훅 처리 시작 시점"""

