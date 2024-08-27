import dataclasses
from typing import Optional

@dataclasses.dataclass
class RegisterStoreReceiptResponse:
    """영수증 내 하위 상점 거래 등록 응답"""
    receipt_url: Optional[str] = dataclasses.field(metadata={"serde_rename": "receiptUrl", "serde_skip_if": lambda value: value is None})
    """결제 영수증 URL"""

