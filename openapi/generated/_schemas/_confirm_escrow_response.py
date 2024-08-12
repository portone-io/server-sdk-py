import dataclasses

@dataclasses.dataclass(kw_only=True)
class ConfirmEscrowResponse:
    """에스크로 구매 확정 성공 응답"""
    completedAt: str
    """에스크로 구매 확정 시점"""

