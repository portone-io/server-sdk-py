import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._card_credential import CardCredential

@dataclasses.dataclass
class InstantPaymentMethodInputCard:
    """카드 수단 정보 입력 정보"""
    credential: CardCredential
    """카드 인증 관련 정보"""
    installmentMonth: Optional[int]
    """카드 할부 개월 수"""
    useFreeInstallmentPlan: Optional[bool]
    """무이자 할부 적용 여부"""
    useFreeInterestFromMerchant: Optional[bool]
    """무이자 할부 이자를 고객사가 부담할지 여부"""
    useCardPoint: Optional[bool]
    """카드 포인트 사용 여부"""

