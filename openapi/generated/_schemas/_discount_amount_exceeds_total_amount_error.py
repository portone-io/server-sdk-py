import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class DiscountAmountExceedsTotalAmountError:
    """프로모션 할인 금액이 결제 시도 금액 이상인 경우"""
    type: Literal["DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT"]
    message: Optional[str]

