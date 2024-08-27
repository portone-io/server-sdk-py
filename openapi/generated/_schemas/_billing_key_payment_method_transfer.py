import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._bank import Bank

@dataclasses.dataclass
class BillingKeyPaymentMethodTransfer:
    """계좌이체 정보"""
    type: Literal["BillingKeyPaymentMethodTransfer"] = dataclasses.field()
    bank: Optional[Bank] = dataclasses.field()
    """표준 은행 코드"""
    account_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "accountNumber"})
    """계좌번호"""

