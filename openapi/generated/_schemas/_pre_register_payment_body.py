import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._currency import Currency

@dataclasses.dataclass
class PreRegisterPaymentBody:
    """결제 정보 사전 등록 입력 정보"""
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    total_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "totalAmount", "serde_skip_if": lambda value: value is None})
    """결제 총 금액"""
    tax_free_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "taxFreeAmount", "serde_skip_if": lambda value: value is None})
    """결제 면세 금액"""
    currency: Optional[Currency] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """통화 단위"""

