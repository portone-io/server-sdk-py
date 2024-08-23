import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._country import Country

@dataclasses.dataclass
class SeparatedAddress:
    """분리 형식 주소
    
    한 줄 형식 주소와 분리 형식 주소 모두 존재합니다.
    한 줄 형식 주소는 분리 형식 주소를 이어 붙인 형태로 생성됩니다.
    """
    type: Literal["SEPARATED"]
    oneLine: str
    """주소 (한 줄)"""
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

