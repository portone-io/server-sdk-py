import dataclasses
from portone_server_sdk._openapi._schemas._instant_payment_summary import InstantPaymentSummary

@dataclasses.dataclass(kw_only=True)
class PayInstantlyResponse:
    """수기 결제 성공 응답"""
    payment: InstantPaymentSummary
    """결제 건 요약 정보"""

