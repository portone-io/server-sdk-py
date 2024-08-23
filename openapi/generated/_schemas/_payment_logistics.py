import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._payment_logistics_company import PaymentLogisticsCompany
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput

@dataclasses.dataclass
class PaymentLogistics:
    """배송정보"""
    company: PaymentLogisticsCompany
    """물류회사"""
    invoiceNumber: str
    """송장번호"""
    sentAt: str
    """발송시점"""
    receivedAt: Optional[str]
    """수령시점"""
    address: Optional[SeparatedAddressInput]
    """주소"""

