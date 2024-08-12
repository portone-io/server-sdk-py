import dataclasses
from typing import Literal, Optional


@dataclasses.dataclass(kw_only=True)
class PaymentNotPaidError:
    """결제가 완료되지 않은 경우"""

    type: Literal["PAYMENT_NOT_PAID"]
    message: Optional[str]
