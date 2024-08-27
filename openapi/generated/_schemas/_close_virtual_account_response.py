import dataclasses

@dataclasses.dataclass
class CloseVirtualAccountResponse:
    """가상계좌 말소 성공 응답"""
    closed_at: str = dataclasses.field(metadata={"serde_rename": "closedAt"})
    """가상계좌 말소 시점"""

