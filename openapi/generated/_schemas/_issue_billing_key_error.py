from typing import Union
from portone_server_sdk._openapi._schemas._channel_not_found_error import ChannelNotFoundError
from portone_server_sdk._openapi._schemas._channel_specific_error import ChannelSpecificError
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

IssueBillingKeyError = Union[ChannelNotFoundError, ChannelSpecificError, ForbiddenError, InvalidRequestError, PgProviderError, UnauthorizedError]
"""IssueBillingKeyError"""

