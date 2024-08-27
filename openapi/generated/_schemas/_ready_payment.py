import dataclasses
import serde
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._channel_group_summary import ChannelGroupSummary
from portone_server_sdk._openapi._schemas._country import Country
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._customer import Customer
from portone_server_sdk._openapi._schemas._payment_amount import PaymentAmount
from portone_server_sdk._openapi._schemas._payment_escrow import PaymentEscrow
from portone_server_sdk._openapi._schemas._payment_method import PaymentMethod
from portone_server_sdk._openapi._schemas._payment_product import PaymentProduct
from portone_server_sdk._openapi._schemas._payment_webhook import PaymentWebhook
from portone_server_sdk._openapi._schemas._port_one_version import PortOneVersion
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class ReadyPayment:
    """준비 상태의 결제 건"""
    status: Literal["READY"] = dataclasses.field()
    """결제 건 상태"""
    id: str = dataclasses.field()
    """결제 건 아이디"""
    transaction_id: str = dataclasses.field(metadata={"serde_rename": "transactionId"})
    """결제 건 포트원 채번 아이디
    
    V1 결제 건의 경우 imp_uid에 해당합니다.
    """
    merchant_id: str = dataclasses.field(metadata={"serde_rename": "merchantId"})
    """고객사 아이디"""
    store_id: str = dataclasses.field(metadata={"serde_rename": "storeId"})
    """상점 아이디"""
    method: Optional[PaymentMethod] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """결제수단 정보"""
    channel: Optional[SelectedChannel] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """결제 채널"""
    channel_group: Optional[ChannelGroupSummary] = dataclasses.field(metadata={"serde_rename": "channelGroup", "serde_skip_if": lambda value: value is None})
    """결제 채널 그룹 정보"""
    version: PortOneVersion = dataclasses.field()
    """포트원 버전"""
    schedule_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "scheduleId", "serde_skip_if": lambda value: value is None})
    """결제 예약 건 아이디
    
    결제 예약을 이용한 경우에만 존재
    """
    billing_key: Optional[str] = dataclasses.field(metadata={"serde_rename": "billingKey", "serde_skip_if": lambda value: value is None})
    """결제 시 사용된 빌링키
    
    빌링키 결제인 경우에만 존재
    """
    webhooks: Optional[list[PaymentWebhook]] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """웹훅 발송 내역"""
    requested_at: str = dataclasses.field(metadata={"serde_rename": "requestedAt"})
    """결제 요청 시점"""
    updated_at: str = dataclasses.field(metadata={"serde_rename": "updatedAt"})
    """업데이트 시점"""
    status_changed_at: str = dataclasses.field(metadata={"serde_rename": "statusChangedAt"})
    """상태 업데이트 시점"""
    order_name: str = dataclasses.field(metadata={"serde_rename": "orderName"})
    """주문명"""
    amount: PaymentAmount = dataclasses.field()
    """결제 금액 관련 세부 정보"""
    currency: Currency = dataclasses.field()
    """통화"""
    customer: Customer = dataclasses.field()
    """구매자 정보"""
    promotion_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "promotionId", "serde_skip_if": lambda value: value is None})
    """프로모션 아이디"""
    is_cultural_expense: Optional[bool] = dataclasses.field(metadata={"serde_rename": "isCulturalExpense", "serde_skip_if": lambda value: value is None})
    """문화비 지출 여부"""
    escrow: Optional[PaymentEscrow] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """에스크로 결제의 배송 정보
    
    에스크로 결제인 경우 존재합니다.
    """
    products: Optional[list[PaymentProduct]] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """상품 정보"""
    product_count: Optional[int] = dataclasses.field(metadata={"serde_rename": "productCount", "serde_skip_if": lambda value: value is None})
    """상품 갯수"""
    custom_data: Optional[str] = dataclasses.field(metadata={"serde_rename": "customData", "serde_skip_if": lambda value: value is None})
    """사용자 지정 데이터"""
    country: Optional[Country] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """국가 코드"""

