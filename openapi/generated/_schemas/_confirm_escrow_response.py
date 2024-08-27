import dataclasses

@dataclasses.dataclass
class ConfirmEscrowResponse:
    """에스크로 구매 확정 성공 응답"""
    completed_at: str = dataclasses.field(metadata={"serde_rename": "completedAt"})
    """에스크로 구매 확정 시점"""

