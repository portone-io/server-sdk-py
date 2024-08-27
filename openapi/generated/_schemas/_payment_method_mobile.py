import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class PaymentMethodMobile:
    """모바일 상세 정보"""
    type: Literal["PaymentMethodMobile"] = dataclasses.field()
    phone_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "phoneNumber"})
    """전화번호"""

