import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._cash_receipt_type import CashReceiptType
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._issue_cash_receipt_customer_input import IssueCashReceiptCustomerInput
from portone_server_sdk._openapi._schemas._payment_amount_input import PaymentAmountInput
from portone_server_sdk._openapi._schemas._payment_product_type import PaymentProductType

@dataclasses.dataclass
class IssueCashReceiptBody:
    """현금영수증 발급 요청 양식"""
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    payment_id: str = dataclasses.field(metadata={"serde_rename": "paymentId"})
    """결제 건 아이디
    
    외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
    """
    channel_key: str = dataclasses.field(metadata={"serde_rename": "channelKey"})
    """채널 키"""
    type: CashReceiptType = dataclasses.field()
    """현금 영수증 유형"""
    order_name: str = dataclasses.field(metadata={"serde_rename": "orderName"})
    """주문명"""
    currency: Currency = dataclasses.field()
    """화폐"""
    amount: PaymentAmountInput = dataclasses.field()
    """금액 세부 입력 정보"""
    product_type: Optional[PaymentProductType] = dataclasses.field(metadata={"serde_rename": "productType", "serde_skip_if": lambda value: value is None})
    """상품 유형"""
    customer: IssueCashReceiptCustomerInput = dataclasses.field()
    """고객 정보"""
    paid_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "paidAt", "serde_skip_if": lambda value: value is None})
    """결제 일자"""

