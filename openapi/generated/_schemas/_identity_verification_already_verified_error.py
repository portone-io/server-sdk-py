import dataclasses
from typing import Literal, Optional


@dataclasses.dataclass(kw_only=True)
class IdentityVerificationAlreadyVerifiedError:
    """본인인증 건이 이미 인증 완료된 상태인 경우"""

    type: Literal["IDENTITY_VERIFICATION_ALREADY_VERIFIED"]
    message: Optional[str]
