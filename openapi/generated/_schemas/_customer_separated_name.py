import dataclasses

@dataclasses.dataclass
class CustomerSeparatedName:
    """고객 분리형 이름"""
    first: str = dataclasses.field()
    """이름"""
    last: str = dataclasses.field()
    """성"""

