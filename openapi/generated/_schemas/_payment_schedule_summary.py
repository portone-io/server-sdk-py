import dataclasses

@dataclasses.dataclass
class PaymentScheduleSummary:
    """결제 예약 건"""
    id: str = dataclasses.field()
    """결제 예약 건 아이디"""

