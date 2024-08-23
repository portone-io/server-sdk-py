import dataclasses

@dataclasses.dataclass
class ChannelGroupSummary:
    """채널 그룹 정보"""
    id: str
    """채널 그룹 아이디"""
    name: str
    """채널 그룹 이름"""
    isForTest: bool
    """테스트 채널 그룹 여부"""

