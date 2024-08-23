import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._country import Country
from portone_server_sdk._openapi._schemas._customer_name_input import CustomerNameInput
from portone_server_sdk._openapi._schemas._gender import Gender
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput

@dataclasses.dataclass
class CustomerInput:
    """고객 정보 입력 정보"""
    id: Optional[str]
    """고객 아이디
    
    고객사가 지정한 고객의 고유 식별자입니다.
    """
    name: Optional[CustomerNameInput]
    """이름"""
    birthYear: Optional[str]
    """출생 연도"""
    birthMonth: Optional[str]
    """출생월"""
    birthDay: Optional[str]
    """출생일"""
    country: Optional[Country]
    """국가"""
    gender: Optional[Gender]
    """성별"""
    email: Optional[str]
    """이메일"""
    phoneNumber: Optional[str]
    """전화번호"""
    address: Optional[SeparatedAddressInput]
    """주소"""
    zipcode: Optional[str]
    """우편번호"""
    businessRegistrationNumber: Optional[str]
    """사업자 등록 번호"""

