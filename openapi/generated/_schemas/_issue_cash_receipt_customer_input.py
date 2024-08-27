import dataclasses
from typing import Optional

@dataclasses.dataclass
class IssueCashReceiptCustomerInput:
    """현금영수증 발급 시 고객 관련 입력 정보"""
    identity_number: str = dataclasses.field(metadata={"serde_rename": "identityNumber"})
    """고객 식별값"""
    name: Optional[str] = dataclasses.field()
    """이름"""
    email: Optional[str] = dataclasses.field()
    """이메일"""
    phone_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "phoneNumber"})
    """전화번호"""

