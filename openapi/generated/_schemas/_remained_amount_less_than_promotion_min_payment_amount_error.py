import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass(kw_only=True)
class RemainedAmountLessThanPromotionMinPaymentAmountError:
    """부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우"""
    type: Literal["REMAINED_AMOUNT_LESS_THAN_PROMOTION_MIN_PAYMENT_AMOUNT"]
    message: Optional[str]

