import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class BillingKeyPaymentMethodMobile:
    """모바일 정보"""
    type: Literal["BillingKeyPaymentMethodMobile"] = dataclasses.field()
    phone_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "phoneNumber"})
    """전화번호"""

