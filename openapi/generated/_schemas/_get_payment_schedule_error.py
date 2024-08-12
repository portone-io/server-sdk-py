from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import (
    InvalidRequestError,
)
from portone_server_sdk._openapi._schemas._payment_schedule_not_found_error import (
    PaymentScheduleNotFoundError,
)
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

type GetPaymentScheduleError = (
    ForbiddenError
    | InvalidRequestError
    | PaymentScheduleNotFoundError
    | UnauthorizedError
)
"""GetPaymentScheduleError"""
