import dataclasses
from typing import Optional

@dataclasses.dataclass
class SendIdentityVerificationBodyCustomer:
    """본인인증 요청을 위한 고객 정보"""
    id: Optional[str]
    """식별 아이디"""
    name: str
    """이름"""
    phoneNumber: str
    """전화번호
    
    특수 문자(-) 없이 숫자만 입력합니다.
    """
    identityNumber: Optional[str]
    """주민등록번호 앞 7자리
    
    SMS 방식의 경우 필수로 입력합니다.
    """
    ipAddress: str
    """IP 주소
    
    고객의 요청 속도 제한에 사용됩니다.
    """

