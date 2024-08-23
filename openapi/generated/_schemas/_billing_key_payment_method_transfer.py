import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._bank import Bank

@dataclasses.dataclass
class BillingKeyPaymentMethodTransfer:
    """계좌이체 정보"""
    type: Literal["BillingKeyPaymentMethodTransfer"]
    bank: Optional[Bank]
    """표준 은행 코드"""
    accountNumber: Optional[str]
    """계좌번호"""

