import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._bank import Bank
from portone_server_sdk._openapi._schemas._payment_method_virtual_account_refund_status import PaymentMethodVirtualAccountRefundStatus
from portone_server_sdk._openapi._schemas._payment_method_virtual_account_type import PaymentMethodVirtualAccountType

@dataclasses.dataclass
class PaymentMethodVirtualAccount:
    """가상계좌 상세 정보"""
    type: Literal["PaymentMethodVirtualAccount"] = dataclasses.field()
    bank: Optional[Bank] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """표준 은행 코드"""
    account_number: str = dataclasses.field(metadata={"serde_rename": "accountNumber"})
    """계좌번호"""
    account_type: Optional[PaymentMethodVirtualAccountType] = dataclasses.field(metadata={"serde_rename": "accountType", "serde_skip_if": lambda value: value is None})
    """계좌 유형"""
    remittee_name: Optional[str] = dataclasses.field(metadata={"serde_rename": "remitteeName", "serde_skip_if": lambda value: value is None})
    """계좌주"""
    remitter_name: Optional[str] = dataclasses.field(metadata={"serde_rename": "remitterName", "serde_skip_if": lambda value: value is None})
    """송금인(입금자)"""
    expired_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "expiredAt", "serde_skip_if": lambda value: value is None})
    """입금만료시점"""
    issued_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "issuedAt", "serde_skip_if": lambda value: value is None})
    """계좌발급시점"""
    refund_status: Optional[PaymentMethodVirtualAccountRefundStatus] = dataclasses.field(metadata={"serde_rename": "refundStatus", "serde_skip_if": lambda value: value is None})
    """가상계좌 결제가 환불 단계일 때의 환불 상태"""

