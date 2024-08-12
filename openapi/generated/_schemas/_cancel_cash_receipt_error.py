from portone_server_sdk._openapi._schemas._cash_receipt_not_found_error import (
    CashReceiptNotFoundError,
)
from portone_server_sdk._openapi._schemas._cash_receipt_not_issued_error import (
    CashReceiptNotIssuedError,
)
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import (
    InvalidRequestError,
)
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

type CancelCashReceiptError = (
    CashReceiptNotFoundError
    | CashReceiptNotIssuedError
    | ForbiddenError
    | InvalidRequestError
    | PgProviderError
    | UnauthorizedError
)
"""CancelCashReceiptError"""