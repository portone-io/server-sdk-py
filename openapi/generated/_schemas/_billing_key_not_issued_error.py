import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class BillingKeyNotIssuedError:
    """BillingKeyNotIssuedError"""
    type: Literal["BILLING_KEY_NOT_ISSUED"]
    message: Optional[str]

