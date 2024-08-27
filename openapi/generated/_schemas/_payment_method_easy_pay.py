import dataclasses
import serde
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._easy_pay_provider import EasyPayProvider
from portone_server_sdk._openapi._schemas._payment_method_easy_pay_method import PaymentMethodEasyPayMethod

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class PaymentMethodEasyPay:
    """간편 결제 상세 정보"""
    type: Literal["PaymentMethodEasyPay"] = dataclasses.field()
    provider: Optional[EasyPayProvider] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """간편 결제 PG사"""
    easy_pay_method: Optional[PaymentMethodEasyPayMethod] = dataclasses.field(metadata={"serde_rename": "easyPayMethod", "serde_skip_if": lambda value: value is None})
    """간편 결제 수단"""

