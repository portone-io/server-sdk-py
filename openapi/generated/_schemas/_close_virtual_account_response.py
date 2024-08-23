import dataclasses

@dataclasses.dataclass
class CloseVirtualAccountResponse:
    """가상계좌 말소 성공 응답"""
    closedAt: str
    """가상계좌 말소 시점"""

