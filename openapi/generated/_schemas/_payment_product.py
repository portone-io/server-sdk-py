import dataclasses
from typing import Optional

@dataclasses.dataclass
class PaymentProduct:
    """상품 정보"""
    id: str
    """상품 고유 식별자
    
    고객사가 직접 부여한 식별자입니다.
    """
    name: str
    """상품명"""
    tag: Optional[str]
    """상품 태그
    
    카테고리 등으로 활용될 수 있습니다.
    """
    code: Optional[str]
    """상품 코드"""
    amount: int
    """상품 단위가격"""
    quantity: int
    """주문 수량"""

