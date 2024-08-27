import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class AlreadyPaidError:
    """결제가 이미 완료된 경우"""
    type: Literal["ALREADY_PAID"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

