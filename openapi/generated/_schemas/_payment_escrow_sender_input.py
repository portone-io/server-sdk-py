import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput

@dataclasses.dataclass
class PaymentEscrowSenderInput:
    """에스크로 발송자 정보"""
    name: Optional[str]
    """이름"""
    phoneNumber: Optional[str]
    """전화번호"""
    zipcode: Optional[str]
    """우편번호"""
    relationship: Optional[str]
    """수취인과의 관계"""
    address: Optional[SeparatedAddressInput]
    """주소"""

