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
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 빌링키를 조회합니다.
    """
    time_range_field: Optional[BillingKeyTimeRangeField] = dataclasses.field(metadata={"serde_rename": "timeRangeField", "serde_skip_if": lambda value: value is None})
    """조회 기준 시점 유형"""
    from_: Optional[str] = dataclasses.field(metadata={"serde_rename": "from", "serde_skip_if": lambda value: value is None})
    """조회 기준 시점 범위의 시작
    
    값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
    """
    until: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """조회 기준 시점 범위의 끝
    
    값을 입력하지 않으면 현재 시점으로 설정됩니다.
    """
    status: Optional[list[BillingKeyStatus]] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """빌링키 상태 리스트
    
    값을 입력하지 않으면 빌링키 상태 필터링이 적용되지 않습니다.
    """
    channel_group_ids: Optional[list[str]] = dataclasses.field(metadata={"serde_rename": "channelGroupIds", "serde_skip_if": lambda value: value is None})
    """채널 그룹 아이디 리스트
    
    값을 입력하지 않으면 스마트 라우팅 그룹 아이디 필터링이 적용되지 않습니다.
    """
    customer_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "customerId", "serde_skip_if": lambda value: value is None})
    """고객 ID"""
    platform_type: Optional[PaymentClientType] = dataclasses.field(metadata={"serde_rename": "platformType", "serde_skip_if": lambda value: value is None})
    """플랫폼 유형"""
    text_search: Optional[BillingKeyTextSearch] = dataclasses.field(metadata={"serde_rename": "textSearch", "serde_skip_if": lambda value: value is None})
    """통합 검색 필터"""
    pg_providers: Optional[list[PgProvider]] = dataclasses.field(metadata={"serde_rename": "pgProviders", "serde_skip_if": lambda value: value is None})
    """PG사 결제 모듈 리스트
    
    값을 입력하지 않으면 PG사 결제 모듈 필터링이 적용되지 않습니다.
    """
    pg_companies: Optional[list[PgCompany]] = dataclasses.field(metadata={"serde_rename": "pgCompanies", "serde_skip_if": lambda value: value is None})
    """PG사 리스트
    
    값을 입력하지 않으면 PG사 필터링이 적용되지 않습니다.
    """
    methods: Optional[list[BillingKeyPaymentMethodType]] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """결제수단 리스트
    
    값을 입력하지 않으면 결제수단 필터링이 적용되지 않습니다.
    """
    version: Optional[PortOneVersion] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """포트원 버전"""

