import dataclasses
from typing import Literal, Optional


@dataclasses.dataclass(kw_only=True)
class CancelAmountExceedsCancellableAmountError:
    """결제 취소 금액이 취소 가능 금액을 초과한 경우"""

    type: Literal["CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT"]
    message: Optional[str]
