import dataclasses
from typing import Optional

@dataclasses.dataclass
class RevokePaymentSchedulesResponse:
    """결제 예약 건 취소 성공 응답"""
    revokedScheduleIds: list[str]
    """취소 완료된 결제 예약 건 아이디 목록"""
    revokedAt: Optional[str]
    """결제 예약 건 취소 완료 시점"""

