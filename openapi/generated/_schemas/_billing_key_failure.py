import dataclasses
from typing import Optional

@dataclasses.dataclass
class BillingKeyFailure:
    """발급 실패 상세 정보"""
    message: Optional[str]
    """실패 사유"""
    pgCode: Optional[str]
    """PG사 실패 코드"""
    pgMessage: Optional[str]
    """PG사 실패 사유"""
    failedAt: str
    """실패 시점"""

