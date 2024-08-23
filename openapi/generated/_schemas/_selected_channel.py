import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._pg_provider import PgProvider
from portone_server_sdk._openapi._schemas._selected_channel_type import SelectedChannelType

@dataclasses.dataclass
class SelectedChannel:
    """(결제, 본인인증 등에) 선택된 채널 정보"""
    type: SelectedChannelType
    """채널 타입"""
    id: Optional[str]
    """채널 아이디"""
    key: Optional[str]
    """채널 키"""
    name: Optional[str]
    """채널 명"""
    pgProvider: PgProvider
    """PG사"""
    pgMerchantId: str
    """PG사 고객사 식별 아이디"""

