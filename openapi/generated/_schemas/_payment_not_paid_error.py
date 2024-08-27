import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class PaymentNotPaidError:
    """결제가 완료되지 않은 경우"""
    type: Literal["PAYMENT_NOT_PAID"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

