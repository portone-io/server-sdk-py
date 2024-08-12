import dataclasses
from portone_server_sdk._openapi._schemas._payment import Payment

@dataclasses.dataclass(kw_only=True)
class PaymentWithCursor:
    """결제 건 및 커서 정보"""
    payment: Payment
    """결제 건 정보"""
    cursor: str
    """해당 결제 건의 커서 정보"""

