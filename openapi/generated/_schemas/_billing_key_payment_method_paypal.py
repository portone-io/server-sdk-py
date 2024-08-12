import dataclasses
from typing import Literal

@dataclasses.dataclass(kw_only=True)
class BillingKeyPaymentMethodPaypal:
    """페이팔 정보"""
    type: Literal["BillingKeyPaymentMethodPaypal"]

