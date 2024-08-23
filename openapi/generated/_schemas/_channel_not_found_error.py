import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class ChannelNotFoundError:
    """요청된 채널이 존재하지 않는 경우"""
    type: Literal["CHANNEL_NOT_FOUND"]
    message: Optional[str]

