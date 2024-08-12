import dataclasses
from portone_server_sdk._openapi._schemas._payment_cancellation import PaymentCancellation

@dataclasses.dataclass(kw_only=True)
class CancelPaymentResponse:
    """결제 취소 성공 응답"""
    cancellation: PaymentCancellation
    """결체 취소 내역"""

