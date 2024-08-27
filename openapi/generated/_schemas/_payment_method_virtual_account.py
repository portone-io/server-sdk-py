import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._bank import Bank
from portone_server_sdk._openapi._schemas._payment_method_virtual_account_refund_status import PaymentMethodVirtualAccountRefundStatus
from portone_server_sdk._openapi._schemas._payment_method_virtual_account_type import PaymentMethodVirtualAccountType

@dataclasses.dataclass
class PaymentMethodVirtualAccount:
    """가상계좌 상세 정보"""
    type: Literal["PaymentMethodVirtualAccount"] = dataclasses.field()
    bank: Optional[Bank] = dataclasses.field()
    """표준 은행 코드"""
    account_number: str = dataclasses.field(metadata={"serde_rename": "accountNumber"})
    """계좌번호"""
    account_type: Optional[PaymentMethodVirtualAccountType] = dataclasses.field(metadata={"serde_rename": "accountType"})
    """계좌 유형"""
    remittee_name: Optional[str] = dataclasses.field(metadata={"serde_rename": "remitteeName"})
    """계좌주"""
    remitter_name: Optional[str] = dataclasses.field(metadata={"serde_rename": "remitterName"})
    """송금인(입금자)"""
    expired_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "expiredAt"})
    """입금만료시점"""
    issued_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "issuedAt"})
    """계좌발급시점"""
    refund_status: Optional[PaymentMethodVirtualAccountRefundStatus] = dataclasses.field(metadata={"serde_rename": "refundStatus"})
    """가상계좌 결제가 환불 단계일 때의 환불 상태"""

