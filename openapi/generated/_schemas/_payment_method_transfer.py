import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._bank import Bank

@dataclasses.dataclass
class PaymentMethodTransfer:
    """계좌 이체 상세 정보"""
    type: Literal["PaymentMethodTransfer"]
    bank: Optional[Bank]
    """표준 은행 코드"""

