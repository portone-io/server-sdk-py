import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._country import Country
from portone_server_sdk._openapi._schemas._customer_name_input import CustomerNameInput
from portone_server_sdk._openapi._schemas._gender import Gender
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput

@dataclasses.dataclass
class CustomerInput:
    """고객 정보 입력 정보"""
    id: Optional[str] = dataclasses.field()
    """고객 아이디
    
    고객사가 지정한 고객의 고유 식별자입니다.
    """
    name: Optional[CustomerNameInput] = dataclasses.field()
    """이름"""
    birth_year: Optional[str] = dataclasses.field(metadata={"serde_rename": "birthYear"})
    """출생 연도"""
    birth_month: Optional[str] = dataclasses.field(metadata={"serde_rename": "birthMonth"})
    """출생월"""
    birth_day: Optional[str] = dataclasses.field(metadata={"serde_rename": "birthDay"})
    """출생일"""
    country: Optional[Country] = dataclasses.field()
    """국가"""
    gender: Optional[Gender] = dataclasses.field()
    """성별"""
    email: Optional[str] = dataclasses.field()
    """이메일"""
    phone_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "phoneNumber"})
    """전화번호"""
    address: Optional[SeparatedAddressInput] = dataclasses.field()
    """주소"""
    zipcode: Optional[str] = dataclasses.field()
    """우편번호"""
    business_registration_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "businessRegistrationNumber"})
    """사업자 등록 번호"""

