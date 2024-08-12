from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._identity_verification_not_found_error import (
    IdentityVerificationNotFoundError,
)
from portone_server_sdk._openapi._schemas._invalid_request_error import (
    InvalidRequestError,
)
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

type GetIdentityVerificationError = (
    ForbiddenError
    | IdentityVerificationNotFoundError
    | InvalidRequestError
    | UnauthorizedError
)
"""GetIdentityVerificationError"""