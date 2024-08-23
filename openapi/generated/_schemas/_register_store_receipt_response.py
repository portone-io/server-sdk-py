import dataclasses
from typing import Optional

@dataclasses.dataclass
class RegisterStoreReceiptResponse:
    """영수증 내 하위 상점 거래 등록 응답"""
    receiptUrl: Optional[str]
    """결제 영수증 URL"""

