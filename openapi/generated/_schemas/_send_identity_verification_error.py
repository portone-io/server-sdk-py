from portone_server_sdk._openapi._schemas._channel_not_found_error import (
    ChannelNotFoundError,
)
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._identity_verification_already_sent_error import (
    IdentityVerificationAlreadySentError,
)
from portone_server_sdk._openapi._schemas._identity_verification_already_verified_error import (
    IdentityVerificationAlreadyVerifiedError,
)
from portone_server_sdk._openapi._schemas._identity_verification_not_found_error import (
    IdentityVerificationNotFoundError,
)
from portone_server_sdk._openapi._schemas._invalid_request_error import (
    InvalidRequestError,
)
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

type SendIdentityVerificationError = (
    ChannelNotFoundError
    | ForbiddenError
    | IdentityVerificationAlreadySentError
    | IdentityVerificationAlreadyVerifiedError
    | IdentityVerificationNotFoundError
    | InvalidRequestError
    | PgProviderError
    | UnauthorizedError
)
"""SendIdentityVerificationError"""
