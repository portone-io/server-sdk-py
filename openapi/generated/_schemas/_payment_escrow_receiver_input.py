import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput

@dataclasses.dataclass
class PaymentEscrowReceiverInput:
    """에스크로 수취인 정보"""
    name: Optional[str]
    """이름"""
    phoneNumber: Optional[str]
    """전화번호"""
    zipcode: Optional[str]
    """우편번호"""
    address: Optional[SeparatedAddressInput]
    """주소"""

