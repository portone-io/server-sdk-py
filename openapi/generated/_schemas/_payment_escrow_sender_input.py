import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput

@dataclasses.dataclass
class PaymentEscrowSenderInput:
    """에스크로 발송자 정보"""
    name: Optional[str] = dataclasses.field()
    """이름"""
    phone_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "phoneNumber"})
    """전화번호"""
    zipcode: Optional[str] = dataclasses.field()
    """우편번호"""
    relationship: Optional[str] = dataclasses.field()
    """수취인과의 관계"""
    address: Optional[SeparatedAddressInput] = dataclasses.field()
    """주소"""

