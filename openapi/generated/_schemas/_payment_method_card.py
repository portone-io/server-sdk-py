import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._card import Card
from portone_server_sdk._openapi._schemas._payment_installment import PaymentInstallment

@dataclasses.dataclass
class PaymentMethodCard:
    """결제수단 카드 정보"""
    type: Literal["PaymentMethodCard"]
    card: Optional[Card]
    """카드 상세 정보"""
    approvalNumber: Optional[str]
    """승인 번호"""
    installment: Optional[PaymentInstallment]
    """할부 정보"""
    pointUsed: Optional[bool]
    """카드 포인트 사용여부"""

