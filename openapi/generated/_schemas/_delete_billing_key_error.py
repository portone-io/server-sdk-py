from portone_server_sdk._openapi._schemas._billing_key_already_deleted_error import (
    BillingKeyAlreadyDeletedError,
)
from portone_server_sdk._openapi._schemas._billing_key_not_found_error import (
    BillingKeyNotFoundError,
)
from portone_server_sdk._openapi._schemas._billing_key_not_issued_error import (
    BillingKeyNotIssuedError,
)
from portone_server_sdk._openapi._schemas._channel_specific_error import (
    ChannelSpecificError,
)
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import (
    InvalidRequestError,
)
from portone_server_sdk._openapi._schemas._payment_schedule_already_exists_error import (
    PaymentScheduleAlreadyExistsError,
)
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

type DeleteBillingKeyError = (
    BillingKeyAlreadyDeletedError
    | BillingKeyNotFoundError
    | BillingKeyNotIssuedError
    | ChannelSpecificError
    | ForbiddenError
    | InvalidRequestError
    | PaymentScheduleAlreadyExistsError
    | PgProviderError
    | UnauthorizedError
)
"""DeleteBillingKeyError"""
