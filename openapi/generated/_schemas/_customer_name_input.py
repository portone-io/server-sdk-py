import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._customer_separated_name import CustomerSeparatedName

@dataclasses.dataclass
class CustomerNameInput:
    """고객 이름 입력 정보
    
    두 개의 이름 형식 중 한 가지만 선택하여 입력해주세요.
    """
    full: Optional[str]
    """한 줄 이름 형식"""
    separated: Optional[CustomerSeparatedName]
    """분리형 이름 형식"""

