import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class PaymentScheduleAlreadyRevokedError:
    """결제 예약건이 이미 취소된 경우"""
    type: Literal["PAYMENT_SCHEDULE_ALREADY_REVOKED"]
    message: Optional[str]

