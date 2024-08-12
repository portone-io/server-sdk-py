import dataclasses
from typing import Literal, Optional


@dataclasses.dataclass(kw_only=True)
class PaymentAlreadyCancelledError:
    """결제가 이미 취소된 경우"""

    type: Literal["PAYMENT_ALREADY_CANCELLED"]
    message: Optional[str]
