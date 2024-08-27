import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._country import Country

@dataclasses.dataclass
class SeparatedAddress:
    """분리 형식 주소
    
    한 줄 형식 주소와 분리 형식 주소 모두 존재합니다.
    한 줄 형식 주소는 분리 형식 주소를 이어 붙인 형태로 생성됩니다.
    """
    type: Literal["SEPARATED"] = dataclasses.field()
    one_line: str = dataclasses.field(metadata={"serde_rename": "oneLine"})
    """주소 (한 줄)"""
    address_line1: str = dataclasses.field(metadata={"serde_rename": "addressLine1"})
    """상세 주소 1"""
    address_line2: str = dataclasses.field(metadata={"serde_rename": "addressLine2"})
    """상세 주소 2"""
    city: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """시/군/구"""
    province: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """주/도/시"""
    country: Optional[Country] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """국가"""

