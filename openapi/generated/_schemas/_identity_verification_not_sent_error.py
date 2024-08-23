import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class IdentityVerificationNotSentError:
    """본인인증 건이 API로 요청된 상태가 아닌 경우"""
    type: Literal["IDENTITY_VERIFICATION_NOT_SENT"]
    message: Optional[str]

