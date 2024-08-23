import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class WebhookNotFoundError:
    """웹훅 내역이 존재하지 않는 경우"""
    type: Literal["WEBHOOK_NOT_FOUND"]
    message: Optional[str]

