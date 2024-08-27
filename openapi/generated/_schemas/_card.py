import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._card_brand import CardBrand
from portone_server_sdk._openapi._schemas._card_owner_type import CardOwnerType
from portone_server_sdk._openapi._schemas._card_type import CardType

@dataclasses.dataclass
class Card:
    """카드 상세 정보"""
    publisher: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """발행사 코드"""
    issuer: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """발급사 코드"""
    brand: Optional[CardBrand] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """카드 브랜드"""
    type: Optional[CardType] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """카드 유형"""
    owner_type: Optional[CardOwnerType] = dataclasses.field(metadata={"serde_rename": "ownerType", "serde_skip_if": lambda value: value is None})
    """카드 소유주 유형"""
    bin: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """카드 번호 앞 6자리 또는 8자리의 BIN (Bank Identification Number)"""
    name: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """카드 상품명"""
    number: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """마스킹된 카드 번호"""

