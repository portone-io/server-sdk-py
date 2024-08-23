import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class ConfirmedPaymentEscrow:
    """구매 확정"""
    status: Literal["CONFIRMED"]
    """에스크로 상태"""
    company: str
    """택배사"""
    invoiceNumber: str
    """송장번호"""
    sentAt: Optional[str]
    """발송 일시"""
    appliedAt: Optional[str]
    """배송등록 처리 일자"""
    isAutomaticallyConfirmed: bool
    """자동 구매 확정 처리 여부"""

