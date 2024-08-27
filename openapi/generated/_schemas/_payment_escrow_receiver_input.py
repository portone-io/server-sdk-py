import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput

@dataclasses.dataclass
class PaymentEscrowReceiverInput:
    """에스크로 수취인 정보"""
    name: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """이름"""
    phone_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "phoneNumber", "serde_skip_if": lambda value: value is None})
    """전화번호"""
    zipcode: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """우편번호"""
    address: Optional[SeparatedAddressInput] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """주소"""

