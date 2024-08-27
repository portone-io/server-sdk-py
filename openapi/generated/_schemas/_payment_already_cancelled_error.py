import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class PaymentAlreadyCancelledError:
    """결제가 이미 취소된 경우"""
    type: Literal["PAYMENT_ALREADY_CANCELLED"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

