import dataclasses

@dataclasses.dataclass
class PageInfo:
    """반환된 페이지 결과 정보"""
    number: int
    """요청된 페이지 번호"""
    size: int
    """요청된 페이지 당 객체 수"""
    totalCount: int
    """실제 반환된 객체 수"""

