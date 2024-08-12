from portone_server_sdk._openapi._schemas._already_paid_or_waiting_error import (
    AlreadyPaidOrWaitingError,
)
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
from portone_server_sdk._openapi._schemas._payment_schedule_already_exists_error import (
    PaymentScheduleAlreadyExistsError,
)
from portone_server_sdk._openapi._schemas._sum_of_parts_exceeds_total_amount_error import (
    SumOfPartsExceedsTotalAmountError,
)
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

type CreatePaymentScheduleError = (
    AlreadyPaidOrWaitingError
    | BillingKeyAlreadyDeletedError
    | BillingKeyNotFoundError
    | ForbiddenError
    | InvalidRequestError
    | PaymentScheduleAlreadyExistsError
    | SumOfPartsExceedsTotalAmountError
    | UnauthorizedError
)
"""CreatePaymentScheduleError"""
