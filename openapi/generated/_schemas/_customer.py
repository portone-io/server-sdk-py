import dataclasses
import serde
from typing import Optional
from portone_server_sdk._openapi._schemas._address import Address
from portone_server_sdk._openapi._schemas._gender import Gender

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class Customer:
    """고객 정보"""
    id: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """고객 아이디
    
    고객사가 지정한 고객의 고유 식별자입니다.
    """
    name: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """이름"""
    birth_year: Optional[str] = dataclasses.field(metadata={"serde_rename": "birthYear", "serde_skip_if": lambda value: value is None})
    """출생 연도"""
    gender: Optional[Gender] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """성별"""
    email: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """이메일"""
    phone_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "phoneNumber", "serde_skip_if": lambda value: value is None})
    """전화번호"""
    address: Optional[Address] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """주소"""
    zipcode: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """우편번호"""

