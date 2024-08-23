import dataclasses

@dataclasses.dataclass
class ConfirmEscrowResponse:
    """에스크로 구매 확정 성공 응답"""
    completedAt: str
    """에스크로 구매 확정 시점"""

