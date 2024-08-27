import dataclasses
import serde
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._billing_key_payment_method_easy_pay_method import BillingKeyPaymentMethodEasyPayMethod
from portone_server_sdk._openapi._schemas._easy_pay_provider import EasyPayProvider

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class BillingKeyPaymentMethodEasyPay:
    """간편 결제 정보"""
    type: Literal["BillingKeyPaymentMethodEasyPay"] = dataclasses.field()
    provider: Optional[EasyPayProvider] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """간편 결제 PG사"""
    method: Optional[BillingKeyPaymentMethodEasyPayMethod] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """간편 결제 수단"""

