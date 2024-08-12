import dataclasses
from typing import Optional


@dataclasses.dataclass(kw_only=True)
class ConfirmIdentityVerificationBody:
    """본인인증 확인을 위한 입력 정보"""

    storeId: Optional[str]
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    otp: Optional[str]
    """OTP (One-Time Password)
    
    SMS 방식에서만 사용됩니다.
    """
