import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._customer import Customer
from portone_server_sdk._openapi._schemas._payment_product import PaymentProduct

@dataclasses.dataclass
class SucceededPaymentSchedule:
    """결제 성공 상태"""
    status: Literal["SUCCEEDED"] = dataclasses.field()
    """결제 예약 건 상태"""
    id: str = dataclasses.field()
    """결제 예약 건 아이디"""
    merchant_id: str = dataclasses.field(metadata={"serde_rename": "merchantId"})
    """고객사 아이디"""
    store_id: str = dataclasses.field(metadata={"serde_rename": "storeId"})
    """상점 아이디"""
    payment_id: str = dataclasses.field(metadata={"serde_rename": "paymentId"})
    """결제 건 아이디"""
    billing_key: str = dataclasses.field(metadata={"serde_rename": "billingKey"})
    """빌링키"""
    order_name: str = dataclasses.field(metadata={"serde_rename": "orderName"})
    """주문명"""
    is_cultural_expense: bool = dataclasses.field(metadata={"serde_rename": "isCulturalExpense"})
    """문화비 지출 여부"""
    is_escrow: bool = dataclasses.field(metadata={"serde_rename": "isEscrow"})
    """에스크로 결제 여부"""
    customer: Customer = dataclasses.field()
    """고객 정보"""
    custom_data: str = dataclasses.field(metadata={"serde_rename": "customData"})
    """사용자 지정 데이터"""
    total_amount: int = dataclasses.field(metadata={"serde_rename": "totalAmount"})
    """결제 총 금액"""
    tax_free_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "taxFreeAmount", "serde_skip_if": lambda value: value is None})
    """면세액"""
    vat_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "vatAmount", "serde_skip_if": lambda value: value is None})
    """부가세"""
    currency: Currency = dataclasses.field()
    """통화"""
    installment_month: Optional[int] = dataclasses.field(metadata={"serde_rename": "installmentMonth", "serde_skip_if": lambda value: value is None})
    """할부 개월 수"""
    notice_urls: Optional[list[str]] = dataclasses.field(metadata={"serde_rename": "noticeUrls", "serde_skip_if": lambda value: value is None})
    """웹훅 주소"""
    products: Optional[list[PaymentProduct]] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """상품 정보"""
    created_at: str = dataclasses.field(metadata={"serde_rename": "createdAt"})
    """결제 예약 등록 시점"""
    time_to_pay: str = dataclasses.field(metadata={"serde_rename": "timeToPay"})
    """결제 예정 시점"""
    started_at: str = dataclasses.field(metadata={"serde_rename": "startedAt"})
    """결제 시작 시점"""
    completed_at: str = dataclasses.field(metadata={"serde_rename": "completedAt"})
    """결제 완료 시점"""

