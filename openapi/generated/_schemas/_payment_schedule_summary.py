import dataclasses


@dataclasses.dataclass(kw_only=True)
class PaymentScheduleSummary:
    """결제 예약 건"""

    id: str
    """결제 예약 건 아이디"""
