import dataclasses
from portone_server_sdk._openapi._schemas._card_credential import CardCredential

@dataclasses.dataclass(kw_only=True)
class InstantBillingKeyPaymentMethodInputCard:
    """카드 수단 정보 입력 양식"""
    credential: CardCredential

