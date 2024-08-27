import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class PaymentScheduleAlreadyExistsError:
    """결제 예약건이 이미 존재하는 경우"""
    type: Literal["PAYMENT_SCHEDULE_ALREADY_EXISTS"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

