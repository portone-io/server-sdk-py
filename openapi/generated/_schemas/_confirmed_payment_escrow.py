import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class ConfirmedPaymentEscrow:
    """구매 확정"""
    status: Literal["CONFIRMED"] = dataclasses.field()
    """에스크로 상태"""
    company: str = dataclasses.field()
    """택배사"""
    invoice_number: str = dataclasses.field(metadata={"serde_rename": "invoiceNumber"})
    """송장번호"""
    sent_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "sentAt", "serde_skip_if": lambda value: value is None})
    """발송 일시"""
    applied_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "appliedAt", "serde_skip_if": lambda value: value is None})
    """배송등록 처리 일자"""
    is_automatically_confirmed: bool = dataclasses.field(metadata={"serde_rename": "isAutomaticallyConfirmed"})
    """자동 구매 확정 처리 여부"""

