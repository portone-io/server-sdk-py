import dataclasses
from typing import Optional

@dataclasses.dataclass
class CardCredential:
    """카드 인증 관련 정보"""
    number: str = dataclasses.field()
    """카드 번호 (숫자만)"""
    expiry_year: str = dataclasses.field(metadata={"serde_rename": "expiryYear"})
    """유효 기간 만료 연도 (2자리)"""
    expiry_month: str = dataclasses.field(metadata={"serde_rename": "expiryMonth"})
    """유효 기간 만료 월 (2자리)"""
    birth_or_business_registration_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "birthOrBusinessRegistrationNumber", "serde_skip_if": lambda value: value is None})
    """생년월일 (yyMMdd) 또는 사업자 등록 번호 (10자리, 숫자만)"""
    password_two_digits: Optional[str] = dataclasses.field(metadata={"serde_rename": "passwordTwoDigits", "serde_skip_if": lambda value: value is None})
    """비밀번호 앞 2자리"""

