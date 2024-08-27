import dataclasses
from typing import Optional

@dataclasses.dataclass
class RevokePaymentSchedulesResponse:
    """결제 예약 건 취소 성공 응답"""
    revoked_schedule_ids: list[str] = dataclasses.field(metadata={"serde_rename": "revokedScheduleIds"})
    """취소 완료된 결제 예약 건 아이디 목록"""
    revoked_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "revokedAt", "serde_skip_if": lambda value: value is None})
    """결제 예약 건 취소 완료 시점"""

