import dataclasses
from typing import Optional

@dataclasses.dataclass
class PaymentAmount:
    """결제 금액 세부 정보"""
    total: int
    """총 결제금액"""
    taxFree: int
    """면세액"""
    vat: Optional[int]
    """부가세액"""
    supply: Optional[int]
    """공급가액"""
    discount: int
    """할인금액
    
    카드사 프로모션, 포트원 프로모션, 적립형 포인트 결제, 쿠폰 할인 등을 포함합니다.
    """
    paid: int
    """실제 결제금액"""
    cancelled: int
    """취소금액"""
    cancelledTaxFree: int
    """취소금액 중 면세액"""

