import dataclasses

@dataclasses.dataclass
class CustomerSeparatedName:
    """고객 분리형 이름"""
    first: str
    """이름"""
    last: str
    """성"""

