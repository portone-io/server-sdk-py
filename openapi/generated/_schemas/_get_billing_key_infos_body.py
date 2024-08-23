import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._billing_key_filter_input import BillingKeyFilterInput
from portone_server_sdk._openapi._schemas._billing_key_sort_input import BillingKeySortInput
from portone_server_sdk._openapi._schemas._page_input import PageInput

@dataclasses.dataclass
class GetBillingKeyInfosBody:
    """GetBillingKeyInfosBody
    
    빌링키 다건 조회를 위한 입력 정보
    """
    page: Optional[PageInput]
    """요청할 페이지 정보
    
    미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
    """
    sort: Optional[BillingKeySortInput]
    """정렬 조건
    
    미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
    """
    filter: Optional[BillingKeyFilterInput]
    """조회할 빌링키 조건 필터
    
    V1 빌링키 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
    """

