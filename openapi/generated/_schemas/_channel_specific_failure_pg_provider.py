import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class ChannelSpecificFailurePgProvider:
    """PG사에서 오류를 전달한 경우"""
    type: Literal["PG_PROVIDER"]
    channel: SelectedChannel
    message: Optional[str]
    pgCode: str
    pgMessage: str

