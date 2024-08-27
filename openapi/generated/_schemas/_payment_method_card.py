import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._card import Card
from portone_server_sdk._openapi._schemas._payment_installment import PaymentInstallment

@dataclasses.dataclass
class PaymentMethodCard:
    """결제수단 카드 정보"""
    type: Literal["PaymentMethodCard"] = dataclasses.field()
    card: Optional[Card] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """카드 상세 정보"""
    approval_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "approvalNumber", "serde_skip_if": lambda value: value is None})
    """승인 번호"""
    installment: Optional[PaymentInstallment] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """할부 정보"""
    point_used: Optional[bool] = dataclasses.field(metadata={"serde_rename": "pointUsed", "serde_skip_if": lambda value: value is None})
    """카드 포인트 사용여부"""

