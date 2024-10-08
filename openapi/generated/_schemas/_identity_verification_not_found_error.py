import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class IdentityVerificationNotFoundError:
    """요청된 본인인증 건이 존재하지 않는 경우"""
    type: Literal["IDENTITY_VERIFICATION_NOT_FOUND"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

