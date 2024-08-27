import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class PaymentScheduleAlreadyProcessedError:
    """결제 예약건이 이미 처리된 경우"""
    type: Literal["PAYMENT_SCHEDULE_ALREADY_PROCESSED"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

