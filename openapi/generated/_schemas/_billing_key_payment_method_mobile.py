import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class BillingKeyPaymentMethodMobile:
    """모바일 정보"""
    type: Literal["BillingKeyPaymentMethodMobile"]
    phoneNumber: Optional[str]
    """전화번호"""

