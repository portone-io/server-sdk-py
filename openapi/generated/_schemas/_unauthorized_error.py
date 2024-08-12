import dataclasses
from typing import Literal, Optional


@dataclasses.dataclass(kw_only=True)
class UnauthorizedError:
    """인증 정보가 올바르지 않은 경우"""

    type: Literal["UNAUTHORIZED"]
    message: Optional[str]
