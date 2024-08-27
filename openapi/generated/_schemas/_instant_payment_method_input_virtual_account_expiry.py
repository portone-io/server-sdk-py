import dataclasses
from typing import Optional

@dataclasses.dataclass
class InstantPaymentMethodInputVirtualAccountExpiry:
    """입금 만료 기한
    
    validHours와 dueDate 둘 중 하나의 필드만 입력합니다.
    """
    valid_hours: Optional[int] = dataclasses.field(metadata={"serde_rename": "validHours", "serde_skip_if": lambda value: value is None})
    """유효 시간
    
    시간 단위로 입력합니다.
    """
    due_date: Optional[str] = dataclasses.field(metadata={"serde_rename": "dueDate", "serde_skip_if": lambda value: value is None})
    """만료 시점"""

