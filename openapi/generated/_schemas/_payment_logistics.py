import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._payment_logistics_company import PaymentLogisticsCompany
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput

@dataclasses.dataclass
class PaymentLogistics:
    """배송정보"""
    company: PaymentLogisticsCompany = dataclasses.field()
    """물류회사"""
    invoice_number: str = dataclasses.field(metadata={"serde_rename": "invoiceNumber"})
    """송장번호"""
    sent_at: str = dataclasses.field(metadata={"serde_rename": "sentAt"})
    """발송시점"""
    received_at: Optional[str] = dataclasses.field(metadata={"serde_rename": "receivedAt", "serde_skip_if": lambda value: value is None})
    """수령시점"""
    address: Optional[SeparatedAddressInput] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """주소"""

