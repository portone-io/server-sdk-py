import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class PromotionPayMethodDoesNotMatchError:
    """결제수단이 프로모션에 지정된 것과 일치하지 않는 경우"""
    type: Literal["PROMOTION_PAY_METHOD_DOES_NOT_MATCH"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

