import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class AlreadyPaidError:
    """결제가 이미 완료된 경우"""
    type: Literal["ALREADY_PAID"]
    message: Optional[str]

