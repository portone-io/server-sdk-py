from typing import Union
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

GetKakaopayPaymentOrderError = Union[InvalidRequestError, UnauthorizedError]
"""GetKakaopayPaymentOrderError"""

