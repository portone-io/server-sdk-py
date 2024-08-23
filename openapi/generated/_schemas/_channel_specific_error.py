import dataclasses
import serde
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._channel_specific_failure import ChannelSpecificFailure
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class ChannelSpecificError:
    """여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우"""
    type: Literal["CHANNEL_SPECIFIC"]
    message: Optional[str]
    failures: list[ChannelSpecificFailure]
    succeededChannels: list[SelectedChannel]
    """(결제, 본인인증 등에) 선택된 채널 정보"""

