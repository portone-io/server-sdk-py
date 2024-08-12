from typing import Literal

type PaymentScheduleStatus = Literal[
    "SCHEDULED", "STARTED", "SUCCEEDED", "FAILED", "REVOKED", "PENDING"
]
"""결제 예약 건 상태"""
