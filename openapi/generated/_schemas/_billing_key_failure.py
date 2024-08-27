import dataclasses
from typing import Optional

@dataclasses.dataclass
class BillingKeyFailure:
    """발급 실패 상세 정보"""
    message: Optional[str] = dataclasses.field()
    """실패 사유"""
    pg_code: Optional[str] = dataclasses.field(metadata={"serde_rename": "pgCode"})
    """PG사 실패 코드"""
    pg_message: Optional[str] = dataclasses.field(metadata={"serde_rename": "pgMessage"})
    """PG사 실패 사유"""
    failed_at: str = dataclasses.field(metadata={"serde_rename": "failedAt"})
    """실패 시점"""

