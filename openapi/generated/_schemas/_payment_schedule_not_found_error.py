import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class PaymentScheduleNotFoundError:
    """결제 예약건이 존재하지 않는 경우"""
    type: Literal["PAYMENT_SCHEDULE_NOT_FOUND"]
    message: Optional[str]

