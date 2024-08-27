import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._instant_payment_method_input_card import InstantPaymentMethodInputCard
from portone_server_sdk._openapi._schemas._instant_payment_method_input_virtual_account import InstantPaymentMethodInputVirtualAccount

@dataclasses.dataclass
class InstantPaymentMethodInput:
    """수기 결제 수단 입력 정보
    
    하나의 필드만 입력합니다.
    """
    card: Optional[InstantPaymentMethodInputCard] = dataclasses.field()
    """카드"""
    virtual_account: Optional[InstantPaymentMethodInputVirtualAccount] = dataclasses.field(metadata={"serde_rename": "virtualAccount"})
    """가상계좌"""

