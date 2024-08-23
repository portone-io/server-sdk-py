import dataclasses
from portone_server_sdk._openapi._schemas._cash_receipt_input_type import CashReceiptInputType

@dataclasses.dataclass
class InstantPaymentMethodInputVirtualAccountCashReceiptInfo:
    """가상계좌 결제 시 현금영수증 정보"""
    type: CashReceiptInputType
    """현금영수증 유형"""
    customerIdentityNumber: str
    """사용자 식별 번호"""

