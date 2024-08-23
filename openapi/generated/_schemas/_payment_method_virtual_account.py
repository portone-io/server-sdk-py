import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._bank import Bank
from portone_server_sdk._openapi._schemas._payment_method_virtual_account_refund_status import PaymentMethodVirtualAccountRefundStatus
from portone_server_sdk._openapi._schemas._payment_method_virtual_account_type import PaymentMethodVirtualAccountType

@dataclasses.dataclass
class PaymentMethodVirtualAccount:
    """가상계좌 상세 정보"""
    type: Literal["PaymentMethodVirtualAccount"]
    bank: Optional[Bank]
    """표준 은행 코드"""
    accountNumber: str
    """계좌번호"""
    accountType: Optional[PaymentMethodVirtualAccountType]
    """계좌 유형"""
    remitteeName: Optional[str]
    """계좌주"""
    remitterName: Optional[str]
    """송금인(입금자)"""
    expiredAt: Optional[str]
    """입금만료시점"""
    issuedAt: Optional[str]
    """계좌발급시점"""
    refundStatus: Optional[PaymentMethodVirtualAccountRefundStatus]
    """가상계좌 결제가 환불 단계일 때의 환불 상태"""

