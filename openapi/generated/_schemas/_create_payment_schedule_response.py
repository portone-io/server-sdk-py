import dataclasses
from portone_server_sdk._openapi._schemas._payment_schedule_summary import PaymentScheduleSummary

@dataclasses.dataclass
class CreatePaymentScheduleResponse:
    """결제 예약 성공 응답"""
    schedule: PaymentScheduleSummary
    """결제 예약 건"""

