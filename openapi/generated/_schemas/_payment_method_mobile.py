import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass(kw_only=True)
class PaymentMethodMobile:
    """모바일 상세 정보"""
    type: Literal["PaymentMethodMobile"]
    phoneNumber: Optional[str]
    """전화번호"""

