import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._card_brand import CardBrand
from portone_server_sdk._openapi._schemas._card_owner_type import CardOwnerType
from portone_server_sdk._openapi._schemas._card_type import CardType

@dataclasses.dataclass
class Card:
    """카드 상세 정보"""
    publisher: Optional[str]
    """발행사 코드"""
    issuer: Optional[str]
    """발급사 코드"""
    brand: Optional[CardBrand]
    """카드 브랜드"""
    type: Optional[CardType]
    """카드 유형"""
    ownerType: Optional[CardOwnerType]
    """카드 소유주 유형"""
    bin: Optional[str]
    """카드 번호 앞 6자리 또는 8자리의 BIN (Bank Identification Number)"""
    name: Optional[str]
    """카드 상품명"""
    number: Optional[str]
    """마스킹된 카드 번호"""

