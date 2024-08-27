import dataclasses
import serde
from typing import Optional
from portone_server_sdk._openapi._schemas._billing_key_info_summary import BillingKeyInfoSummary
from portone_server_sdk._openapi._schemas._channel_specific_failure import ChannelSpecificFailure

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class IssueBillingKeyResponse:
    """빌링키 발급 성공 응답"""
    billing_key_info: BillingKeyInfoSummary = dataclasses.field(metadata={"serde_rename": "billingKeyInfo"})
    """빌링키 정보"""
    channel_specific_failures: Optional[list[ChannelSpecificFailure]] = dataclasses.field(metadata={"serde_rename": "channelSpecificFailures", "serde_skip_if": lambda value: value is None})
    """발급에 실패한 채널이 있을시 실패 정보"""

