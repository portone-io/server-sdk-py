import dataclasses
from typing import Optional

@dataclasses.dataclass
class ConfirmIdentityVerificationBody:
    """본인인증 확인을 위한 입력 정보"""
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    otp: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """OTP (One-Time Password)
    
    SMS 방식에서만 사용됩니다.
    """

