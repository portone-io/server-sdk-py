import dataclasses
from typing import Any, Optional
from portone_server_sdk._openapi._schemas._cash_receipt_input import CashReceiptInput
from portone_server_sdk._openapi._schemas._country import Country
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._customer_input import CustomerInput
from portone_server_sdk._openapi._schemas._payment_amount_input import PaymentAmountInput
from portone_server_sdk._openapi._schemas._payment_product import PaymentProduct
from portone_server_sdk._openapi._schemas._payment_product_type import PaymentProductType
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput

@dataclasses.dataclass
class BillingKeyPaymentInput:
    """빌링키 결제 요청 입력 정보"""
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId"})
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    billing_key: str = dataclasses.field(metadata={"serde_rename": "billingKey"})
    """빌링키 결제에 사용할 빌링키"""
    channel_key: Optional[str] = dataclasses.field(metadata={"serde_rename": "channelKey"})
    """채널 키
    
    다수 채널에 대해 발급된 빌링키에 대해, 결제 채널을 특정하고 싶을 때 명시
    """
    order_name: str = dataclasses.field(metadata={"serde_rename": "orderName"})
    """주문명"""
    customer: Optional[CustomerInput] = dataclasses.field()
    """고객 정보"""
    custom_data: Optional[str] = dataclasses.field(metadata={"serde_rename": "customData"})
    """사용자 지정 데이터"""
    amount: PaymentAmountInput = dataclasses.field()
    """결제 금액 세부 입력 정보"""
    currency: Currency = dataclasses.field()
    """통화"""
    installment_month: Optional[int] = dataclasses.field(metadata={"serde_rename": "installmentMonth"})
    """할부 개월 수"""
    use_free_interest_from_merchant: Optional[bool] = dataclasses.field(metadata={"serde_rename": "useFreeInterestFromMerchant"})
    """무이자 할부 이자를 고객사가 부담할지 여부"""
    use_card_point: Optional[bool] = dataclasses.field(metadata={"serde_rename": "useCardPoint"})
    """카드 포인트 사용 여부"""
    cash_receipt: Optional[CashReceiptInput] = dataclasses.field(metadata={"serde_rename": "cashReceipt"})
    """현금영수증 정보"""
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
    bypass: Optional[Any] = dataclasses.field()
    """PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)"""

