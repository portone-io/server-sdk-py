import dataclasses
from typing import Optional

@dataclasses.dataclass
class PageInput:
    """다건 조회 API 에 사용되는 페이지 입력 정보"""
    number: Optional[int]
    """0부터 시작하는 페이지 번호"""
    size: Optional[int]
    """각 페이지 당 포함할 객체 수"""

