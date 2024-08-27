import dataclasses
from typing import Optional

@dataclasses.dataclass
class PageInput:
    """다건 조회 API 에 사용되는 페이지 입력 정보"""
    number: Optional[int] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """0부터 시작하는 페이지 번호"""
    size: Optional[int] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """각 페이지 당 포함할 객체 수"""

