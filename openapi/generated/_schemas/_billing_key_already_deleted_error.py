import dataclasses
from typing import Literal, Optional


@dataclasses.dataclass(kw_only=True)
class BillingKeyAlreadyDeletedError:
    """빌링키가 이미 삭제된 경우"""

    type: Literal["BILLING_KEY_ALREADY_DELETED"]
    message: Optional[str]
