import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._country import Country
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._customer_input import CustomerInput
from portone_server_sdk._openapi._schemas._instant_payment_method_input import InstantPaymentMethodInput
from portone_server_sdk._openapi._schemas._payment_amount_input import PaymentAmountInput
from portone_server_sdk._openapi._schemas._payment_product import PaymentProduct
from portone_server_sdk._openapi._schemas._payment_product_type import PaymentProductType
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput

@dataclasses.dataclass
class InstantPaymentInput:
    """수기 결제 요청 정보"""
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId"})
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    channel_key: Optional[str] = dataclasses.field(metadata={"serde_rename": "channelKey"})
    """채널 키
    
    채널 키 또는 채널 그룹 ID 필수
    """
    channel_group_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "channelGroupId"})
    """채널 그룹 ID
    
    채널 키 또는 채널 그룹 ID 필수
    """
    method: InstantPaymentMethodInput = dataclasses.field()
    """결제수단 정보"""
    order_name: str = dataclasses.field(metadata={"serde_rename": "orderName"})
    """주문명"""
    is_cultural_expense: Optional[bool] = dataclasses.field(metadata={"serde_rename": "isCulturalExpense"})
    """문화비 지출 여부
    
    기본값은 false 입니다.
    """
    is_escrow: Optional[bool] = dataclasses.field(metadata={"serde_rename": "isEscrow"})
    """에스크로 결제 여부
    
    기본값은 false 입니다.
    """
    customer: Optional[CustomerInput] = dataclasses.field()
    """고객 정보"""
    custom_data: Optional[str] = dataclasses.field(metadata={"serde_rename": "customData"})
    """사용자 지정 데이터"""
    amount: PaymentAmountInput = dataclasses.field()
    """결제 금액 세부 입력 정보"""
    currency: Currency = dataclasses.field()
    """통화"""
    country: Optional[Country] = dataclasses.field()
    """결제 국가"""
    notice_urls: Optional[list[str]] = dataclasses.field(metadata={"serde_rename": "noticeUrls"})
    """웹훅 주소
    
    결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
    상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
    입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
    """
    products: Optional[list[PaymentProduct]] = dataclasses.field()
    """상품 정보
    
    입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
    """
    product_count: Optional[int] = dataclasses.field(metadata={"serde_rename": "productCount"})
    """상품 개수"""
    product_type: Optional[PaymentProductType] = dataclasses.field(metadata={"serde_rename": "productType"})
    """상품 유형"""
    shipping_address: Optional[SeparatedAddressInput] = dataclasses.field(metadata={"serde_rename": "shippingAddress"})
    """배송지 주소"""
    promotion_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "promotionId"})
    """해당 결제에 적용할 프로모션 아이디"""

