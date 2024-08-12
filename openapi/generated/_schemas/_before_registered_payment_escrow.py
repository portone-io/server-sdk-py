import dataclasses
from typing import Literal


@dataclasses.dataclass(kw_only=True)
class BeforeRegisteredPaymentEscrow:
    """배송 정보 등록 전"""

    status: Literal["BEFORE_REGISTERED"]
    """에스크로 상태"""
