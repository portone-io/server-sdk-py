import dataclasses
from typing import Optional

@dataclasses.dataclass
class CardCredential:
    """카드 인증 관련 정보"""
    number: str
    """카드 번호 (숫자만)"""
    expiryYear: str
    """유효 기간 만료 연도 (2자리)"""
    expiryMonth: str
    """유효 기간 만료 월 (2자리)"""
    birthOrBusinessRegistrationNumber: Optional[str]
    """생년월일 (yyMMdd) 또는 사업자 등록 번호 (10자리, 숫자만)"""
    passwordTwoDigits: Optional[str]
    """비밀번호 앞 2자리"""

