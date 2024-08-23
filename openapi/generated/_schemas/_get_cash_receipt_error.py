from typing import Union
from portone_server_sdk._openapi._schemas._cash_receipt_not_found_error import CashReceiptNotFoundError
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

GetCashReceiptError = Union[CashReceiptNotFoundError, ForbiddenError, InvalidRequestError, UnauthorizedError]
"""GetCashReceiptError"""

