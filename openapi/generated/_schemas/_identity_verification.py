from portone_server_sdk._openapi._schemas._failed_identity_verification import (
    FailedIdentityVerification,
)
from portone_server_sdk._openapi._schemas._ready_identity_verification import (
    ReadyIdentityVerification,
)
from portone_server_sdk._openapi._schemas._verified_identity_verification import (
    VerifiedIdentityVerification,
)

type IdentityVerification = (
    FailedIdentityVerification
    | ReadyIdentityVerification
    | VerifiedIdentityVerification
)
"""본인인증 내역"""
