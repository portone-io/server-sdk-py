import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._country import Country

@dataclasses.dataclass
class SeparatedAddressInput:
    """분리 형식 주소 입력 정보"""
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

