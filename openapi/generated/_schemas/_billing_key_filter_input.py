import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._billing_key_payment_method_type import BillingKeyPaymentMethodType
from portone_server_sdk._openapi._schemas._billing_key_status import BillingKeyStatus
from portone_server_sdk._openapi._schemas._billing_key_text_search import BillingKeyTextSearch
from portone_server_sdk._openapi._schemas._billing_key_time_range_field import BillingKeyTimeRangeField
from portone_server_sdk._openapi._schemas._payment_client_type import PaymentClientType
from portone_server_sdk._openapi._schemas._pg_company import PgCompany
from portone_server_sdk._openapi._schemas._pg_provider import PgProvider
from portone_server_sdk._openapi._schemas._port_one_version import PortOneVersion

@dataclasses.dataclass
class BillingKeyFilterInput:
    """빌링키 다건 조회를 위한 입력 정보"""
    storeId: Optional[str]
    """상점 아이디
    
    Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 빌링키를 조회합니다.
    """
    timeRangeField: Optional[BillingKeyTimeRangeField]
    """조회 기준 시점 유형"""
    from_: Optional[str] = dataclasses.field(metadata={"serde_rename": "from"})
    """조회 기준 시점 범위의 시작
    
    값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
    """
    until: Optional[str]
    """조회 기준 시점 범위의 끝
    
    값을 입력하지 않으면 현재 시점으로 설정됩니다.
    """
    status: Optional[list[BillingKeyStatus]]
    """빌링키 상태 리스트
    
    값을 입력하지 않으면 빌링키 상태 필터링이 적용되지 않습니다.
    """
    channelGroupIds: Optional[list[str]]
    """채널 그룹 아이디 리스트
    
    값을 입력하지 않으면 스마트 라우팅 그룹 아이디 필터링이 적용되지 않습니다.
    """
    customerId: Optional[str]
    """고객 ID"""
    platformType: Optional[PaymentClientType]
    """플랫폼 유형"""
    textSearch: Optional[BillingKeyTextSearch]
    """통합 검색 필터"""
    pgProviders: Optional[list[PgProvider]]
    """PG사 결제 모듈 리스트
    
    값을 입력하지 않으면 PG사 결제 모듈 필터링이 적용되지 않습니다.
    """
    pgCompanies: Optional[list[PgCompany]]
    """PG사 리스트
    
    값을 입력하지 않으면 PG사 필터링이 적용되지 않습니다.
    """
    methods: Optional[list[BillingKeyPaymentMethodType]]
    """결제수단 리스트
    
    값을 입력하지 않으면 결제수단 필터링이 적용되지 않습니다.
    """
    version: Optional[PortOneVersion]
    """포트원 버전"""

