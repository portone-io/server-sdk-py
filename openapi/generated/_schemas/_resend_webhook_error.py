from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import (
    InvalidRequestError,
)
from portone_server_sdk._openapi._schemas._payment_not_found_error import (
    PaymentNotFoundError,
)
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError
from portone_server_sdk._openapi._schemas._webhook_not_found_error import (
    WebhookNotFoundError,
)

type ResendWebhookError = (
    ForbiddenError
    | InvalidRequestError
    | PaymentNotFoundError
    | UnauthorizedError
    | WebhookNotFoundError
)
"""ResendWebhookError"""