import dataclasses
import serde
from typing import Optional
from portone_server_sdk._openapi._schemas._billing_key_info_summary import BillingKeyInfoSummary
from portone_server_sdk._openapi._schemas._channel_specific_failure import ChannelSpecificFailure

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class IssueBillingKeyResponse:
    """빌링키 발급 성공 응답"""
    billingKeyInfo: BillingKeyInfoSummary
    """빌링키 정보"""
    channelSpecificFailures: Optional[list[ChannelSpecificFailure]]
    """발급에 실패한 채널이 있을시 실패 정보"""

