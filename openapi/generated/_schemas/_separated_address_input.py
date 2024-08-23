import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._country import Country

@dataclasses.dataclass
class SeparatedAddressInput:
    """분리 형식 주소 입력 정보"""
    addressLine1: str
    """상세 주소 1"""
    addressLine2: str
    """상세 주소 2"""
    city: Optional[str]
    """시/군/구"""
    province: Optional[str]
    """주/도/시"""
    country: Optional[Country]
    """국가"""

