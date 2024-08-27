import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class ForbiddenError:
    """요청이 거절된 경우"""
    type: Literal["FORBIDDEN"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

