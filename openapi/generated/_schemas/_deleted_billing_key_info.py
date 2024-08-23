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
class DeletedBillingKeyInfo:
    """빌링키 삭제 완료 상태 건"""
    status: Literal["DELETED"]
    """빌링키 상태"""
    billingKey: str
    """빌링키"""
    merchantId: str
    """고객사 아이디"""
    storeId: str
    """상점 아이디"""
    methods: Optional[list[BillingKeyPaymentMethod]]
    """빌링키 결제수단 상세 정보
    
    추후 슈퍼빌링키 기능 제공 시 여러 결제수단 정보가 담길 수 있습니다.
    """
    channels: list[SelectedChannel]
    """빌링키 발급 시 사용된 채널
    
    추후 슈퍼빌링키 기능 제공 시 여러 채널 정보가 담길 수 있습니다.
    """
    customer: Customer
    """고객 정보"""
    customData: Optional[str]
    """사용자 지정 데이터"""
    issueId: Optional[str]
    """고객사가 채번하는 빌링키 발급 건 고유 아이디"""
    issueName: Optional[str]
    """빌링키 발급 건 이름"""
    requestedAt: Optional[str]
    """발급 요청 시점"""
    issuedAt: str
    """발급 시점"""
    channelGroup: Optional[ChannelGroupSummary]
    """채널 그룹"""
    pgBillingKeyIssueResponses: Optional[list[PgBillingKeyIssueResponse]]
    """채널 별 빌링키 발급 응답
    
    슈퍼빌링키의 경우, 빌링키 발급이 성공하더라도 일부 채널에 대한 발급은 실패할 수 있습니다.
    """
    deletedAt: str
    """발급 삭제 시점"""

