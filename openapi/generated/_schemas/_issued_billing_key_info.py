import dataclasses
import serde
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._billing_key_payment_method import BillingKeyPaymentMethod
from portone_server_sdk._openapi._schemas._channel_group_summary import ChannelGroupSummary
from portone_server_sdk._openapi._schemas._customer import Customer
from portone_server_sdk._openapi._schemas._pg_billing_key_issue_response import PgBillingKeyIssueResponse
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class IssuedBillingKeyInfo:
    """빌링키 발급 완료 상태 건"""
    status: Literal["ISSUED"] = dataclasses.field()
    """빌링키 상태"""
    billing_key: str = dataclasses.field(metadata={"serde_rename": "billingKey"})
    """빌링키"""
    merchant_id: str = dataclasses.field(metadata={"serde_rename": "merchantId"})
    """고객사 아이디"""
    store_id: str = dataclasses.field(metadata={"serde_rename": "storeId"})
    """상점 아이디"""
    methods: Optional[list[BillingKeyPaymentMethod]] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """빌링키 결제수단 상세 정보
    
    추후 슈퍼빌링키 기능 제공 시 여러 결제수단 정보가 담길 수 있습니다.
    """
    channels: list[SelectedChannel] = dataclasses.field()
    """빌링키 발급 시 사용된 채널
    
    추후 슈퍼빌링키 기능 제공 시 여러 채널 정보가 담길 수 있습니다.
    """
    customer: Customer = dataclasses.field()
    """고객 정보"""
    custom_data: Optional[str] = dataclasses.field(metadata={"serde_rename": "customData", "serde_skip_if": lambda value: value is None})
    """사용자 지정 데이터"""
    issue_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "issueId", "serde_skip_if": lambda value: value is None})
    """고객사가 채번하는 빌링키 발급 건 고유 아이디"""
    issue_name: Optional[str] = dataclasses.field(metadata={"serde_rename": "issueName", "serde_skip_if": lambda value: value is None})
    """빌링키 발급 건 이름"""
    requested_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "requestedAt", "serde_skip_if": lambda value: value is None})
    """발급 요청 시점"""
    issued_at: str = dataclasses.field(metadata={"serde_rename": "issuedAt"})
    """발급 시점"""
    channel_group: Optional[ChannelGroupSummary] = dataclasses.field(metadata={"serde_rename": "channelGroup", "serde_skip_if": lambda value: value is None})
    """채널 그룹"""
    pg_billing_key_issue_responses: Optional[list[PgBillingKeyIssueResponse]] = dataclasses.field(metadata={"serde_rename": "pgBillingKeyIssueResponses", "serde_skip_if": lambda value: value is None})
    """채널 별 빌링키 발급 응답
    
    슈퍼빌링키의 경우, 빌링키 발급이 성공하더라도 일부 채널에 대한 빌링키 발급은 실패할 수 있습니다.
    """

