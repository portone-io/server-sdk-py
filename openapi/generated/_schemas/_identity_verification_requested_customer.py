import dataclasses
from typing import Optional

@dataclasses.dataclass
class IdentityVerificationRequestedCustomer:
    """요청 시 고객 정보"""
    id: Optional[str] = dataclasses.field()
    """식별 아이디"""
    name: Optional[str] = dataclasses.field()
    """이름"""
    phone_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "phoneNumber"})
    """전화번호
    
    특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
    """

