import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._bank import Bank

@dataclasses.dataclass
class BillingKeyPaymentMethodTransfer:
    """계좌이체 정보"""
    type: Literal["BillingKeyPaymentMethodTransfer"] = dataclasses.field()
    bank: Optional[Bank] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """표준 은행 코드"""
    account_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "accountNumber", "serde_skip_if": lambda value: value is None})
    """계좌번호"""

