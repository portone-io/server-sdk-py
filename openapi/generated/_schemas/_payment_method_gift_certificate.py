import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._payment_method_gift_certificate_type import PaymentMethodGiftCertificateType

@dataclasses.dataclass
class PaymentMethodGiftCertificate:
    """상품권 상세 정보"""
    type: Literal["PaymentMethodGiftCertificate"]
    giftCertificateType: Optional[PaymentMethodGiftCertificateType]
    """상품권 종류"""
    approvalNumber: str
    """상품권 승인 번호"""

