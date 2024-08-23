import dataclasses
from portone_server_sdk._openapi._schemas._billing_key_payment_input import BillingKeyPaymentInput

@dataclasses.dataclass
class CreatePaymentScheduleBody:
    """결제 예약 요청 입력 정보"""
    payment: BillingKeyPaymentInput
    """빌링키 결제 입력 정보"""
    timeToPay: str
    """결제 예정 시점"""

