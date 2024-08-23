import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._customer import Customer
from portone_server_sdk._openapi._schemas._payment_product import PaymentProduct

@dataclasses.dataclass
class PendingPaymentSchedule:
    """결제 대기 상태"""
    status: Literal["PENDING"]
    """결제 예약 건 상태"""
    id: str
    """결제 예약 건 아이디"""
    merchantId: str
    """고객사 아이디"""
    storeId: str
    """상점 아이디"""
    paymentId: str
    """결제 건 아이디"""
    billingKey: str
    """빌링키"""
    orderName: str
    """주문명"""
    isCulturalExpense: bool
    """문화비 지출 여부"""
    isEscrow: bool
    """에스크로 결제 여부"""
    customer: Customer
    """고객 정보"""
    customData: str
    """사용자 지정 데이터"""
    totalAmount: int
    """결제 총 금액"""
    taxFreeAmount: Optional[int]
    """면세액"""
    vatAmount: Optional[int]
    """부가세"""
    currency: Currency
    """통화"""
    installmentMonth: Optional[int]
    """할부 개월 수"""
    noticeUrls: Optional[list[str]]
    """웹훅 주소"""
    products: Optional[list[PaymentProduct]]
    """상품 정보"""
    createdAt: str
    """결제 예약 등록 시점"""
    timeToPay: str
    """결제 예정 시점"""
    startedAt: str
    """결제 시작 시점"""
    completedAt: str
    """결제 완료 시점"""

