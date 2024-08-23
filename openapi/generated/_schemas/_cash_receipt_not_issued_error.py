import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class CashReceiptNotIssuedError:
    """현금영수증이 발급되지 않은 경우"""
    type: Literal["CASH_RECEIPT_NOT_ISSUED"]
    message: Optional[str]

