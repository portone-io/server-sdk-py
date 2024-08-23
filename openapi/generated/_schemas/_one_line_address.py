import dataclasses
from typing import Literal

@dataclasses.dataclass
class OneLineAddress:
    """한 줄 형식 주소
    
    한 줄 형식 주소만 존재합니다.
    """
    type: Literal["ONE_LINE"]
    oneLine: str
    """주소 (한 줄)"""

