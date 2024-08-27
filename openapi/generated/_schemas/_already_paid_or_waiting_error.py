import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class AlreadyPaidOrWaitingError:
    """결제가 이미 완료되었거나 대기중인 경우"""
    type: Literal["ALREADY_PAID_OR_WAITING"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

