import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._country import Country
from portone_server_sdk._openapi._schemas._customer_name_input import CustomerNameInput
from portone_server_sdk._openapi._schemas._gender import Gender
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput

@dataclasses.dataclass
class CustomerInput:
    """고객 정보 입력 정보"""
    id: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """고객 아이디
    
    고객사가 지정한 고객의 고유 식별자입니다.
    """
    name: Optional[CustomerNameInput] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """이름"""
    birth_year: Optional[str] = dataclasses.field(metadata={"serde_rename": "birthYear", "serde_skip_if": lambda value: value is None})
    """출생 연도"""
    birth_month: Optional[str] = dataclasses.field(metadata={"serde_rename": "birthMonth", "serde_skip_if": lambda value: value is None})
    """출생월"""
    birth_day: Optional[str] = dataclasses.field(metadata={"serde_rename": "birthDay", "serde_skip_if": lambda value: value is None})
    """출생일"""
    country: Optional[Country] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """국가"""
    gender: Optional[Gender] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """성별"""
    email: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """이메일"""
    phone_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "phoneNumber", "serde_skip_if": lambda value: value is None})
    """전화번호"""
    address: Optional[SeparatedAddressInput] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """주소"""
    zipcode: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """우편번호"""
    business_registration_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "businessRegistrationNumber", "serde_skip_if": lambda value: value is None})
    """사업자 등록 번호"""

