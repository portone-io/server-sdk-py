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
    storeId: Optional[str]
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    channelKey: Optional[str]
    """채널 키
    
    채널 키 또는 채널 그룹 ID 필수
    """
    channelGroupId: Optional[str]
    """채널 그룹 ID
    
    채널 키 또는 채널 그룹 ID 필수
    """
    method: InstantPaymentMethodInput
    """결제수단 정보"""
    orderName: str
    """주문명"""
    isCulturalExpense: Optional[bool]
    """문화비 지출 여부
    
    기본값은 false 입니다.
    """
    isEscrow: Optional[bool]
    """에스크로 결제 여부
    
    기본값은 false 입니다.
    """
    customer: Optional[CustomerInput]
    """고객 정보"""
    customData: Optional[str]
    """사용자 지정 데이터"""
    amount: PaymentAmountInput
    """결제 금액 세부 입력 정보"""
    currency: Currency
    """통화"""
    country: Optional[Country]
    """결제 국가"""
    noticeUrls: Optional[list[str]]
    """웹훅 주소
    
    결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
    상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
    입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
    """
    products: Optional[list[PaymentProduct]]
    """상품 정보
    
    입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
    """
    productCount: Optional[int]
    """상품 개수"""
    productType: Optional[PaymentProductType]
    """상품 유형"""
    shippingAddress: Optional[SeparatedAddressInput]
    """배송지 주소"""
    promotionId: Optional[str]
    """해당 결제에 적용할 프로모션 아이디"""

