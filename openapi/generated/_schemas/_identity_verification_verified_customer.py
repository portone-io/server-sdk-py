import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._gender import Gender
from portone_server_sdk._openapi._schemas._identity_verification_operator import IdentityVerificationOperator

@dataclasses.dataclass
class IdentityVerificationVerifiedCustomer:
    """인증된 고객 정보"""
    id: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """식별 아이디"""
    name: str = dataclasses.field()
    """이름"""
    operator: Optional[IdentityVerificationOperator] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """통신사"""
    phone_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "phoneNumber", "serde_skip_if": lambda value: value is None})
    """전화번호
    
    특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
    """
    birth_date: str = dataclasses.field(metadata={"serde_rename": "birthDate"})
    """생년월일 (yyyy-MM-dd)
    
    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    gender: Gender = dataclasses.field()
    """성별"""
    is_foreigner: Optional[bool] = dataclasses.field(metadata={"serde_rename": "isForeigner", "serde_skip_if": lambda value: value is None})
    """외국인 여부"""
    ci: str = dataclasses.field()
    """CI (개인 고유 식별키)"""
    di: str = dataclasses.field()
    """DI (사이트별 개인 고유 식별키)"""

