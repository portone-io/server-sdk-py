import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._cash_receipt_input_type import CashReceiptInputType

@dataclasses.dataclass
class CashReceiptInput:
    """현금영수증 입력 정보"""
    type: CashReceiptInputType
    """현금영수증 유형"""
    customerIdentityNumber: Optional[str]
    """사용자 식별 번호
    
    미발행 유형 선택 시 입력하지 않습니다.
    """

