import dataclasses
from typing import Optional

@dataclasses.dataclass
class SendIdentityVerificationBodyCustomer:
    """본인인증 요청을 위한 고객 정보"""
    id: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """식별 아이디"""
    name: str = dataclasses.field()
    """이름"""
    phone_number: str = dataclasses.field(metadata={"serde_rename": "phoneNumber"})
    """전화번호
    
    특수 문자(-) 없이 숫자만 입력합니다.
    """
    identity_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "identityNumber", "serde_skip_if": lambda value: value is None})
    """주민등록번호 앞 7자리
    
    SMS 방식의 경우 필수로 입력합니다.
    """
    ip_address: str = dataclasses.field(metadata={"serde_rename": "ipAddress"})
    """IP 주소
    
    고객의 요청 속도 제한에 사용됩니다.
    """

