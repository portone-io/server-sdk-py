import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class BillingKeyNotIssuedError:
    """BillingKeyNotIssuedError"""
    type: Literal["BILLING_KEY_NOT_ISSUED"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})

