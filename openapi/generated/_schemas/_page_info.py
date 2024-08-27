import dataclasses

@dataclasses.dataclass
class PageInfo:
    """반환된 페이지 결과 정보"""
    number: int = dataclasses.field()
    """요청된 페이지 번호"""
    size: int = dataclasses.field()
    """요청된 페이지 당 객체 수"""
    total_count: int = dataclasses.field(metadata={"serde_rename": "totalCount"})
    """실제 반환된 객체 수"""

