import dataclasses
import serde
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._billing_key_payment_method import BillingKeyPaymentMethod
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class IssuedPgBillingKeyIssueResponse:
    """빌링키 발급 성공 채널 응답"""
    type: Literal["ISSUED"] = dataclasses.field()
    channel: SelectedChannel = dataclasses.field()
    """채널
    
    빌링키 발급을 시도한 채널입니다.
    """
    pg_tx_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "pgTxId", "serde_skip_if": lambda value: value is None})
    """PG사 거래 아이디"""
    method: Optional[BillingKeyPaymentMethod] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """빌링키 결제수단 상세 정보
    
    채널에 대응되는 PG사에서 응답한 빌링키 발급 수단 정보입니다.
    """

