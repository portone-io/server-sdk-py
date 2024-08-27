import dataclasses

@dataclasses.dataclass
class PaymentInstallment:
    """할부 정보"""
    month: int = dataclasses.field()
    """할부 개월 수"""
    is_interest_free: bool = dataclasses.field(metadata={"serde_rename": "isInterestFree"})
    """무이자할부 여부"""

