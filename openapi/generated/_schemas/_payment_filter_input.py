import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._card_brand import CardBrand
from portone_server_sdk._openapi._schemas._card_owner_type import CardOwnerType
from portone_server_sdk._openapi._schemas._card_type import CardType
from portone_server_sdk._openapi._schemas._cash_receipt_input_type import CashReceiptInputType
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._date_time_range import DateTimeRange
from portone_server_sdk._openapi._schemas._payment_cash_receipt_status import PaymentCashReceiptStatus
from portone_server_sdk._openapi._schemas._payment_client_type import PaymentClientType
from portone_server_sdk._openapi._schemas._payment_filter_input_escrow_status import PaymentFilterInputEscrowStatus
from portone_server_sdk._openapi._schemas._payment_method_gift_certificate_type import PaymentMethodGiftCertificateType
from portone_server_sdk._openapi._schemas._payment_method_type import PaymentMethodType
from portone_server_sdk._openapi._schemas._payment_sort_by import PaymentSortBy
from portone_server_sdk._openapi._schemas._payment_status import PaymentStatus
from portone_server_sdk._openapi._schemas._payment_text_search import PaymentTextSearch
from portone_server_sdk._openapi._schemas._payment_timestamp_type import PaymentTimestampType
from portone_server_sdk._openapi._schemas._payment_webhook_status import PaymentWebhookStatus
from portone_server_sdk._openapi._schemas._pg_provider import PgProvider
from portone_server_sdk._openapi._schemas._port_one_version import PortOneVersion
from portone_server_sdk._openapi._schemas._sort_order import SortOrder

@dataclasses.dataclass
class PaymentFilterInput:
    """결제 건 다건 조회를 위한 입력 정보"""
    merchantId: Optional[str]
    """고객사 아이디"""
    storeId: Optional[str]
    """상점 아이디
    
    Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 결제 건을 조회합니다.
    """
    timestampType: Optional[PaymentTimestampType]
    """조회 기준 시점 유형"""
    from_: Optional[str] = dataclasses.field(metadata={"serde_rename": "from"})
    """결제 요청/상태 승인 시점 범위의 시작
    
    값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
    """
    until: Optional[str]
    """결제 요청/상태 승인 시점 범위의 끝
    
    값을 입력하지 않으면 현재 시점으로 설정됩니다.
    """
    status: Optional[list[PaymentStatus]]
    """결제 상태 리스트
    
    값을 입력하지 않으면 결제상태 필터링이 적용되지 않습니다.
    """
    methods: Optional[list[PaymentMethodType]]
    """결제수단 리스트
    
    값을 입력하지 않으면 결제수단 필터링이 적용되지 않습니다.
    """
    pgProvider: Optional[list[PgProvider]]
    """PG사 리스트
    
    값을 입력하지 않으면 결제대행사 필터링이 적용되지 않습니다.
    """
    isTest: Optional[bool]
    """테스트 결제 필터링"""
    isScheduled: Optional[bool]
    """결제 예약 건 필터링"""
    sortBy: Optional[PaymentSortBy]
    """결제 건 정렬 기준"""
    sortOrder: Optional[SortOrder]
    """결제 건 정렬 방식"""
    version: Optional[PortOneVersion]
    """포트원 버전"""
    webhookStatus: Optional[PaymentWebhookStatus]
    """웹훅 상태"""
    platformType: Optional[PaymentClientType]
    """플랫폼 유형"""
    currency: Optional[Currency]
    """통화"""
    isEscrow: Optional[bool]
    """에스크로 결제 여부"""
    escrowStatus: Optional[PaymentFilterInputEscrowStatus]
    """에스크로 결제의 배송 정보 상태"""
    cardBrand: Optional[CardBrand]
    """카드 브랜드"""
    cardType: Optional[CardType]
    """카드 유형"""
    cardOwnerType: Optional[CardOwnerType]
    """카드 소유주 유형"""
    giftCertificateType: Optional[PaymentMethodGiftCertificateType]
    """상품권 종류"""
    cashReceiptType: Optional[CashReceiptInputType]
    """현금영수증 유형"""
    cashReceiptStatus: Optional[PaymentCashReceiptStatus]
    """현금영수증 상태"""
    cashReceiptIssuedAtRange: Optional[DateTimeRange]
    """현금영수증 발급 시간 범위"""
    cashReceiptCancelledAtRange: Optional[DateTimeRange]
    """현금영수증 취소 시간 범위"""
    textSearch: Optional[list[PaymentTextSearch]]
    """통합 검색 리스트 필터"""

