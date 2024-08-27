import dataclasses
from typing import Optional

@dataclasses.dataclass
class PaymentAmountInput:
    """금액 세부 입력 정보"""
    total: int = dataclasses.field()
    """총 금액"""
    tax_free: Optional[int] = dataclasses.field(metadata={"serde_rename": "taxFree", "serde_skip_if": lambda value: value is None})
    """면세액"""
    vat: Optional[int] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """부가세액
    
    고객사에서 직접 계산이 필요한 경우 입력합니다.
    입력하지 않으면 면세 금액을 제외한 금액의 1/11 로 자동 계산됩니다.
    """

