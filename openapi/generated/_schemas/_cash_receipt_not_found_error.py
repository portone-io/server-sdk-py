import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class CashReceiptNotFoundError:
    """현금영수증이 존재하지 않는 경우"""
    type: Literal["CASH_RECEIPT_NOT_FOUND"]
    message: Optional[str]

