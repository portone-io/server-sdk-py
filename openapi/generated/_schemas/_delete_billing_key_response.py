import dataclasses

@dataclasses.dataclass
class DeleteBillingKeyResponse:
    """빌링키 삭제 성공 응답"""
    deleted_at: str = dataclasses.field(metadata={"serde_rename": "deletedAt"})
    """빌링키 삭제 완료 시점"""

