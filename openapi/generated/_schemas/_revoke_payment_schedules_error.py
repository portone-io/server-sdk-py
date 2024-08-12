from portone_server_sdk._openapi._schemas._billing_key_already_deleted_error import (
    BillingKeyAlreadyDeletedError,
)
from portone_server_sdk._openapi._schemas._billing_key_not_found_error import (
    BillingKeyNotFoundError,
)
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import (
    InvalidRequestError,
)
from portone_server_sdk._openapi._schemas._payment_schedule_already_processed_error import (
    PaymentScheduleAlreadyProcessedError,
)
from portone_server_sdk._openapi._schemas._payment_schedule_already_revoked_error import (
    PaymentScheduleAlreadyRevokedError,
)
from portone_server_sdk._openapi._schemas._payment_schedule_not_found_error import (
    PaymentScheduleNotFoundError,
)
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

type RevokePaymentSchedulesError = (
    BillingKeyAlreadyDeletedError
    | BillingKeyNotFoundError
    | ForbiddenError
    | InvalidRequestError
    | PaymentScheduleAlreadyProcessedError
    | PaymentScheduleAlreadyRevokedError
    | PaymentScheduleNotFoundError
    | UnauthorizedError
)
"""RevokePaymentSchedulesError"""