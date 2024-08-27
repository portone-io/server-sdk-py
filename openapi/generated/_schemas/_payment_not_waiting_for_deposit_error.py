import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class PaymentNotWaitingForDepositError:
    """결제 건이 입금 대기 상태가 아닌 경우"""
    type: Literal["PAYMENT_NOT_WAITING_FOR_DEPOSIT"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

