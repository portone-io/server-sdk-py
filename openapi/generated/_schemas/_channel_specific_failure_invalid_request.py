import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class ChannelSpecificFailureInvalidRequest:
    """요청된 입력 정보가 유효하지 않은 경우
    
    허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
    """
    type: Literal["INVALID_REQUEST"]
    channel: SelectedChannel
    message: Optional[str]

