import dataclasses
from typing import Literal

@dataclasses.dataclass
class BeforeRegisteredPaymentEscrow:
    """배송 정보 등록 전"""
    status: Literal["BEFORE_REGISTERED"] = dataclasses.field()
    """에스크로 상태"""

