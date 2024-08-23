import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class RejectedPaymentEscrow:
    """구매 거절"""
    status: Literal["REJECTED"]
    """에스크로 상태"""
    company: str
    """택배사"""
    invoiceNumber: str
    """송장번호"""
    sentAt: Optional[str]
    """발송 일시"""
    appliedAt: Optional[str]
    """배송등록 처리 일자"""

