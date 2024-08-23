import dataclasses
from typing import Optional

@dataclasses.dataclass
class IssueCashReceiptCustomerInput:
    """현금영수증 발급 시 고객 관련 입력 정보"""
    identityNumber: str
    """고객 식별값"""
    name: Optional[str]
    """이름"""
    email: Optional[str]
    """이메일"""
    phoneNumber: Optional[str]
    """전화번호"""

