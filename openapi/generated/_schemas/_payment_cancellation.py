from portone_server_sdk._openapi._schemas._failed_payment_cancellation import (
    FailedPaymentCancellation,
)
from portone_server_sdk._openapi._schemas._requested_payment_cancellation import (
    RequestedPaymentCancellation,
)
from portone_server_sdk._openapi._schemas._succeeded_payment_cancellation import (
    SucceededPaymentCancellation,
)

type PaymentCancellation = (
    FailedPaymentCancellation
    | RequestedPaymentCancellation
    | SucceededPaymentCancellation
)
"""결제 취소 내역"""
