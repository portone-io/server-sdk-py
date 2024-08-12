from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._identity_verification_already_verified_error import (
    IdentityVerificationAlreadyVerifiedError,
)
from portone_server_sdk._openapi._schemas._identity_verification_not_found_error import (
    IdentityVerificationNotFoundError,
)
from portone_server_sdk._openapi._schemas._identity_verification_not_sent_error import (
    IdentityVerificationNotSentError,
)
from portone_server_sdk._openapi._schemas._invalid_request_error import (
    InvalidRequestError,
)
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

type ResendIdentityVerificationError = (
    ForbiddenError
    | IdentityVerificationAlreadyVerifiedError
    | IdentityVerificationNotFoundError
    | IdentityVerificationNotSentError
    | InvalidRequestError
    | PgProviderError
    | UnauthorizedError
)
"""ResendIdentityVerificationError"""
