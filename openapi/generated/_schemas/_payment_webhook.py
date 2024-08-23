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
    paymentStatus: Optional[PaymentWebhookPaymentStatus]
    """웹훅 발송 시 결제 건 상태
    
    V1 결제 건인 경우, 값이 존재하지 않습니다.
    """
    id: str
    """웹훅 아이디"""
    status: Optional[PaymentWebhookStatus]
    """웹훅 상태"""
    url: str
    """웹훅이 발송된 url
    
    V1 결제 건인 경우, 값이 존재하지 않습니다.
    """
    isAsync: Optional[bool]
    """비동기 웹훅 여부
    
    V1 결제 건인 경우, 값이 존재하지 않습니다.
    """
    currentExecutionCount: Optional[int]
    """현재 발송 횟수"""
    maxExecutionCount: Optional[int]
    """최대 발송 횟수"""
    trigger: Optional[PaymentWebhookTrigger]
    """웹훅 실행 맥락"""
    request: Optional[PaymentWebhookRequest]
    """웹훅 요청 정보"""
    response: Optional[PaymentWebhookResponse]
    """웹훅 응답 정보"""
    triggeredAt: Optional[str]
    """웹훅 처리 시작 시점"""

