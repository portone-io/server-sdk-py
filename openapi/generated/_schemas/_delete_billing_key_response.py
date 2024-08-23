import dataclasses

@dataclasses.dataclass
class DeleteBillingKeyResponse:
    """빌링키 삭제 성공 응답"""
    deletedAt: str
    """빌링키 삭제 완료 시점"""

