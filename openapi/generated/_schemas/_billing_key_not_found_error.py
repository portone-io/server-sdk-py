import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class BillingKeyNotFoundError:
    """빌링키가 존재하지 않는 경우"""
    type: Literal["BILLING_KEY_NOT_FOUND"]
    message: Optional[str]

