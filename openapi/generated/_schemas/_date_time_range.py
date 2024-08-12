import dataclasses

@dataclasses.dataclass(kw_only=True)
class DateTimeRange:
    """시간 범위"""
    from_: str = dataclasses.field(metadata={"serde_rename": "from"})
    until: str

