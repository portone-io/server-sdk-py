import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class CancellableAmountConsistencyBrokenError:
    """취소 가능 잔액 검증에 실패한 경우"""
    type: Literal["CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

