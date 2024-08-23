import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class PaymentNotFoundError:
    """결제 건이 존재하지 않는 경우"""
    type: Literal["PAYMENT_NOT_FOUND"]
    message: Optional[str]

