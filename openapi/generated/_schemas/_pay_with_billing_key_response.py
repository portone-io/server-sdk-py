import dataclasses
from portone_server_sdk._openapi._schemas._billing_key_payment_summary import BillingKeyPaymentSummary

@dataclasses.dataclass
class PayWithBillingKeyResponse:
    """빌링키 결제 성공 응답"""
    payment: BillingKeyPaymentSummary
    """결제 건 요약 정보"""

