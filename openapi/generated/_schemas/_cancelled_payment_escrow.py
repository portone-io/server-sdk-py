import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class CancelledPaymentEscrow:
    """거래 취소"""
    status: Literal["CANCELLED"] = dataclasses.field()
    """에스크로 상태"""
    company: str = dataclasses.field()
    """택배사"""
    invoice_number: str = dataclasses.field(metadata={"serde_rename": "invoiceNumber"})
    """송장번호"""
    sent_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "sentAt"})
    """발송 일시"""
    applied_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "appliedAt"})
    """배송등록 처리 일자"""

