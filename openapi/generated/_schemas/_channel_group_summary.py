import dataclasses

@dataclasses.dataclass
class ChannelGroupSummary:
    """채널 그룹 정보"""
    id: str = dataclasses.field()
    """채널 그룹 아이디"""
    name: str = dataclasses.field()
    """채널 그룹 이름"""
    is_for_test: bool = dataclasses.field(metadata={"serde_rename": "isForTest"})
    """테스트 채널 그룹 여부"""

