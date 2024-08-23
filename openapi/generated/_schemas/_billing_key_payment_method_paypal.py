import dataclasses
from typing import Literal

@dataclasses.dataclass
class BillingKeyPaymentMethodPaypal:
    """페이팔 정보"""
    type: Literal["BillingKeyPaymentMethodPaypal"]

