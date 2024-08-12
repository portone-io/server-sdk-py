from portone_server_sdk._openapi._schemas._failed_payment_schedule import (
    FailedPaymentSchedule,
)
from portone_server_sdk._openapi._schemas._pending_payment_schedule import (
    PendingPaymentSchedule,
)
from portone_server_sdk._openapi._schemas._revoked_payment_schedule import (
    RevokedPaymentSchedule,
)
from portone_server_sdk._openapi._schemas._scheduled_payment_schedule import (
    ScheduledPaymentSchedule,
)
from portone_server_sdk._openapi._schemas._started_payment_schedule import (
    StartedPaymentSchedule,
)
from portone_server_sdk._openapi._schemas._succeeded_payment_schedule import (
    SucceededPaymentSchedule,
)

type PaymentSchedule = (
    FailedPaymentSchedule
    | PendingPaymentSchedule
    | RevokedPaymentSchedule
    | ScheduledPaymentSchedule
    | StartedPaymentSchedule
    | SucceededPaymentSchedule
)
"""결제 예약 건"""
