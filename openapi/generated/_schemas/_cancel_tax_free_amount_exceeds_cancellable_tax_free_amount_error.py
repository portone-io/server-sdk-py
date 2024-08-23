import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError:
    """취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우"""
    type: Literal["CANCEL_TAX_FREE_AMOUNT_EXCEEDS_CANCELLABLE_TAX_FREE_AMOUNT"]
    message: Optional[str]

