import dataclasses
from typing import Literal, Optional


@dataclasses.dataclass(kw_only=True)
class CashReceiptAlreadyIssuedError:
    """현금영수증이 이미 발급된 경우"""

    type: Literal["CASH_RECEIPT_ALREADY_ISSUED"]
    message: Optional[str]
