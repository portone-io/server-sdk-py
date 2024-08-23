import dataclasses

@dataclasses.dataclass
class PaymentInstallment:
    """할부 정보"""
    month: int
    """할부 개월 수"""
    isInterestFree: bool
    """무이자할부 여부"""

