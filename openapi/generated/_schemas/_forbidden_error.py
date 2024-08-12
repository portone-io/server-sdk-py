import dataclasses
from typing import Literal, Optional


@dataclasses.dataclass(kw_only=True)
class ForbiddenError:
    """요청이 거절된 경우"""

    type: Literal["FORBIDDEN"]
    message: Optional[str]
