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
class VirtualAccountIssuedPayment:
    """가상계좌 발급 완료 상태 건"""
    status: Literal["VIRTUAL_ACCOUNT_ISSUED"]
    """결제 건 상태"""
    id: str
    """결제 건 아이디"""
    transactionId: str
    """결제 건 포트원 채번 아이디
    
    V1 결제 건의 경우 imp_uid에 해당합니다.
    """
    merchantId: str
    """고객사 아이디"""
    storeId: str
    """상점 아이디"""
    method: Optional[PaymentMethod]
    """결제수단 정보"""
    channel: SelectedChannel
    """결제 채널"""
    channelGroup: Optional[ChannelGroupSummary]
    """결제 채널 그룹 정보"""
    version: PortOneVersion
    """포트원 버전"""
    scheduleId: Optional[str]
    """결제 예약 건 아이디
    
    결제 예약을 이용한 경우에만 존재
    """
    billingKey: Optional[str]
    """결제 시 사용된 빌링키
    
    빌링키 결제인 경우에만 존재
    """
    webhooks: Optional[list[PaymentWebhook]]
    """웹훅 발송 내역"""
    requestedAt: str
    """결제 요청 시점"""
    updatedAt: str
    """업데이트 시점"""
    statusChangedAt: str
    """상태 업데이트 시점"""
    orderName: str
    """주문명"""
    amount: PaymentAmount
    """결제 금액 관련 세부 정보"""
    currency: Currency
    """통화"""
    customer: Customer
    """구매자 정보"""
    promotionId: Optional[str]
    """프로모션 아이디"""
    isCulturalExpense: Optional[bool]
    """문화비 지출 여부"""
    escrow: Optional[PaymentEscrow]
    """에스크로 결제 정보
    
    에스크로 결제인 경우 존재합니다.
    """
    products: Optional[list[PaymentProduct]]
    """상품 정보"""
    productCount: Optional[int]
    """상품 갯수"""
    customData: Optional[str]
    """사용자 지정 데이터"""
    country: Optional[Country]
    """국가 코드"""
    pgTxId: Optional[str]
    """PG사 거래 아이디"""

