import dataclasses
from typing import Literal
from portone_server_sdk._openapi._schemas._billing_key_failure import BillingKeyFailure
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class FailedPgBillingKeyIssueResponse:
    """빌링키 발급 실패 채널 응답"""
    type: Literal["FAILED"]
    channel: SelectedChannel
    """채널
    
    빌링키 발급을 시도한 채널입니다.
    """
    failure: BillingKeyFailure
    """발급 실패 상세 정보"""

