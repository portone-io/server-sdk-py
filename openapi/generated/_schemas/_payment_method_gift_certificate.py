import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._payment_method_gift_certificate_type import PaymentMethodGiftCertificateType

@dataclasses.dataclass
class PaymentMethodGiftCertificate:
    """상품권 상세 정보"""
    type: Literal["PaymentMethodGiftCertificate"] = dataclasses.field()
    gift_certificate_type: Optional[PaymentMethodGiftCertificateType] = dataclasses.field(metadata={"serde_rename": "giftCertificateType", "serde_skip_if": lambda value: value is None})
    """상품권 종류"""
    approval_number: str = dataclasses.field(metadata={"serde_rename": "approvalNumber"})
    """상품권 승인 번호"""

