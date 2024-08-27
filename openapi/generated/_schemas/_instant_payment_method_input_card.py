import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._card_credential import CardCredential

@dataclasses.dataclass
class InstantPaymentMethodInputCard:
    """카드 수단 정보 입력 정보"""
    credential: CardCredential = dataclasses.field()
    """카드 인증 관련 정보"""
    installment_month: Optional[int] = dataclasses.field(metadata={"serde_rename": "installmentMonth"})
    """카드 할부 개월 수"""
    use_free_installment_plan: Optional[bool] = dataclasses.field(metadata={"serde_rename": "useFreeInstallmentPlan"})
    """무이자 할부 적용 여부"""
    use_free_interest_from_merchant: Optional[bool] = dataclasses.field(metadata={"serde_rename": "useFreeInterestFromMerchant"})
    """무이자 할부 이자를 고객사가 부담할지 여부"""
    use_card_point: Optional[bool] = dataclasses.field(metadata={"serde_rename": "useCardPoint"})
    """카드 포인트 사용 여부"""

