import dataclasses
import serde
from typing import Optional
from portone_server_sdk._openapi._schemas._address import Address
from portone_server_sdk._openapi._schemas._gender import Gender

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class Customer:
    """고객 정보"""
    id: Optional[str]
    """고객 아이디
    
    고객사가 지정한 고객의 고유 식별자입니다.
    """
    name: Optional[str]
    """이름"""
    birthYear: Optional[str]
    """출생 연도"""
    gender: Optional[Gender]
    """성별"""
    email: Optional[str]
    """이메일"""
    phoneNumber: Optional[str]
    """전화번호"""
    address: Optional[Address]
    """주소"""
    zipcode: Optional[str]
    """우편번호"""

