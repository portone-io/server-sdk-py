import dataclasses
from typing import Optional

@dataclasses.dataclass
class PaymentAmount:
    """결제 금액 세부 정보"""
    total: int = dataclasses.field()
    """총 결제금액"""
    tax_free: int = dataclasses.field(metadata={"serde_rename": "taxFree"})
    """면세액"""
    vat: Optional[int] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """부가세액"""
    supply: Optional[int] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """공급가액"""
    discount: int = dataclasses.field()
    """할인금액
    
    카드사 프로모션, 포트원 프로모션, 적립형 포인트 결제, 쿠폰 할인 등을 포함합니다.
    """
    paid: int = dataclasses.field()
    """실제 결제금액"""
    cancelled: int = dataclasses.field()
    """취소금액"""
    cancelled_tax_free: int = dataclasses.field(metadata={"serde_rename": "cancelledTaxFree"})
    """취소금액 중 면세액"""

