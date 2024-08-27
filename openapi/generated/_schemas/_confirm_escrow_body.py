import dataclasses
from typing import Optional

@dataclasses.dataclass
class ConfirmEscrowBody:
    """에스크로 구매 확정 입력 정보"""
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    from_store: Optional[bool] = dataclasses.field(metadata={"serde_rename": "fromStore", "serde_skip_if": lambda value: value is None})
    """확인 주체가 상점인지 여부
    
    구매확정요청 주체가 고객사 관리자인지 구매자인지 구분하기 위한 필드입니다.
    네이버페이 전용 파라미터이며, 구분이 모호한 경우 고객사 관리자(true)로 입력합니다.
    """

