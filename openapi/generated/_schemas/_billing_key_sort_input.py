import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._billing_key_sort_by import BillingKeySortBy
from portone_server_sdk._openapi._schemas._sort_order import SortOrder

@dataclasses.dataclass
class BillingKeySortInput:
    """빌링키 다건 조회 시 정렬 조건"""
    by: Optional[BillingKeySortBy] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """정렬 기준 필드
    
    어떤 필드를 기준으로 정렬할 지 결정합니다. 비워서 보낼 경우, REQUESTED_AT이 기본값으로 설정됩니다.
    """
    order: Optional[SortOrder] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """정렬 순서
    
    어떤 순서로 정렬할 지 결정합니다. 비워서 보낼 경우, DESC(내림차순)가 기본값으로 설정됩니다.
    """

