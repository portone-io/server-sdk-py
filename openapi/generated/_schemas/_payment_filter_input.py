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
    merchant_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "merchantId", "serde_skip_if": lambda value: value is None})
    """고객사 아이디"""
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 결제 건을 조회합니다.
    """
    timestamp_type: Optional[PaymentTimestampType] = dataclasses.field(metadata={"serde_rename": "timestampType", "serde_skip_if": lambda value: value is None})
    """조회 기준 시점 유형"""
    from_: Optional[str] = dataclasses.field(metadata={"serde_rename": "from", "serde_skip_if": lambda value: value is None})
    """결제 요청/상태 승인 시점 범위의 시작
    
    값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
    """
    until: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """결제 요청/상태 승인 시점 범위의 끝
    
    값을 입력하지 않으면 현재 시점으로 설정됩니다.
    """
    status: Optional[list[PaymentStatus]] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """결제 상태 리스트
    
    값을 입력하지 않으면 결제상태 필터링이 적용되지 않습니다.
    """
    methods: Optional[list[PaymentMethodType]] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """결제수단 리스트
    
    값을 입력하지 않으면 결제수단 필터링이 적용되지 않습니다.
    """
    pg_provider: Optional[list[PgProvider]] = dataclasses.field(metadata={"serde_rename": "pgProvider", "serde_skip_if": lambda value: value is None})
    """PG사 리스트
    
    값을 입력하지 않으면 결제대행사 필터링이 적용되지 않습니다.
    """
    is_test: Optional[bool] = dataclasses.field(metadata={"serde_rename": "isTest", "serde_skip_if": lambda value: value is None})
    """테스트 결제 필터링"""
    is_scheduled: Optional[bool] = dataclasses.field(metadata={"serde_rename": "isScheduled", "serde_skip_if": lambda value: value is None})
    """결제 예약 건 필터링"""
    sort_by: Optional[PaymentSortBy] = dataclasses.field(metadata={"serde_rename": "sortBy", "serde_skip_if": lambda value: value is None})
    """결제 건 정렬 기준"""
    sort_order: Optional[SortOrder] = dataclasses.field(metadata={"serde_rename": "sortOrder", "serde_skip_if": lambda value: value is None})
    """결제 건 정렬 방식"""
    version: Optional[PortOneVersion] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """포트원 버전"""
    webhook_status: Optional[PaymentWebhookStatus] = dataclasses.field(metadata={"serde_rename": "webhookStatus", "serde_skip_if": lambda value: value is None})
    """웹훅 상태"""
    platform_type: Optional[PaymentClientType] = dataclasses.field(metadata={"serde_rename": "platformType", "serde_skip_if": lambda value: value is None})
    """플랫폼 유형"""
    currency: Optional[Currency] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """통화"""
    is_escrow: Optional[bool] = dataclasses.field(metadata={"serde_rename": "isEscrow", "serde_skip_if": lambda value: value is None})
    """에스크로 결제 여부"""
    escrow_status: Optional[PaymentFilterInputEscrowStatus] = dataclasses.field(metadata={"serde_rename": "escrowStatus", "serde_skip_if": lambda value: value is None})
    """에스크로 결제의 배송 정보 상태"""
    card_brand: Optional[CardBrand] = dataclasses.field(metadata={"serde_rename": "cardBrand", "serde_skip_if": lambda value: value is None})
    """카드 브랜드"""
    card_type: Optional[CardType] = dataclasses.field(metadata={"serde_rename": "cardType", "serde_skip_if": lambda value: value is None})
    """카드 유형"""
    card_owner_type: Optional[CardOwnerType] = dataclasses.field(metadata={"serde_rename": "cardOwnerType", "serde_skip_if": lambda value: value is None})
    """카드 소유주 유형"""
    gift_certificate_type: Optional[PaymentMethodGiftCertificateType] = dataclasses.field(metadata={"serde_rename": "giftCertificateType", "serde_skip_if": lambda value: value is None})
    """상품권 종류"""
    cash_receipt_type: Optional[CashReceiptInputType] = dataclasses.field(metadata={"serde_rename": "cashReceiptType", "serde_skip_if": lambda value: value is None})
    """현금영수증 유형"""
    cash_receipt_status: Optional[PaymentCashReceiptStatus] = dataclasses.field(metadata={"serde_rename": "cashReceiptStatus", "serde_skip_if": lambda value: value is None})
    """현금영수증 상태"""
    cash_receipt_issued_at_range: Optional[DateTimeRange] = dataclasses.field(metadata={"serde_rename": "cashReceiptIssuedAtRange", "serde_skip_if": lambda value: value is None})
    """현금영수증 발급 시간 범위"""
    cash_receipt_cancelled_at_range: Optional[DateTimeRange] = dataclasses.field(metadata={"serde_rename": "cashReceiptCancelledAtRange", "serde_skip_if": lambda value: value is None})
    """현금영수증 취소 시간 범위"""
    text_search: Optional[list[PaymentTextSearch]] = dataclasses.field(metadata={"serde_rename": "textSearch", "serde_skip_if": lambda value: value is None})
    """통합 검색 리스트 필터"""

