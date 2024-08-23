import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._instant_billing_key_payment_method_input_card import InstantBillingKeyPaymentMethodInputCard

@dataclasses.dataclass
class InstantBillingKeyPaymentMethodInput:
    """빌링키 발급 시 결제 수단 입력 양식"""
    card: Optional[InstantBillingKeyPaymentMethodInputCard]

