import dataclasses
import serde
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._easy_pay_provider import EasyPayProvider
from portone_server_sdk._openapi._schemas._payment_method_easy_pay_method import PaymentMethodEasyPayMethod

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class PaymentMethodEasyPay:
    """간편 결제 상세 정보"""
    type: Literal["PaymentMethodEasyPay"]
    provider: Optional[EasyPayProvider]
    """간편 결제 PG사"""
    easyPayMethod: Optional[PaymentMethodEasyPayMethod]
    """간편 결제 수단"""

