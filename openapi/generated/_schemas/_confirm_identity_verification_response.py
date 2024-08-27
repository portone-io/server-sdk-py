import dataclasses
from portone_server_sdk._openapi._schemas._verified_identity_verification import VerifiedIdentityVerification

@dataclasses.dataclass
class ConfirmIdentityVerificationResponse:
    """본인인증 확인 성공 응답"""
    identity_verification: VerifiedIdentityVerification = dataclasses.field(metadata={"serde_rename": "identityVerification"})
    """완료된 본인인증 내역"""

