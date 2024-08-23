import dataclasses
from typing import Optional

@dataclasses.dataclass
class InstantPaymentMethodInputVirtualAccountExpiry:
    """입금 만료 기한
    
    validHours와 dueDate 둘 중 하나의 필드만 입력합니다.
    """
    validHours: Optional[int]
    """유효 시간
    
    시간 단위로 입력합니다.
    """
    dueDate: Optional[str]
    """만료 시점"""

