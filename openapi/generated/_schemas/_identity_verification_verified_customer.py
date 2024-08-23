import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._gender import Gender
from portone_server_sdk._openapi._schemas._identity_verification_operator import IdentityVerificationOperator

@dataclasses.dataclass
class IdentityVerificationVerifiedCustomer:
    """인증된 고객 정보"""
    id: Optional[str]
    """식별 아이디"""
    name: str
    """이름"""
    operator: Optional[IdentityVerificationOperator]
    """통신사"""
    phoneNumber: Optional[str]
    """전화번호
    
    특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
    """
    birthDate: str
    """생년월일 (yyyy-MM-dd)
    
    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    gender: Gender
    """성별"""
    isForeigner: Optional[bool]
    """외국인 여부"""
    ci: str
    """CI (개인 고유 식별키)"""
    di: str
    """DI (사이트별 개인 고유 식별키)"""

