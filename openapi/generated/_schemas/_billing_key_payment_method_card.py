import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._card import Card

@dataclasses.dataclass
class BillingKeyPaymentMethodCard:
    """카드 정보"""
    type: Literal["BillingKeyPaymentMethodCard"] = dataclasses.field()
    card: Optional[Card] = dataclasses.field()
    """카드 상세 정보"""

