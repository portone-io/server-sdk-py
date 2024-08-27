import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class UnauthorizedError:
    """인증 정보가 올바르지 않은 경우"""
    type: Literal["UNAUTHORIZED"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

