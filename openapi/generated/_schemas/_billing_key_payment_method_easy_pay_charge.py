import dataclasses
from typing import Literal

@dataclasses.dataclass(kw_only=True)
class BillingKeyPaymentMethodEasyPayCharge:
    """충전식 포인트 결제 정보"""
    type: Literal["BillingKeyPaymentMethodEasyPayCharge"]

