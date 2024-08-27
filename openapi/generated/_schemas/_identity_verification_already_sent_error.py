import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class IdentityVerificationAlreadySentError:
    """본인인증 건이 이미 API로 요청된 상태인 경우"""
    type: Literal["IDENTITY_VERIFICATION_ALREADY_SENT"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

