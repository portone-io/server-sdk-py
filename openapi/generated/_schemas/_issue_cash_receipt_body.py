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
    storeId: Optional[str]
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    paymentId: str
    """결제 건 아이디
    
    외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
    """
    channelKey: str
    """채널 키"""
    type: CashReceiptType
    """현금 영수증 유형"""
    orderName: str
    """주문명"""
    currency: Currency
    """화폐"""
    amount: PaymentAmountInput
    """금액 세부 입력 정보"""
    productType: Optional[PaymentProductType]
    """상품 유형"""
    customer: IssueCashReceiptCustomerInput
    """고객 정보"""
    paidAt: Optional[str]
    """결제 일자"""

