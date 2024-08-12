import dataclasses
from typing import Literal, Optional


@dataclasses.dataclass(kw_only=True)
class BillingKeyNotIssuedError:
    """BillingKeyNotIssuedError"""

    type: Literal["BILLING_KEY_NOT_ISSUED"]
    message: Optional[str]
