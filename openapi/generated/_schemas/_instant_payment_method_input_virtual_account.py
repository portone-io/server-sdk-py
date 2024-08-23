import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._bank import Bank
from portone_server_sdk._openapi._schemas._instant_payment_method_input_virtual_account_cash_receipt_info import InstantPaymentMethodInputVirtualAccountCashReceiptInfo
from portone_server_sdk._openapi._schemas._instant_payment_method_input_virtual_account_expiry import InstantPaymentMethodInputVirtualAccountExpiry
from portone_server_sdk._openapi._schemas._instant_payment_method_input_virtual_account_option import InstantPaymentMethodInputVirtualAccountOption

@dataclasses.dataclass
class InstantPaymentMethodInputVirtualAccount:
    """가상계좌 수단 정보 입력 정보"""
    bank: Bank
    """은행"""
    expiry: InstantPaymentMethodInputVirtualAccountExpiry
    """입금 만료 기한"""
    option: InstantPaymentMethodInputVirtualAccountOption
    """가상계좌 유형"""
    cashReceipt: InstantPaymentMethodInputVirtualAccountCashReceiptInfo
    """현금영수증 정보"""
    remitteeName: Optional[str]
    """예금주명"""

