import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._bank import Bank

@dataclasses.dataclass
class PaymentMethodEasyPayMethodCharge:
    """충전식 포인트 결제 정보"""
    type: Literal["PaymentMethodEasyPayMethodCharge"]
    bank: Optional[Bank]
    """표준 은행 코드"""

